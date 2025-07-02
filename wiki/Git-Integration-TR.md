# 🐙 Git Entegrasyonu Rehberi

CodeFuser'ın güçlü Git entegrasyonundan yararlanarak değişen koda odaklanın, geliştirme ilerlemesini takip edin ve AI analiz iş akışınızı optimize edin.

## 🎯 Git Entegrasyonu Genel Bakış

CodeFuser, versiyon kontrol durumuna dayalı akıllı dosya filtreleme sağlamak için Git depolarıyla sorunsuz entegre olur ve size değişen ve en önemli olan şeylere odaklanmanıza yardımcı olur.

### Ana Özellikler

| Özellik | Açıklama | Kullanım Durumu |
|---------|----------|-----------------|
| **Durum Algılama** | Her dosya için Git durumunu göster | Değişikliklerin hızlı tanımlanması |
| **Değişiklik Filtreleme** | Değişiklik durumuna göre filtrele | Son geliştirmelere odaklanma |
| **Dal Karşılaştırması** | Dallar arası dosyaları karşılaştır | Feature dal analizi |
| **Commit Aralığı Analizi** | Belirli commit aralıklarını analiz et | Release hazırlığı |
| **Yazar Filtreleme** | Commit yazarına göre filtrele | Bireysel katkı odağı |
| **Ignore Entegrasyonu** | .gitignore desenlerine saygı göster | Temiz dosya listeleri |

## 📊 Git Durum Göstergeleri

### Durum Sembolleri
```
M  - Modified (izlenen dosya değiştirildi)
A  - Added (yeni dosya staged)
D  - Deleted (dosya kaldırıldı)
R  - Renamed (dosya taşındı/yeniden adlandırıldı)
C  - Copied (dosya kopyalandı)
?  - Untracked (yeni dosya Git'te değil)
!  - Ignored (.gitignore'a uyuyor)
U  - Unmerged (merge çakışması)
```

### Görsel Gösterim
Dosya ağacındaki dosyalar Git durumunu gösterir:
```
☑️ 📄 M  🐍 auth.py          (Değiştirilmiş dosya)
☐ 📝✨ A  📜 new_feature.js   (Özel prompt'lu eklenmiş dosya)
☑️ 📄 ?  🎨 styles.css       (İzlenmeyen dosya)
```

## 🔧 Git Yapılandırması

