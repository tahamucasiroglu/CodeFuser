# ⚙️ Yapılandırma Rehberi

CodeFuser v2.0'ı ihtiyaçlarınıza ve ekip iş akışlarınıza göre özelleştirmek için kapsamlı rehber.

## 📁 Yapılandırma Dosyası Konumları

### Windows Taşınabilir EXE
```
CodeFuser_Portable/
├── config/
│   ├── default_settings.json (varsayılan ayarlar)
│   └── user_settings.json (özelleştirmeleriniz)
└── locales/
    ├── en.json (İngilizce çeviriler)
    └── tr.json (Türkçe çeviriler)
```

### Python Kaynak Kurulumu
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
    └── ... (diğer şablonlar)
```

## 🔧 Temel Yapılandırma (user_settings.json)

### Temel Yapı
```json
{
  "interface": {
    "language": "tr",
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
    "file_separator": "=== DOSYA: {filepath} ===",
    "prompt_placeholder": "[PROMPT]",
    "content_placeholder": "[İÇERİK]",
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

## 🎨 Arayüz Yapılandırması

### Dil Ayarları
```json
{
  "interface": {
    "language": "tr",           // "en" İngilizce, "tr" Türkçe için
    "auto_detect_language": false,
    "fallback_language": "en"
  }
}
```

### Pencere ve Görüntü
```json
{
  "interface": {
    "fullscreen": true,         // Tam ekran modunda başlat
    "window_size": "1200x800",  // Tam ekran değilse varsayılan pencere boyutu
    "remember_window_state": true,
    "theme": "modern",          // UI teması
    "font_size": 10,           // Temel font boyutu
    "high_dpi_scaling": "auto"  // "auto", "enabled", "disabled"
  }
}
```

### Renk Şeması Özelleştirmesi
```json
{
  "interface": {
    "colors": {
      "selected_file": "#fff3a0",           // Sarı - dosya seçili
      "selected_with_prompt": "#d4f5d4",    // Yeşil - seçili + prompt
      "prompt_only": "#ffcccc",             // Kırmızı - prompt var ama seçili değil
      "background": "#f8f9fa",              // Varsayılan arka plan
      "accent": "#4CAF50",                  // Düğmeler için vurgu rengi
      "warning": "#FF9800",                 // Uyarı rengi
      "error": "#F44336"                    // Hata rengi
    }
  }
}
```

## 📊 Proje Türü Yapılandırması

### Özel Proje Türleri Ekleme
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

### Dosya Uzantısı Eşleme
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

## 🚫 Dışlama Desenlerı Yapılandırması

### Gelişmiş Dışlama Desenleri
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

### Koşullu Dışlama
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

## 📤 Çıktı Yapılandırması

### Export Ayarları
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

### Format-Özel Ayarlar
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

## 🔍 Akıllı Filtreler Yapılandırması

### Filtre Ön Ayarları
```json
{
  "smart_filter_presets": {
    "production_review": {
      "description": "Üretim kodu incelemesi için dosyalar",
      "include_patterns": ["src/**", "lib/**", "app/**"],
      "exclude_patterns": ["**/*test*", "**/*spec*"],
      "max_file_size_mb": 2,
      "git_status": ["modified", "added"]
    },
    "security_audit": {
      "description": "Güvenlik açısından hassas dosyalar",
      "include_patterns": ["**/auth*", "**/security*", "**/crypto*"],
      "include_extensions": [".py", ".js", ".php", ".cs"],
      "exclude_test_files": true
    },
    "api_documentation": {
      "description": "API ve arayüz dosyaları",
      "include_patterns": ["**/api/**", "**/controllers/**", "**/routes/**"],
      "include_extensions": [".py", ".js", ".ts", ".php", ".cs"],
      "include_documentation": true
    }
  }
}
```

### Özel Filtre Kuralları
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

## 🐙 Git Entegrasyonu Yapılandırması

### Git Ayarları
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

### Dal ve Commit Filtreleri
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

## ⚡ Performans Yapılandırması

### Tarama Performansı
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

### Önbellekleme Ayarları
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

## 🔧 Gelişmiş Yapılandırma

### Eklenti Yapılandırması
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

### Şablon Yapılandırması
```json
{
  "templates": {
    "custom_template_directory": "templates/custom/",
    "auto_detect_templates": true,
    "default_template": "16x_prompt",
    "template_variables": {
      "project_name": "{{AUTO_DETECT}}",
      "author": "Adınız",
      "company": "Şirketiniz"
    }
  }
}
```

### Güvenlik Ayarları
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

## 🔄 Yapılandırma Yönetimi

### Yedekleme ve Geri Yükleme
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

### Ekip Yapılandırması
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

## 📝 Yapılandırma Örnekleri

### Minimal Yapılandırma
```json
{
  "interface": {
    "language": "tr"
  },
  "output_settings": {
    "default_format": "html"
  }
}
```

### Güçlü Kullanıcı Yapılandırması
```json
{
  "interface": {
    "language": "tr",
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

## 🆘 Yapılandırma Sorun Giderme

### Yaygın Sorunlar

#### Yapılandırma Yüklenmiyor
```bash
# Dosya izinlerini kontrol et
# JSON sözdizimini çevrimiçi doğrulayıcıyla kontrol et
# Dosya kodlamasının UTF-8 olduğundan emin ol
```

#### Geçersiz JSON Sözdizimi
```bash
# JSON doğrulayıcı kullan: jsonlint.com
# Eksik virgül, tırnak, parantez kontrolü
# Dosya yollarındaki kaçış karakterlerini doğrula
```

#### Ayarlar Etkili Olmuyor
```bash
# Yapılandırma değişikliklerinden sonra CodeFuser'ı yeniden başlat
# Çakışan ayarları kontrol et
# Yapılandırma dosyası konumunu doğrula
```

---

**Daha fazla özelleştirme mi gerekiyor?** Şablon yapılandırması için [Şablonlar Rehberi](Templates-Guide-TR)'ni veya gelişmiş filtreleme seçenekleri için [Akıllı Filtreler](Smart-Filters-TR)'i kontrol edin!