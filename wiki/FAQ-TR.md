# ❓ Sıkça Sorulan Sorular

## 🚀 Genel Sorular

### CodeFuser nedir?
CodeFuser, proje dosyalarını dosya bazında özel prompt'lar, gelişmiş filtreleme ve çoklu dışa aktarma formatlarıyla yapay zeka için hazır çıktılarda birleştiren yapay zeka destekli bir kod birleştirme aracıdır.

### v2.0'da neler yeni?
Devrimci **dosya bazında özel prompt'lar** özelliği her dosyaya bireysel talimatlar eklemenize olanak tanır, yapay zeka analizini daha hedefli ve etkili hale getirir. Ayrıca bağımsız Windows EXE, gelişmiş arayüz ve iyileştirilmiş renk kodlama.

### CodeFuser ücretsiz mi?
Evet! CodeFuser MIT Lisansı altında tamamen ücretsiz ve açık kaynaklıdır.

### CodeFuser hangi platformları destekler?
- **Windows**: Bağımsız EXE (önerilen) veya Python kaynak kodu
- **macOS**: Python kaynak kodu
- **Linux**: Python kaynak kodu
- **VSCode**: Tüm platformlar için uzantı

## 🎯 Dosya Bazında Prompt'lar

### Dosya bazında prompt'lar nasıl çalışır?
Herhangi bir dosyaya özel talimatlar eklemek için dosyanın yanındaki 📄 ikonuna tıklayın. Bu prompt'lar dosya içeriğiyle birlikte dışa aktarmaya dahil edilir ve yapay zeka araçlarına her bileşen için hedeflenmiş rehberlik sağlar.

### Genel ve dosya bazında prompt'lar arasındaki fark nedir?
- **Genel prompt**: Tüm projeye uygulanır (şablonlardan veya özel girişten)
- **Dosya bazında prompt**: Hedeflenmiş analiz için sadece bireysel dosyalara uygulanır

### Hem genel hem de dosya bazında prompt'ları kullanabilir miyim?
Evet! Birlikte çalışırlar. Genel prompt genel bağlam sağlarken, dosya bazında prompt'lar her dosya için detaylı talimatlar verir.

### Renk kodlaması ne anlama gelir?
- 🟢 **Yeşil**: Dosya seçili VE özel prompt'u var (optimal)
- 🟡 **Sarı**: Dosya seçili ama özel prompt yok (iyi)
- 🔴 **Kırmızı**: Dosyada özel prompt var ama seçili DEĞİL (uyarı - prompt kullanılmayacak)

### Dosya bazında prompt'lar ne kadar uzun olmalı?
En iyi sonuçlar için 500 karakter altında tutun. Dialog karakter sayısını renk kodlamasıyla gösterir (yeşil < 500, turuncu < 1000, kırmızı > 1000).

### Dosya bazında prompt'ları kaydedip yeniden kullanabilir miyim?
Şu anda prompt'lar oturum başına kaydediliyor. Prompt şablonları ve projeler arası yeniden kullanım v2.1 için planlandı.

## 🔧 Kurulum ve Ayar

### Hangi kurulum yöntemini seçmeliyim?
- **Yeni başlayanlar/Windows kullanıcıları**: Bağımsız EXE
- **Geliştiriciler**: Python kaynak kodu
- **VSCode kullanıcıları**: VSCode uzantısı

### Windows Defender neden EXE hakkında uyarı veriyor?
Bu yeni çalıştırılabilir dosyalar için normaldir. CodeFuser tamamen güvenlidir - uyarı EXE henüz dijital olarak imzalanmadığı için görünür. "Daha fazla bilgi" → "Yine de çalıştır" tıklayın.

### Bağımsız EXE için Python'a ihtiyacım var mı?
Hayır! Bağımsız EXE CodeFuser'ı herhangi bir bağımlılık olmadan çalıştırmak için gereken her şeyi içerir.

### CodeFuser'ı eski Windows sürümlerinde çalıştırabilir miyim?
Bağımsız EXE Windows 10 veya 11 gerektirir. Eski sürümler için Python kaynak kodu yöntemini kullanın.

### EXE dosyası neden bu kadar büyük (22MB)?
EXE, kurulum olmadan çalışmasını sağlamak için Python yorumlayıcısı, GUI kütüphaneleri, dışa aktarma kütüphaneleri (PDF, DOCX) ve tüm bağımlılıkları içerir.

