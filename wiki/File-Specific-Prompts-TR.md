# 🎯 Dosya Bazında Prompt Rehberi

**CodeFuser v2.0'ı en güçlü yapay zeka kod analiz aracı yapan devrimci özellik.**

## 🔥 Bu Özellik Neden Devrimci?

### CodeFuser v2.0 Öncesi
```
Geleneksel araçlar: "İşte tüm kod tabanım, analiz et"
Sonuç: Tüm dosyalarda genel analiz
```

### CodeFuser v2.0 ile
```
CodeFuser v2.0: "İşte her dosya için özel talimatlarla kod tabanım"
├── auth.py → "Güvenlik açıklarına ve kimlik doğrulama akışlarına odaklan"
├── api.py → "Hız sınırlama ve girdi doğrulama kontrol et" 
├── database.py → "Sorgu performansını ve bağlantı yönetimini analiz et"
└── utils.py → "Yardımcı fonksiyonları potansiyel optimizasyonlar için incele"
Sonuç: Her bileşen için hedeflenmiş, hassas analiz
```

## 📋 Adım Adım Öğretici

### Adım 1: Arayüzü Anlama
1. **Projenizi tarayın** ve dosya ağacındaki tüm dosyaları görün
2. **Her dosya adının yanındaki 📄 ikonlarına bakın**
3. **Checkbox düzenini fark edin**: `☑️   📄  🐍 dosyaadi.py`
4. **Boşlukları gözlemleyin** - checkbox'lar ve ikonlar düzgün ayrılmış

### Adım 2: İlk Dosya Bazında Prompt'unuzu Ekleme
1. **Kritik bir dosya bulun** (`main.py` veya `app.py` gibi)
2. **O dosyanın yanındaki 📄 ikonuna tıklayın**
3. **Bir dialog penceresi açılır** ve şunları içerir:
   - Üstte dosya adı ve yolu
   - Prompt'unuz için büyük metin alanı
   - Karakter sayacı
   - Örnek prompt'lar düğmesi
   - Kaydet/İptal düğmeleri

### Adım 3: Etkili Prompt'lar Yazma
```
✅ İYİ Örnekler:
- "Bu kimlik doğrulama modülündeki hata yönetimini analiz et"
- "Bu veritabanı sorgularında SQL injection açıklarını kontrol et"
- "Önbellekleme mantığını potansiyel yarış koşulları için incele"
- "API endpoint'lerinde uygun girdi doğrulaması olup olmadığını kontrol et"

❌ KÖTÜ Örnekler:
- "Bu dosyaya bak" (çok genel)
- "Hataları düzelt" (yeterince spesifik değil)
- "Daha iyi yap" (uygulanabilir yön yok)
```

### Adım 4: Görsel Geri Bildirim Sistemini Kullanma
Prompt'lar ekledikten sonra, dosya arka planlarının nasıl değiştiğini fark edin:

- 🟢 **Yeşil**: `☑️   📝✨  🐍 auth.py` - Seçili + Özel Prompt *(Mükemmel!)*
- 🟡 **Sarı**: `☑️   📄   🐍 utils.py` - Sadece Seçili *(İyi)*
- 🔴 **Kırmızı**: `☐   📝✨  🐍 eski_kod.py` - Sadece Prompt *(Uyarı!)*

## 🎨 Gelişmiş Teknikler

### Çok Katmanlı Prompt Stratejisi
```
Katman 1 - Genel Şablon: "Code Review"
Katman 2 - Dosya Bazında Prompt'lar:
├── security.py → "Kimlik doğrulama ve yetkilendirmeye odaklan"
├── payment.py → "Finansal işlem güvenliğini kontrol et"
├── logging.py → "Hassas veri ifşası için incele"
└── config.py → "Güvenli konfigürasyon yönetimini doğrula"
```

### Alan Özel Prompt Desenleri

