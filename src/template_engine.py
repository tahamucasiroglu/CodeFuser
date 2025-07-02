import json
import re
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime
import os

from utils import get_template_path, ensure_dir


class TemplateEngine:
    def __init__(self, config_manager):
        self.config_manager = config_manager
        # Create user templates directory
        self.custom_templates_dir = ensure_dir(Path.home() / '.codefuser' / 'templates')
        
        self._create_default_templates()
    
    def _create_default_templates(self):
        """Create default template files if they don't exist"""
        # Sadece custom templates klasöründe varsayılan template'leri oluştur
        default_templates = {
            "16x_prompt": {
                "name": "16x Prompt Style",
                "description": "Popular 16x prompt format for AI code analysis",
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
Please provide a comprehensive analysis of this codebase focusing on code quality, maintainability, and best practices.""",
                "variables": ["project_name", "file_count", "primary_language", "timestamp", "file_contents"]
            },
            
            "cursor_rules": {
                "name": "Cursor IDE Rules",
                "description": "Template for Cursor IDE .cursorrules file",
                "template": """# Cursor IDE Rules for {project_name}

## Project Context
This is a {primary_language} project with {file_count} files.
Generated on {timestamp}

## Coding Standards
- Follow {primary_language} best practices
- Maintain consistent code style
- Add meaningful comments
- Write unit tests for new features

## Project Structure
{file_structure}

## Key Files
{file_contents}

## Instructions for AI
When working on this project:
1. Understand the existing code structure
2. Maintain consistency with current patterns
3. Suggest improvements where appropriate
4. Focus on code quality and maintainability""",
                "variables": ["project_name", "primary_language", "file_count", "timestamp", "file_structure", "file_contents"]
            },
            
            "claude_project": {
                "name": "Claude Project Format",
                "description": "Template optimized for Claude AI projects",
                "template": """# {project_name} - Claude Project

## Project Information
- **Name**: {project_name}
- **Language**: {primary_language}
- **Files**: {file_count}
- **Size**: {total_size}
- **Created**: {timestamp}

## Project Goals
This project aims to [describe your project goals here].

## Architecture Overview
{architecture_summary}

## Source Code

{file_contents}

## Next Steps
1. Review the code structure
2. Identify areas for improvement
3. Implement suggested changes
4. Test thoroughly

Please analyze this code and provide actionable feedback.""",
                "variables": ["project_name", "primary_language", "file_count", "total_size", "timestamp", "architecture_summary", "file_contents"]
            },
            
            "documentation": {
                "name": "Documentation Template",
                "description": "Template for generating project documentation",
                "template": """# {project_name} Documentation

## Overview
This document provides a comprehensive overview of the {project_name} project.

**Generated**: {timestamp}  
**Total Files**: {file_count}  
**Primary Language**: {primary_language}  
**Project Size**: {total_size}

## File Structure
{file_structure}

## Source Code Analysis

{file_contents}

## Dependencies
{dependencies}

## Setup Instructions
1. Clone the repository
2. Install dependencies
3. Run the application

## Contributing
Please follow the coding standards outlined in this documentation.""",
                "variables": ["project_name", "timestamp", "file_count", "primary_language", "total_size", "file_structure", "file_contents", "dependencies"]
            },
            
            "code_review": {
                "name": "Code Review Template",
                "description": "Template for code review purposes",
                "template": """# Code Review: {project_name}

## Review Information
- **Reviewer**: [Your Name]
- **Date**: {timestamp}
- **Files Reviewed**: {file_count}
- **Language**: {primary_language}

## Review Checklist
- [ ] Code follows project standards
- [ ] Functions are well-documented
- [ ] Error handling is appropriate
- [ ] Security considerations addressed
- [ ] Performance is acceptable
- [ ] Tests are included

## Files Under Review

{file_contents}

## Review Comments
[Add your review comments here]

## Recommendations
[Add your recommendations here]""",
                "variables": ["project_name", "timestamp", "file_count", "primary_language", "file_contents"]
            }
        }
        
        for template_id, template_data in default_templates.items():
            template_file = self.custom_templates_dir / f"{template_id}.json"
            if not template_file.exists():
                try:
                    with open(template_file, 'w', encoding='utf-8') as f:
                        json.dump(template_data, f, indent=4, ensure_ascii=False)
                except Exception as e:
                    print(f"⚠️ Template oluşturulamadı {template_id}: {e}")
    
    def get_available_templates(self) -> Dict[str, Dict[str, Any]]:
        """Get all available templates"""
        templates = {}
        
        # Fallback templates when files not found
        if not any(self.custom_templates_dir.glob("*.json")):
            return self._get_fallback_templates()
        
        # Load custom templates
        for template_file in self.custom_templates_dir.glob("*.json"):
            try:
                with open(template_file, 'r', encoding='utf-8') as f:
                    template_data = json.load(f)
                    templates[f"custom_{template_file.stem}"] = template_data
                    templates[f"custom_{template_file.stem}"]['type'] = 'custom'
            except Exception as e:
                print(f"Error loading custom template {template_file}: {e}")
        
        return templates
    
    def apply_template(self, template_id: str, files: List[Dict[str, Any]], 
                      custom_variables: Dict[str, str] = None) -> str:
        """Apply a template to the given files"""
        templates = self.get_available_templates()
        
        if template_id not in templates:
            raise ValueError(f"Template '{template_id}' not found")
        
        template_data = templates[template_id]
        template_content = template_data['template']
        
        # Generate variables
        variables = self._generate_variables(files, custom_variables or {})
        
        # Replace variables in template
        result = self._replace_variables(template_content, variables)
        
        return result
    
    def _generate_variables(self, files: List[Dict[str, Any]], 
                          custom_variables: Dict[str, str]) -> Dict[str, str]:
        """Generate all template variables"""
        variables = {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'file_count': str(len(files)),
            'project_name': custom_variables.get('project_name', 'Unknown Project'),
        }
        
        # Detect primary language
        extensions = [Path(f['relative_path']).suffix.lower() for f in files]
        ext_count = {}
        for ext in extensions:
            ext_count[ext] = ext_count.get(ext, 0) + 1
        
        if ext_count:
            primary_ext = max(ext_count, key=ext_count.get)
            language_map = {
                '.py': 'Python', '.js': 'JavaScript', '.ts': 'TypeScript',
                '.java': 'Java', '.cs': 'C#', '.cpp': 'C++', '.c': 'C',
                '.php': 'PHP', '.rb': 'Ruby', '.go': 'Go', '.rs': 'Rust'
            }
            variables['primary_language'] = language_map.get(primary_ext, 'Unknown')
        else:
            variables['primary_language'] = 'Unknown'
        
        # Calculate total size
        total_size = sum(f.get('size', 0) for f in files)
        if total_size > 1024 * 1024:
            variables['total_size'] = f"{total_size / (1024 * 1024):.1f} MB"
        elif total_size > 1024:
            variables['total_size'] = f"{total_size / 1024:.1f} KB"
        else:
            variables['total_size'] = f"{total_size} B"
        
        # Generate file structure
        variables['file_structure'] = self._generate_file_structure(files)
        
        # Generate file contents
        variables['file_contents'] = self._generate_file_contents(files)
        
        # Generate architecture summary
        variables['architecture_summary'] = self._generate_architecture_summary(files)
        
        # Generate dependencies
        variables['dependencies'] = self._generate_dependencies(files)
        
        # Add custom variables
        variables.update(custom_variables)
        
        return variables
    
    def _generate_file_structure(self, files: List[Dict[str, Any]]) -> str:
        """Generate a file structure tree"""
        structure = []
        
        # Group files by directory
        dirs = {}
        for file_info in files:
            path = Path(file_info['relative_path'])
            dir_path = str(path.parent) if path.parent != Path('.') else 'root'
            
            if dir_path not in dirs:
                dirs[dir_path] = []
            dirs[dir_path].append(path.name)
        
        # Build tree structure
        for dir_path, filenames in sorted(dirs.items()):
            if dir_path == 'root':
                structure.append("📁 Project Root")
            else:
                depth = len(Path(dir_path).parts)
                indent = "  " * (depth - 1)
                structure.append(f"{indent}📁 {Path(dir_path).name}/")
            
            for filename in sorted(filenames):
                depth = len(Path(dir_path).parts) if dir_path != 'root' else 0
                indent = "  " * depth
                structure.append(f"{indent}📄 {filename}")
        
        return "\n".join(structure)
    
    def _generate_file_contents(self, files: List[Dict[str, Any]]) -> str:
        """Generate formatted file contents"""
        contents = []
        
        for file_info in files:
            file_path = file_info['relative_path']
            
            try:
                with open(file_info['path'], 'r', encoding='utf-8') as f:
                    content = f.read()
                
                contents.append(f"## 📄 {file_path}")
                contents.append(f"```{self._get_language_for_syntax(file_path)}")
                contents.append(content)
                contents.append("```")
                contents.append("")
                
            except Exception as e:
                contents.append(f"## 📄 {file_path}")
                contents.append(f"❌ Error reading file: {str(e)}")
                contents.append("")
        
        return "\n".join(contents)
    
    def _generate_architecture_summary(self, files: List[Dict[str, Any]]) -> str:
        """Generate a basic architecture summary"""
        summary = []
        
        # Count by file type
        types = {}
        for file_info in files:
            ext = Path(file_info['relative_path']).suffix.lower()
            types[ext] = types.get(ext, 0) + 1
        
        summary.append("### File Distribution")
        for ext, count in sorted(types.items()):
            lang = self._get_language_for_syntax("file" + ext)
            summary.append(f"- {lang}: {count} files")
        
        return "\n".join(summary)
    
    def _generate_dependencies(self, files: List[Dict[str, Any]]) -> str:
        """Detect and list dependencies"""
        dependencies = set()
        
        # Look for common dependency files
        for file_info in files:
            filename = Path(file_info['relative_path']).name.lower()
            
            if filename in ['package.json', 'requirements.txt', 'composer.json', 
                          'pom.xml', 'cargo.toml', 'go.mod']:
                try:
                    with open(file_info['path'], 'r', encoding='utf-8') as f:
                        content = f.read()
                        dependencies.add(f"📄 {filename}")
                        
                        # Extract some dependency info
                        if filename == 'package.json':
                            try:
                                package_data = json.loads(content)
                                if 'dependencies' in package_data:
                                    for dep in list(package_data['dependencies'].keys())[:5]:
                                        dependencies.add(f"  - {dep}")
                            except:
                                pass
                        
                except Exception:
                    continue
        
        if dependencies:
            return "\n".join(dependencies)
        else:
            return "No dependency files detected."
    
    def _get_language_for_syntax(self, filename: str) -> str:
        """Get language identifier for syntax highlighting"""
        ext = Path(filename).suffix.lower()
        lang_map = {
            '.py': 'python', '.js': 'javascript', '.ts': 'typescript',
            '.html': 'html', '.css': 'css', '.java': 'java',
            '.cs': 'csharp', '.cpp': 'cpp', '.c': 'c',
            '.php': 'php', '.rb': 'ruby', '.go': 'go',
            '.rs': 'rust', '.json': 'json', '.xml': 'xml',
            '.yml': 'yaml', '.yaml': 'yaml', '.md': 'markdown'
        }
        return lang_map.get(ext, 'text')
    
    def _replace_variables(self, template: str, variables: Dict[str, str]) -> str:
        """Replace template variables with actual values"""
        result = template
        
        for var_name, var_value in variables.items():
            placeholder = f"{{{var_name}}}"
            result = result.replace(placeholder, str(var_value))
        
        return result
    
    def save_custom_template(self, template_id: str, name: str, 
                           description: str, template_content: str) -> bool:
        """Save a custom template"""
        try:
            template_data = {
                "name": name,
                "description": description,
                "template": template_content,
                "variables": self._extract_variables(template_content),
                "created": datetime.now().isoformat()
            }
            
            template_file = self.custom_templates_dir / f"{template_id}.json"
            with open(template_file, 'w', encoding='utf-8') as f:
                json.dump(template_data, f, indent=4, ensure_ascii=False)
            
            return True
        except Exception as e:
            print(f"Error saving template: {e}")
            return False
    
    def delete_custom_template(self, template_id: str) -> bool:
        """Delete a custom template"""
        try:
            if template_id.startswith('custom_'):
                template_id = template_id[7:]  # Remove 'custom_' prefix
            
            template_file = self.custom_templates_dir / f"{template_id}.json"
            if template_file.exists():
                template_file.unlink()
                return True
            return False
        except Exception as e:
            print(f"Error deleting template: {e}")
            return False
    
    def _extract_variables(self, template_content: str) -> List[str]:
        """Extract variable names from template content"""
        pattern = r'\{([^}]+)\}'
        variables = re.findall(pattern, template_content)
        return list(set(variables))  # Remove duplicates
    
    def _get_fallback_templates(self) -> Dict[str, Dict[str, Any]]:
        """Fallback templates when template files are not found"""
        return {
            "16x_prompt": {
                "name": "16x Prompt Style",
                "description": "AI code analysis prompt",
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
4. Performance optimization opportunities

## Codebase

{file_contents}

## Recommendations
[Add your recommendations here]""",
                "variables": ["project_name", "timestamp", "file_count", "primary_language", "file_contents"],
                "type": "default"
            },
            "claude_project": {
                "name": "Claude Project Setup",
                "description": "Setup prompt for Claude Projects",
                "template": """# {project_name} - Claude Project

## Overview
This is a {primary_language} project with {file_count} files.

## Architecture
{architecture_summary}

## File Structure
{file_structure}

## Dependencies
{dependencies}

## Source Code

{file_contents}

## Instructions
Please analyze this codebase and help with development tasks.""",
                "variables": ["project_name", "primary_language", "file_count", "architecture_summary", "file_structure", "dependencies", "file_contents"],
                "type": "default"
            },
            "code_review": {
                "name": "Code Review",
                "description": "Code review and analysis prompt",
                "template": """# Code Review Request

## Project Details
- **Name**: {project_name}
- **Language**: {primary_language}
- **Files**: {file_count}
- **Size**: {total_size}
- **Date**: {timestamp}

## Review Focus Areas
Please review this code for:
- ✅ Code quality and best practices
- 🔒 Security vulnerabilities
- ⚡ Performance issues
- 📝 Documentation completeness
- 🧪 Test coverage
- 🏗️ Architecture design

## Codebase

{file_contents}

## Findings
Please provide detailed feedback on each focus area.""",
                "variables": ["project_name", "primary_language", "file_count", "total_size", "timestamp", "file_contents"],
                "type": "default"
            }
        }