# 📖 CodeFuser v2.0 ile Başlangıç Rehberi

CodeFuser'a hoş geldiniz! Bu rehber, en güçlü yapay zeka destekli kod birleştirme aracını kullanmaya başlamanızda size yardımcı olacaktır.

## 🚀 Hızlı Başlangıç (5 Dakika)

### Adım 1: İndirme ve Kurulum
Tercih ettiğiniz kurulum yöntemini seçin:

#### 📥 Seçenek A: Bağımsız EXE (Önerilen)
1. [Sürümler](https://github.com/tahamucasiroglu/CodeFuser/releases/latest) sayfasına gidin
2. `CodeFuser_Portable.zip` dosyasını indirin
3. ZIP dosyasını çıkartın
4. `CodeFuser.exe` dosyasına çift tıklayın - Hazır! ✨

#### 🐍 Seçenek B: Python Kaynak Kodu
```bash
git clone https://github.com/tahamucasiroglu/CodeFuser.git
cd CodeFuser
pip install -r requirements.txt
python main.py
```

### Adım 2: İlk Proje
1. **Klasör Seçin**: "Gözat" düğmesine tıklayın ve proje dizininizi seçin
2. **Dosyaları Tarayın**: Tüm kod dosyalarını keşfetmek için "Dosyaları Tara" düğmesine tıklayın
3. **Dosyaları Seçin**: Dahil etmek istediğiniz dosyaların yanındaki kutuları işaretleyin
4. **Şablon Seçin**: Yapay zeka analizi için "16x Prompt" seçin
5. **İşlem Yapın**: "İşlemi Başlat" düğmesine tıklayın ve çıktı formatını seçin

## 🎯 Dosya Bazında Prompt'ları Anlama (v2.0 Özelliği)

### Dosya Bazında Prompt'lar Nedir?
Tüm dosyalara aynı talimatı vermek yerine, artık her dosya için hedeflenmiş talimatlar verebilirsiniz.

### Nasıl Kullanılır
1. **İkonu Bulun**: Her dosyanın yanındaki 📄 ikonlarına bakın
2. **Özelleştirmek İçin Tıklayın**: Prompt dialog'unu açmak için 📄 ikonuna tıklayın
3. **Talimatları Yazın**: O dosya için özel talimatlar ekleyin
4. **Görsel Geri Bildirimi Görün**: Prompt'u olan dosyalar 📝✨ ve renkli arka planlar gösterir

### Renk Kodlama Sistemi
- 🟢 **Yeşil Arka Plan**: Dosya seçili VE özel prompt'u var (Mükemmel!)
- 🟡 **Sarı Arka Plan**: Dosya seçili ama özel prompt yok (İyi)
- 🔴 **Kırmızı Arka Plan**: Dosyada özel prompt var ama seçili DEĞİL (Uyarı!)

## 📊 Arayüzü Anlama

### Ana Pencere Bileşenleri
1. **Araç Çubuğu**: Gözat, tara, ayarlar ve dil seçenekleri
2. **Dosya Ağacı**: Checkbox'larla birlikte keşfedilen tüm dosyaları gösterir
3. **Şablon Alanı**: Önceden oluşturulmuş şablonlardan seçin veya özel oluşturun
4. **Prompt Editörü**: Ana talimatlarınızı yazın
5. **Dışa Aktarma Seçenekleri**: Çıktı formatını ve konumunu seçin
6. **Durum Çubuğu**: İlerleme ve dosya sayısını gösterir

### Dosya Ağacı Özellikleri
- **Arama Kutusu**: Dosyaları ada göre filtreleyin (dosya ağacının üstünde)
- **Tümünü Seç/Hiçbiri**: Toplu seçim düğmeleri
- **Dosya Sayacı**: "X / Y dosya seçili • Z prompt'lu" gösterir
- **Seçilenleri Kaldır**: İstenmeyen dosyaları listeden kaldırın

## 🎨 İlk Yapay Zeka Analiziniz

### Örnek: Güvenlik İncelemesi
1. **Web uygulamanızdaki Python dosyalarını seçin**
2. **Dosya bazında prompt'lar ekleyin**:
   - `auth.py` → "Kimlik doğrulama açıklarına odaklan"
   - `api.py` → "SQL injection ve XSS kontrol et"
   - `utils.py` → "Girdi doğrulama fonksiyonlarını incele"
3. **"Code Review" şablonunu seçin**
4. **Kolay okuma için HTML olarak dışa aktarın**
5. **Yapay zeka aracınıza kopyalayın** (ChatGPT, Claude, vb.)

### Örnek: Performans Analizi
1. **Temel uygulama dosyalarını seçin**
2. **Hedeflenmiş prompt'lar ekleyin**:
   - `database.py` → "Sorgu verimliliğini ve N+1 problemlerini analiz et"
   - `cache.py` → "Önbellekleme stratejisi etkinliğini incele"
   - `main.py` → "Ana yürütme akışındaki darboğazları kontrol et"
3. **"16x Prompt" şablonunu kullanın**
4. **Yapay zeka girişi için TXT olarak dışa aktarın**

## ⚡ Yeni Başlayanlar İçin Pro İpuçları

### ✅ Bunu Yapın
- **Küçük başlayın**: 3-5 önemli dosya ile başlayın
- **Spesifik olun**: Her dosya için net, uygulanabilir prompt'lar yazın
- **Şablonları kullanın**: Mükemmel başlangıç noktaları sağlarlar
- **Renkleri kontrol edin**: Yeşil dosyalar = optimal kurulum
- **HTML olarak dışa aktarın**: Görüntüleme ve kopyalama için en iyi

### ❌ Bunu Yapmayın
- **Her şeyi seçmeyin**: Kalite nicelikten önemli
- **Genel prompt'lar kullanmayın**: Her dosya için spesifik olun
- **Kırmızı dosyaları görmezden gelmeyin**: Kullanılmayan prompt'ları var
- **Şablonları atlama**: Zaman tasarrufu sağlar ve sonuçları iyileştirir

## 🔧 Temel Yapılandırma

### Dil Ayarları
- **Dil Değiştirme**: Ayarlar → Dil → Türkçe/İngilizce
- **Yeniden Başlatma Gerekli**: Bazı değişiklikler uygulama yeniden başlatılmasını gerektirir

### Varsayılan Tercihler
- **Çıktı Formatı**: Tercih ettiğiniz dışa aktarma formatını seçin
- **Dosya Filtreleri**: Yaygın hariç tutmalar ayarlayın (testler, dokümantasyon, vb.)
- **Şablon**: En çok kullandığınız şablonu varsayılan olarak ayarlayın

## 🆘 Yardıma İhtiyacınız Var mı?

### Yaygın İlk Kullanım Sorunları
1. **"Dosya bulunamadı"**: Klasörde kod dosyaları olup olmadığını kontrol edin, filtreleri ayarlayın
2. **"Dışa aktarma başarısız"**: Yazma izinlerini, mevcut disk alanını kontrol edin
3. **"Şablon hatası"**: Şablonun geçerli placeholder sözdizimi olduğundan emin olun

### Destek Alma
- **📖 Wiki'yi Kontrol Edin**: Çoğu soru burada yanıtlanmıştır
- **🐛 Sorun Bildirin**: [GitHub Issues](https://github.com/tahamucasiroglu/CodeFuser/issues)
- **💡 Soru Sorun**: [GitHub Discussions](https://github.com/tahamucasiroglu/CodeFuser/discussions)

## 🎓 Sonraki Adımlar

Temel bilgilerde rahat olduğunuzda:

1. **[🎯 Dosya Bazında Prompt'larda Uzmanlaşın](File-Specific-Prompts-TR)** - v2.0'ın öne çıkan özelliğine derinlemesine dalış
2. **[🎨 Şablonları Öğrenin](Templates-Guide-TR)** - Şablon oluşturma ve özelleştirme
3. **[🔍 Akıllı Filtreleri Keşfedin](Smart-Filters-TR)** - Gelişmiş dosya filtreleme
4. **[🐙 Git Entegrasyonunu Kullanın](Git-Integration-TR)** - Versiyon kontrolüyle çalışma

---

**Kodunuzu yapay zeka hassasiyetiyle birleştirmeye hazır mısınız?** 🚀

*[Dosya Bazında Prompt Rehberi](File-Specific-Prompts-TR) ile devam edin →*