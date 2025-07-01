#!/usr/bin/env python3
"""
CodeFuser Web API - FastAPI Backend
Web tabanlı CodeFuser uygulaması
"""

import os
import uuid
import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Any, Optional, Union
from dataclasses import dataclass

from fastapi import FastAPI, HTTPException, Depends, status, File, UploadFile, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.responses import FileResponse

from pydantic import BaseModel, EmailStr
from motor.motor_asyncio import AsyncIOMotorClient
from passlib.context import CryptContext
from jose import JWTError, jwt

import uvicorn
from pymongo import MongoClient

# Pydantic modelleri
class UserSignup(BaseModel):
    email: EmailStr
    password: str
    name: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class ProcessRequest(BaseModel):
    files: List[Dict[str, Any]]  # Dosya bilgileri tarayıcıdan gelecek
    general_prompt: Optional[str] = ""
    file_prompts: Optional[Dict[str, str]] = {}  # file_path -> prompt mapping
    output_format: str = "html"
    template_id: Optional[str] = None
    filters: Optional[List[str]] = []

class ProjectAnalysis(BaseModel):
    total_files: int
    total_size: int
    languages: Dict[str, int]
    file_types: Dict[str, int]

# Config
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 24 * 60  # 1 day

# MongoDB connection
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
client = MongoClient(MONGO_URL)
db = client.codefuser

# Collections
users_collection = db.users
queries_collection = db.queries
sessions_collection = db.sessions

# Security
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
security = HTTPBearer()