## 📊 Dışa Aktarma ve Çıktı

### Hangi dışa aktarma formatları destekleniyor?
- **TXT**: Ayırıcılı basit metin
- **HTML**: Kopyalama işlevli sözdizimi vurgulamalı web sayfası
- **DOCX**: Profesyonel Word belgesi
- **PDF**: Uygun formatlamalı yazdırıya hazır belge

### Yapay zeka araçları için hangi format en iyi?
- **HTML**: Yapay zeka araçlarına görüntüleme ve kopyalama için en iyi
- **TXT**: En basit format, tüm yapay zeka araçlarıyla çalışır
- **DOCX**: Resmi dokümantasyon ve takım paylaşımı için iyi

### Dosya bazında prompt'lar dışa aktarmalara nasıl dahil ediliyor?
Her dosyanın özel prompt'u tüm dışa aktarma formatlarında dosya içeriğinden önce açıkça işaretlenmiş bir bölümde görünür.

### Dışa aktarma formatını özelleştirebilir miyim?
Temel özelleştirme yapılandırma dosyaları aracılığıyla mevcut. Gelişmiş formatlama seçenekleri gelecek sürümler için planlandı.

### Dışa aktarılan dosyalar nereye kaydediliyor?
Varsayılan olarak, dışa aktarmalar Belgeler klasörünüze kaydedilir. Dışa aktarma işlemi sırasında farklı bir konum seçebilirsiniz.

## 🔍 Filtreleme ve Seçim

### Akıllı filtreler nasıl çalışır?
Akıllı filtreler içerik analizi, dosya türleri, Git durumu ve kod desenlerine dayalı olarak dosyaları otomatik kategorize eder. "Gelişmiş Filtreler" bölümünden erişin.

### Hangi Git entegrasyon özellikleri mevcut?
- Sadece değiştirilmiş dosyaları göster
- Git durumuna göre filtrele (staged, unstaged, untracked)
- Branch'leri karşılaştır
- Yok sayılan dosyaları hariç tut

### Filtre yapılandırmalarını kaydedebilir miyim?
Filtre tercihleri otomatik olarak kaydedilir. Özel filtre setleri gelecek sürümler için planlandı.

### Test dosyalarını nasıl hariç tutarım?
Yaygın test dosyası desenlerini otomatik olarak filtrelemek için Akıllı Filtreler → "Test dosyalarını hariç tut" kullanın.

### Neden tüm dosyalarımı görmüyorum?
Dosya filtrelerinizi ve arama kutunuzu kontrol edin. Varsayılan olarak, bazı dosya türleri (ikili dosyalar gibi) daha iyi performans için hariç tutulur.

## 🎨 Şablonlar ve Özelleştirme

### Hangi şablonlar dahil?
- **16x Prompt**: Popüler yapay zeka analiz formatı
- **Claude Project**: Claude AI için optimize edilmiş
- **Code Review**: Yapılandırılmış kod inceleme formatı
- **Documentation**: Otomatik dokümantasyon oluşturma
- **Cursor Rules**: IDE'ye özel konfigürasyonlar

### Özel şablonlar oluşturabilir miyim?
Evet! Şablonlar değişken ikameli JSON dosyalarıdır. Detaylar için [Şablon Rehberi](Templates-Guide-TR)'ne bakın.

### Şablonları takımımla nasıl paylaşırım?
Paylaşmak için şablon JSON dosyalarını kopyalayın. Takım şablonu yönetimi v2.2 için planlandı.

### Mevcut şablonları değiştirebilir miyim?
Evet, şablonlar `templates/` klasöründe saklanır ve doğrudan düzenlenebilir.

## 🌍 Dil ve Yerelleştirme

### Hangi diller destekleniyor?
Şu anda tam arayüz çevirisiyle Türkçe ve İngilizce.

### Dili nasıl değiştiririm?
Ayarlar → Dil → Tercih ettiğiniz dili seçin. Yeniden başlatma gerekebilir.

### Yeni bir dil ekleyebilir miyim?
Evet! Dil dosyaları `locales/` klasöründe. Katkı talimatları için [Geliştirme Rehberi](Development-TR)'ne bakın.

## 🐛 Sorun Giderme

