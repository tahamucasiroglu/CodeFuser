# 🎨 Şablonlar Rehberi

CodeFuser'ın güçlü şablon sisteminde ustalaşarak tutarlı, profesyonel AI-hazır kod çıktıları oluşturun.

## 🎯 Şablon Genel Bakış

Şablonlar, AI analizini belirli yönlerde yönlendiren önceden yazılmış, profesyonel olarak hazırlanmış prompt'lar sağlar. Zaman tasarrufu sağlar ve projeler arasında tutarlı sonuçlar garanti eder.

### Yerleşik Şablonlar

| Şablon | En İyi Kullanım | AI Araçları | Kullanım Durumu |
|--------|-----------------|-------------|-----------------|
| **16x Prompt** | Genel analiz | Tümü | Kapsamlı kod incelemesi |
| **Claude Project** | Claude AI | Claude | Proje kurulumu ve analizi |
| **Code Review** | Ekip incelemeleri | Tümü | Yapılandırılmış kod denetimi |
| **Documentation** | Doküman oluşturma | Tümü | API ve kod dokümantasyonu |
| **Cursor Rules** | IDE kurulumu | Cursor IDE | Geliştirme ortamı |

## 📝 Yerleşik Şablonlar Detayı

### 🔥 16x Prompt Şablonu

**Amaç**: En popüler AI analiz formatı, kapsamlı kod inceleme sağlar.

**Şablon İçeriği**:
```
Uzman bir yazılım mühendisisiniz. Lütfen sağlanan kod tabanını analiz edin ve aşağıdaki yapılandırılmış formatta öngörüler sunun:

## 1. **Mimari Genel Bakış**
- Genel sistem tasarımı ve desenleri
- Ana bileşenler ve ilişkileri
- Teknoloji yığını analizi

## 2. **Kod Kalitesi Değerlendirmesi**
- Kod organizasyonu ve yapısı
- İsimlendirme kuralları ve okunabilirlik
- Dokümantasyon kalitesi

## 3. **Güvenlik Analizi**
- Potansiyel güvenlik açıkları
- Kimlik doğrulama ve yetkilendirme
- Veri doğrulama ve temizleme

## 4. **Performans Değerlendirmeleri**
- Darboğazlar ve optimizasyon fırsatları
- Kaynak kullanım desenleri
- Ölçeklenebilirlik endişeleri

## 5. **En İyi Uygulamalar Uyumu**
- Sektör standardı uygunluğu
- Framework-özel en iyi uygulamalar
- Kod sürdürülebilirliği

## 6. **Test Stratejisi**
- Test kapsamı analizi
- Test desenleri ve kalitesi
- Eksik test senaryoları

## 7. **Bağımlılıklar ve Kütüphaneler**
- Üçüncü parti kütüphane kullanımı
- Versiyon yönetimi
- Bağımlılıkların güvenliği

## 8. **Hata İşleme**
- İstisna işleme desenleri
- Hata loglama ve izleme
- Zarif başarısızlık mekanizmaları

## 9. **Veritabanı ve Veri Katmanı**
- Veri modeli tasarımı
- Sorgu optimizasyonu
- Veri bütünlüğü

## 10. **API Tasarımı** (varsa)
- RESTful tasarım prensipleri
- API dokümantasyonu
- Versiyon stratejisi

## 11. **Yapılandırma Yönetimi**
- Ortam-özel ayarlar
- Gizli bilgi yönetimi
- Yapılandırma doğrulama

## 12. **Loglama ve İzleme**
- Loglama stratejisi ve implementasyonu
- İzleme ve uyarı
- Performans metrikleri

## 13. **Dağıtım ve DevOps**
- Dağıtım stratejisi
- CI/CD pipeline
- Kod olarak altyapı

## 14. **Ölçeklenebilirlik ve Güvenilirlik**
- Yatay ölçekleme kabiliyeti
- Hata toleransı
- Yük dağıtımı

## 15. **Bakım ve Teknik Borç**
- Kod borcu değerlendirmesi
- Refaktoring fırsatları
- Uzun vadeli sürdürülebilirlik

## 16. **Öneriler**
- Öncelikli iyileştirmeler
- Zaman çizelgeli eylem maddeleri
- İmplementasyon stratejileri

Lütfen ilgili yerlerde koddan spesifik örnekler verin ve bulguları etki ve aciliyete göre önceliklendirin.
```