app = FastAPI(title="CodeFuser Web API", version="1.0.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Prod'da frontend URL'i koyulacak
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Utility functions
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(credentials.token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user = users_collection.find_one({"email": email})
    if user is None:
        raise credentials_exception
    return user

def check_user_limits(user: Dict[str, Any]) -> Dict[str, Any]:
    """Kullanıcının günlük limitlerini kontrol et"""
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Bugün yapılan sorgu sayısını kontrol et
    today_queries = queries_collection.count_documents({
        "user_email": user["email"],
        "created_at": {"$gte": datetime.strptime(today, "%Y-%m-%d")}
    })
    
    # Üyelik paketine göre limitler
    subscription = user.get("subscription", "guest")
    limits = {
        "guest": {"daily_queries": 3, "file_prompts": False},
        "free": {"daily_queries": 3, "file_prompts": False},
        "starter": {"daily_queries": 100, "file_prompts": False},
        "pro": {"daily_queries": -1, "file_prompts": True}  # -1 = unlimited
    }
    
    user_limits = limits.get(subscription, limits["guest"])
    
    return {
        "subscription": subscription,
        "daily_queries_used": today_queries,
        "daily_queries_limit": user_limits["daily_queries"],
        "can_query": user_limits["daily_queries"] == -1 or today_queries < user_limits["daily_queries"],
        "file_prompts_enabled": user_limits["file_prompts"]
    }

# File Processing Logic (Desktop kodundan adapt edildi)
class WebFileProcessor:
    def __init__(self):
        self.templates = self._load_templates()
    
    def _load_templates(self) -> Dict[str, Dict[str, Any]]:
        """Desktop'taki template'leri web için yükle"""
        return {
            "16x_prompt": {
                "name": "16x Prompt Style",
                "template": """# 16x Prompt Analysis

## Project Overview
- **Project Name**: {project_name}
- **Total Files**: {file_count}
- **Primary Language**: {primary_language}
- **Generated**: {timestamp}

## Instructions
Analyze this codebase and provide insights on:
1. Code structure and architecture
2. Potential improvements
3. Security considerations
4. Performance optimizations

## Code Files

{file_contents}

## Analysis Request
Please provide a comprehensive analysis of this codebase focusing on code quality, maintainability, and best practices."""
            },
            "cursor_rules": {
                "name": "Cursor IDE Rules",
                "template": """# Cursor IDE Rules for {project_name}

## Project Context
This is a {primary_language} project with {file_count} files.
Generated on {timestamp}

## Coding Standards
- Follow {primary_language} best practices
- Maintain consistent code style
- Add meaningful comments
- Write unit tests for new features

## Key Files
{file_contents}

## Instructions for AI
When working on this project:
1. Understand the existing code structure
2. Maintain consistency with current patterns
3. Suggest improvements where appropriate
4. Focus on code quality and maintainability"""
            },
            "claude_project": {
                "name": "Claude Project Format",
                "template": """# {project_name} - Claude Project

## Project Information
- **Name**: {project_name}
- **Language**: {primary_language}
- **Files**: {file_count}
- **Generated**: {timestamp}

## Source Code

{file_contents}

## Next Steps
1. Review the code structure
2. Identify areas for improvement
3. Implement suggested changes
4. Test thoroughly

Please analyze this code and provide actionable feedback."""
            }
        }
    
    def process_files(self, request: ProcessRequest, user_email: str) -> Dict[str, Any]:
        """Ana dosya işleme fonksiyonu"""
        
        # Template uygula
        if request.template_id and request.template_id in self.templates:
            template = self.templates[request.template_id]["template"]
            processed_content = self._apply_template(template, request.files, request.general_prompt)
        else:
            processed_content = self._generate_custom_output(request.files, request.general_prompt, request.file_prompts)
        
        # Output format'a göre işle
        if request.output_format == "html":
            output = self._generate_html_output(processed_content, request.files)
        elif request.output_format == "txt":
            output = self._generate_text_output(processed_content, request.files)
        else:
            output = processed_content
        
        # Sorguyu veritabanına kaydet
        query_record = {
            "id": str(uuid.uuid4()),
            "user_email": user_email,
            "files_count": len(request.files),
            "general_prompt": request.general_prompt,
            "file_prompts": request.file_prompts,
            "output_format": request.output_format,
            "template_id": request.template_id,
            "created_at": datetime.utcnow(),
            "processed_content": processed_content[:1000] + "..." if len(processed_content) > 1000 else processed_content  # İlk 1000 karakter
        }
        queries_collection.insert_one(query_record)
        
        return {
            "output": output,
            "query_id": query_record["id"],
            "processed_at": query_record["created_at"].isoformat()
        }
    
    def _apply_template(self, template: str, files: List[Dict[str, Any]], general_prompt: str) -> str:
        """Template'i dosyalara uygula"""
        # Değişkenleri hesapla
        variables = {
            "project_name": "Web Project",
            "file_count": str(len(files)),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "primary_language": self._detect_primary_language(files),
            "file_contents": self._format_file_contents(files),
            "general_prompt": general_prompt
        }
        
        # Template'e değişkenleri uygula
        result = template
        for key, value in variables.items():
            result = result.replace(f"{{{key}}}", str(value))
        
        return result
    
    def _generate_custom_output(self, files: List[Dict[str, Any]], general_prompt: str, file_prompts: Dict[str, str]) -> str:
        """Custom output üret"""
        output = []
        
        if general_prompt:
            output.append(f"# General Instructions\n{general_prompt}\n")
        
        output.append("# Project Files\n")
        
        for file_info in files:
            file_path = file_info.get("name", "unknown")
            content = file_info.get("content", "")
            
            output.append(f"## File: {file_path}")
            
            # Dosyaya özel prompt varsa ekle
            if file_path in file_prompts:
                output.append(f"### File-specific instructions:\n{file_prompts[file_path]}\n")
            
            output.append(f"```\n{content}\n```\n")
        
        return "\n".join(output)
    
    def _format_file_contents(self, files: List[Dict[str, Any]]) -> str:
        """Dosya içeriklerini formatla"""
        contents = []
        
        for file_info in files:
            file_path = file_info.get("name", "unknown")
            content = file_info.get("content", "")
            extension = Path(file_path).suffix.lower()
            
            # Dil tespiti
            lang_map = {
                ".py": "python", ".js": "javascript", ".ts": "typescript",
                ".html": "html", ".css": "css", ".json": "json"
            }
            language = lang_map.get(extension, "text")
            
            contents.append(f"### File: {file_path}")
            contents.append(f"```{language}\n{content}\n```\n")
        
        return "\n".join(contents)
    
    def _detect_primary_language(self, files: List[Dict[str, Any]]) -> str:
        """Ana dili tespit et"""
        extensions = {}
        for file_info in files:
            ext = Path(file_info.get("name", "")).suffix.lower()
            extensions[ext] = extensions.get(ext, 0) + 1
        
        if not extensions:
            return "Unknown"
        
        primary_ext = max(extensions, key=extensions.get)
        lang_map = {
            ".py": "Python", ".js": "JavaScript", ".ts": "TypeScript",
            ".html": "HTML", ".css": "CSS", ".java": "Java"
        }
        return lang_map.get(primary_ext, "Unknown")
    
    def _generate_html_output(self, content: str, files: List[Dict[str, Any]]) -> str:
        """HTML output üret"""
        html_template = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CodeFuser Output</title>
    <style>
        body { 
            font-family: 'Segoe UI', system-ui, sans-serif; 
            line-height: 1.6; 
            margin: 40px; 
            background: #f5f7fa;
        }
        .container { 
            max-width: 1200px; 
            margin: 0 auto; 
            background: white; 
            padding: 40px; 
            border-radius: 8px; 
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .header { 
            text-align: center; 
            border-bottom: 2px solid #eee; 
            padding-bottom: 20px; 
            margin-bottom: 30px;
        }
        .header h1 { 
            color: #2c3e50; 
            margin: 0;
        }
        .meta { 
            color: #7f8c8d; 
            margin-top: 10px;
        }
        pre { 
            background: #f8f9fa; 
            padding: 20px; 
            border-radius: 6px; 
            overflow-x: auto; 
            border: 1px solid #e9ecef;
        }
        .file-section { 
            margin: 30px 0; 
            border: 1px solid #dee2e6; 
            border-radius: 6px; 
            overflow: hidden;
        }
        .file-header { 
            background: #f8f9fa; 
            padding: 15px 20px; 
            font-weight: 600; 
            color: #495057;
        }
        .file-content { 
            padding: 20px;
        }
        .copy-btn {
            background: #007bff;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 4px;
            cursor: pointer;
            float: right;
            margin-top: -5px;
        }
        .copy-btn:hover {
            background: #0056b3;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚀 CodeFuser Output</h1>
            <div class="meta">
                Generated on {timestamp}<br>
                {file_count} files processed
            </div>
        </div>
        
        <div class="content">
            <pre>{content}</pre>
        </div>
        
        <script>
            function copyToClipboard(text) {
                navigator.clipboard.writeText(text).then(() => {
                    alert('Copied to clipboard!');
                });
            }
        </script>
    </div>
</body>
</html>
        """
        
        return html_template.format(
            content=content.replace("<", "&lt;").replace(">", "&gt;"),
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            file_count=len(files)
        )
    
    def _generate_text_output(self, content: str, files: List[Dict[str, Any]]) -> str:
        """Text output üret"""
        header = f"""# CodeFuser Output
# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
# Total Files: {len(files)}

{'='*80}

"""
        return header + content

# API Routes

@app.get("/")
async def root():
    return {"message": "CodeFuser Web API", "version": "1.0.0"}

@app.post("/api/auth/signup")
async def signup(user_data: UserSignup):
    # Email kontrolü
    if users_collection.find_one({"email": user_data.email}):
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Kullanıcı oluştur
    user = {
        "email": user_data.email,
        "name": user_data.name,
        "password": hash_password(user_data.password),
        "subscription": "free",
        "created_at": datetime.utcnow(),
        "is_active": True
    }
    
    users_collection.insert_one(user)
    
    # Token oluştur
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["email"]}, expires_delta=access_token_expires
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "email": user["email"],
            "name": user["name"],
            "subscription": user["subscription"]
        }
    }

@app.post("/api/auth/login")
async def login(user_data: UserLogin):
    user = users_collection.find_one({"email": user_data.email})
    
    if not user or not verify_password(user_data.password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["email"]}, expires_delta=access_token_expires
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "email": user["email"],
            "name": user["name"],
            "subscription": user["subscription"]
        }
    }

@app.get("/api/auth/me")
async def get_current_user_info(current_user: dict = Depends(get_current_user)):
    limits = check_user_limits(current_user)
    
    return {
        "email": current_user["email"],
        "name": current_user["name"],
        "subscription": current_user["subscription"],
        "limits": limits
    }

@app.post("/api/process")
async def process_files(
    request: ProcessRequest,
    current_user: dict = Depends(get_current_user)
):
    # Limit kontrolü
    limits = check_user_limits(current_user)
    
    if not limits["can_query"]:
        raise HTTPException(
            status_code=429,
            detail=f"Daily query limit exceeded. You have used {limits['daily_queries_used']}/{limits['daily_queries_limit']} queries today."
        )
    
    # File prompt kontrolü
    if request.file_prompts and not limits["file_prompts_enabled"]:
        raise HTTPException(
            status_code=403,
            detail="File-specific prompts are only available for Pro users."
        )
    
    # Dosya işleme
    processor = WebFileProcessor()
    result = processor.process_files(request, current_user["email"])
    
    return result

@app.post("/api/process/guest")
async def process_files_guest(request: ProcessRequest):
    """Misafir kullanıcılar için (3 hak)"""
    
    # Session kontrolü (IP based simple tracking)
    # Gerçek üretimde daha sofistike olmalı
    
    # Sadece genel prompt, file prompt yok
    if request.file_prompts:
        raise HTTPException(
            status_code=403,
            detail="File-specific prompts require registration."
        )
    
    # Dosya işleme
    processor = WebFileProcessor()
    result = processor.process_files(request, "guest")
    
    return result

@app.get("/api/templates")
async def get_templates():
    processor = WebFileProcessor()
    return {"templates": processor.templates}

@app.get("/api/queries")
async def get_user_queries(current_user: dict = Depends(get_current_user)):
    queries = list(queries_collection.find(
        {"user_email": current_user["email"]},
        {"processed_content": 0}  # Exclude large content from list
    ).sort("created_at", -1).limit(50))
    
    # Convert ObjectId to string
    for query in queries:
        query["_id"] = str(query["_id"])
        query["created_at"] = query["created_at"].isoformat()
    
    return {"queries": queries}

@app.get("/api/stats")
async def get_stats():
    total_users = users_collection.count_documents({})
    total_queries = queries_collection.count_documents({})
    
    return {
        "total_users": total_users,
        "total_queries": total_queries,
        "templates_available": len(WebFileProcessor().templates)
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)