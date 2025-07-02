# 📊 Export Formatları Rehberi

CodeFuser'ın dört profesyonel export formatının tamamı ve farklı kullanım durumları için optimizasyonları.

## 🎯 Format Genel Bakış

| Format | En İyi Kullanım | Dosya Boyutu | AI Araçları | Profesyonel Kullanım |
|--------|-----------------|--------------|-------------|---------------------|
| **HTML** | Görüntüleme, AI kopyalama | Orta | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **TXT** | Basit AI girişi | Küçük | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| **DOCX** | Dokümantasyon, paylaşım | Büyük | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **PDF** | Yazdırma, arşivleme | Büyük | ⭐⭐ | ⭐⭐⭐⭐⭐ |

## 📄 TXT Formatı

### ✨ En İyi Kullanım
- **AI Aracı Girişi**: ChatGPT, Claude vb. doğrudan kopyala-yapıştır
- **Basit İşleme**: Metin analiz araçları
- **Hızlı İnceleme**: Formatlama olmadan hızlı okuma
- **Versiyon Kontrolü**: Git'te temiz diff'ler

### 🔧 Yapı
```
# CodeFuser Çıktısı
# Oluşturulma: 2024-01-15 14:30:25
# Toplam Dosya: 5

================================================================================

[PROMPT]
Bu kod tabanını güvenlik açıkları için analiz edin ve iyileştirmeler önerin.

--------------------------------------------------------------------------------

=== DOSYA: src/auth.py ===

[BU DOSYA İÇİN ÖZEL PROMPT]
Kimlik doğrulama mantığı ve oturum yönetimi güvenliğine odaklan

[İÇERİK]
def authenticate_user(username, password):
    # Burada implementasyon...

=== DOSYA: src/api.py ===

[İÇERİK]
class APIHandler:
    # Burada implementasyon...
```

### ⚙️ Yapılandırma Seçenekleri
```json
{
  "format_settings": {
    "txt": {
      "line_ending": "auto",        // "windows", "unix", "auto"
      "encoding": "utf-8",          // "utf-8", "ascii", "latin1"
      "include_separators": true,   // Dosya ayırıcıları
      "separator_length": 80,       // Ayırıcı çizgi uzunluğu
      "include_timestamps": true,   // Oluşturma meta verisi
      "include_file_stats": true    // Dosya sayısı ve boyutları
    }
  }
}
```

### 💡 İpuçları
- **AI için Mükemmel**: Formatlama dikkat dağıtmaz
- **Hafif**: En küçük dosya boyutu
- **Hızlı Yükleme**: Herhangi bir metin editöründe anında açılır
- **Arama Dostu**: İçerikte kolay arama

## 🌐 HTML Formatı

### ✨ En İyi Kullanım
- **Etkileşimli Görüntüleme**: Tarayıcı tabanlı navigasyonlu inceleme
- **AI Aracı Entegrasyonu**: Sözdizimi vurgulamalı kolay kopyalama
- **Ekip Paylaşımı**: E-posta veya web barındırma ile gönderme
- **Kod Sunumu**: Profesyonel kod vitrinleme

### 🎨 Özellikler
- **Sözdizimi Vurgulama**: 100+ dilli Prism.js entegrasyonu
- **Kopyalama Düğmeleri**: Her dosya için tek tıkla kopyalama
- **İçindekiler Tablosu**: Dosyalar arası hızlı navigasyon
- **İstatistik Panosu**: Dosya sayıları, boyutları, diller
- **Responsive Tasarım**: Masaüstü, tablet, mobilde çalışır
- **Karanlık Tema**: Profesyonel karanlık renk şeması

### 🔧 Yapı
```html
<!DOCTYPE html>
<html lang="tr">
<head>
    <title>CodeFuser Çıktısı</title>
    <!-- Sözdizimi vurgulama için Prism.js -->
    <!-- Modern CSS stillendirme -->
</head>
<body>
    <!-- Proje bilgili başlık -->
    <div class="header">
        <h1>🚀 CodeFuser Çıktısı</h1>
        <div class="meta">2024-01-15 tarihinde oluşturuldu</div>
    </div>
    
    <!-- İstatistik panosu -->
    <div class="stats">
        <div class="stat-item">
            <div class="stat-value">5</div>
            <div class="stat-label">Toplam Dosya</div>
        </div>
    </div>
    
    <!-- Prompt bölümü -->
    <div class="prompt-section">
        <h2>🎯 Prompt Talimatları</h2>
        <div class="prompt-content">Prompt'unuz burada...</div>
    </div>
    
    <!-- İçindekiler -->
    <div class="toc">
        <h3>📋 İçindekiler</h3>
        <ul>
            <li><a href="#file1">src/auth.py</a></li>
        </ul>
    </div>
    
    <!-- Sözdizimi vurgulamalı dosya içerikleri -->
    <div class="file-section" id="file1">
        <div class="file-header">
            <div class="file-path">📄 src/auth.py</div>
        </div>
        <!-- Bu dosya için özel prompt -->
        <div class="custom-prompt">
            <h4>🎯 Bu dosya için özel prompt:</h4>
            <div>Kimlik doğrulama güvenliğine odaklan...</div>
        </div>
        <div class="file-content">
            <pre><code class="language-python">
def authenticate_user(username, password):
    # Sözdizimi vurgulamalı kod
            </code></pre>
        </div>
    </div>
</body>
</html>
```