**En İyi Kullanım**:
- Hedefli analiz için dosya-özel prompt'larla
- Kolay okuma için HTML export'u
- Kapsamlı inceleme gerektiren büyük kod tabanları

### 🤖 Claude Project Şablonu

**Amaç**: Claude AI'ın proje özelliği için optimize edilmiş, yapılandırılmış bağlam sağlar.

**Şablon İçeriği**:
```
Bu {{PROJECT_NAME}} projesi için bir kod tabanıdır. Lütfen bu kod tabanını aşağıdakileri anlamak için analiz edin:

## Proje Bağlamı
{{PROJECT_DESCRIPTION}}

## Analiz Hedefleri
- Genel mimari ve tasarım desenlerini anlama
- Ana işlevsellik ve iş mantığını belirleme
- Kod kalitesini ve potansiyel iyileştirmeleri inceleme
- Güvenlik değerlendirmelerini assess etme
- Performans ve ölçeklenebilirlik açılarını değerlendirme

## Ana Odak Alanları
1. **Temel İşlevsellik**: Ana iş mantığı ve özellikler
2. **Veri Akışı**: Verinin sistem içindeki hareketi
3. **Entegrasyon Noktaları**: Harici API'lar, veritabanları, servisler
4. **Hata İşleme**: İstisna yönetimi ve kurtarma
5. **Test**: Test kapsamı ve kalitesi

## Spesifik Sorular
- Hangi ana mimari desenler kullanılıyor?
- Potansiyel güvenlik açıkları var mı?
- Performans darboğazları neler?
- Kod ne kadar sürdürülebilir ve genişletilebilir?
- Hangi iyileştirmeleri önerirsiniz?

Lütfen spesifik kod örnekleri ve uygulanabilir önerilerle kapsamlı bir analiz sağlayın.

## Kod Yapısı
Aşağıdaki dosyalar sistemin ana bileşenlerini temsil eder:
{{FILE_LIST}}

Her dosyanın spesifik analiz talimatları olabilir. Lütfen sağlanan dosya-özel prompt'lara dikkat edin.
```

**En İyi Kullanım**:
- Claude AI platformu
- Proje kurulumu ve ilk analiz
- Ekip onboardingı ve bilgi transferi

### 🔍 Code Review Şablonu

**Amaç**: Ekip işbirliği ve kapsamlı kod incelemeleri için yapılandırılmış şablon.

