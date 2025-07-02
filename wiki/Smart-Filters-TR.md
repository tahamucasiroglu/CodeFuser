# 🔍 Akıllı Filtreler Rehberi

CodeFuser'ın akıllı filtreleme sisteminde ustalaşarak analiziniz için önemli olan koda tam odaklanın.

## 🎯 Filtre Genel Bakış

Akıllı Filtreler kod dosyalarınızı otomatik olarak analiz eder ve kategorize eder, manuel dosya seçimi yapmadan projenizin belirli yönlerine odaklanmanıza olanak tanır.

### Filtre Kategorileri

| Kategori | Amaç | Örnekler |
|----------|------|----------|
| **İçerik Analizi** | Kod içeriğine göre filtrele | Fonksiyonlar, sınıflar, TODO'lar |
| **Dosya Türleri** | Dosya özelliklerine göre filtrele | Testler, konfigürasyonlar, dokümantasyon |
| **Git Entegrasyonu** | Versiyon kontrol durumuna göre filtrele | Değiştirilmiş, staged, untracked |
| **Kod Kalitesi** | Kod metriklerine göre filtrele | Karmaşıklık, boyut, sorunlar |
| **Dile Özel** | Programlama diline göre filtrele | Python modülleri, JS bileşenleri |
| **Proje Yapısı** | Proje organizasyonuna göre filtrele | Kaynak, testler, build dosyaları |

## 🧠 İçerik Analizi Filtreleri

### Kod Deseni Algılama

#### Fonksiyon ve Sınıf Algılama
```json
{
  "content_filters": {
    "has_functions": {
      "description": "Fonksiyon tanımları içeren dosyalar",
      "patterns": [
        "def\\\\s+\\\\w+\\\\s*\\\\(",      // Python fonksiyonları
        "function\\\\s+\\\\w+\\\\s*\\\\(", // JavaScript fonksiyonları
        "public\\\\s+\\\\w+\\\\s+\\\\w+\\\\s*\\\\(", // Java/C# metodları
        "fn\\\\s+\\\\w+\\\\s*\\\\("        // Rust fonksiyonları
      ]
    },
    "has_classes": {
      "description": "Sınıf tanımları içeren dosyalar",
      "patterns": [
        "class\\\\s+\\\\w+",          // Çoğu dil
        "interface\\\\s+\\\\w+",      // Arayüzler
        "struct\\\\s+\\\\w+",         // Go/Rust struct'ları
        "type\\\\s+\\\\w+\\\\s*="       // TypeScript türleri
      ]
    }
  }
}
```

#### Dokümantasyon ve Yorumlar
```json
{
  "documentation_filters": {
    "well_documented": {
      "description": "İyi dokümante edilmiş dosyalar",
      "criteria": {
        "docstring_ratio": "> 0.1",
        "comment_ratio": "> 0.05",
        "has_module_docstring": true
      }
    },
    "needs_documentation": {
      "description": "Dokümantasyon eksik dosyalar",
      "criteria": {
        "docstring_ratio": "< 0.05",
        "comment_ratio": "< 0.02",
        "has_public_functions": true
      }
    }
  }
}
```

#### TODO ve FIXME Algılama
```json
{
  "task_filters": {
    "has_todos": {
      "description": "TODO yorumları içeren dosyalar",
      "patterns": [
        "TODO:",
        "FIXME:",
        "HACK:",
        "XXX:",
        "BUG:",
        "NOTE:"
      ]
    },
    "urgent_items": {
      "description": "Acil görevler içeren dosyalar",
      "patterns": [
        "URGENT:",
        "CRITICAL:",
        "SECURITY:",
        "BREAKING:"
      ]
    }
  }
}
```

### Güvenlik Deseni Algılama
```json
{
  "security_filters": {
    "potential_vulnerabilities": {
      "description": "Potansiyel güvenlik sorunları olan dosyalar",
      "patterns": [
        "eval\\\\(",                    // Kod enjeksiyonu
        "exec\\\\(",                    // Kod çalıştırma
        "input\\\\(",                   // Kullanıcı girişi
        "raw_input\\\\(",              // Ham giriş
        "os\\\\.system\\\\(",            // Sistem komutları
        "subprocess\\\\.",             // Process çalıştırma
        "sql\\\\s*=.*\\\\+",            // SQL birleştirme
        "innerHTML\\\\s*=",            // XSS potansiyeli
        "document\\\\.write\\\\("        // DOM manipülasyonu
      ]
    },
    "authentication_files": {
      "description": "Kimlik doğrulama ve güvenlik ilgili dosyalar",
      "patterns": [
        "password",
        "auth",
        "login",
        "session",
        "token",
        "crypto",
        "security",
        "permission"
      ],
      "filename_patterns": true
    }
  }
}
```