### Temel Git Ayarları
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
      "untracked": "?",
      "ignored": "!",
      "unmerged": "U"
    },
    "include_untracked": true,
    "ignore_git_ignored": true,
    "refresh_interval_seconds": 5
  }
}
```

### Gelişmiş Git Yapılandırması
```json
{
  "git_advanced": {
    "branch_comparison": {
      "enabled": true,
      "default_base_branch": "main",
      "show_ahead_behind": true,
      "auto_detect_base": true
    },
    "commit_analysis": {
      "enabled": true,
      "max_commits_analyze": 100,
      "include_merge_commits": false
    },
    "performance": {
      "cache_git_status": true,
      "cache_duration_seconds": 30,
      "parallel_git_commands": true
    }
  }
}
```

## 🔍 Git Tabanlı Filtreleme

### Durum Tabanlı Filtreler

#### Sadece Değiştirilmiş Dosyalar
```json
{
  "git_filters": {
    "modified_only": {
      "description": "Sadece değiştirilmiş dosyaları göster",
      "include_status": ["M", "A", "D", "R"],
      "exclude_status": ["?", "!"]
    }
  }
}
```

#### Son Değişiklikler
```json
{
  "git_filters": {
    "recent_changes": {
      "description": "Son 7 günde değişen dosyalar",
      "time_range": {
        "since": "7 days ago",
        "until": "now"
      },
      "include_status": ["M", "A", "R"]
    }
  }
}
```

#### Staged Değişiklikler
```json
{
  "git_filters": {
    "staged_changes": {
      "description": "Commit için hazır dosyalar",
      "git_command": "git diff --cached --name-only",
      "include_untracked_staged": true
    }
  }
}
```

### Dal Tabanlı Filtreleme

#### Feature Dal Değişiklikleri
```json
{
  "branch_filters": {
    "feature_branch_changes": {
      "description": "Mevcut feature dalındaki değişiklikler",
      "base_branch": "develop",
      "current_branch": "feature/new-auth",
      "comparison_type": "diff"
    }
  }
}
```

#### Release Hazırlığı
```json
{
  "release_filters": {
    "release_changes": {
      "description": "Son release'den bu yana değişiklikler",
      "base_ref": "v1.0.0",
      "current_ref": "HEAD",
      "include_new_files": true
    }
  }
}
```

### Commit Tabanlı Filtreleme

#### Commit Aralığı Analizi
```json
{
  "commit_filters": {
    "commit_range": {
      "description": "Belirli commit'lerde değişen dosyalar",
      "from_commit": "abc123",
      "to_commit": "def456",
      "include_merge_commits": false
    }
  }
}
```

#### Yazara Özel Değişiklikler
```json
{
  "author_filters": {
    "my_changes": {
      "description": "Benim değiştirdiğim dosyalar",
      "authors": ["john.doe@company.com"],
      "time_range": "last 30 days",
      "min_commits": 1
    }
  }
}
```

## 🚀 Yaygın Git İş Akışları

### 1. Kod İncelemesi İş Akışı

#### Pre-Commit İncelemesi
```
Senaryo: Commit öncesi değişiklikleri incele
Filtre: Değiştirilmiş ve staged dosyalar
Şablon: Kod İncelemesi
Odak: Kalite ve standart uyumu
```

**Yapılandırma:**
```json
{
  "workflow": "pre_commit_review",
  "filters": {
    "git_status": ["M", "A"],
    "exclude_patterns": ["test_*", "*.md"],
    "max_files": 20
  },
  "template": "code_review",
  "export_format": "html"
}
```

#### Pull Request İncelemesi
```
Senaryo: Merge öncesi feature dalını incele
Filtre: Main'e karşı dal karşılaştırması
Şablon: Kod İncelemesi
Odak: Entegrasyon ve etki analizi
```

**Yapılandırma:**
```json
{
  "workflow": "pull_request_review",
  "git_comparison": {
    "base_branch": "main",
    "feature_branch": "feature/user-auth",
    "include_context_files": true
  },
  "template": "code_review",
  "file_prompts": {
    "pattern": "auth.*\\.py",
    "prompt": "Kimlik doğrulama değişikliklerinin güvenlik etkilerine odaklan"
  }
}
```

### 2. Bug Araştırması İş Akışı

#### Son Değişiklikler Analizi
```
Senaryo: Son bug girişini araştır
Filtre: Geçen hafta değişen dosyalar
Şablon: Bug Analizi
Odak: Potansiyel nedenleri belirleme
```

**Yapılandırma:**
```json
{
  "workflow": "bug_investigation",
  "git_filters": {
    "time_range": "7 days",
    "exclude_tests": false,
    "include_config_changes": true
  },
  "template": "bug_analysis",
  "analysis_focus": "potential_issues"
}
```

#### Blame Tabanlı Analiz
```
Senaryo: Belirli değişiklikler için sorumluluğu takip et
Filtre: Belirli yazarlar tarafından değiştirilen dosyalar
Şablon: Değişiklik Etki Analizi
Odak: Değişiklik bağlamını anlama
```

### 3. Release Hazırlığı İş Akışı

#### Release Diff Analizi
```
Senaryo: Release notları ve inceleme hazırla
Filtre: Son release tag'den bu yana değişiklikler
Şablon: Release İncelemesi
Odak: Özellik tamamlığı ve kararlılık
```

**Yapılandırma:**
```json
{
  "workflow": "release_preparation",
  "git_comparison": {
    "base_ref": "v1.2.0",
    "current_ref": "HEAD",
    "group_by_feature": true
  },
  "template": "release_review",
  "include_statistics": true
}
```

### 4. Güvenlik Denetimi İş Akışı

#### Güvenlik Odaklı Git Analizi
```
Senaryo: Son değişikliklerin güvenlik denetimi
Filtre: Kimlik doğrulama ve güvenlik ilgili dosyalar
Şablon: Güvenlik Denetimi
Odak: Açık değerlendirmesi
```

**Yapılandırma:**
```json
{
  "workflow": "security_audit",
  "git_filters": {
    "modified_files": true,
    "security_patterns": [
      "**/auth/**",
      "**/security/**",
      "**/*password*",
      "**/*token*"
    ]
  },
  "template": "security_audit",
  "file_prompts": {
    "auto_generate": true,
    "focus": "security_vulnerabilities"
  }
}
```

## 📈 Git Analitik ve İçgörüler

### Commit Sıklığı Analizi
```json
{
  "git_analytics": {
    "commit_frequency": {
      "time_period": "last_30_days",
      "group_by": "author",
      "include_merge_commits": false,
      "file_types": [".py", ".js", ".ts"]
    }
  }
}
```

### Kod Churn Analizi
```json
{
  "code_churn": {
    "description": "Yüksek değişiklik sıklığına sahip dosyalar",
    "criteria": {
      "commits_per_week": "> 5",
      "lines_changed_per_commit": "> 50",
      "time_period": "last_quarter"
    },
    "risk_assessment": true
  }
}
```

### Hotspot Algılama
```json
{
  "hotspot_analysis": {
    "description": "Sıkça birlikte değişen dosyalar",
    "min_co_change_frequency": 0.7,
    "time_window": "6_months",
    "visualization": "dependency_graph"
  }
}
```

## 🔧 Gelişmiş Git Özellikleri

### Submodule Desteği
```json
{
  "submodule_integration": {
    "enabled": true,
    "include_submodule_changes": true,
    "track_submodule_updates": true,
    "recursive_analysis": false
  }
}
```

### Git LFS Entegrasyonu
```json
{
  "git_lfs": {
    "enabled": true,
    "track_lfs_files": false,
    "include_lfs_metadata": true,
    "lfs_file_handling": "reference_only"
  }
}
```

### Worktree Desteği
```json
{
  "worktree_support": {
    "enabled": true,
    "auto_detect_worktrees": true,
    "include_all_worktrees": false,
    "current_worktree_only": true
  }
}
```

## 🎛️ Git Filtre Ön Ayarları

### Geliştirme Ön Ayarları
```json
{
  "git_presets": {
    "daily_review": {
      "description": "Bugünkü değişiklikleri incele",
      "filters": {
        "since": "today",
        "author": "current_user",
        "exclude_merges": true
      }
    },
    "sprint_review": {
      "description": "Sprint değişikliklerini incele",
      "filters": {
        "since": "2 weeks ago",
        "include_team": true,
        "group_by_feature": true
      }
    },
    "hotfix_analysis": {
      "description": "Hotfix değişikliklerini analiz et",
      "filters": {
        "branch_pattern": "hotfix/*",
        "urgency": "high",
        "include_tests": true
      }
    }
  }
}
```

### Kalite Güvencesi Ön Ayarları
```json
{
  "qa_presets": {
    "regression_risk": {
      "description": "Yüksek regresyon riski olan dosyalar",
      "criteria": {
        "change_frequency": "high",
        "test_coverage": "low",
        "complexity": "high"
      }
    },
    "stability_review": {
      "description": "Kararlılık açısından kritik dosyalar",
      "criteria": {
        "change_impact": "high",
        "dependency_count": "high",
        "bug_history": "exists"
      }
    }
  }
}
```

## 🔍 Git Entegrasyonu Sorun Giderme

### Yaygın Sorunlar

#### Git Algılanmadı
```bash
# Git kurulumunu kontrol et
git --version