### ⚙️ Yapılandırma Seçenekleri
```json
{
  "format_settings": {
    "html": {
      "syntax_highlighting": true,      // Prism.js vurgulamayı etkinleştir
      "theme": "tomorrow-night",        // Sözdizimi teması
      "include_css": true,             // CSS'i HTML'e göm
      "copy_button": true,             // Kopyalama düğmeleri ekle
      "toc_navigation": true,          // İçindekiler tablosu
      "responsive_design": true,       // Mobil dostu
      "include_statistics": true,      // İstatistik panosu
      "custom_css_file": null,         // Özel CSS dosyası yolu
      "javascript_enabled": true,      // Etkileşimli özellikler
      "print_styles": true            // Yazdırma dostu CSS
    }
  }
}
```

### 🎨 Özelleştirme Örnekleri

#### Özel Renk Şeması
```css
/* Özel CSS dosyasına ekle */
.header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.file-section {
    border-left: 4px solid #667eea;
}

.custom-prompt {
    background: #e8f4fd;
    border: 2px solid #2196f3;
}
```

#### Karanlık Mod Geçersiz Kılma
```css
body {
    background: #1a1a1a;
    color: #e0e0e0;
}

.file-header {
    background: #2d2d2d;
    border-bottom: 1px solid #404040;
}
```

### 💡 İpuçları
- **AI Araçları için En İyi**: Sözdizimi vurgulama kod yapısını belirlemeye yardımcı olur
- **Kopyalama Düğmeleri**: Dosyaların tamamını veya bölümlerini kopyalamak için tıklayın
- **Tarayıcı Yer İmleri**: Hızlı referans için kaydedin
- **Ekip Paylaşımı**: Dahili sunucularda barındırın veya e-posta ile gönderin

## 📝 DOCX Formatı

### ✨ En İyi Kullanım
- **Resmi Dokümantasyon**: Kurumsal raporlar ve dokümantasyon
- **Ekip İşbirliği**: Word'de yorumlar ve değişiklikleri izleme
- **Profesyonel Paylaşım**: Müşteri sunumları ve incelemeleri
- **Şablon Entegrasyonu**: Şirket doküman şablonları

### 🎨 Özellikler
- **Profesyonel Formatlama**: Başlıklar, stiller, sayfa kırmaları
- **İçindekiler Tablosu**: Sayfa numaralarıyla otomatik oluşturma
- **Özel Prompt Stillendirmesi**: Dosya-özel prompt'lar için turuncu vurgulama
- **Kod Formatlaması**: Düzgün girintili monospace font
- **Meta Veri**: Doküman özellikleri ve istatistikleri
- **Yazdırma Hazır**: Uygun kenar boşlukları ve sayfa düzeni

### 🔧 Yapı
```
CodeFuser Çıktısı
Oluşturulma: 2024-01-15 14:30:25
Toplam Dosya: 5

[PROMPT]
Ana prompt metniniz burada...
────────────────────────────────────────

📄 src/auth.py

🎯 Bu dosya için özel prompt:
Kimlik doğrulama mantığı ve oturum yönetimi güvenliğine odaklan
────────────────────────

[İÇERİK]
def authenticate_user(username, password):
    """Kullanıcı kimlik bilgilerini doğrula."""
    # İmplementasyon kodu...

[Sayfa Kırması]

📄 src/api.py
...
```