## 📁 Dosya Türü Filtreleri

### Test Dosyası Algılama
```json
{
  "test_filters": {
    "test_files": {
      "description": "Test ve spec dosyaları",
      "patterns": [
        "**/test_*.py",
        "**/*_test.py",
        "**/*.test.js",
        "**/*.spec.js",
        "**/tests/**",
        "**/__tests__/**",
        "**/spec/**"
      ]
    },
    "mock_files": {
      "description": "Mock ve fixture dosyaları",
      "patterns": [
        "**/mock*.py",
        "**/fixture*.py",
        "**/*mock*",
        "**/stubs/**"
      ]
    }
  }
}
```

### Konfigürasyon Dosyaları
```json
{
  "config_filters": {
    "configuration_files": {
      "description": "Konfigürasyon ve ayar dosyaları",
      "extensions": [".json", ".yaml", ".yml", ".toml", ".ini", ".cfg", ".conf"],
      "filenames": [
        "config.py",
        "settings.py",
        "constants.py",
        "environment.js",
        "webpack.config.js",
        "package.json",
        "requirements.txt",
        "Dockerfile",
        ".env"
      ]
    },
    "build_files": {
      "description": "Build ve deployment dosyaları",
      "patterns": [
        "Makefile",
        "gulpfile.js",
        "Gruntfile.js",
        "build.gradle",
        "pom.xml",
        "CMakeLists.txt",
        "setup.py",
        "pyproject.toml"
      ]
    }
  }
}
```

### Dokümantasyon Dosyaları
```json
{
  "documentation_filters": {
    "readme_files": {
      "description": "README ve dokümantasyon dosyaları",
      "patterns": [
        "README*",
        "CHANGELOG*",
        "CONTRIBUTING*",
        "LICENSE*",
        "DOCS*",
        "*.md",
        "*.rst",
        "*.txt"
      ]
    },
    "api_documentation": {
      "description": "API dokümantasyon dosyaları",
      "patterns": [
        "**/docs/**",
        "**/api/**",
        "swagger.json",
        "openapi.yaml",
        "**/schema/**"
      ]
    }
  }
}
```

## 🎨 Dile Özel Filtreler

### Python Filtreleri
```json
{
  "python_filters": {
    "django_files": {
      "description": "Django framework dosyaları",
      "patterns": [
        "**/models.py",
        "**/views.py",
        "**/forms.py",
        "**/admin.py",
        "**/urls.py",
        "**/settings.py",
        "**/migrations/**"
      ]
    },
    "flask_files": {
      "description": "Flask framework dosyaları",
      "patterns": [
        "app.py",
        "run.py",
        "**/routes/**",
        "**/blueprints/**",
        "**/templates/**"
      ]
    },
    "data_science": {
      "description": "Veri bilimi ve ML dosyaları",
      "extensions": [".ipynb"],
      "patterns": [
        "**/analysis/**",
        "**/notebooks/**",
        "**/models/**",
        "**/data/**"
      ],
      "content_patterns": [
        "import pandas",
        "import numpy",
        "import sklearn",
        "import tensorflow",
        "import torch"
      ]
    }
  }
}
```

### JavaScript/TypeScript Filtreleri
```json
{
  "javascript_filters": {
    "react_components": {
      "description": "React bileşen dosyaları",
      "extensions": [".jsx", ".tsx"],
      "content_patterns": [
        "import React",
        "from 'react'",
        "useState",
        "useEffect",
        "Component"
      ]
    },
    "vue_components": {
      "description": "Vue.js bileşen dosyaları",
      "extensions": [".vue"],
      "content_patterns": [
        "<template>",
        "<script>",
        "<style>"
      ]
    },
    "node_backend": {
      "description": "Node.js backend dosyaları",
      "patterns": [
        "**/routes/**",
        "**/controllers/**",
        "**/middleware/**",
        "**/models/**",
        "server.js",
        "app.js"
      ]
    }
  }
}
```

### Web Geliştirme Filtreleri
```json
{
  "web_filters": {
    "frontend_files": {
      "description": "Frontend web dosyaları",
      "extensions": [".html", ".css", ".scss", ".sass", ".less"],
      "patterns": [
        "**/assets/**",
        "**/static/**",
        "**/public/**",
        "**/src/**"
      ]
    },
    "api_files": {
      "description": "API ve backend dosyaları",
      "patterns": [
        "**/api/**",
        "**/endpoints/**",
        "**/routes/**",
        "**/controllers/**"
      ]
    }
  }
}
```

## 📊 Kod Kalitesi Filtreleri