#### 🔒 Güvenlik Analizi
```
auth.py → "Kimlik doğrulama mekanizmalarını şunlar için analiz et:
- Şifre politikası uygulaması
- Oturum yönetimi güvenliği
- Çok faktörlü kimlik doğrulama implementasyonu
- Zamanlama saldırılarına karşı koruma"

api.py → "API güvenliğini şunlar için incele:
- Girdi doğrulaması ve temizleme
- Hız sınırlama implementasyonu
- CORS konfigürasyonu
- Kimlik doğrulama token işleme"
```

#### ⚡ Performans Optimizasyonu
```
database.py → "Veritabanı işlemlerini şunlar için incele:
- N+1 sorgu problemleri
- Eksik indeksler
- Bağlantı havuzu verimliliği
- İşlem sınırı optimizasyonu"

cache.py → "Önbellekleme stratejisini şunlar için analiz et:
- Önbellek geçersizleştirme mantığı
- Bellek kullanım desenleri
- Yarış koşulu önleme
- TTL konfigürasyon etkinliği"
```

#### 🧪 Kod Kalite İncelemesi
```
models.py → "Veri modellerini şunlar için incele:
- Uygun doğrulama kuralları
- İlişki tanımları
- İndeks optimizasyon fırsatları
- Migration uyumluluğu"

utils.py → "Yardımcı fonksiyonları şunlar için incele:
- Kod yeniden kullanılabilirliği
- Hata yönetimi bütünlüğü
- Performans darboğazları
- Dokümantasyon kalitesi"
```

## 🎯 Pro İpuçları ve En İyi Uygulamalar

### ✅ Maksimum Etki İçin Bunu Yapın

#### 1. **Bağlamsal Olarak Spesifik Olun**
```
Şunun yerine: "Bu dosyayı incele"
Şunu yazın: "PCI uyumluluğu ve hata yönetimi için ödeme işleme mantığını analiz et"
```

#### 2. **Beklenen Çıktıları Dahil Edin**
```
"API kimlik doğrulamasını incele ve şunları sağla:
1. Güvenlik açığı değerlendirmesi
2. Önerilen iyileştirmeler
3. Düzeltmeler için kod örnekleri"
```

#### 3. **Eylem Odaklı Dil Kullanın**
```
✅ "Tanımla", "Analiz et", "İncele", "Kontrol et", "İnceleme yap"
❌ "Bak", "Gör", "Düşün"
```

#### 4. **Spesifik Teknolojilere Referans Verin**
```
"Bu Django modelini şunlar için analiz et:
- select_related() ve prefetch_related() doğru kullanımı
- PostgreSQL için indeks optimizasyonu
- Üretim dağıtımı için migration güvenliği"
```

### ❌ Kaçınılması Gereken Yaygın Hatalar

#### 1. **Genel Prompt'lar**
```
❌ "Bunu daha iyi yap"
✅ "Bu modüldeki veritabanı sorgu performansını optimize et"
```

#### 2. **Aşırı Uzun Prompt'lar**
En iyi sonuçlar için prompt'ları 500 karakterin altında tutun.

#### 3. **Kullanılmayan Prompt'lar**
Kırmızı arka planlı dosyalarda prompt var ama seçili değil - ya seçin ya da prompt'u kaldırın.

#### 4. **Tutarsız Prompt Stilleri**
Tutarlı analiz için dosyalar arası benzer yapılar kullanın.

## 📊 Prompt Stratejinizi İzleme

### Sayacı Anlama
Dosya sayacı şunu gösterir: `"12 / 45 dosya seçili • 8 prompt'lu • ⚠️ 2 kullanılmayan prompt"`

- **12 / 45**: Toplam seçim durumu
- **8 prompt'lu**: Özel talimatları olan dosyalar
- **⚠️ 2 kullanılmayan**: Prompt'u olan ama seçilmeyen dosyalar (kırmızı arka plan)

