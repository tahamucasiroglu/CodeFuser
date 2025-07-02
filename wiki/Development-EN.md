# 👨‍💻 Development Guide

Complete guide for contributing to CodeFuser v2.0, extending functionality, and creating custom integrations.

## 🚀 Getting Started

### Development Environment Setup

#### Prerequisites
```bash
# Required Software
- Python 3.8+ (3.9+ recommended)
- Git
- Code Editor (VS Code, PyCharm, etc.)
- Virtual Environment tool (venv, conda, virtualenv)

# Optional Tools
- Docker (for containerized development)
- Node.js (for web-based extensions)
- PostgreSQL/SQLite (for database features)
```

#### Clone and Setup
```bash
# Clone the repository
git clone https://github.com/tahamucasiroglu/CodeFuser.git
cd CodeFuser

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Install in development mode
pip install -e .
```

#### Development Dependencies
```txt
# requirements-dev.txt
pytest>=7.0.0
pytest-cov>=4.0.0
black>=22.0.0
flake8>=5.0.0
mypy>=1.0.0
pre-commit>=2.20.0
sphinx>=5.0.0
sphinx-rtd-theme>=1.0.0
```

### Project Structure

#### Core Architecture
```
CodeFuser/
├── src/                          # Main source code
│   ├── __init__.py
│   ├── main_app.py              # Main application entry
│   ├── file_tree_widget.py     # File tree component
│   ├── file_prompt_dialog.py   # Custom prompt dialog
│   ├── export_manager.py       # Export functionality
│   ├── template_manager.py     # Template system
│   ├── git_integration.py      # Git features
│   ├── smart_filters.py        # Filtering system
│   └── utils/                   # Utility modules
│       ├── file_utils.py
│       ├── config_manager.py
│       └── localization.py
├── config/                      # Configuration files
│   ├── default_settings.json
│   └── user_settings.json
├── templates/                   # Built-in templates
│   ├── 16x_prompt.json
│   ├── claude_project.json
│   └── ...
├── locales/                     # Internationalization
│   ├── en.json
│   └── tr.json
├── tests/                       # Test suite
│   ├── unit/
│   ├── integration/
│   └── fixtures/
├── docs/                        # Documentation
├── assets/                      # Static assets
├── main.py                      # Entry point
├── build_exe.py                # Build script
└── requirements.txt
```

#### Module Dependencies
```python
# Core Dependencies
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import json
import os
import subprocess
from pathlib import Path
from typing import Dict, List, Optional, Union

# Export Dependencies
from docx import Document
from reportlab.pdfgen import canvas
import html
import base64

# Git Integration
import git
from git import Repo, InvalidGitRepositoryError

# Template System
import jinja2
from jinja2 import Template, Environment
```

## 🏗️ Architecture Overview

### Core Components

#### 1. Main Application (main_app.py)
```python
class CodeFuserApp:
    """Main application controller"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.config_manager = ConfigManager()
        self.template_manager = TemplateManager()
        self.export_manager = ExportManager()
        self.file_tree = FileTreeWidget(self.root)
        
    def initialize_ui(self):
        """Setup main user interface"""
        pass
        
    def handle_export(self):
        """Handle export operations"""
        pass
```

#### 2. File Tree Widget (file_tree_widget.py)
```python
class FileTreeWidget:
    """Enhanced file tree with custom prompts"""
    
    def __init__(self, parent):
        self.parent = parent
        self.selected_files = set()
        self.file_prompts = {}  # File-specific prompts
        
    def populate_tree(self, root_path: str):
        """Populate tree with files and folders"""
        pass
        
    def handle_document_icon_click(self, file_path: str):
        """Handle custom prompt icon clicks"""
        pass
        
    def apply_row_color(self, file_path: str):
        """Apply color coding based on file status"""
        pass
```

#### 3. Export Manager (export_manager.py)
```python
class ExportManager:
    """Handle all export operations"""
    
    def __init__(self):
        self.supported_formats = ['txt', 'html', 'docx', 'pdf']
        
    def export_to_format(self, format_type: str, data: dict, output_path: str):
        """Export data to specified format"""
        exporters = {
            'txt': self._export_txt,
            'html': self._export_html,
            'docx': self._export_docx,
            'pdf': self._export_pdf
        }
        return exporters[format_type](data, output_path)
```

