# ⚙️ Configuration Guide

Complete guide to customizing CodeFuser v2.0 for your needs and team workflows.

## 📁 Configuration File Locations

### Windows Standalone EXE
```
CodeFuser_Portable/
├── config/
│   ├── default_settings.json (default settings)
│   └── user_settings.json (your customizations)
└── locales/
    ├── en.json (English translations)
    └── tr.json (Turkish translations)
```

### Python Source Installation
```
CodeFuser/
├── config/
│   ├── default_settings.json
│   └── user_settings.json
├── locales/
│   ├── en.json
│   └── tr.json
└── templates/
    ├── 16x_prompt.json
    ├── claude_project.json
    ├── code_review.json
    └── ... (more templates)
```

## 🔧 Core Configuration (user_settings.json)

### Basic Structure
```json
{
  "interface": {
    "language": "en",
    "fullscreen": true,
    "window_size": "1200x800",
    "theme": "modern"
  },
  "project_types": {
    "Python": [".py", ".pyx", ".pyi", ".ipynb"],
    "JavaScript": [".js", ".jsx", ".ts", ".tsx", ".mjs"],
    "Web": [".html", ".htm", ".css", ".scss", ".sass"],
    "C#": [".cs", ".cshtml", ".csproj", ".config"],
    "Java": [".java", ".jsp", ".xml"],
    "PHP": [".php", ".phtml", ".twig"],
    "Ruby": [".rb", ".erb", ".haml"],
    "Go": [".go", ".mod", ".sum"],
    "Rust": [".rs", ".toml"],
    "C/C++": [".c", ".cpp", ".cc", ".cxx", ".h", ".hpp"]
  },
  "ignore_folders": [
    "node_modules", ".git", ".svn", ".hg",
    "__pycache__", ".pytest_cache", ".venv", "venv",
    "bin", "obj", "target", "build", "dist",
    ".idea", ".vscode", ".vs"
  ],
  "ignore_files": [
    "*.log", "*.tmp", "*.cache", "*.pid",
    "*.exe", "*.dll", "*.so", "*.dylib",
    "*.jpg", "*.jpeg", "*.png", "*.gif", "*.ico",
    "*.zip", "*.tar", "*.gz", "*.rar",
    ".DS_Store", "Thumbs.db", "desktop.ini"
  ],
  "output_settings": {
    "default_format": "html",
    "default_location": "~/Documents/CodeFuser_Exports",
    "file_separator": "=== FILE: {filepath} ===",
    "prompt_placeholder": "[PROMPT]",
    "content_placeholder": "[CONTENT]",
    "include_metadata": true,
    "include_statistics": true
  },
  "smart_filters": {
    "max_file_size_mb": 5,
    "exclude_test_files": true,
    "exclude_documentation": false,
    "exclude_configuration": false,
    "include_only_modified": false
  },
  "git_integration": {
    "enabled": true,
    "show_git_status": true,
    "include_untracked": true,
    "ignore_git_ignored": true
  },
  "performance": {
    "max_files_scan": 10000,
    "scan_timeout_seconds": 30,
    "ui_update_interval_ms": 100
  }
}
```

## 🎨 Interface Configuration

### Language Settings
```json
{
  "interface": {
    "language": "tr",           // "en" for English, "tr" for Turkish
    "auto_detect_language": false,
    "fallback_language": "en"
  }
}
```

### Window and Display
```json
{
  "interface": {
    "fullscreen": true,         // Start in fullscreen mode
    "window_size": "1200x800",  // Default window size if not fullscreen
    "remember_window_state": true,
    "theme": "modern",          // UI theme
    "font_size": 10,           // Base font size
    "high_dpi_scaling": "auto"  // "auto", "enabled", "disabled"
  }
}
```

### Color Scheme Customization
```json
{
  "interface": {
    "colors": {
      "selected_file": "#fff3a0",           // Yellow - file selected
      "selected_with_prompt": "#d4f5d4",    // Green - selected + prompt
      "prompt_only": "#ffcccc",             // Red - prompt but not selected
      "background": "#f8f9fa",              // Default background
      "accent": "#4CAF50",                  // Accent color for buttons
      "warning": "#FF9800",                 // Warning color
      "error": "#F44336"                    // Error color
    }
  }
}
```

## 📊 Project Type Configuration