### Optimizasyon Hedefleri
- **Yeşil dosyalar**: %70-80 (spesifik prompt'larla temel işlevsellik)
- **Sarı dosyalar**: %15-25 (destekleyici dosyalar, genel analiz)
- **Kırmızı dosyalar**: %0-5 (minimize edilmeli)

## 🔧 Teknik Özellikler

### Dialog Penceresi Özellikleri
- **640x640 optimal boyut** rahat prompt yazımı için
- **Karakter sayacı** renk kodlamalı (yeşil < 500, turuncu < 1000, kırmızı > 1000)
- **Örnek prompt'lar kütüphanesi** 8 önceden yazılmış örnekle
- **Otomatik kaydetme** oturumlar arası prompt'ları korur
- **Klavye kısayolları**: Kaydetmek için Ctrl+Enter, tümünü seçmek için Ctrl+A

### Dışa Aktarma Formatlarıyla Entegrasyon

#### TXT Dışa Aktarma
```
=== DOSYA: src/auth.py ===

[BU DOSYA İÇİN ÖZEL PROMPT]
Güvenlik açıkları için kimlik doğrulama mekanizmalarını analiz et

[İÇERİK]
def authenticate_user(username, password):
    # ... kod içeriği ...
```

#### HTML Dışa Aktarma
Dosya bazında prompt'lar her dosyanın içeriğinin üstünde vurgulanan turuncu kutularda görünür.

#### DOCX Dışa Aktarma
Özel prompt'lar turuncu metinle stilize edilmiş başlıklar olarak formatlanır.

#### PDF Dışa Aktarma  
Prompt'lar farklı formatlamayla ayrı bölümler olarak dahil edilir.

## 🚀 Gelişmiş İş Akışları

### İş Akışı 1: Güvenlik Denetimi
1. **Güvenlik açısından kritik dosyaları filtreleyin** (auth, api, crypto, vb.)
2. **Her dosyaya güvenlik odaklı prompt'lar ekleyin**
3. **Temel olarak "Code Review" şablonunu kullanın**
4. **Resmi dokümantasyon için DOCX olarak dışa aktarın**
5. **Kapsamlı güvenlik raporu oluşturun**

### İş Akışı 2: Performans Analizi
1. **Performans açısından kritik dosyaları seçin** (database, cache, algoritmalar)
2. **Spesifik metriklerle performans odaklı prompt'lar ekleyin**
3. **Detaylı analiz için "16x Prompt" şablonunu kullanın**
4. **İnteraktif inceleme için HTML olarak dışa aktarın**
5. **Yapay zeka geri bildirimlerine dayanarak yineleyin**

### İş Akışı 3: Kod İnceleme Süreci
1. **Sadece değişen dosyaları göstermek için Git entegrasyonunu kullanın**
2. **Değişiklik bağlamına dayalı inceleme odaklı prompt'lar ekleyin**
3. **Yeni işlevsellik için test prompt'larını dahil edin**
4. **Farklı paydaşlar için birden fazla formatta dışa aktarın**
5. **Zaman içinde prompt etkinliğini takip edin**

## 🔮 Gelecek Geliştirmeler (Yakında Geliyor)

- **Prompt Şablonları**: Projeler arası prompt setlerini kaydedin ve yeniden kullanın
- **Akıllı Öneriler**: Dosya içeriğine dayalı yapay zeka destekli prompt önerileri
- **Toplu Atama**: Desen eşleştirmeyle birden fazla dosyaya prompt uygulayın
- **Prompt Geçmişi**: Önceden etkili olan prompt'ları takip edin ve yeniden kullanın
- **Takım Paylaşımı**: Geliştirme takımları arasında prompt stratejilerini paylaşın

---

**Dosya bazında prompt'larda uzmanlaşmaya hazır mısınız?** Küçük bir proje ile başlayın ve yavaş yavaş prompt kütüphanenizi oluşturun!

*Güçlü şablon kombinasyonlarını öğrenmek için [Şablon Rehberi](Templates-Guide-TR) ile devam edin →*