**Şablon İçeriği**:
```
# Kod İncelemesi: {{PROJECT_NAME}}

## İnceleme Bağlamı
- **İnceleyici**: {{REVIEWER_NAME}}
- **İnceleme Tarihi**: {{REVIEW_DATE}}
- **İnceleme Türü**: {{REVIEW_TYPE}} (Pre-commit, Post-commit, Güvenlik, Performans)
- **Değişen Dosyalar**: {{CHANGED_FILES_COUNT}} dosya

## İnceleme Kontrol Listesi

### 🔍 **İşlevsellik**
- [ ] Kod amaçlanan işlevselliği gerçekleştiriyor
- [ ] Mantık doğru ve verimli
- [ ] Kenar durumlar uygun şekilde işleniyor
- [ ] İş gereksinimleri karşılanıyor

### 🏗️ **Tasarım ve Mimari**
- [ ] Kod yerleşik tasarım desenlerini takip ediyor
- [ ] Endişelerin ayrılması korunuyor
- [ ] Bağımlılıklar düzgün yönetiliyor
- [ ] Arayüzler iyi tanımlanmış

### 📖 **Kod Kalitesi**
- [ ] Kod okunabilir ve iyi dokümante edilmiş
- [ ] İsimlendirme kuralları takip ediliyor
- [ ] Fonksiyonlar/metodlar uygun boyutta
- [ ] Kod tekrarı minimize edilmiş

### 🔒 **Güvenlik**
- [ ] Girdi doğrulama implementé edilmiş
- [ ] Kimlik doğrulama/yetkilendirme doğru
- [ ] Hassas veriler düzgün işleniyor
- [ ] SQL injection/XSS açıkları kontrol edilmiş

### ⚡ **Performans**
- [ ] Belirgin performans darboğazları yok
- [ ] Veritabanı sorguları optimize edilmiş
- [ ] Bellek kullanımı makul
- [ ] Önbellekleme uygun şekilde kullanılmış

### 🧪 **Test**
- [ ] Birim testler kapsamlı
- [ ] Entegrasyon testleri ana akışları kapsıyor
- [ ] Test verisi uygun
- [ ] Hata senaryoları test edilmiş

### 📝 **Dokümantasyon**
- [ ] Kod yorumları karmaşık mantığı açıklıyor
- [ ] API dokümantasyonu güncellenmiş
- [ ] README dosyaları güncel
- [ ] Değişiklik logları korunuyor

## Detaylı Analiz

Lütfen her dosyayı analiz edin ve sağlayın:

1. **Özet**: Değişikliklerin/işlevselliğin kısa genel bakışı
2. **Güçlü Yanlar**: İyi yapılmış şeyler
3. **Sorunlar**: Bulunan problemler (önem derecesine göre kategorize)
4. **Öneriler**: Spesifik iyileştirme tavsiyeleri
5. **Sorular**: Açıklama gereken noktalar

## Risk Değerlendirmesi
- **Yüksek Risk**: Düzeltilmesi gereken kritik sorunlar
- **Orta Risk**: Ele alınması gereken önemli sorunlar
- **Düşük Risk**: Küçük iyileştirmeler ve öneriler

## Onay Durumu
- [ ] Onaylandı (merge'e hazır)
- [ ] Küçük değişikliklerle onaylandı
- [ ] Önemli değişiklikler gerekiyor
- [ ] Reddedildi (büyük yeniden çalışma gerekiyor)

## Eylem Maddeleri
Sorumlu ve son tarihli spesifik görevleri listeleyin.
```

**En İyi Kullanım**:
- Ekip kod incelemeleri
- Pull request analizi
- Kalite güvence süreçleri
- Resmi dokümantasyon için DOCX export'u

### 📚 Documentation Şablonu

**Amaç**: Kod analizinden kapsamlı dokümantasyon oluşturma.

