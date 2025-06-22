import re
from pathlib import Path
from typing import List, Dict, Any, Callable, Tuple
from datetime import datetime, timedelta
import os
import fnmatch


class SmartFilters:
    def __init__(self, config_manager):
        self.config_manager = config_manager
        self.filters = self._initialize_filters()
    
    def _initialize_filters(self) -> Dict[str, Callable]:
        """Initialize all available smart filters"""
        return {
            # Size-based filters
            'size_small': lambda files: self._filter_by_size(files, max_size=1024),  # < 1KB
            'size_medium': lambda files: self._filter_by_size(files, min_size=1024, max_size=10240),  # 1-10KB
            'size_large': lambda files: self._filter_by_size(files, min_size=10240, max_size=102400),  # 10-100KB
            'size_huge': lambda files: self._filter_by_size(files, min_size=102400),  # > 100KB
            
            # Line count filters
            'lines_short': lambda files: self._filter_by_lines(files, max_lines=50),
            'lines_medium': lambda files: self._filter_by_lines(files, min_lines=50, max_lines=200),
            'lines_long': lambda files: self._filter_by_lines(files, min_lines=200, max_lines=1000),
            'lines_very_long': lambda files: self._filter_by_lines(files, min_lines=1000),
            
            # Time-based filters
            'modified_today': lambda files: self._filter_by_modification_time(files, hours=24),
            'modified_week': lambda files: self._filter_by_modification_time(files, hours=168),
            'modified_month': lambda files: self._filter_by_modification_time(files, hours=720),
            'modified_old': lambda files: self._filter_by_modification_time(files, hours=720, older=True),
            
            # Content-based filters
            'has_todos': lambda files: self._filter_by_content_pattern(files, [r'TODO', r'FIXME', r'HACK', r'XXX']),
            'has_comments': lambda files: self._filter_by_content_pattern(files, [r'#.*', r'//.*', r'/\*.*\*/', r'<!--.*-->']),
            'has_imports': lambda files: self._filter_by_content_pattern(files, [r'import\s+', r'from\s+.*import', r'#include', r'require\(']),
            'has_functions': lambda files: self._filter_by_content_pattern(files, [r'def\s+\w+', r'function\s+\w+', r'func\s+\w+', r'public\s+\w+\s+\w+']),
            'has_classes': lambda files: self._filter_by_content_pattern(files, [r'class\s+\w+', r'interface\s+\w+', r'struct\s+\w+']),
            'has_urls': lambda files: self._filter_by_content_pattern(files, [r'https?://\S+', r'www\.\S+\.\w+']),
            'has_emails': lambda files: self._filter_by_content_pattern(files, [r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b']),
            'has_secrets': lambda files: self._filter_by_content_pattern(files, [
                r'password\s*[=:]\s*["\'][^"\']+["\']',
                r'api[_-]?key\s*[=:]\s*["\'][^"\']+["\']',
                r'secret\s*[=:]\s*["\'][^"\']+["\']',
                r'token\s*[=:]\s*["\'][^"\']+["\']'
            ]),
            
            # Name pattern filters
            'test_files': lambda files: self._filter_by_name_pattern(files, ['*test*', '*spec*', 'test_*', '*_test.*']),
            'config_files': lambda files: self._filter_by_name_pattern(files, ['*config*', '*.conf', '*.ini', '*.yaml', '*.yml', '*.json']),
            'documentation': lambda files: self._filter_by_name_pattern(files, ['*.md', '*.txt', '*.rst', 'README*', 'CHANGELOG*', 'LICENSE*']),
            'main_files': lambda files: self._filter_by_name_pattern(files, ['main.*', 'index.*', 'app.*', '__init__.*']),
            
            # Language-specific filters
            'python_files': lambda files: self._filter_by_extension(files, ['.py', '.pyx', '.pyi']),
            'javascript_files': lambda files: self._filter_by_extension(files, ['.js', '.jsx', '.ts', '.tsx']),
            'web_files': lambda files: self._filter_by_extension(files, ['.html', '.htm', '.css', '.scss', '.sass']),
            'data_files': lambda files: self._filter_by_extension(files, ['.json', '.xml', '.csv', '.yaml', '.yml']),
            'image_files': lambda files: self._filter_by_extension(files, ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp']),
            
            # Code quality filters
            'potential_issues': lambda files: self._filter_by_potential_issues(files),
            'no_documentation': lambda files: self._filter_by_missing_documentation(files),
            'complex_files': lambda files: self._filter_by_complexity(files),
        }
    
    def get_available_filters(self) -> List[Tuple[str, str, str]]:
        """Get all available filters with categories"""
        filter_categories = [
            # (filter_id, display_name, category)
            ('size_small', 'Small Files (< 1KB)', 'Size'),
            ('size_medium', 'Medium Files (1-10KB)', 'Size'),
            ('size_large', 'Large Files (10-100KB)', 'Size'),
            ('size_huge', 'Huge Files (> 100KB)', 'Size'),
            
            ('lines_short', 'Short Files (< 50 lines)', 'Lines'),
            ('lines_medium', 'Medium Files (50-200 lines)', 'Lines'),
            ('lines_long', 'Long Files (200-1000 lines)', 'Lines'),
            ('lines_very_long', 'Very Long Files (> 1000 lines)', 'Lines'),
            
            ('modified_today', 'Modified Today', 'Time'),
            ('modified_week', 'Modified This Week', 'Time'),
            ('modified_month', 'Modified This Month', 'Time'),
            ('modified_old', 'Old Files (> 1 month)', 'Time'),
            
            ('has_todos', 'Contains TODOs/FIXMEs', 'Content'),
            ('has_comments', 'Has Comments', 'Content'),
            ('has_imports', 'Has Import Statements', 'Content'),
            ('has_functions', 'Contains Functions', 'Content'),
            ('has_classes', 'Contains Classes', 'Content'),
            ('has_urls', 'Contains URLs', 'Content'),
            ('has_emails', 'Contains Email Addresses', 'Content'),
            ('has_secrets', 'Potential Secrets/Keys', 'Content'),
            
            ('test_files', 'Test Files', 'Type'),
            ('config_files', 'Configuration Files', 'Type'),
            ('documentation', 'Documentation Files', 'Type'),
            ('main_files', 'Main/Entry Files', 'Type'),
            
            ('python_files', 'Python Files', 'Language'),
            ('javascript_files', 'JavaScript/TypeScript Files', 'Language'),
            ('web_files', 'Web Files (HTML/CSS)', 'Language'),
            ('data_files', 'Data Files (JSON/XML/CSV)', 'Language'),
            ('image_files', 'Image Files', 'Language'),
            
            ('potential_issues', 'Potential Code Issues', 'Quality'),
            ('no_documentation', 'Undocumented Files', 'Quality'),
            ('complex_files', 'Complex Files', 'Quality'),
        ]
        
        return filter_categories
    
    def apply_filter(self, files: List[Dict[str, Any]], filter_id: str) -> List[Dict[str, Any]]:
        """Apply a specific filter to the file list"""
        if filter_id not in self.filters:
            return files
        
        try:
            return self.filters[filter_id](files)
        except Exception as e:
            print(f"Error applying filter {filter_id}: {e}")
            return files
    
    def apply_multiple_filters(self, files: List[Dict[str, Any]], 
                             filter_ids: List[str], 
                             operation: str = 'AND') -> List[Dict[str, Any]]:
        """Apply multiple filters with AND/OR operation"""
        if not filter_ids:
            return files
        
        if operation == 'AND':
            result = files
            for filter_id in filter_ids:
                result = self.apply_filter(result, filter_id)
            return result
        
        elif operation == 'OR':
            all_results = set()
            for filter_id in filter_ids:
                filtered = self.apply_filter(files, filter_id)
                all_results.update(f['relative_path'] for f in filtered)
            
            return [f for f in files if f['relative_path'] in all_results]
        
        return files
    
    def create_custom_filter(self, name: str, 
                           size_range: Tuple[int, int] = None,
                           line_range: Tuple[int, int] = None,
                           extensions: List[str] = None,
                           content_patterns: List[str] = None,
                           name_patterns: List[str] = None) -> str:
        """Create a custom filter with specified criteria"""
        
        def custom_filter(files: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
            result = files
            
            if size_range:
                result = self._filter_by_size(result, size_range[0], size_range[1])
            
            if line_range:
                result = self._filter_by_lines(result, line_range[0], line_range[1])
            
            if extensions:
                result = self._filter_by_extension(result, extensions)
            
            if content_patterns:
                result = self._filter_by_content_pattern(result, content_patterns)
            
            if name_patterns:
                result = self._filter_by_name_pattern(result, name_patterns)
            
            return result
        
        filter_id = f"custom_{name.lower().replace(' ', '_')}"
        self.filters[filter_id] = custom_filter
        return filter_id
    
    # Filter implementation methods
    
    def _filter_by_size(self, files: List[Dict[str, Any]], 
                       min_size: int = 0, max_size: int = float('inf')) -> List[Dict[str, Any]]:
        """Filter files by size in bytes"""
        result = []
        for file_info in files:
            size = file_info.get('size', 0)
            if min_size <= size <= max_size:
                result.append(file_info)
        return result
    
    def _filter_by_lines(self, files: List[Dict[str, Any]], 
                        min_lines: int = 0, max_lines: int = float('inf')) -> List[Dict[str, Any]]:
        """Filter files by line count"""
        result = []
        for file_info in files:
            try:
                with open(file_info['path'], 'r', encoding='utf-8', errors='ignore') as f:
                    line_count = sum(1 for _ in f)
                
                if min_lines <= line_count <= max_lines:
                    result.append(file_info)
            except Exception:
                continue
        return result
    
    def _filter_by_modification_time(self, files: List[Dict[str, Any]], 
                                   hours: int, older: bool = False) -> List[Dict[str, Any]]:
        """Filter files by modification time"""
        threshold = datetime.now() - timedelta(hours=hours)
        result = []
        
        for file_info in files:
            try:
                file_path = Path(file_info['path'])
                mod_time = datetime.fromtimestamp(file_path.stat().st_mtime)
                
                if older:
                    if mod_time < threshold:
                        result.append(file_info)
                else:
                    if mod_time > threshold:
                        result.append(file_info)
            except Exception:
                continue
        
        return result
    
    def _filter_by_content_pattern(self, files: List[Dict[str, Any]], 
                                 patterns: List[str]) -> List[Dict[str, Any]]:
        """Filter files by content patterns (regex)"""
        compiled_patterns = [re.compile(pattern, re.IGNORECASE | re.MULTILINE) 
                           for pattern in patterns]
        result = []
        
        for file_info in files:
            try:
                with open(file_info['path'], 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                for pattern in compiled_patterns:
                    if pattern.search(content):
                        result.append(file_info)
                        break
            except Exception:
                continue
        
        return result
    
    def _filter_by_name_pattern(self, files: List[Dict[str, Any]], 
                              patterns: List[str]) -> List[Dict[str, Any]]:
        """Filter files by filename patterns (glob)"""
        result = []
        
        for file_info in files:
            filename = Path(file_info['relative_path']).name.lower()
            
            for pattern in patterns:
                if fnmatch.fnmatch(filename, pattern.lower()):
                    result.append(file_info)
                    break
        
        return result
    
    def _filter_by_extension(self, files: List[Dict[str, Any]], 
                           extensions: List[str]) -> List[Dict[str, Any]]:
        """Filter files by extension"""
        ext_set = set(ext.lower() for ext in extensions)
        result = []
        
        for file_info in files:
            file_ext = Path(file_info['relative_path']).suffix.lower()
            if file_ext in ext_set:
                result.append(file_info)
        
        return result
    
    def _filter_by_potential_issues(self, files: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Filter files that might contain code issues"""
        issue_patterns = [
            r'console\.log\(',  # Debug statements
            r'print\s*\(',      # Debug prints
            r'debugger;',       # Debugger statements
            r'alert\s*\(',      # Alert statements
            r'eval\s*\(',       # Eval usage
            r'document\.write\(', # Dangerous DOM manipulation
            r'innerHTML\s*=',   # Potential XSS
            r'exec\s*\(',       # Exec usage
            r'system\s*\(',     # System calls
        ]
        
        return self._filter_by_content_pattern(files, issue_patterns)
    
    def _filter_by_missing_documentation(self, files: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Filter files that appear to lack documentation"""
        result = []
        
        for file_info in files:
            try:
                with open(file_info['path'], 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                # Check for various documentation patterns
                has_docs = False
                
                # Check for docstrings, comments, etc.
                doc_patterns = [
                    r'""".*?"""',       # Python docstrings
                    r"'''.*?'''",       # Python docstrings
                    r'/\*\*.*?\*/',     # JSDoc comments
                    r'#.*',             # Hash comments
                    r'//.*',            # Line comments
                    r'<!--.*?-->',      # HTML comments
                ]
                
                for pattern in doc_patterns:
                    if re.search(pattern, content, re.DOTALL):
                        has_docs = True
                        break
                
                if not has_docs:
                    result.append(file_info)
                    
            except Exception:
                continue
        
        return result
    
    def _filter_by_complexity(self, files: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Filter files that appear to be complex (heuristic-based)"""
        result = []
        
        for file_info in files:
            try:
                with open(file_info['path'], 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                # Simple complexity metrics
                line_count = len(content.split('\n'))
                
                # Count nesting levels (rough estimate)
                nesting_patterns = [r'\{', r'\(', r'\[', r'if\s', r'for\s', r'while\s', r'def\s', r'class\s']
                complexity_score = 0
                
                for pattern in nesting_patterns:
                    complexity_score += len(re.findall(pattern, content, re.IGNORECASE))
                
                # Consider file complex if it has high line count or complexity score
                if line_count > 200 or complexity_score > 50:
                    result.append(file_info)
                    
            except Exception:
                continue
        
        return result