### ⚙️ Yapılandırma Seçenekleri
```json
{
  "format_settings": {
    "docx": {
      "font_family": "Courier New",        // Kod fontu
      "font_size": 10,                     // Temel font boyutu
      "include_toc": true,                 // İçindekiler tablosu
      "page_breaks_between_files": true,   // Dosya başına yeni sayfa
      "header_footer": true,               // Sayfa üst/alt bilgileri
      "line_spacing": 1.15,               // Satır aralığı
      "margin_inches": 1.0,               // Sayfa kenar boşlukları
      "highlight_prompts": true,           // Turuncu prompt stillendirmesi
      "include_metadata": true,            // Doküman özellikleri
      "watermark": null                    // İsteğe bağlı filigran metni
    }
  }
}
```

### 📋 Şablon Entegrasyonu
```json
{
  "docx_template": {
    "company_template": "templates/company_template.docx",
    "header_text": "Kod İncelemesi - Gizli",
    "footer_text": "CodeFuser v2.0 tarafından oluşturuldu",
    "logo_path": "assets/company_logo.png",
    "custom_styles": {
      "code_style": "CodeBlock",
      "prompt_style": "PromptHighlight"
    }
  }
}
```

### 💡 İpuçları
- **Değişiklikleri İzle**: İşbirlikçi inceleme için Word'de etkinleştirin
- **Yorumlar**: İnceleme yorumlarını doğrudan Word'de ekleyin
- **Versiyon Kontrolü**: Yinelemeler için farklı versiyonlar olarak kaydedin
- **PDF Export**: Nihai dağıtım için Word'den PDF'e dönüştürün

## 📄 PDF Formatı

### ✨ En İyi Kullanım
- **Arşivleme**: Uzun vadeli saklama ve koruma
- **Yazdırma**: Yüksek kaliteli basılı dokümantasyon
- **Güvenlik**: Şifre koruması ve dijital imzalar
- **Dağıtım**: Platformlar arası tutarlı görüntüleme

### 🎨 Özellikler
- **Profesyonel Düzen**: Uygun tipografi ve aralık
- **Sayfa Numaraları**: Otomatik sayfalama
- **Tutarlı Görüntüleme**: Tüm cihazlarda aynı görünüm
- **Yer İmleri**: PDF navigasyon yer imleri
- **Meta Veri**: PDF özellikleri ve arama indeksleme
- **Yazdırma Optimizasyonu**: Uygun kenar boşlukları ve sayfa kırmaları

### 🔧 Yapı
```
┌─────────────────────────────────────────┐
│              CodeFuser Çıktısı            │
│         Oluşturulma: 2024-01-15           │
│             Toplam Dosya: 5              │
└─────────────────────────────────────────┘

[PROMPT]
Ana prompt metniniz uygun formatlama ve
okunabilirlik için satır kaydırma ile burada görünür.

────────────────────────────────────────────

📄 src/auth.py

[İÇERİK]
def authenticate_user(username, password):
    """Kullanıcı kimlik bilgilerini doğrula."""
    # Kod monospace font ve girintilerle
    # düzgün formatlanmıştır
                                    Sayfa 1
┌─────────────────────────────────────────┐
│                                         │
│              [Yeni Dosya]               │
│                                         │
└─────────────────────────────────────────┘
```

### ⚙️ Yapılandırma Seçenekleri
```json
{
  "format_settings": {
    "pdf": {
      "page_size": "A4",                  // "A4", "Letter", "Legal"
      "orientation": "portrait",          // "portrait", "landscape"
      "font_size": 9,                    // Temel font boyutu
      "line_height": 1.2,                // Satır aralığı
      "margins": {                       // İnç cinsinden sayfa kenar boşlukları
        "top": 1.0,
        "bottom": 1.0,
        "left": 1.0,
        "right": 1.0
      },
      "include_page_numbers": true,       // Sayfa numaralama
      "include_bookmarks": true,          // PDF navigasyonu
      "syntax_highlighting": false,       // Daha iyi yazdırma için false
      "page_breaks_between_files": true,  // Dosya başına yeni sayfa
      "header_text": "CodeFuser Export",  // Sayfa başlığı
      "footer_text": "Gizli",           // Sayfa alt bilgisi
      "watermark": null,                 // İsteğe bağlı filigran
      "security": {                      // PDF güvenlik seçenekleri
        "password_protect": false,
        "allow_printing": true,
        "allow_copying": true,
        "allow_editing": false
      }
    }
  }
}
```