# Depoyu doğrula
git status

# CodeFuser Git ayarlarını kontrol et
{
  "git_integration": {
    "enabled": true,
    "auto_detect_repository": true
  }
}
```

#### Yavaş Git İşlemleri
```json
{
  "performance_optimization": {
    "git_cache": {
      "enabled": true,
      "cache_size_mb": 50,
      "cache_duration_minutes": 10
    },
    "parallel_operations": {
      "enabled": true,
      "max_concurrent": 3
    },
    "command_timeout_seconds": 30
  }
}
```

#### Büyük Depo Performansı
```json
{
  "large_repo_optimization": {
    "partial_clone": true,
    "shallow_analysis": true,
    "max_files_analyze": 1000,
    "skip_binary_files": true,
    "use_git_filters": true
  }
}
```

### Git Komut Özelleştirmesi
```json
{
  "custom_git_commands": {
    "status_command": "git status --porcelain",
    "diff_command": "git diff --name-only",
    "log_command": "git log --oneline --since='1 week ago'",
    "blame_command": "git blame --line-porcelain"
  }
}
```

## 💡 Git Entegrasyonu En İyi Uygulamaları

### ✅ Etkili Git İş Akışları

#### Son Değişikliklerle Başla
```
1. Başlangıç noktası olarak "değiştirilmiş dosyalar" filtresini kullan
2. Kritik değişikliklere dosya-özel prompt'lar ekle
3. Gerekirse bağlam dosyalarını dahil et
4. Temel işlevselliği etkileyen değişikliklere odaklan
```

#### Git'i Akıllı Filtrelerle Birleştir
```
1. Git filtresi: Son değiştirilen dosyalar
2. Akıllı filtre: Test dosyalarını hariç tut
3. Kalite filtresi: Sadece iyi dokümante edilmiş dosyaları dahil et
4. Sonuç: Yüksek kaliteli, son değiştirilen temel kod
```

#### Dal Karşılaştırmalarını Kullan
```
1. Feature dalını main'e karşı karşılaştır
2. Yeni işlevselliğe odaklan
3. Kimlik doğrulama değişikliklerine güvenlik prompt'ları ekle
4. Veritabanı değişikliklerine performans prompt'ları ekle
```

### ❌ Yaygın Git Entegrasyonu Hataları

#### Merge Commit'leri Görmezden Gelme
- Merge commit'ler önemli bağlam sağlar
- Kapsamlı analiz için bunları dahil et
- Entegrasyon noktalarını gösterirler

#### Sadece Son Değişikliklere Odaklanma
- Son değişiklikler tarihsel bağlama ihtiyaç duyar
- İlgili değişmemiş dosyaları dahil et
- Bağımlılık etkilerini düşün

#### Konfigürasyon Değişikliklerini Gözardı Etme
- Konfigürasyon değişiklikleri büyük etkilere sahip olabilir
- Ortam ve build dosyalarını dahil et
- Genellikle davranışsal değişiklikleri açıklarlar

### 🎯 Git-Özel Prompt Stratejileri

#### Değiştirilmiş Dosyalar İçin
```
"Bu dosya yakın zamanda değiştirildi. Şunlara odaklan:
1. Neyin değiştiği ve neden
2. Bağımlı kod üzerindeki etki
3. Potansiyel yan etkiler
4. Test gereksinimleri"
```

#### Yeni Dosyalar İçin
```
"Bu yeni bir dosya. Analiz et:
1. Amaç ve entegrasyon noktaları
2. Kod kalitesi ve standart uyumu
3. Eksik dokümantasyon veya testler
4. Mimari uyumu"
```

#### Silinen Dosyalar İçin
```
"Bu dosya kaldırıldı. Düşün:
1. Kaybedilen işlevsellik neydi
2. Nereye taşındı (varsa)
3. Bağımlı kod üzerindeki etki
4. Kullanıcılar için geçiş yolu"
```

## 🚀 Gelişmiş Git İş Akışları

### Sürekli Entegrasyon Entegrasyonu
```json
{
  "ci_integration": {
    "pre_commit_analysis": {
      "enabled": true,
      "run_on_staged_files": true,
      "block_commit_on_issues": false
    },
    "pull_request_analysis": {
      "enabled": true,
      "comment_on_pr": true,
      "analysis_threshold": "high_impact_changes"
    }
  }
}
```

### Ekip İşbirliği Özellikleri
```json
{
  "team_features": {
    "shared_git_filters": {
      "enabled": true,
      "sync_across_team": true,
      "filter_repository": "team-codefuser-filters"
    },
    "author_expertise_mapping": {
      "enabled": true,
      "expertise_database": "team_expertise.json",
      "suggest_reviewers": true
    }
  }
}
```

---

**Git iş akışınızı süperşarj etmeye hazır mısınız?** Temel durum filtreleme ile başlayın ve yavaş yavaş gelişmiş dal karşılaştırmaları ve commit analizini dahil edin!

*Git entegrasyonu sorunları için yardım almak üzere [Sorun Giderme Rehberi](Troubleshooting-TR)'ne devam edin →*