**Şablon İçeriği**:
```
# {{PROJECT_NAME}} Dokümantasyonu

Bu kod tabanı için aşağıdakileri içeren kapsamlı dokümantasyon oluşturun:

## 📋 **Proje Genel Bakış**
- Amaç ve ana işlevsellik
- Hedef kitle ve kullanım durumları
- Ana özellikler ve kabiliyetler
- Teknoloji yığını ve bağımlılıklar

## 🏗️ **Mimari Dokümantasyonu**
- Sistem mimarisi diyagramı (metinle açıklayın)
- Bileşen ilişkileri ve etkileşimleri
- Veri akışı ve işleme pipeline'ı
- Harici entegrasyonlar ve bağımlılıklar

## 📖 **API Dokümantasyonu**
Her API endpoint'i veya genel arayüz için:
- Amaç ve işlevsellik
- Girdi parametreleri ve doğrulama
- Çıktı formatı ve örnekleri
- Hata yanıtları ve işleme
- Kimlik doğrulama gereksinimleri

## 🔧 **Kurulum ve Yükleme**
- Sistem gereksinimleri
- Yükleme adımları
- Yapılandırma talimatları
- Ortam kurulumu
- Veritabanı kurulumu (varsa)

## 💻 **Kullanım Örnekleri**
- Temel kullanım senaryoları
- Açıklamalı kod örnekleri
- Yaygın kullanım durumları
- Entegrasyon için en iyi uygulamalar

## 📁 **Kod Yapısı**
Her ana bileşen/dosya için:
- Amaç ve sorumluluk
- Ana sınıflar/fonksiyonlar
- Bağımlılıklar ve ilişkiler
- Yapılandırma seçenekleri

## 🔌 **Entegrasyon Rehberi**
- Harici sistemlerle entegrasyon nasıl
- API kullanım örnekleri
- SDK veya kütüphane kullanımı
- Üçüncü parti servis entegrasyonları

## 🧪 **Test Rehberi**
- Test stratejisi ve yaklaşımı
- Testlerin nasıl çalıştırılacağı
- Test verisi kurulumu
- Kapsam gereksinimleri

## 🚀 **Dağıtım Rehberi**
- Dağıtım gereksinimleri
- Ortam yapılandırması
- CI/CD pipeline kurulumu
- İzleme ve loglama

## 🔧 **Yapılandırma Referansı**
- Tüm yapılandırma seçenekleri
- Ortam değişkenleri
- Özellik bayrakları
- Performans ayarlama

## 📞 **Sorun Giderme**
- Yaygın sorunlar ve çözümleri
- Hata mesajları ve düzeltmeleri
- Performans sorun giderme
- Debug bilgileri

## 🔄 **Bakım**
- Düzenli bakım görevleri
- Güncelleme prosedürleri
- Yedekleme ve kurtarma
- Güvenlik değerlendirmeleri

Lütfen dokümantasyonu açık, kapsamlı ve hem geliştiriciler hem de son kullanıcılar için uygun hale getirin. Yardımcı olacak yerlerde spesifik kod örnekleri ekleyin.
```

**En İyi Kullanım**:
- Dokümantasyon oluşturma projeleri
- API dokümantasyonu
- Ekip bilgi tabanları
- Web dokümantasyonu için HTML export'u

### ⚙️ Cursor Rules Şablonu

**Amaç**: Cursor IDE için IDE-özel yapılandırma ve kurallar oluşturma.

**Şablon İçeriği**:
```
# {{PROJECT_NAME}} için Cursor IDE Kuralları

Bu kod tabanı analizine dayanarak, Cursor IDE kuralları ve yapılandırması oluşturun:

## 🎯 **Proje-Özel Kurallar**

### Kod Stili ve Formatlama
- Girinti tercihleri (spaces/tabs, boyut)
- Satır uzunluğu limitleri
- Değişkenler, fonksiyonlar, sınıflar için isimlendirme kuralları
- Dosya organizasyon desenleri

### Dile-Özel Ayarlar
Projedeki her dil için:
- Linter yapılandırması
- Formatter ayarları
- Language server seçenekleri
- Uzantı önerileri

### AI Assistant Yapılandırması
- AI önerileri için tercih edilen kodlama desenleri
- Kod tamamlama için bağlam tercihleri
- Kod incelemesi odak alanları
- Dokümantasyon stili tercihleri

## 🔧 **Workspace Ayarları**

### Dosya Eşleştirmeleri
- Dosya türü eşleştirmeleri
- Sözdizimi vurgulama tercihleri
- Farklı dosya türleri için ikon temaları

### Arama ve Navigasyon
- Arama için dışlama desenleri
- Dosya izleyici yapılandırmaları
- Hızlı açma tercihleri

### Git Entegrasyonu
- Dışlama desenleri
- Commit mesaj şablonları
- Dal isimlendirme kuralları
- Pre-commit hook'ları

## 📝 **Kod Şablonları ve Snippet'ler**

Aşağıdakiler için snippet'ler oluşturun:
- Yaygın fonksiyon şablonları
- Sınıf yapısı şablonları
- Test dosyası şablonları
- Dokümantasyon şablonları

## 🛠️ **Debugging Yapılandırması**
- Launch yapılandırmaları
- Ortam değişkenleri
- Debugging tercihleri
- Breakpoint şablonları

## 📦 **Uzantı Önerileri**
Teknoloji yığınına dayalı:
- Proje için temel uzantılar
- İsteğe bağlı verimlilik uzantıları
- Tema ve UI uzantıları
- Dile-özel uzantılar

## 🔍 **Linting ve Validation Kuralları**
- ESLint/TSLint yapılandırması
- Python linting kuralları
- Özel validation kuralları
- Kod kalitesi metrikleri

## 🧪 **Test Entegrasyonu**
- Test runner yapılandırması
- Test dosyası desenleri
- Kapsam raporlama
- Test debugging kurulumu

Bu spesifik proje için optimal olan tam `.cursor-rules` dosya içeriğini oluşturun.
```