#### 4. Template Manager (template_manager.py)
```python
class TemplateManager:
    """Template system management"""
    
    def __init__(self):
        self.templates = {}
        self.load_templates()
        
    def load_templates(self):
        """Load all available templates"""
        pass
        
    def render_template(self, template_name: str, variables: dict) -> str:
        """Render template with variables"""
        pass
        
    def validate_template(self, template_data: dict) -> bool:
        """Validate template structure"""
        pass
```

### Design Patterns

#### 1. Observer Pattern
```python
class EventManager:
    """Central event management"""
    
    def __init__(self):
        self.listeners = {}
        
    def subscribe(self, event_type: str, callback):
        """Subscribe to events"""
        if event_type not in self.listeners:
            self.listeners[event_type] = []
        self.listeners[event_type].append(callback)
        
    def notify(self, event_type: str, data=None):
        """Notify all listeners"""
        for callback in self.listeners.get(event_type, []):
            callback(data)
```

#### 2. Strategy Pattern
```python
class ExportStrategy:
    """Base export strategy"""
    
    def export(self, data: dict, output_path: str):
        raise NotImplementedError
        
class HTMLExportStrategy(ExportStrategy):
    """HTML export implementation"""
    
    def export(self, data: dict, output_path: str):
        # HTML-specific export logic
        pass
```

#### 3. Factory Pattern
```python
class ExportFactory:
    """Factory for creating exporters"""
    
    @staticmethod
    def create_exporter(format_type: str) -> ExportStrategy:
        exporters = {
            'html': HTMLExportStrategy,
            'pdf': PDFExportStrategy,
            'docx': DOCXExportStrategy,
            'txt': TXTExportStrategy
        }
        return exporters[format_type]()
```

## 🔧 Development Workflow

### Code Style and Standards

#### Python Style Guide
```python
# Use Black for formatting
black src/ tests/

# Use flake8 for linting
flake8 src/ tests/

# Use mypy for type checking
mypy src/

# Example properly formatted code
def process_files(
    file_paths: List[str], 
    output_format: str,
    template_name: Optional[str] = None
) -> Dict[str, Any]:
    """
    Process files for export.
    
    Args:
        file_paths: List of file paths to process
        output_format: Target export format
        template_name: Optional template to use
        
    Returns:
        Dictionary containing processed data
        
    Raises:
        ValueError: If format is not supported
        FileNotFoundError: If files don't exist
    """
    if output_format not in SUPPORTED_FORMATS:
        raise ValueError(f"Unsupported format: {output_format}")
        
    result = {
        "files": [],
        "metadata": {},
        "statistics": {}
    }
    
    for file_path in file_paths:
        if not Path(file_path).exists():
            raise FileNotFoundError(f"File not found: {file_path}")
            
        # Process file...
        
    return result
```

#### Git Workflow
```bash
# Feature development workflow
git checkout main
git pull origin main
git checkout -b feature/new-export-format

# Make changes...
git add .
git commit -m "feat: add new export format support

- Add XML export functionality
- Update export manager
- Add tests for XML export"

# Push and create PR
git push origin feature/new-export-format
# Create pull request on GitHub
```

#### Pre-commit Hooks
```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: 22.3.0
    hooks:
      - id: black
        language_version: python3.9

  - repo: https://github.com/pycqa/flake8
    rev: 4.0.1
    hooks:
      - id: flake8

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v0.950
    hooks:
      - id: mypy
```

### Testing Strategy

#### Unit Tests
```python
# tests/unit/test_template_manager.py
import pytest
from src.template_manager import TemplateManager

class TestTemplateManager:
    
    @pytest.fixture
    def template_manager(self):
        return TemplateManager()
        
    def test_load_templates(self, template_manager):
        """Test template loading"""
        template_manager.load_templates()
        assert len(template_manager.templates) > 0
        
    def test_render_template(self, template_manager):
        """Test template rendering"""
        template_data = {
            "name": "Test Template",
            "prompt": "Analyze {{PROJECT_NAME}} for security issues",
            "variables": {
                "PROJECT_NAME": {"type": "string", "default": "TestProject"}
            }
        }
        
        rendered = template_manager.render_template(template_data, {
            "PROJECT_NAME": "MyApp"
        })
        
        assert "Analyze MyApp for security issues" in rendered
        
    def test_invalid_template(self, template_manager):
        """Test validation of invalid templates"""
        invalid_template = {"name": "Invalid"}  # Missing required fields
        
        with pytest.raises(ValueError):
            template_manager.validate_template(invalid_template)
```

