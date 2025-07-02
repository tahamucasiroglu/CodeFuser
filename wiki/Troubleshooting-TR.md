# 🔧 Sorun Giderme Rehberi

CodeFuser v2.0 için kapsamlı sorun giderme rehberi - yaygın sorunları çözün ve performansı optimize edin.

## 🚨 Yaygın Sorunlar

### Kurulum ve Başlatma Sorunları

#### Windows EXE Başlamıyor
```
Belirtiler: CodeFuser.exe'ye çift tıklıyorsun ama hiçbir şey olmuyor
Çözümler:
1. Yönetici olarak çalıştır
2. Windows Defender/Antivirüs dışlamalarını kontrol et
3. Windows sürüm uyumluluğunu doğrula (Windows 10/11)
4. Eksik Visual C++ Redistributable'ları kontrol et
5. Hata mesajlarını görmek için Komut İstemi'nden çalıştır
```

#### Python Sürüm Sorunları
```bash
# Python sürümünü kontrol et
python --version

# Gerekli: Python 3.8+
# Sürüm çok eskiyse:
# - python.org'dan Python 3.8+ yükle
# - PATH ortam değişkenini güncelle
# - Terminal/komut istemi'ni yeniden başlat
```

#### Eksik Bağımlılıklar
```bash
# Gerekli paketleri yükle
pip install -r requirements.txt

# Belirli paket başarısız olursa:
pip install --upgrade pip
pip install package_name --no-cache-dir

# Geliştirme kurulumu için:
pip install -e .
```

### Arayüz ve Görüntü Sorunları

#### Tam Ekran Modu Sorunları
```json
// user_settings.json'da düzelt
{
  "interface": {
    "fullscreen": false,
    "window_size": "1200x800",
    "remember_window_state": true
  }
}
```

#### Font ve Metin Görüntüleme Sorunları
```json
{
  "interface": {
    "font_size": 10,
    "high_dpi_scaling": "auto",
    "theme": "modern"
  }
}
```

#### Renkler Düzgün Görüntülenmiyor
```json
{
  "interface": {
    "colors": {
      "selected_file": "#fff3a0",
      "selected_with_prompt": "#d4f5d4",
      "prompt_only": "#ffcccc",
      "background": "#f8f9fa"
    }
  }
}
```

### Dosya Ağacı ve Seçim Sorunları

#### Dosyalar Görünmüyor
```
Bu ayarları kontrol et:
1. Proje türü seçimi (Python, JavaScript, vb.)
2. Dosya uzantısı filtreleri
3. Yapılandırmadaki dışlama desenleri
4. Maksimum dosya tarama limitleri
5. Gizli dosya görünürlüğü
```

#### Dosya Ağacı Yavaş Yükleniyor
```json
{
  "performance": {
    "max_files_scan": 5000,
    "scan_timeout_seconds": 30,
    "parallel_scanning": true,
    "max_worker_threads": 2
  }
}
```

#### Özel Prompt'lar Kaydedilmiyor
```
Yaygın nedenler:
1. Config dizininde dosya izinleri
2. user_settings.json'da JSON sözdizimi hataları
3. Dosya yolu kodlama sorunları
4. Yetersiz disk alanı
```

### Export ve Çıktı Sorunları

#### Büyük Projelerle Export Başarısız
```json
{
  "performance": {
    "memory_limit_mb": 1024,
    "max_export_size_mb": 100
  },
  "output_settings": {
    "chunk_large_files": true,
    "compress_output": true
  }
}
```

#### PDF Export Sorunları
```json
{
  "format_settings": {
    "pdf": {
      "embed_fonts": true,
      "fallback_font": "Arial",
      "reduce_file_size": true,
      "image_quality": "medium"
    }
  }
}
```

#### HTML Export Açılmıyor
```
Çözümler:
1. Varsayılan tarayıcı ayarlarını kontrol et
2. Farklı tarayıcı dene
3. HTML dosyasının bozuk olmadığını doğrula
4. Dosya izinlerini kontrol et
5. Gizli/incognito modda test et
```