**En İyi Kullanım**:
- Cursor IDE kurulumu
- Ekip geliştirme ortamı standardizasyonu
- Proje onboardingı
- Doğrudan IDE yapılandırması için TXT export'u

## 🛠️ Özel Şablon Oluşturma

### Şablon Dosya Yapısı

Şablonlar `templates/` dizininde JSON dosyaları olarak saklanır:

```json
{
  "name": "Özel Şablonum",
  "description": "Bu şablonun ne yaptığının açıklaması",
  "version": "1.0.0",
  "author": "Adınız",
  "category": "custom",
  "variables": {
    "PROJECT_NAME": {
      "type": "string",
      "default": "{{AUTO_DETECT}}",
      "description": "Projenin adı"
    },
    "ANALYSIS_TYPE": {
      "type": "select",
      "options": ["security", "performance", "quality", "architecture"],
      "default": "quality",
      "description": "Yapılacak analiz türü"
    },
    "REVIEWER_NAME": {
      "type": "string",
      "default": "{{USER_NAME}}",
      "description": "İncelemeyi yapan kişinin adı"
    }
  },
  "prompt": "Şablon içeriğiniz burada...\\n\\nDeğişken ikamesi için {{PROJECT_NAME}} kullanın.\\nAnaliz türü: {{ANALYSIS_TYPE}}\\nİnceleyici: {{REVIEWER_NAME}}"
}
```

### Değişken Türleri

#### String Değişkenleri
```json
{
  "PROJECT_NAME": {
    "type": "string",
    "default": "Projem",
    "description": "Proje adı",
    "required": true
  }
}
```

#### Select Değişkenleri
```json
{
  "ANALYSIS_TYPE": {
    "type": "select",
    "options": ["security", "performance", "quality"],
    "default": "quality",
    "description": "Analiz türü"
  }
}
```

#### Boolean Değişkenleri
```json
{
  "INCLUDE_TESTS": {
    "type": "boolean",
    "default": true,
    "description": "Test dosyalarını analize dahil et"
  }
}
```

#### Otomatik Algılama Değişkenleri
```json
{
  "PROJECT_NAME": {
    "type": "string",
    "default": "{{AUTO_DETECT}}",
    "description": "Klasör adından otomatik algılanır"
  }
}
```

### Yerleşik Değişken İkameleri

CodeFuser birçok yerleşik değişken sağlar:

```
{{PROJECT_NAME}}        - Otomatik algılanan proje adı
{{USER_NAME}}          - Mevcut kullanıcı adı
{{DATE}}               - Mevcut tarih (YYYY-MM-DD)
{{TIME}}               - Mevcut saat (HH:MM:SS)
{{TIMESTAMP}}          - ISO timestamp
{{FILE_COUNT}}         - Seçilen dosya sayısı
{{FILE_LIST}}          - Seçilen dosyaların listesi
{{PROJECT_DESCRIPTION}} - Otomatik algılanan veya kullanıcı sağlanan
{{REVIEWER_NAME}}      - Mevcut kullanıcı veya belirtilen
{{REVIEW_DATE}}        - Formatlanmış mevcut tarih
{{CHANGED_FILES_COUNT}} - Dosya sayısı (Git entegrasyonu için)
```

### Özel Şablon Örnekleri

#### Güvenlik Denetimi Şablonu
```json
{
  "name": "Güvenlik Denetimi",
  "description": "Kapsamlı güvenlik analizi şablonu",
  "version": "1.0.0",
  "category": "security",
  "variables": {
    "SECURITY_LEVEL": {
      "type": "select",
      "options": ["basic", "standard", "comprehensive", "enterprise"],
      "default": "standard",
      "description": "Güvenlik analizi seviyesi"
    },
    "COMPLIANCE_STANDARD": {
      "type": "select",
      "options": ["OWASP", "PCI-DSS", "GDPR", "SOX", "HIPAA"],
      "default": "OWASP",
      "description": "Kontrol edilecek uyum standardı"
    }
  },
  "prompt": "# Güvenlik Denetimi: {{PROJECT_NAME}}\\n\\n{{COMPLIANCE_STANDARD}} uyumuna odaklanan {{SECURITY_LEVEL}} güvenlik analizi yapın.\\n\\n## Analiz Kapsamı\\n- Kimlik doğrulama ve yetkilendirme mekanizmaları\\n- Girdi doğrulama ve temizleme\\n- Veri şifreleme ve koruma\\n- Oturum yönetimi\\n- Hata işleme ve bilgi sızıntısı\\n- Bağımlılık açıkları\\n\\nÖnem derecesi ve çözüm adımlarıyla spesifik bulgular sağlayın."
}
```

#### Performans Analizi Şablonu
```json
{
  "name": "Performans Analizi",
  "description": "Kod performans optimizasyon şablonu",
  "version": "1.0.0",
  "category": "performance",
  "variables": {
    "TARGET_ENVIRONMENT": {
      "type": "select",
      "options": ["development", "staging", "production"],
      "default": "production",
      "description": "Analiz için hedef ortam"
    },
    "PERFORMANCE_GOALS": {
      "type": "string",
      "default": "< 100ms yanıt süresi",
      "description": "Performans hedefleri"
    }
  },
  "prompt": "# Performans Analizi: {{PROJECT_NAME}}\\n\\n{{TARGET_ENVIRONMENT}} ortamı için kod performansını analiz edin.\\n\\n## Performans Hedefleri\\n{{PERFORMANCE_GOALS}}\\n\\n## Analiz Alanları\\n1. Algoritma karmaşıklığı ve optimizasyon\\n2. Veritabanı sorgu performansı\\n3. Bellek kullanımı ve garbage collection\\n4. I/O işlemleri ve blocking çağrılar\\n5. Önbellekleme stratejileri\\n6. Eşzamanlılık ve paralel işleme\\n\\nBeklenen etkiyle spesifik optimizasyon önerileri sağlayın."
}
```

## 🔧 Şablon Yönetimi

### Özel Şablonları Yükleme

1. **Şablon Dosyası Oluştur**: `templates/my_template.json` olarak kaydet
2. **CodeFuser'ı Yeniden Başlat**: Şablonlar başlangıçta yüklenir
3. **Şablon Seç**: Şablon dropdown'ında mevcut olur

### Şablonları Paylaşma

#### Ekip Şablon Deposu
```json
{
  "team_templates": {
    "repository_url": "https://github.com/yourteam/codefuser-templates",
    "auto_update": true,
    "templates": [
      "security_audit.json",
      "performance_review.json",
      "architecture_analysis.json"
    ]
  }
}
```