### Adding Custom Project Types
```json
{
  "project_types": {
    "React": [".js", ".jsx", ".ts", ".tsx", ".css", ".scss"],
    "Vue": [".vue", ".js", ".ts", ".css", ".scss"],
    "Angular": [".ts", ".js", ".html", ".css", ".scss"],
    "Django": [".py", ".html", ".css", ".js"],
    "Rails": [".rb", ".erb", ".haml", ".scss", ".coffee"],
    "Laravel": [".php", ".blade.php", ".css", ".js"],
    "Spring": [".java", ".xml", ".properties", ".yml"],
    "ASP.NET": [".cs", ".cshtml", ".config", ".json"],
    "Flutter": [".dart", ".yaml", ".json"],
    "Unity": [".cs", ".unity", ".prefab", ".asset"]
  }
}
```

### File Extension Mapping
```json
{
  "file_extensions": {
    ".jsx": {
      "language": "javascript",
      "icon": "⚛️",
      "category": "component"
    },
    ".vue": {
      "language": "vue",
      "icon": "💚",
      "category": "component"
    },
    ".blade.php": {
      "language": "php",
      "icon": "🐘",
      "category": "template"
    }
  }
}
```

## 🚫 Ignore Patterns Configuration

### Advanced Ignore Patterns
```json
{
  "ignore_patterns": {
    "folders": [
      "node_modules/**",
      ".git/**",
      "**/build/**",
      "**/dist/**",
      "**/__pycache__/**",
      "**/target/**",
      "**/bin/**",
      "**/obj/**"
    ],
    "files": [
      "*.log",
      "*.tmp",
      "*.cache",
      "**/package-lock.json",
      "**/yarn.lock",
      "**/.env*",
      "**/secrets.*"
    ],
    "patterns": [
      "test_*.py",
      "*_test.go",
      "*.spec.js",
      "*.test.tsx"
    ]
  }
}
```

### Conditional Ignoring
```json
{
  "conditional_ignore": {
    "large_files": {
      "enabled": true,
      "max_size_mb": 5,
      "exceptions": [".md", ".txt", ".json"]
    },
    "binary_files": {
      "enabled": true,
      "exceptions": [".pdf", ".docx"]
    },
    "generated_files": {
      "enabled": true,
      "patterns": ["*.generated.*", "*.auto.*", "**/migrations/**"]
    }
  }
}
```

## 📤 Output Configuration

### Export Settings
```json
{
  "output_settings": {
    "default_format": "html",
    "default_location": "~/Documents/CodeFuser_Exports",
    "auto_open_after_export": true,
    "filename_pattern": "CodeFuser_{project_name}_{timestamp}",
    "timestamp_format": "%Y%m%d_%H%M%S",
    "include_metadata": true,
    "include_statistics": true,
    "include_file_tree": true
  }
}
```

### Format-Specific Settings
```json
{
  "format_settings": {
    "html": {
      "syntax_highlighting": true,
      "include_css": true,
      "theme": "tomorrow-night",
      "copy_button": true,
      "toc_navigation": true
    },
    "pdf": {
      "page_size": "A4",
      "font_size": 9,
      "include_page_numbers": true,
      "syntax_highlighting": false
    },
    "docx": {
      "font_family": "Courier New",
      "font_size": 10,
      "include_toc": true,
      "page_breaks_between_files": true
    },
    "txt": {
      "line_ending": "auto",
      "encoding": "utf-8",
      "include_separators": true
    }
  }
}
```

## 🔍 Smart Filters Configuration

### Filter Presets
```json
{
  "smart_filter_presets": {
    "production_review": {
      "description": "Files for production code review",
      "include_patterns": ["src/**", "lib/**", "app/**"],
      "exclude_patterns": ["**/*test*", "**/*spec*"],
      "max_file_size_mb": 2,
      "git_status": ["modified", "added"]
    },
    "security_audit": {
      "description": "Security-sensitive files",
      "include_patterns": ["**/auth*", "**/security*", "**/crypto*"],
      "include_extensions": [".py", ".js", ".php", ".cs"],
      "exclude_test_files": true
    },
    "api_documentation": {
      "description": "API and interface files",
      "include_patterns": ["**/api/**", "**/controllers/**", "**/routes/**"],
      "include_extensions": [".py", ".js", ".ts", ".php", ".cs"],
      "include_documentation": true
    }
  }
}
```

### Custom Filter Rules
```json
{
  "custom_filters": {
    "complexity_filter": {
      "max_lines": 500,
      "max_functions": 20,
      "exclude_if_over_complexity": true
    },
    "modification_filter": {
      "last_modified_days": 30,
      "include_only_recent": false
    },
    "content_filter": {
      "must_contain": ["TODO", "FIXME", "BUG"],
      "must_not_contain": ["DEBUG", "TEMP"]
    }
  }
}
```