#### Integration Tests
```python
# tests/integration/test_export_workflow.py
import pytest
import tempfile
from pathlib import Path
from src.main_app import CodeFuserApp

class TestExportWorkflow:
    
    @pytest.fixture
    def app(self):
        return CodeFuserApp()
        
    @pytest.fixture
    def sample_project(self):
        """Create sample project for testing"""
        with tempfile.TemporaryDirectory() as temp_dir:
            project_dir = Path(temp_dir)
            
            # Create sample files
            (project_dir / "main.py").write_text("print('Hello World')")
            (project_dir / "utils.py").write_text("def helper(): pass")
            
            yield project_dir
            
    def test_full_export_workflow(self, app, sample_project):
        """Test complete export workflow"""
        # Setup
        app.file_tree.populate_tree(str(sample_project))
        app.file_tree.select_all_files()
        
        # Set template and export
        app.set_template("16x_prompt")
        
        with tempfile.NamedTemporaryFile(suffix=".html") as output_file:
            result = app.export_manager.export_to_format(
                "html", 
                app.get_export_data(),
                output_file.name
            )
            
            assert result.success
            assert Path(output_file.name).exists()
            
            # Verify content
            content = Path(output_file.name).read_text()
            assert "Hello World" in content
            assert "16x Prompt" in content
```

#### Test Configuration
```ini
# pytest.ini
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = 
    --cov=src
    --cov-report=html
    --cov-report=term-missing
    --cov-fail-under=80
```

## 🔌 Plugin Development

### Plugin Architecture

#### Plugin Interface
```python
# src/plugins/base_plugin.py
from abc import ABC, abstractmethod
from typing import Dict, Any

class BasePlugin(ABC):
    """Base class for all plugins"""
    
    def __init__(self):
        self.name = ""
        self.version = "1.0.0"
        self.description = ""
        
    @abstractmethod
    def initialize(self, app_context: Dict[str, Any]):
        """Initialize plugin with app context"""
        pass
        
    @abstractmethod
    def get_capabilities(self) -> Dict[str, Any]:
        """Return plugin capabilities"""
        pass
        
    def cleanup(self):
        """Cleanup resources"""
        pass
```

#### Export Plugin Example
```python
# plugins/xml_exporter.py
from src.plugins.base_plugin import BasePlugin
import xml.etree.ElementTree as ET

class XMLExportPlugin(BasePlugin):
    """XML export plugin"""
    
    def __init__(self):
        super().__init__()
        self.name = "XML Exporter"
        self.version = "1.0.0"
        self.description = "Export code analysis to XML format"
        
    def initialize(self, app_context):
        """Register XML export capability"""
        export_manager = app_context['export_manager']
        export_manager.register_format('xml', self.export_xml)
        
    def get_capabilities(self):
        return {
            "export_formats": ["xml"],
            "features": ["structured_data", "schema_validation"]
        }
        
    def export_xml(self, data: dict, output_path: str):
        """Export data to XML format"""
        root = ET.Element("code_analysis")
        
        # Add metadata
        metadata = ET.SubElement(root, "metadata")
        ET.SubElement(metadata, "generated_at").text = data.get("timestamp", "")
        ET.SubElement(metadata, "total_files").text = str(data.get("file_count", 0))
        
        # Add files
        files_elem = ET.SubElement(root, "files")
        for file_data in data.get("files", []):
            file_elem = ET.SubElement(files_elem, "file")
            file_elem.set("path", file_data["path"])
            
            if file_data.get("custom_prompt"):
                prompt_elem = ET.SubElement(file_elem, "custom_prompt")
                prompt_elem.text = file_data["custom_prompt"]
                
            content_elem = ET.SubElement(file_elem, "content")
            content_elem.text = file_data["content"]
            
        # Write to file
        tree = ET.ElementTree(root)
        tree.write(output_path, encoding="utf-8", xml_declaration=True)
```

#### Plugin Manifest
```json
{
  "name": "XML Exporter",
  "version": "1.0.0",
  "description": "Export code analysis to XML format",
  "author": "Developer Name",
  "entry_point": "xml_exporter.XMLExportPlugin",
  "dependencies": {
    "python": ">=3.8",
    "packages": []
  },
  "capabilities": {
    "export_formats": ["xml"],
    "hooks": ["pre_export", "post_export"]
  },
  "configuration": {
    "xml_schema": "schema.xsd",
    "validation": true,
    "pretty_print": true
  }
}
```

### Custom Template Development