### 🔒 Güvenlik Özellikleri
```json
{
  "pdf_security": {
    "owner_password": "admin_password",
    "user_password": "view_password",
    "permissions": {
      "print": "high_quality",          // "none", "low_quality", "high_quality"
      "copy": false,                    // Metin kopyalamaya izin ver
      "edit": false,                    // Doküman düzenlemeye izin ver
      "annotate": true,                 // Yorumlara/açıklamalara izin ver
      "fill_forms": false,              // Form doldurmaya izin ver
      "extract": false,                 // İçerik çıkarmaya izin ver
      "assemble": false                 // Sayfa birleştirmeye izin ver
    }
  }
}
```

### 💡 İpuçları
- **Yazdırma Önizlemesi**: Yazdırmadan önce PDF'i her zaman kontrol edin
- **Font Gömme**: Tutarlı görünüm sağlar
- **Sıkıştırma**: Kaliteyi koruyarak daha küçük dosya boyutları
- **Yer İmleri**: Büyük dokümanlarda kolay navigasyon için kullanın

## 🚀 Gelişmiş Export Özellikleri

### Dosya-Özel Prompt Entegrasyonu

Tüm formatlar dosya-özel prompt'ları içerir:

#### TXT Formatı
```
[BU DOSYA İÇİN ÖZEL PROMPT]
Kimlik doğrulama mekanizmalarını güvenlik açıkları için analiz et
```

#### HTML Formatı
```html
<div class="custom-prompt">
    <h4>🎯 Bu dosya için özel prompt:</h4>
    <div class="custom-prompt-content">
        Kimlik doğrulama mekanizmalarını güvenlik açıkları için analiz et
    </div>
</div>
```

#### DOCX Formatı
- Turuncu vurgulanmış metin kutusu
- Ana içerikten ayrı stillendirme
- Uygun aralık ve formatlama

#### PDF Formatı
- Ayrı formatlanmış bölüm
- Tutarlı tipografi
- Net görsel ayrım

### Toplu Export
```json
{
  "batch_export": {
    "enabled": true,
    "formats": ["html", "docx", "pdf"],
    "output_directory": "exports/",
    "filename_template": "{project}_{format}_{timestamp}"
  }
}
```

### Export Otomasyonu
```json
{
  "automation": {
    "auto_export_on_scan": false,
    "scheduled_exports": {
      "enabled": false,
      "frequency": "daily",
      "time": "18:00",
      "formats": ["html"]
    },
    "git_hook_export": {
      "enabled": false,
      "on_commit": true,
      "on_push": false
    }
  }
}
```

## 📊 Format Karşılaştırması

### Dosya Boyutları (Örnek 50 dosya, toplam 10MB kod)
- **TXT**: 10.2 MB (minimal ek yük)
- **HTML**: 12.5 MB (CSS + JavaScript)
- **DOCX**: 15.8 MB (XML yapısı + formatlama)
- **PDF**: 18.3 MB (gömülü fontlar + düzen)

### Oluşturma Hızı
- **TXT**: ~1 saniye (en hızlı)
- **HTML**: ~3 saniye (sözdizimi vurgulama)
- **DOCX**: ~5 saniye (doküman yapısı)
- **PDF**: ~8 saniye (düzen görüntüleme)

### AI Aracı Uyumluluğu
- **TXT**: Mükemmel - doğrudan kopyala-yapıştır
- **HTML**: Mükemmel - kopyalama düğmeleri + vurgulama
- **DOCX**: İyi - Word'den kopyalanabilir
- **PDF**: Sınırlı - kopyalama formatı bozabilir

## 🔧 Export Sorun Giderme

### Yaygın Sorunlar

#### Büyük Dosya Export'u Başarısız
```json
{
  "performance": {
    "max_export_size_mb": 100,
    "chunk_large_files": true,
    "memory_limit_mb": 512
  }
}
```

#### PDF'de Font Sorunları
```json
{
  "pdf_fonts": {
    "embed_fonts": true,
    "fallback_font": "Arial",
    "code_font": "Courier New",
    "custom_fonts_path": "fonts/"
  }
}
```

#### HTML Düzgün Görüntülenmiyor
- Tarayıcı uyumluluğunu kontrol edin
- CSS yüklenmesini doğrulayın
- JavaScript özelliklerini test edin
- HTML yapısını valide edin

#### DOCX Formatlama Sorunları
- Word sürümü uyumluluğunu kontrol edin
- Şablon yapısını doğrulayın
- Özel stilleri test edin
- Font mevcudiyetini inceleyin

---

**Export'a hazır mısınız?** İş akışınıza en uygun formatı seçin ve profesyonel kod dokümantasyonu oluşturmaya başlayın! 

*Export formatları ile şablonları birleştirmeyi öğrenmek için [Şablonlar Rehberi](Templates-Guide-TR)'ne devam edin →*