## 🐙 Git Integration Configuration

### Git Settings
```json
{
  "git_integration": {
    "enabled": true,
    "auto_detect_repository": true,
    "show_git_status": true,
    "status_indicators": {
      "modified": "M",
      "added": "A",
      "deleted": "D",
      "renamed": "R",
      "copied": "C",
      "untracked": "?"
    },
    "include_untracked": true,
    "ignore_git_ignored": true,
    "branch_comparison": {
      "enabled": true,
      "default_base_branch": "main",
      "show_ahead_behind": true
    }
  }
}
```

### Branch and Commit Filters
```json
{
  "git_filters": {
    "commit_range": {
      "enabled": false,
      "from_commit": "HEAD~10",
      "to_commit": "HEAD"
    },
    "author_filter": {
      "enabled": false,
      "include_authors": ["user@example.com"],
      "exclude_authors": ["bot@automated.com"]
    },
    "time_range": {
      "enabled": false,
      "since": "2024-01-01",
      "until": "2024-12-31"
    }
  }
}
```

## ⚡ Performance Configuration

### Scanning Performance
```json
{
  "performance": {
    "max_files_scan": 10000,
    "scan_timeout_seconds": 30,
    "parallel_scanning": true,
    "max_worker_threads": 4,
    "memory_limit_mb": 512,
    "ui_update_interval_ms": 100
  }
}
```

### Caching Settings
```json
{
  "caching": {
    "enabled": true,
    "cache_duration_hours": 24,
    "cache_location": "~/.codefuser_cache",
    "max_cache_size_mb": 100,
    "clear_cache_on_startup": false
  }
}
```

## 🔧 Advanced Configuration

### Plugin Configuration
```json
{
  "plugins": {
    "enabled": true,
    "plugin_directory": "plugins/",
    "auto_load": true,
    "allowed_plugins": ["custom_exporter", "ai_integration"]
  }
}
```

### Template Configuration
```json
{
  "templates": {
    "custom_template_directory": "templates/custom/",
    "auto_detect_templates": true,
    "default_template": "16x_prompt",
    "template_variables": {
      "project_name": "{{AUTO_DETECT}}",
      "author": "Your Name",
      "company": "Your Company"
    }
  }
}
```

### Security Settings
```json
{
  "security": {
    "scan_for_secrets": true,
    "secret_patterns": [
      "api[_-]?key",
      "password",
      "secret",
      "token",
      "auth"
    ],
    "exclude_suspicious_files": true,
    "max_file_read_size_mb": 10
  }
}
```

## 🔄 Configuration Management

### Backup and Restore
```json
{
  "backup": {
    "auto_backup": true,
    "backup_interval_days": 7,
    "max_backups": 5,
    "backup_location": "~/.codefuser_backups"
  }
}
```

### Team Configuration
```json
{
  "team": {
    "shared_config_location": "\\\\server\\shared\\codefuser_config.json",
    "allow_local_overrides": true,
    "sync_templates": true,
    "sync_filters": false
  }
}
```

## 📝 Configuration Examples

### Minimal Configuration
```json
{
  "interface": {
    "language": "en"
  },
  "output_settings": {
    "default_format": "html"
  }
}
```

### Power User Configuration
```json
{
  "interface": {
    "language": "en",
    "fullscreen": false,
    "window_size": "1400x900"
  },
  "project_types": {
    "My_Stack": [".py", ".js", ".html", ".css", ".sql"]
  },
  "smart_filters": {
    "max_file_size_mb": 10,
    "exclude_test_files": true
  },
  "output_settings": {
    "default_format": "html",
    "include_metadata": true,
    "auto_open_after_export": true
  },
  "git_integration": {
    "enabled": true,
    "show_git_status": true
  }
}
```

## 🆘 Configuration Troubleshooting

### Common Issues

#### Configuration Not Loading
```bash
# Check file permissions
# Verify JSON syntax with online validator
# Ensure file encoding is UTF-8
```

#### Invalid JSON Syntax
```bash
# Use JSON validator: jsonlint.com
# Check for missing commas, quotes, brackets
# Verify escape characters in file paths
```

#### Settings Not Taking Effect
```bash
# Restart CodeFuser after configuration changes
# Check for conflicting settings
# Verify configuration file location
```

---

**Need more customization?** Check the [Templates Guide](Templates-Guide-EN) for template configuration or [Smart Filters](Smart-Filters-EN) for advanced filtering options!