#### Template Structure
```json
{
  "name": "Security Audit Template",
  "description": "Comprehensive security analysis template",
  "version": "1.0.0",
  "author": "Security Team",
  "category": "security",
  "variables": {
    "COMPLIANCE_FRAMEWORK": {
      "type": "select",
      "options": ["OWASP", "NIST", "ISO27001", "PCI-DSS"],
      "default": "OWASP",
      "description": "Security compliance framework"
    },
    "SECURITY_LEVEL": {
      "type": "select",
      "options": ["basic", "standard", "comprehensive"],
      "default": "standard",
      "description": "Depth of security analysis"
    },
    "FOCUS_AREAS": {
      "type": "multiselect",
      "options": [
        "authentication", "authorization", "input_validation",
        "data_protection", "session_management", "error_handling"
      ],
      "default": ["authentication", "authorization"],
      "description": "Security areas to focus on"
    }
  },
  "conditional_sections": {
    "include_compliance_check": "{{COMPLIANCE_FRAMEWORK}} != 'custom'",
    "include_advanced_analysis": "{{SECURITY_LEVEL}} == 'comprehensive'"
  },
  "prompt": "# Security Analysis for {{PROJECT_NAME}}\n\nPerform a {{SECURITY_LEVEL}} security audit focusing on {{COMPLIANCE_FRAMEWORK}} compliance.\n\n## Analysis Scope\n{{#each FOCUS_AREAS}}\n- {{this}}\n{{/each}}\n\n{{#if include_compliance_check}}\n## Compliance Requirements\nEnsure code meets {{COMPLIANCE_FRAMEWORK}} standards.\n{{/if}}\n\n{{#if include_advanced_analysis}}\n## Advanced Security Analysis\n- Threat modeling\n- Attack surface analysis\n- Cryptographic implementation review\n{{/if}}\n\nProvide specific findings with severity ratings and remediation steps."
}
```

#### Template Engine Integration
```python
# src/template_engine.py
from jinja2 import Environment, FileSystemLoader, Template
from typing import Dict, Any

class TemplateEngine:
    """Advanced template rendering engine"""
    
    def __init__(self, template_dirs: List[str]):
        self.env = Environment(loader=FileSystemLoader(template_dirs))
        self.env.globals.update({
            'project_name': self._get_project_name,
            'current_date': self._get_current_date,
            'file_count': self._get_file_count
        })
        
    def render_template(self, template_data: dict, context: dict) -> str:
        """Render template with advanced features"""
        template = Template(template_data['prompt'])
        
        # Process conditional sections
        processed_context = self._process_conditionals(
            template_data, context
        )
        
        # Add built-in variables
        processed_context.update(self._get_builtin_variables(context))
        
        return template.render(**processed_context)
        
    def _process_conditionals(self, template_data: dict, context: dict) -> dict:
        """Process conditional template sections"""
        result = context.copy()
        
        for condition_name, condition_expr in template_data.get('conditional_sections', {}).items():
            # Evaluate condition
            try:
                condition_result = self._evaluate_condition(condition_expr, context)
                result[condition_name] = condition_result
            except Exception as e:
                logger.warning(f"Failed to evaluate condition {condition_name}: {e}")
                result[condition_name] = False
                
        return result
```

## 🌐 API Development

### REST API Interface

#### API Server Setup
```python
# src/api/server.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import threading

class CodeFuserAPI:
    """REST API for CodeFuser"""
    
    def __init__(self, app_instance):
        self.app = Flask(__name__)
        CORS(self.app)
        self.codefuser_app = app_instance
        self.setup_routes()
        
    def setup_routes(self):
        """Setup API routes"""
        
        @self.app.route('/api/v1/scan', methods=['POST'])
        def scan_project():
            """Scan project directory"""
            data = request.json
            project_path = data.get('path')
            
            if not project_path:
                return jsonify({'error': 'Project path required'}), 400
                
            try:
                files = self.codefuser_app.scan_directory(project_path)
                return jsonify({
                    'success': True,
                    'files': files,
                    'count': len(files)
                })
            except Exception as e:
                return jsonify({'error': str(e)}), 500
                
        @self.app.route('/api/v1/export', methods=['POST'])
        def export_analysis():
            """Export code analysis"""
            data = request.json
            
            try:
                result = self.codefuser_app.export_manager.export_to_format(
                    data.get('format', 'html'),
                    data.get('export_data'),
                    data.get('output_path')
                )
                
                return jsonify({
                    'success': True,
                    'output_path': result.output_path,
                    'file_size': result.file_size
                })
            except Exception as e:
                return jsonify({'error': str(e)}), 500
                
        @self.app.route('/api/v1/templates', methods=['GET'])
        def get_templates():
            """Get available templates"""
            templates = self.codefuser_app.template_manager.get_templates()
            return jsonify({
                'templates': [
                    {
                        'name': t.name,
                        'description': t.description,
                        'version': t.version,
                        'variables': t.variables
                    }
                    for t in templates
                ]
            })
            
    def start_server(self, host='localhost', port=5000):
        """Start API server in separate thread"""
        def run_server():
            self.app.run(host=host, port=port, debug=False)
            
        server_thread = threading.Thread(target=run_server, daemon=True)
        server_thread.start()
        return server_thread
```