#### DOCX Export Sorunları
```json
{
  "format_settings": {
    "docx": {
      "compatibility_mode": "2016",
      "embed_fonts": false,
      "use_fallback_fonts": true
    }
  }
}
```

### Git Entegrasyonu Sorunları

#### Git Algılanmadı
```bash
# Git kurulumunu doğrula
git --version

# PATH'te Git'i kontrol et
echo $PATH  # Linux/Mac
echo %PATH%  # Windows

# Gerekirse Git repo başlat
git init
```

#### Git Durumu Güncellenmiyor
```json
{
  "git_integration": {
    "refresh_interval_seconds": 5,
    "auto_detect_repository": true,
    "cache_git_status": false
  }
}
```

#### Büyük Depo Performansı
```json
{
  "git_integration": {
    "shallow_analysis": true,
    "max_files_analyze": 1000,
    "skip_binary_files": true,
    "use_git_filters": true
  }
}
```

### Şablon ve Prompt Sorunları

#### Şablonlar Yüklenmiyor
```
Kontrol et:
1. Şablon dizini mevcut
2. JSON sözdizimi geçerli
3. Dosya izinleri
4. Şablon dosya kodlaması (UTF-8)
5. Gerekli şablon alanları mevcut
```

#### Değişken İkamesi Çalışmıyor
```json
// Şablonlarda değişken sözdizimini doğrula
{
  "prompt": "{{PROJECT_NAME}} güvenlik sorunları için analiz et",
  "variables": {
    "PROJECT_NAME": {
      "type": "string",
      "default": "{{AUTO_DETECT}}"
    }
  }
}
```

#### Özel Şablon Hataları
```bash
# Şablon JSON'unu doğrula
python -m json.tool template.json

# Yaygın sorunları kontrol et:
# - Eksik gerekli alanlar
# - Geçersiz değişken referansları
# - Döngüsel bağımlılıklar
```

## ⚡ Performans Sorunları

### Yavaş Dosya Tarama

#### Büyük Proje Optimizasyonu
```json
{
  "performance": {
    "max_files_scan": 5000,
    "parallel_scanning": true,
    "max_worker_threads": 4,
    "exclude_large_files": true,
    "max_file_size_mb": 5
  }
}
```

#### Ağ Sürücüsü Performansı
```json
{
  "performance": {
    "network_timeout_seconds": 60,
    "cache_network_files": true,
    "batch_file_operations": true
  }
}
```

### Bellek Kullanım Sorunları

#### Yüksek Bellek Tüketimi
```json
{
  "performance": {
    "memory_limit_mb": 512,
    "garbage_collection_interval": 100,
    "clear_cache_threshold_mb": 200
  }
}
```

#### Bellek Sızıntıları
```
Çözümler:
1. CodeFuser'ı periyodik olarak yeniden başlat
2. Önbelleği manuel temizle
3. Eşzamanlı işlemleri azalt
4. En son sürüme güncelle
```

### UI Yanıtlılığı

#### Yavaş Arayüz Güncellemeleri
```json
{
  "performance": {
    "ui_update_interval_ms": 200,
    "defer_non_critical_updates": true,
    "batch_ui_updates": true
  }
}
```

#### İşlemler Sırasında Donma
```json
{
  "performance": {
    "async_operations": true,
    "show_progress_bars": true,
    "allow_operation_cancellation": true
  }
}
```

## 🔒 Güvenlik ve Gizlilik Sorunları

### Dosya Erişim Sorunları

#### İzin Reddedildi Hataları
```bash
# Windows: Yönetici olarak çalıştır
# Linux/Mac: Dosya izinlerini kontrol et
chmod 755 /path/to/codefuser
chmod 644 /path/to/config/files
```

#### Antivirüs Yanlış Pozitifler
```
Çözümler:
1. CodeFuser'ı antivirüs dışlamalarına ekle
2. Windows Defender dışlamalarını kullan
3. Gerçek zamanlı korumayı geçici devre dışı bırak
4. AV satıcısına yanlış pozitif raporu gönder
```