### Dosya Boyutu ve Karmaşıklığı
```json
{
  "quality_filters": {
    "large_files": {
      "description": "Refaktoring gerekebilecek büyük dosyalar",
      "criteria": {
        "lines": "> 500",
        "size_mb": "> 1"
      }
    },
    "small_files": {
      "description": "Çok küçük dosyalar",
      "criteria": {
        "lines": "< 10",
        "size_kb": "< 1"
      }
    },
    "complex_files": {
      "description": "Yüksek karmaşıklık dosyaları",
      "criteria": {
        "functions": "> 20",
        "classes": "> 5",
        "nested_blocks": "> 4"
      }
    }
  }
}
```

### Kod Sağlığı Göstergeleri
```json
{
  "health_filters": {
    "potential_issues": {
      "description": "Potansiyel kod sorunları olan dosyalar",
      "patterns": [
        "print\\\\(",                   // Debug print'leri
        "console\\\\.log\\\\(",          // Console log'ları
        "debugger;",                 // Debug ifadeleri
        "//\\\\s*TODO",               // TODO yorumları
        "#\\\\s*FIXME"                // FIXME yorumları
      ]
    },
    "unused_imports": {
      "description": "Potansiyel kullanılmayan import'lar",
      "language_specific": {
        "python": ["^import \\\\w+$", "^from \\\\w+ import"],
        "javascript": ["^import .* from", "const .* = require"]
      }
    }
  }
}
```

## ⏰ Zaman Tabanlı Filtreler

### Değişiklik Zamanı Filtreleri
```json
{
  "time_filters": {
    "recently_modified": {
      "description": "Son 7 günde değiştirilmiş dosyalar",
      "criteria": {
        "modified_days_ago": "< 7"
      }
    },
    "stale_files": {
      "description": "6+ aydır değiştirilmemiş dosyalar",
      "criteria": {
        "modified_days_ago": "> 180"
      }
    },
    "active_development": {
      "description": "Aktif geliştirme altındaki dosyalar",
      "criteria": {
        "modified_days_ago": "< 30",
        "commits_last_month": "> 3"
      }
    }
  }
}
```

## 🔧 Özel Filtre Oluşturma

### Basit Desen Filtresi
```json
{
  "name": "Veritabanı Modelleri",
  "description": "Veritabanı model ve şema dosyaları",
  "type": "pattern",
  "criteria": {
    "filename_patterns": [
      "**/models/**",
      "**/schemas/**",
      "**/*model*.py",
      "**/*schema*.py"
    ],
    "content_patterns": [
      "class.*Model",
      "db\\\\.Model",
      "models\\\\.Model",
      "Schema"
    ]
  }
}
```

### Gelişmiş Mantık Filtresi
```json
{
  "name": "API Endpoint'leri",
  "description": "REST API endpoint dosyaları",
  "type": "advanced",
  "criteria": {
    "and": [
      {
        "or": [
          {"filename_contains": "api"},
          {"filename_contains": "endpoint"},
          {"path_contains": "/api/"}
        ]
      },
      {
        "content_matches": [
          "@app\\\\.route",
          "@api\\\\.route",
          "app\\\\.get\\\\(",
          "app\\\\.post\\\\(",
          "router\\\\."
        ]
      },
      {
        "not": {
          "filename_contains": "test"
        }
      }
    ]
  }
}
```

### Bileşik Filtre
```json
{
  "name": "Güvenlik Kritik Dosyalar",
  "description": "Güvenlik incelemesi gerektiren dosyalar",
  "type": "composite",
  "filters": [
    "authentication_files",
    "potential_vulnerabilities",
    "user_input_handlers"
  ],
  "logic": "OR"
}
```

## 🎛️ Filtre Ön Ayarları

### Geliştirme İş Akışı Ön Ayarları
```json
{
  "presets": {
    "code_review": {
      "name": "Kod İncelemesi Odağı",
      "description": "Kod incelemesi için en önemli dosyalar",
      "filters": [
        "recently_modified",
        "has_functions",
        "not test_files",
        "not configuration_files"
      ]
    },
    "security_audit": {
      "name": "Güvenlik Denetimi",
      "description": "Güvenlik açısından hassas dosyalar",
      "filters": [
        "authentication_files",
        "potential_vulnerabilities",
        "user_input_handlers",
        "api_endpoints"
      ]
    },
    "performance_review": {
      "name": "Performans İncelemesi",
      "description": "Performansı etkileyen dosyalar",
      "filters": [
        "database_queries",
        "large_files",
        "complex_algorithms",
        "api_endpoints"
      ]
    },
    "refactoring_candidates": {
      "name": "Refaktoring Adayları",
      "description": "Refaktoring gerekebilecek dosyalar",
      "filters": [
        "large_files",
        "complex_files",
        "has_todos",
        "potential_issues"
      ]
    }
  }
}
```