### CodeFuser başlamıyor
1. **Bağımsız EXE**: Windows Defender'ı kontrol edin, yönetici olarak çalıştırın
2. **Python kaynak kodu**: Python kurulumu ve bağımlılıkları doğrulayın
3. **Sistem gereksinimlerini ve mevcut belleği kontrol edin**

### Dosyalar algılanmıyor
1. Klasörün kod dosyaları içerdiğini doğrulayın
2. Dosya filtrelerini ve hariç tutmaları kontrol edin
3. Uygun klasör izinlerini sağlayın

### Dışa aktarma başarısız oluyor
1. Mevcut disk alanını kontrol edin
2. Çıktı klasörüne yazma izinlerini doğrulayın
3. Farklı bir dışa aktarma formatı deneyin

### Arayüz bozuk veya hizasız görünüyor
1. Ekran ölçekleme ayarlarını kontrol edin
2. Farklı ekran çözünürlüğü deneyin
3. Uygulamayı yeniden başlatın

### Performans yavaş
1. Seçili dosya sayısını azaltın
2. Gereksiz dosyaları hariç tutmak için akıllı filtreleri kullanın
3. Diğer bellek yoğun uygulamaları kapatın

## 💡 En İyi Uygulamalar

### Kaç dosya seçmeliyim?
5-10 önemli dosyayla başlayın. Kalite nicelikten daha iyi yapay zeka analiz sonuçları verir.

### İyi bir dosya bazında prompt nasıl olur?
- Spesifik ve uygulanabilir olun
- Dosyanın birincil amacına odaklanın
- Beklenen çıktı türünü dahil edin
- Kodla ilgili teknik terminoloji kullanın

### Büyük projeleri nasıl organize ederim?
1. Son değişikliklere odaklanmak için Git filtrelerini kullanın
2. Testleri ve bağımlılıkları hariç tutmak için akıllı filtreleri uygulayın
3. Farklı amaçlar için birden fazla dışa aktarma oluşturun
4. Dosya bazında prompt'ları sadece temel dosyalarda kullanın

### Yapay zeka analizi için en iyi iş akışı nedir?
1. Temel uygulama dosyalarını seçin
2. Kritik bileşenlere spesifik prompt'lar ekleyin
3. Uygun şablonu kullanın (genel analiz için 16x Prompt)
4. Kolay yapay zeka aracı entegrasyonu için HTML olarak dışa aktarın
5. Yapay zeka geri bildirimlerine dayalı olarak yineleyin

## 🔮 Gelecek Özellikler

### v2.1'de neler geliyor?
- Prompt şablonu kütüphaneleri
- Toplu prompt ataması
- Prompt geçmişi ve yeniden kullanım
- Gelişmiş dışa aktarma seçenekleri

### VSCode uzantısı ne zaman market'te olacak?
Market başvurusu üzerinde çalışıyoruz. Şu anda manuel kurulum olarak mevcut.

### Web sürümü olacak mı?
Gerçek zamanlı işbirliği özellikleriyle web arayüzü v3.0 için planlandı.

### Özellik isteyebilir miyim?
Evet! Özellik istekleri için [GitHub Discussions](https://github.com/tahamucasiroglu/CodeFuser/discussions) kullanın.

## 🆘 Hâlâ Yardıma İhtiyacınız Var mı?

### Topluluk Desteği
- **GitHub Discussions**: [Soru sorun](https://github.com/tahamucasiroglu/CodeFuser/discussions)
- **GitHub Issues**: [Hata bildirin](https://github.com/tahamucasiroglu/CodeFuser/issues)

### Dokümantasyon
- **[Başlangıç Rehberi](Getting-Started-TR)**: Temel kullanım
- **[Dosya Bazında Prompt Rehberi](File-Specific-Prompts-TR)**: v2.0 özelliğinde uzmanlaşın
- **[Sorun Giderme Rehberi](Troubleshooting-TR)**: Yaygın sorunlar ve çözümler

### Yardım İstemeden Önce
1. Bu SSS'yi kontrol edin
2. Mevcut GitHub sorunlarını arayın
3. Temel sorun giderme adımlarını deneyin
4. Raporunuzda sistem bilgilerini ve hata mesajlarını dahil edin

---

**Sorunuz burada yanıtlanmadı mı?** [Tam dokümantasyonumuzu](Home) kontrol edin veya [topluluğa sorun](https://github.com/tahamucasiroglu/CodeFuser/discussions)!