### Veri Gizliliği Endişeleri

#### Hassas Dosya Algılama
```json
{
  "security": {
    "scan_for_secrets": true,
    "secret_patterns": [
      "password", "api_key", "secret", "token"
    ],
    "exclude_suspicious_files": true,
    "warn_before_export": true
  }
}
```

#### Yerel Veri Depolama
```json
{
  "privacy": {
    "store_file_paths_only": true,
    "clear_cache_on_exit": true,
    "encrypt_sensitive_data": true,
    "log_level": "warning"
  }
}
```

## 🌐 Dil ve Yerelleştirme Sorunları

### Dil Değişmiyor

#### Locale Yapılandırması
```json
{
  "interface": {
    "language": "tr",  // veya "en"
    "auto_detect_language": false,
    "fallback_language": "en"
  }
}
```

#### Eksik Çeviriler
```
Kontrol et:
1. locales/tr.json mevcut
2. Dosya kodlaması UTF-8
3. JSON sözdizimi geçerli
4. Tüm gerekli anahtarlar mevcut
```

### Metin Kodlama Sorunları

#### Özel Karakterler Görüntülenmiyor
```json
{
  "output_settings": {
    "encoding": "utf-8",
    "normalize_unicode": true,
    "handle_special_chars": true
  }
}
```

## 🔄 Yapılandırma Sorunları

### Ayarlar Kaydedilmiyor

#### Yapılandırma Dosyası Sorunları
```bash
# Dosya izinlerini kontrol et
ls -la config/user_settings.json

# JSON sözdizimini doğrula
python -c "import json; json.load(open('config/user_settings.json'))"

# Bozuksa varsayılanlara sıfırla
mv user_settings.json user_settings.json.backup
# Varsayılanları yeniden oluşturmak için CodeFuser'ı yeniden başlat
```

#### Geçersiz Yapılandırma Değerleri
```json
// Yaygın doğrulama sorunları:
{
  "window_size": "1200x800",    // String formatı olmalı
  "max_files_scan": 10000,      // Integer olmalı
  "enabled": true,              // Boolean olmalı
  "file_extensions": [".py"]    // Array olmalı
}
```

### Ekip Yapılandırma Çakışmaları

#### Paylaşılan Ayar Sorunları
```json
{
  "team": {
    "shared_config_location": "//server/shared/config.json",
    "allow_local_overrides": true,
    "conflict_resolution": "local_wins"
  }
}
```

## 🧪 Geliştirme ve Gelişmiş Sorunlar

### Plugin Geliştirme

#### Plugin Yüklenmiyor
```python
# Plugin yapısını kontrol et
plugins/
├── __init__.py
├── my_plugin.py
└── manifest.json

# manifest.json'u doğrula
{
  "name": "My Plugin",
  "version": "1.0.0",
  "entry_point": "my_plugin.main"
}
```

#### API Entegrasyon Sorunları
```python
# API çağrılarında debug
import logging
logging.basicConfig(level=logging.DEBUG)

# API endpoint'leri kontrol et
try:
    response = api_call()
    print(f"Durum: {response.status_code}")
    print(f"Yanıt: {response.text}")
except Exception as e:
    print(f"Hata: {e}")
```

### Özel Export Formatları

#### Export Format Geliştirme
```python
class CustomExporter:
    def __init__(self):
        self.format_name = "custom"
        
    def export(self, data, output_path):
        try:
            # İmplementasyon burada
            pass
        except Exception as e:
            logging.error(f"Export başarısız: {e}")
            raise
```

## 🔍 Debug Araçları

### Debug Modunu Etkinleştir

#### Ayrıntılı Loglama
```json
{
  "debug": {
    "enabled": true,
    "log_level": "DEBUG",
    "log_file": "codefuser_debug.log",
    "include_stack_traces": true
  }
}
```