#### API Client Library
```python
# src/api/client.py
import requests
from typing import Dict, List, Optional

class CodeFuserClient:
    """Python client for CodeFuser API"""
    
    def __init__(self, base_url: str = "http://localhost:5000"):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        
    def scan_project(self, project_path: str) -> Dict:
        """Scan project directory"""
        response = self.session.post(
            f"{self.base_url}/api/v1/scan",
            json={'path': project_path}
        )
        response.raise_for_status()
        return response.json()
        
    def export_analysis(
        self, 
        export_data: Dict,
        output_path: str,
        format_type: str = 'html'
    ) -> Dict:
        """Export code analysis"""
        response = self.session.post(
            f"{self.base_url}/api/v1/export",
            json={
                'export_data': export_data,
                'output_path': output_path,
                'format': format_type
            }
        )
        response.raise_for_status()
        return response.json()
        
    def get_templates(self) -> List[Dict]:
        """Get available templates"""
        response = self.session.get(f"{self.base_url}/api/v1/templates")
        response.raise_for_status()
        return response.json()['templates']

# Usage example
client = CodeFuserClient()
scan_result = client.scan_project('/path/to/project')
templates = client.get_templates()

export_data = {
    'files': scan_result['files'],
    'template': templates[0],
    'custom_prompts': {}
}

export_result = client.export_analysis(
    export_data, 
    '/path/to/output.html',
    'html'
)
```

## 📦 Build and Distribution

### PyInstaller Configuration

#### Build Script (build_exe.py)
```python
# build_exe.py
import PyInstaller.__main__
import sys
import os
from pathlib import Path

def build_executable():
    """Build standalone executable"""
    
    # Define paths
    src_path = Path("src")
    main_file = "main.py"
    
    # PyInstaller arguments
    args = [
        main_file,
        "--onefile",
        "--windowed",
        "--name=CodeFuser_v2.0",
        "--icon=assets/icon.ico",
        f"--distpath=dist/",
        f"--workpath=build/",
        "--clean",
        
        # Add data files
        "--add-data=config;config",
        "--add-data=templates;templates",
        "--add-data=locales;locales",
        "--add-data=assets;assets",
        
        # Hidden imports
        "--hidden-import=tkinter",
        "--hidden-import=tkinter.ttk",
        "--hidden-import=docx",
        "--hidden-import=reportlab",
        "--hidden-import=git",
        
        # Exclude unnecessary modules
        "--exclude-module=pytest",
        "--exclude-module=sphinx",
        "--exclude-module=black",
        
        # Optimization
        "--optimize=2",
        "--strip",
    ]
    
    # Add source files to path
    for py_file in src_path.glob("**/*.py"):
        args.append(f"--additional-hooks-dir={py_file.parent}")
    
    # Run PyInstaller
    PyInstaller.__main__.run(args)
    
    # Create portable package
    create_portable_package()

def create_portable_package():
    """Create portable package with all resources"""
    import shutil
    
    dist_dir = Path("dist")
    portable_dir = dist_dir / "CodeFuser_Portable"
    
    # Create directory structure
    portable_dir.mkdir(exist_ok=True)
    
    # Copy executable
    exe_file = dist_dir / "CodeFuser_v2.0.exe"
    if exe_file.exists():
        shutil.copy2(exe_file, portable_dir / "CodeFuser.exe")
    
    # Copy resources
    for resource_dir in ["config", "templates", "locales"]:
        if Path(resource_dir).exists():
            shutil.copytree(
                resource_dir, 
                portable_dir / resource_dir,
                dirs_exist_ok=True
            )
    
    # Create README
    readme_content = create_portable_readme()
    (portable_dir / "README.txt").write_text(readme_content, encoding='utf-8')
    
    print(f"Portable package created: {portable_dir}")

def create_portable_readme():
    """Create README for portable package"""
    return """
CodeFuser v2.0 - Portable Edition
=================================

Bu taşınabilir sürümde:
- Kurulum gerektirmez
- Python gerektirmez  
- Tüm özellikler dahil
- Ayarlar config/ klasöründe saklanır

Kullanım:
1. CodeFuser.exe dosyasını çalıştırın
2. Proje klasörünüzü seçin
3. Dosyaları seçin ve analiz edin
4. Çıktıyı istediğiniz formatta export edin

Daha fazla bilgi için:
https://github.com/tahamucasiroglu/CodeFuser/wiki
"""

if __name__ == "__main__":
    build_executable()
```