#### Şablon Paketi
```json
{
  "template_package": {
    "name": "Şirket Şablonları v1.0",
    "templates": [
      {
        "file": "security_audit.json",
        "category": "security"
      },
      {
        "file": "code_review.json",
        "category": "review"
      }
    ]
  }
}
```

### Şablon Doğrulama

Şablonlar şunlar için doğrulanır:
- **JSON Sözdizimi**: Geçerli JSON yapısı
- **Gerekli Alanlar**: name, description, prompt
- **Değişken Sözdizimi**: Uygun {{VARIABLE}} formatı
- **Döngüsel Referanslar**: Kendine referans veren değişkenler yok

### Şablon Test Etme

```json
{
  "template_test": {
    "template_file": "my_template.json",
    "test_variables": {
      "PROJECT_NAME": "Test Projesi",
      "ANALYSIS_TYPE": "security"
    },
    "expected_output": "Oluşturulan prompt şunları içermeli..."
  }
}
```

## 🚀 Gelişmiş Şablon Özellikleri

### Koşullu İçerik
```json
{
  "prompt": "# {{PROJECT_NAME}} için Analiz\\n\\n{{IF INCLUDE_TESTS}}## Test Analizi\\nTest kapsamı ve kalitesini analiz edin.{{ENDIF}}\\n\\n{{IF SECURITY_FOCUS}}## Güvenlik İncelemesi\\nGüvenlik açıklarına odaklanın.{{ENDIF}}"
}
```

### Şablon Mirası
```json
{
  "extends": "base_template.json",
  "override_variables": {
    "ANALYSIS_TYPE": "security"
  },
  "additional_prompt": "\\n\\n## Ek Güvenlik Kontrolleri\\n..."
}
```

### Çok Dilli Şablonlar
```json
{
  "name": "Kod İncelemesi",
  "localized": {
    "en": {
      "name": "Code Review",
      "description": "Comprehensive code review template"
    },
    "tr": {
      "name": "Kod İncelemesi",
      "description": "Kapsamlı kod inceleme şablonu"
    }
  }
}
```

## 💡 Şablon En İyi Uygulamaları

### ✅ Bunu Yapın
- **Net Açıklamalar**: Şablonun ne yaptığını açıklayın
- **Mantıklı Değişkenler**: Anlamlı değişken isimleri kullanın
- **Yapılandırılmış Prompt'lar**: Başlıklar ve bölümlerle organize edin
- **Spesifik Talimatlar**: Beklenen çıktılar hakkında net olun
- **Versiyon Kontrolü**: Şablon değişikliklerini takip edin
- **Test Şablonları**: Örnek projelerle doğrulayın

### ❌ Bunu Yapmayın
- **Genel Prompt'lar**: Çok geniş veya belirsiz talimatlar
- **Çok Fazla Değişken**: Basit ve odaklı tutun
- **Döngüsel Bağımlılıklar**: Kendine referans veren değişkenler
- **Aşırı Uzun Prompt'lar**: 2000 karakterin altında tutun
- **Sabit Kodlanmış Değerler**: Esneklik için değişken kullanın

### 🎯 Şablon Kategorileri

Şablonları amaca göre organize edin:
- **Analysis**: Genel kod analizi şablonları
- **Security**: Güvenlik odaklı şablonlar
- **Performance**: Performans optimizasyon şablonları
- **Documentation**: Dokümantasyon oluşturma şablonları
- **Review**: Kod incelemesi ve kalite şablonları
- **Custom**: Organizasyon-özel şablonlar

---

**Güçlü şablonlar oluşturmaya hazır mısınız?** Yerleşik şablonlarla başlayın ve spesifik ihtiyaçlarınız için özelleştirin!

*Şablonları gelişmiş filtreleme ile birleştirmeyi öğrenmek için [Akıllı Filtreler](Smart-Filters-TR)'e devam edin →*