#### Performans Profilleme
```json
{
  "profiling": {
    "enabled": true,
    "profile_file_operations": true,
    "profile_ui_updates": true,
    "profile_exports": true
  }
}
```

### Log Analizi

#### Yaygın Log Desenleri
```bash
# Loglarda hataları bul
grep "ERROR" codefuser.log

# Performans sorunlarını bul
grep "SLOW" codefuser.log

# Bellek sorunlarını bul
grep "MEMORY" codefuser.log
```

#### Log Konumu
```
Windows EXE: CodeFuser_Portable/logs/
Python: ./logs/
Debug Modu: ./debug/
```

## 📞 Yardım Alma

### Toplanacak Bilgiler

#### Sistem Bilgileri
```bash
# İşletim Sistemi
uname -a  # Linux/Mac
systeminfo  # Windows

# Python sürümü
python --version

# CodeFuser sürümü
# Hakkında dialog'unu kontrol et veya --version flag'i
```

#### Yapılandırma Export'u
```json
// Destek için mevcut yapılandırmayı export et
{
  "system_info": "...",
  "configuration": "...",
  "recent_errors": "...",
  "performance_metrics": "..."
}
```

### Hata Raporlama

#### Bug Raporu Şablonu
```markdown
**Ortam:**
- OS: Windows 10/11, macOS, Linux
- CodeFuser Sürümü: 2.0.x
- Python Sürümü: 3.x.x

**Sorun Açıklaması:**
- Ne yapmaya çalışıyordunuz?
- Bunun yerine ne oldu?
- Hata mesajları (varsa)

**Yeniden Oluşturma Adımları:**
1. Birinci adım
2. İkinci adım
3. Üçüncü adım

**Yapılandırma:**
- user_settings.json'u ekle
- Özel şablonları/eklentileri belirt

**Loglar:**
- İlgili log dosyalarını ekle
- Varsa debug çıktısını dahil et
```

### Topluluk Kaynakları

#### Dokümantasyon
- [GitHub Wiki](https://github.com/tahamucasiroglu/CodeFuser/wiki)
- [Yapılandırma Rehberi](Configuration-TR)
- [Şablonlar Rehberi](Templates-Guide-TR)

#### Destek Kanalları
- [GitHub Issues](https://github.com/tahamucasiroglu/CodeFuser/issues)
- [Discussions](https://github.com/tahamucasiroglu/CodeFuser/discussions)

## 🚀 Performans Optimizasyonu

### En İyi Uygulamalar

#### Proje Kurulumu
```
✅ Yapın:
- Uygun proje türü filtrelerini kullanın
- Dışlama desenlerini düzgün yapılandırın
- Makul dosya boyutu limitleri koyun
- İlgili projeler için Git entegrasyonunu etkinleştirin

❌ Yapmayın:
- Tüm sistem sürücülerini taramayın
- Devasa binary dosyaları dahil etmeyin
- Aşırı karmaşık filtre desenlerini kullanmayın
- Önbellekleme olmadan ağ sürücülerinde çalıştırmayın
```

#### Export Optimizasyonu
```
✅ Yapın:
- Uygun export formatını seçin
- Dosya-özel prompt'ları stratejik kullanın
- Önce küçük projelerle test edin
- Bellek kullanımını izleyin

❌ Yapmayın:
- Binlerce dosyayı aynı anda export etmeyin
- Export'larda yüksek DPI görseller kullanmayın
- Doğrudan ağ konumlarına export etmeyin
- Export format sınırlarını görmezden gelmeyin
```

---

**Hala sorun mu yaşıyorsunuz?** Gelişmiş sorun giderme için [Geliştirme Rehberi](Development-TR)'ni kontrol edin veya GitHub'da [bug bildirin](https://github.com/tahamucasiroglu/CodeFuser/issues)!

*Katkıda bulunanlar için bilgi ve gelişmiş özelleştirme için [Geliştirme Rehberi](Development-TR)'ne devam edin →*