#### Spec File Customization
```python
# codefuser.spec
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('config', 'config'),
        ('templates', 'templates'),
        ('locales', 'locales'),
        ('assets', 'assets'),
    ],
    hiddenimports=[
        'tkinter',
        'tkinter.ttk',
        'docx',
        'reportlab.pdfgen',
        'git',
        'jinja2',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'pytest',
        'sphinx',
        'black',
        'mypy',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='CodeFuser_v2.0',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='assets/icon.ico',
)
```

### CI/CD Pipeline

#### GitHub Actions Workflow
```yaml
# .github/workflows/build.yml
name: Build and Release

on:
  push:
    tags:
      - 'v*'
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, '3.10', 3.11]

    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v3
      with:
        python-version: ${{ matrix.python-version }}
        
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install -r requirements-dev.txt
        
    - name: Run tests
      run: |
        pytest tests/ --cov=src --cov-report=xml
        
    - name: Upload coverage
      uses: codecov/codecov-action@v3

  build-windows:
    needs: test
    runs-on: windows-latest
    if: startsWith(github.ref, 'refs/tags/')

    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v3
      with:
        python-version: '3.9'
        
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install pyinstaller
        
    - name: Build executable
      run: |
        python build_exe.py
        
    - name: Create release archive
      run: |
        Compress-Archive -Path dist/CodeFuser_Portable/* -DestinationPath CodeFuser_v2.0_Windows.zip
        
    - name: Upload release artifact
      uses: actions/upload-artifact@v3
      with:
        name: CodeFuser_Windows
        path: CodeFuser_v2.0_Windows.zip

  release:
    needs: [test, build-windows]
    runs-on: ubuntu-latest
    if: startsWith(github.ref, 'refs/tags/')

    steps:
    - name: Download artifacts
      uses: actions/download-artifact@v3
      
    - name: Create Release
      uses: softprops/action-gh-release@v1
      with:
        files: |
          CodeFuser_Windows/CodeFuser_v2.0_Windows.zip
        body: |
          ## CodeFuser v2.0 Release
          
          ### New Features
          - File-specific custom prompts
          - Enhanced Git integration
          - Improved export formats
          - Advanced filtering system
          
          ### Downloads
          - Windows Standalone: CodeFuser_v2.0_Windows.zip
          
          ### Installation
          1. Download the appropriate package
          2. Extract to desired location
          3. Run CodeFuser.exe (Windows)
```

## 📚 Documentation

### Code Documentation

#### Docstring Standards
```python
def export_to_format(
    self,
    format_type: str,
    data: Dict[str, Any],
    output_path: str,
    options: Optional[Dict[str, Any]] = None
) -> ExportResult:
    """
    Export processed data to specified format.
    
    This method handles the conversion of analyzed code data into
    various output formats including HTML, PDF, DOCX, and TXT.
    
    Args:
        format_type: Target export format ('html', 'pdf', 'docx', 'txt')
        data: Processed code analysis data containing:
            - files: List of file data dictionaries
            - metadata: Analysis metadata
            - template: Applied template information
            - custom_prompts: File-specific prompts
        output_path: Absolute path for output file
        options: Optional format-specific configuration:
            - html: {'syntax_highlighting': bool, 'theme': str}
            - pdf: {'page_size': str, 'font_size': int}
            - docx: {'font_family': str, 'include_toc': bool}
            - txt: {'encoding': str, 'line_ending': str}
    
    Returns:
        ExportResult object containing:
            - success: Boolean indicating operation success
            - output_path: Path to generated file
            - file_size: Size of generated file in bytes
            - generation_time: Time taken for export
            - warnings: List of non-fatal issues encountered
    
    Raises:
        ValueError: If format_type is not supported
        FileNotFoundError: If output directory doesn't exist
        PermissionError: If insufficient permissions for output_path
        ExportError: If export process fails
    
    Example:
        >>> exporter = ExportManager()
        >>> data = {
        ...     'files': [{'path': 'main.py', 'content': 'print("hello")'}],
        ...     'metadata': {'project_name': 'MyApp'},
        ...     'template': '16x_prompt'
        ... }
        >>> result = exporter.export_to_format('html', data, '/tmp/output.html')
        >>> print(f"Export {'succeeded' if result.success else 'failed'}")
        Export succeeded
    
    Note:
        Large exports (>100MB) may take significant time and memory.
        Consider using chunked export for very large codebases.
    
    See Also:
        - get_supported_formats(): List of available export formats
        - validate_export_data(): Validate data before export
        - ExportResult: Details on return value structure
    """
```