### Proje Türü Ön Ayarları
```json
{
  "project_presets": {
    "web_application": {
      "include": [
        "frontend_files",
        "api_files",
        "database_models",
        "authentication_files"
      ],
      "exclude": [
        "test_files",
        "build_files",
        "documentation_files"
      ]
    },
    "data_science": {
      "include": [
        "notebooks",
        "data_analysis",
        "model_files",
        "visualization"
      ],
      "exclude": [
        "raw_data",
        "cache_files",
        "temporary_files"
      ]
    },
    "mobile_app": {
      "include": [
        "ui_components",
        "business_logic",
        "api_integration",
        "native_modules"
      ],
      "exclude": [
        "generated_files",
        "build_artifacts",
        "assets"
      ]
    }
  }
}
```

## 🚀 Gelişmiş Filtre Özellikleri

### Dinamik Filtreler
```json
{
  "dynamic_filters": {
    "modified_since_last_release": {
      "description": "Son Git tag'den bu yana değişen dosyalar",
      "git_command": "git diff --name-only $(git describe --tags --abbrev=0)..HEAD"
    },
    "files_by_author": {
      "description": "Belirli yazar tarafından değiştirilen dosyalar",
      "git_command": "git log --author='{{AUTHOR}}' --name-only --pretty=format: | sort -u"
    }
  }
}
```

### Makine Öğrenmesi Filtreleri
```json
{
  "ml_filters": {
    "code_similarity": {
      "description": "Benzer kod desenlerini bul",
      "algorithm": "cosine_similarity",
      "threshold": 0.8
    },
    "complexity_prediction": {
      "description": "Dosya karmaşıklığını tahmin et",
      "model": "trained_complexity_model",
      "threshold": "high"
    }
  }
}
```

### Performans Optimizasyonu
```json
{
  "filter_performance": {
    "caching": {
      "enabled": true,
      "cache_duration": "1 hour",
      "cache_size_mb": 50
    },
    "parallel_processing": {
      "enabled": true,
      "max_threads": 4
    },
    "early_termination": {
      "enabled": true,
      "max_files_per_filter": 1000
    }
  }
}
```

## 💡 Filtre En İyi Uygulamaları

### ✅ Etkili Filtre Stratejileri

#### Geniş Başla, Daralt
```
1. Proje türü ön ayarıyla başla
2. Spesifik teknoloji filtrelerini ekle
3. Kalite filtrelerini uygula
4. Son değişiklikler için Git filtrelerini kullan
5. Kalan dosyalara dosya-özel prompt'lar ekle
```

#### Hassaslık için Filtreleri Katmanla
```
Temel Katman: Proje yapısı (sadece src dosyaları)
Teknoloji Katmanı: Dile özel (Python dosyaları)
Kalite Katmanı: İyi dokümante edilmiş dosyalar
Odak Katmanı: Son değiştirilen dosyalar
```

#### Dosya-Özel Prompt'larla Birleştir
```
1. İlgili dosyaları seçmek için filtreleri kullan
2. Kritik dosyalara hedefli prompt'lar ekle
3. Genel analiz için genel şablon kullan
4. Uygun formatta export et
```

### ❌ Yaygın Filtre Hataları

#### Aşırı Filtreleme
- Çok fazla dosyayı dışlama
- Önemli bağlam kaybolabilir
- Bazı destekleyici dosyaları tut

#### Yetersiz Filtreleme
- Her şeyi dahil etme
- AI analizi için kalite miktardan önemli
- En önemli olana odaklan

#### Bağlamı Görmezden Gelme
- Bazı "önemsiz" dosyalar kritik bağlam sağlar
- Konfigürasyon dosyaları genellikle davranışı etkiler
- Test dosyaları amaçlanan kullanımı gösterir

## 🔍 Filtre Sorun Giderme

### Hiçbir Dosya Filtreyle Eşleşmiyor
```
1. Filtre sözdizimi ve desenlerini kontrol et
2. Dosya uzantılarının eşleştiğini doğrula
3. Dışlama desenlerini incele
4. Önce daha basit filtrelerle test et
```

### Çok Fazla Dosya Seçildi
```
1. Daha spesifik desenler ekle
2. Dışlama filtrelerini kullan
3. Birden fazla filtreyi AND mantığıyla birleştir
4. Dosya sayısı limitleri koy
```

### Filtre Performans Sorunları
```
1. Önbellekleme etkinleştir
2. Desen karmaşıklığını azalt
3. Erken sonlandırma kullan
4. Filtre çalıştırma süresini profille
```

---

**Profesyonel gibi filtrelemeye hazır mısınız?** Yerleşik ön ayarlarla başlayın ve spesifik ihtiyaçlarınız için yavaş yavaş özel filtreler oluşturun!

*Filtreleri versiyon kontrolü ile birleştirmeyi öğrenmek için [Git Entegrasyonu](Git-Integration-TR)'na devam edin →*