#### API Documentation
```python
# src/api/docs.py
from flask import Flask
from flask_restx import Api, Resource, fields

# API documentation with Swagger
api = Api(
    doc='/docs/',
    title='CodeFuser API',
    version='2.0',
    description='REST API for CodeFuser code analysis tool'
)

# Define models for documentation
scan_model = api.model('ScanRequest', {
    'path': fields.String(required=True, description='Project directory path'),
    'filters': fields.Raw(description='Optional filtering criteria'),
    'options': fields.Raw(description='Scan options')
})

scan_response = api.model('ScanResponse', {
    'success': fields.Boolean(description='Operation success status'),
    'files': fields.List(fields.Raw, description='List of discovered files'),
    'count': fields.Integer(description='Total file count'),
    'statistics': fields.Raw(description='Scan statistics')
})

@api.route('/scan')
class ScanProject(Resource):
    @api.expect(scan_model)
    @api.marshal_with(scan_response)
    @api.doc(responses={
        200: 'Success',
        400: 'Invalid request data',
        500: 'Internal server error'
    })
    def post(self):
        """Scan project directory for code files"""
        pass
```

## 🔍 Advanced Features

### Custom Export Formats

#### Creating New Exporters
```python
# src/exporters/markdown_exporter.py
from .base_exporter import BaseExporter
from typing import Dict, Any

class MarkdownExporter(BaseExporter):
    """Export to Markdown format with GitHub flavor"""
    
    def __init__(self):
        super().__init__()
        self.format_name = "markdown"
        self.file_extension = ".md"
        
    def export(self, data: Dict[str, Any], output_path: str) -> ExportResult:
        """Export data to Markdown format"""
        try:
            content = self._generate_markdown(data)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(content)
                
            return ExportResult(
                success=True,
                output_path=output_path,
                file_size=os.path.getsize(output_path)
            )
            
        except Exception as e:
            return ExportResult(
                success=False,
                error=str(e)
            )
            
    def _generate_markdown(self, data: Dict[str, Any]) -> str:
        """Generate Markdown content"""
        lines = []
        
        # Header
        lines.append(f"# {data.get('project_name', 'Code Analysis')}")
        lines.append("")
        lines.append(f"*Generated: {data.get('timestamp')}*")
        lines.append("")
        
        # Table of contents
        lines.append("## Table of Contents")
        lines.append("")
        for i, file_data in enumerate(data.get('files', []), 1):
            file_path = file_data['path']
            anchor = file_path.replace('/', '').replace('.', '').lower()
            lines.append(f"{i}. [{file_path}](#{anchor})")
        lines.append("")
        
        # Prompt section
        if data.get('prompt'):
            lines.append("## Analysis Prompt")
            lines.append("")
            lines.append("```")
            lines.append(data['prompt'])
            lines.append("```")
            lines.append("")
        
        # File contents
        for file_data in data.get('files', []):
            self._add_file_section(lines, file_data)
            
        return "\n".join(lines)
        
    def _add_file_section(self, lines: list, file_data: Dict[str, Any]):
        """Add individual file section to markdown"""
        file_path = file_data['path']
        anchor = file_path.replace('/', '').replace('.', '').lower()
        
        lines.append(f"## {file_path} {{#{anchor}}}")
        lines.append("")
        
        # Custom prompt if exists
        if file_data.get('custom_prompt'):
            lines.append("> **Custom Analysis Prompt:**")
            lines.append(f"> {file_data['custom_prompt']}")
            lines.append("")
        
        # Detect language for syntax highlighting
        language = self._detect_language(file_path)
        
        lines.append(f"```{language}")
        lines.append(file_data['content'])
        lines.append("```")
        lines.append("")
        lines.append("---")
        lines.append("")
        
    def _detect_language(self, file_path: str) -> str:
        """Detect programming language from file extension"""
        ext_map = {
            '.py': 'python',
            '.js': 'javascript',
            '.ts': 'typescript',
            '.jsx': 'jsx',
            '.tsx': 'tsx',
            '.html': 'html',
            '.css': 'css',
            '.scss': 'scss',
            '.java': 'java',
            '.cs': 'csharp',
            '.php': 'php',
            '.rb': 'ruby',
            '.go': 'go',
            '.rs': 'rust',
            '.cpp': 'cpp',
            '.c': 'c',
            '.sql': 'sql',
            '.json': 'json',
            '.xml': 'xml',
            '.yaml': 'yaml',
            '.yml': 'yaml',
        }
        
        ext = Path(file_path).suffix.lower()
        return ext_map.get(ext, 'text')
```

### AI Integration Features

#### OpenAI Integration
```python
# src/ai/openai_integration.py
import openai
from typing import Dict, List, Optional

class OpenAIIntegration:
    """Integration with OpenAI API for enhanced analysis"""
    
    def __init__(self, api_key: str):
        openai.api_key = api_key
        
    def analyze_code_quality(
        self, 
        code_content: str, 
        file_path: str,
        custom_prompt: Optional[str] = None
    ) -> Dict[str, Any]:
        """Analyze code quality using GPT models"""
        
        base_prompt = f"""
        Analyze the following code for quality, security, and best practices:
        
        File: {file_path}
        
        Focus areas:
        - Code structure and organization
        - Potential bugs and issues
        - Security vulnerabilities
        - Performance optimizations
        - Best practice compliance
        
        Code:
        ```
        {code_content}
        ```
        """
        
        if custom_prompt:
            base_prompt += f"\n\nAdditional instructions: {custom_prompt}"
            
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an expert code reviewer and security analyst."},
                    {"role": "user", "content": base_prompt}
                ],
                max_tokens=2000,
                temperature=0.1
            )
            
            return {
                'success': True,
                'analysis': response.choices[0].message.content,
                'tokens_used': response.usage.total_tokens,
                'model': response.model
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
            
    def generate_documentation(
        self, 
        code_files: List[Dict[str, str]]
    ) -> Dict[str, Any]:
        """Generate documentation for code files"""
        
        combined_code = "\n\n".join([
            f"// {file_data['path']}\n{file_data['content']}"
            for file_data in code_files
        ])
        
        prompt = f"""
        Generate comprehensive documentation for this codebase:
        
        {combined_code}
        
        Include:
        1. Overview and purpose
        2. Architecture explanation
        3. API documentation
        4. Usage examples
        5. Setup instructions
        """
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a technical documentation expert."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=4000,
                temperature=0.2
            )
            
            return {
                'success': True,
                'documentation': response.choices[0].message.content,
                'tokens_used': response.usage.total_tokens
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
```

## 🤝 Contributing Guidelines

### Contribution Process

#### 1. Fork and Clone
```bash
# Fork repository on GitHub
# Clone your fork
git clone https://github.com/your-username/CodeFuser.git
cd CodeFuser

# Add upstream remote
git remote add upstream https://github.com/tahamucasiroglu/CodeFuser.git
```

#### 2. Development Setup
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows

# Install in development mode
pip install -e .[dev]

# Install pre-commit hooks
pre-commit install
```

#### 3. Make Changes
```bash
# Create feature branch
git checkout -b feature/amazing-feature

# Make your changes
# Write tests
# Update documentation

# Run tests
pytest tests/

# Run linting
black src/ tests/
flake8 src/ tests/
mypy src/
```

#### 4. Submit Pull Request
```bash
# Commit changes
git add .
git commit -m "feat: add amazing feature

- Implement new functionality
- Add comprehensive tests
- Update documentation"

# Push to your fork
git push origin feature/amazing-feature

# Create pull request on GitHub
```

### Code Review Process

#### Review Checklist
```markdown
- [ ] Code follows project style guidelines
- [ ] All tests pass
- [ ] New features have tests
- [ ] Documentation is updated
- [ ] Breaking changes are documented
- [ ] Performance impact is considered
- [ ] Security implications are reviewed
```

#### Review Guidelines
- Be constructive and helpful
- Focus on code, not the person
- Suggest specific improvements
- Acknowledge good practices
- Test the changes locally

---

**Ready to contribute?** Check out [open issues](https://github.com/tahamucasiroglu/CodeFuser/issues) or [start a discussion](https://github.com/tahamucasiroglu/CodeFuser/discussions) to get involved!

*Continue to [Troubleshooting Guide](Troubleshooting-EN) for help with development issues →*