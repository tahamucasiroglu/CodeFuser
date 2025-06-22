# 🚀 CodeFuser / KodBirleştirici

![image](/assets/Ornek.png)

**English** | [Türkçe](#-türkçe)

---

## **The Ultimate Code Aggregation Tool with AI Integration**

CodeFuser is a powerful application that combines project files into a single output with AI prompts, featuring advanced filtering, template systems, and multi-format export capabilities. Perfect for AI development workflows, code analysis, and documentation generation.

<div align="center">
  <img src="assets/CodeFuser Logo.png" alt="CodeFuser Logo" width="128" height="128">
  <br>
  <em>Your ultimate code aggregation companion</em>
</div>

![CodeFuser Demo](assets/demo.gif)

## ✨ Features

### 🎯 Smart Templates
- **16x Prompt**: Optimized for AI model interactions
- **Cursor Rules**: IDE-specific configurations  
- **Claude Project**: Claude AI project format
- **Documentation**: Auto-generated documentation
- **Code Review**: Structured code review format
- **Custom Templates**: Create your own with variable substitution

### 🔍 Advanced Filtering System
- **Git Integration**: Filter by git status (modified, added, untracked)
- **Smart Content Analysis**: Detect TODOs, functions, classes, potential issues
- **File Type Detection**: Test files, config files, documentation
- **Language-Specific**: Python, JavaScript, Web files, etc.
- **Code Quality**: Find undocumented code, complex files, security issues
- **Time-Based**: Recently modified files, old files

### 📄 Multiple Export Formats
- **TXT**: Simple text format with separators
- **HTML**: Beautiful syntax-highlighted web pages with copy functionality
- **DOCX**: Professional Word documents with formatting
- **PDF**: Print-ready documents with proper styling

### 🌍 Multi-Language Support
- **Turkish (Türkçe)**: Full native support
- **English**: Complete interface translation
- **Extensible**: Easy to add new languages

### 🎨 Modern Interface
- **Full-screen Mode**: Distraction-free workspace
- **Smart File Tree**: Fast search and selection
- **Progress Tracking**: Real-time operation feedback
- **Settings Management**: Configurable preferences

## 🚀 Installation & Quick Start

### 📥 Method 1: Standalone Application (Recommended for Beginners)

**Step-by-step for complete beginners:**

1. **Download the Program**
   - Go to [Releases page](https://github.com/yourusername/codefuser/releases)
   - Click on the latest version (e.g., "v1.0.0")
   - Download `CodeFuser-Windows.zip` file

2. **Extract the Files**
   - Right-click on the downloaded ZIP file
   - Select "Extract All..." or "Extract Here"
   - You'll see a folder called "CodeFuser"

3. **Run the Program**
   - Open the "CodeFuser" folder
   - Double-click on `CodeFuser.exe`
   - The program will start immediately (no installation needed!)

4. **First Use**
   - Click "Browse" button to select your project folder
   - Click "Scan Files" to find all code files
   - Choose which files you want to include (check/uncheck boxes)
   - Add a prompt or select a template
   - Click "Start Process" to create your output file

**That's it! No technical knowledge required.**

### 🔧 Method 2: VSCode Extension (For VSCode Users)

**If you use Visual Studio Code:**

1. **Install the Extension**
   - Open VSCode
   - Press `Ctrl+Shift+X` (Extensions panel)
   - Search for "CodeFuser"
   - Click "Install"

2. **Use the Extension**
   - Right-click any folder in VSCode Explorer
   - Select "Quick Export Selected Files"
   - Or press `Ctrl+Shift+P` and type "CodeFuser"

### 🐍 Method 3: Python Source (For Developers)

**If you have Python installed:**

```bash
# 1. Download the source code
git clone https://github.com/yourusername/codefuser.git
cd codefuser

# 2. Install required packages
pip install -r requirements.txt

# 3. Run the program
python main.py
```

## 📖 Usage Examples

### For AI Development
```
1. Select your project folder
2. Choose "16x Prompt" template
3. Apply smart filters (exclude test files, focus on main logic)
4. Add your specific prompt
5. Export as HTML for easy copying
```

### For Code Review
```
1. Use Git filter to show only modified files
2. Select "Code Review" template
3. Apply quality filters to find potential issues
4. Export as DOCX for team sharing
```

### For Documentation
```
1. Filter for main files and documentation
2. Use "Documentation" template
3. Export as HTML with syntax highlighting
4. Share the beautiful web page
```

## 🛠️ Building from Source

### Build Standalone EXE
```bash
python build_exe.py
```

### Build VSCode Extension
```bash
cd vscode-extension
npm install
npm run compile
vsce package
```

## ⚙️ Configuration

CodeFuser is highly configurable through `config/default_settings.json`:

```json
{
  "project_types": {
    ".NET": [".cs", ".cshtml", ".csproj", ".json"],
    "Python": [".py", ".pyx", ".pyi"],
    "JavaScript": [".js", ".jsx", ".ts", ".tsx"]
  },
  "ignore_folders": ["node_modules", ".git", "bin", "obj"],
  "output_settings": {
    "default_format": "html",
    "available_formats": ["txt", "docx", "pdf", "html"]
  },
  "interface": {
    "fullscreen": true,
    "theme": "modern"
  }
}
```

## 📊 Comparison with Alternatives

| Feature | CodeFuser | 16x Prompt | PasteMax |
|---------|-----------|------------|----------|
| Templates | ✅ 5+ Built-in | ❌ Basic | ❌ None |
| Git Integration | ✅ Full | ❌ None | ❌ None |
| Smart Filters | ✅ 30+ Filters | ❌ Basic | ❌ Basic |
| Export Formats | ✅ 4 Formats | ❌ Text only | ❌ Text only |
| Multi-Language | ✅ TR/EN | ❌ EN only | ❌ EN only |
| Advanced UI | ✅ Modern | ❌ Basic | ❌ Basic |

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Setup
```bash
git clone https://github.com/yourusername/codefuser.git
cd codefuser
pip install -r requirements.txt
python -m pytest tests/
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by 16x Prompt and PasteMax
- Built with Python, Tkinter, and modern web technologies
- Turkish language support for the local developer community

## 🗺️ Roadmap

### 🚀 Version 1.1 (Q2 2024)
- [ ] **Advanced Custom Filters**: Visual filter builder with drag-drop interface
- [ ] **AI Integration**: Direct ChatGPT/Claude API integration
- [ ] **Batch Processing**: Process multiple projects simultaneously
- [ ] **Export Scheduling**: Automated periodic exports
- [ ] **Cloud Storage**: Google Drive, Dropbox, OneDrive integration

### 🎯 Version 1.2 (Q3 2024)
- [ ] **Collaborative Features**: Share templates and filters with team
- [ ] **Project Profiles**: Save and restore project configurations
- [ ] **Advanced Search**: Full-text search across exported files
- [ ] **Plugin System**: Third-party extensions support
- [ ] **Mobile Companion**: View exports on mobile devices

### 🔮 Version 2.0 (Q4 2024)
- [ ] **Web Interface**: Browser-based version
- [ ] **Real-time Collaboration**: Live editing and sharing
- [ ] **AI-Powered Analysis**: Automatic code quality suggestions
- [ ] **Enterprise Features**: SSO, audit logs, compliance
- [ ] **Multi-Language Expansion**: French, German, Spanish, Japanese

### 💡 Community Requests
- [ ] **Database Integration**: Connect to code in databases
- [ ] **Docker Support**: Containerized deployments
- [ ] **Jupyter Notebook**: Integration with data science workflows
- [ ] **More IDE Extensions**: IntelliJ, Sublime Text, Atom
- [ ] **API Access**: RESTful API for automation

**Vote for features** in our [GitHub Discussions](https://github.com/yourusername/codefuser/discussions)!

## 📞 Support

- **GitHub Issues**: [Report bugs or request features](https://github.com/yourusername/codefuser/issues)
- **Discussions**: [Community discussions](https://github.com/yourusername/codefuser/discussions)
- **Documentation**: [Full documentation](https://github.com/yourusername/codefuser/wiki)

---

**Made with ❤️ for the developer community**

*CodeFuser - Fuse your code, fuel your AI*

---

# 🇹🇷 Türkçe

[English](#-codefuser--kodbirleştirici) | **Türkçe**

---

## **Yapay Zeka Entegrasyonlu Üstün Kod Birleştirme Aracı**

CodeFuser, proje dosyalarını yapay zeka komutlarıyla birlikte tek bir çıktıda birleştiren güçlü bir uygulamadır. Gelişmiş filtreleme, şablon sistemleri ve çoklu format dışa aktarma özellikleri sunar. Yapay zeka geliştirme iş akışları, kod analizi ve dokümantasyon oluşturma için mükemmeldir.

<div align="center">
  <img src="assets/CodeFuser Logo.png" alt="CodeFuser Logo" width="128" height="128">
  <br>
  <em>Üstün kod birleştirme arkadaşınız</em>
</div>

![CodeFuser Demo](assets/demo.gif)

## ✨ Özellikler

### 🎯 Akıllı Şablonlar
- **16x Prompt**: Yapay zeka model etkileşimleri için optimize edilmiş
- **Cursor Rules**: IDE'ye özel konfigürasyonlar  
- **Claude Project**: Claude AI proje formatı
- **Documentation**: Otomatik oluşturulan dokümantasyon
- **Code Review**: Yapılandırılmış kod inceleme formatı
- **Özel Şablonlar**: Değişken ikameli kendi şablonlarınızı oluşturun

### 🔍 Gelişmiş Filtreleme Sistemi
- **Git Entegrasyonu**: Git durumuna göre filtreleme (değiştirilmiş, eklenmiş, izlenmeyen)
- **Akıllı İçerik Analizi**: TODO'lar, fonksiyonlar, sınıflar, potansiyel sorunları tespit et
- **Dosya Türü Tespiti**: Test dosyaları, config dosyaları, dokümantasyon
- **Dile Özel**: Python, JavaScript, Web dosyaları, vb.
- **Kod Kalitesi**: Dokümansız kod, karmaşık dosyalar, güvenlik sorunları bul
- **Zamana Dayalı**: Son değiştirilen dosyalar, eski dosyalar

### 📄 Çoklu Dışa Aktarma Formatları
- **TXT**: Ayırıcılı basit metin formatı
- **HTML**: Kopyalama özellikli güzel sözdizimi vurgulamalı web sayfaları
- **DOCX**: Formatlı profesyonel Word belgeleri
- **PDF**: Uygun stillendirmeli yazdırıya hazır belgeler

### 🌍 Çok Dilli Destek
- **Türkçe**: Tam yerel destek
- **English**: Tam arayüz çevirisi
- **Genişletilebilir**: Yeni diller kolayca eklenebilir

### 🎨 Modern Arayüz
- **Tam Ekran Modu**: Dikkat dağıtmayan çalışma alanı
- **Akıllı Dosya Ağacı**: Hızlı arama ve seçim
- **İlerleme Takibi**: Gerçek zamanlı işlem geri bildirimi
- **Ayar Yönetimi**: Yapılandırılabilir tercihler

## 🚀 Kurulum ve Hızlı Başlangıç

### 📥 Yöntem 1: Bağımsız Uygulama (Yeni Başlayanlar İçin Önerilen)

**Hiç bilmeyenler için adım adım:**

1. **Programı İndir**
   - [Sürümler sayfasına](https://github.com/yourusername/codefuser/releases) git
   - En son sürüme tıkla (örn. "v1.0.0")
   - `CodeFuser-Windows.zip` dosyasını indir

2. **Dosyaları Çıkart**
   - İndirilen ZIP dosyasına sağ tıkla
   - "Tümünü Çıkart..." veya "Buraya Çıkart" seç
   - "CodeFuser" adında bir klasör göreceksin

3. **Programı Çalıştır**
   - "CodeFuser" klasörünü aç
   - `CodeFuser.exe` dosyasına çift tıkla
   - Program hemen başlayacak (kurulum gerektirmez!)

4. **İlk Kullanım**
   - Proje klasörünü seçmek için "Gözat" düğmesine tıkla
   - Tüm kod dosyalarını bulmak için "Dosyaları Tara" tıkla
   - Hangi dosyaları dahil etmek istediğini seç (kutuları işaretle/işaretsiz bırak)
   - Bir komut ekle veya şablon seç
   - Çıktı dosyanı oluşturmak için "İşlemi Başlat" tıkla

**Bu kadar! Teknik bilgi gerektirmez.**

### 🔧 Yöntem 2: VSCode Eklentisi (VSCode Kullanıcıları İçin)

**Eğer Visual Studio Code kullanıyorsan:**

1. **Eklentiyi Kur**
   - VSCode'u aç
   - `Ctrl+Shift+X` bas (Eklentiler paneli)
   - "CodeFuser" ara
   - "Install" (Kur) tıkla

2. **Eklentiyi Kullan**
   - VSCode Explorer'da herhangi bir klasöre sağ tıkla
   - "Quick Export Selected Files" (Seçili Dosyaları Hızlı Dışa Aktar) seç
   - Veya `Ctrl+Shift+P` bas ve "CodeFuser" yaz

### 🐍 Yöntem 3: Python Kaynağı (Geliştiriciler İçin)

**Eğer Python yüklüyse:**

```bash
# 1. Kaynak kodu indir
git clone https://github.com/yourusername/codefuser.git
cd codefuser

# 2. Gerekli paketleri kur
pip install -r requirements.txt

# 3. Programı çalıştır
python main.py
```

## 📖 Kullanım Örnekleri

### Yapay Zeka Geliştirme İçin
```
1. Proje klasörünü seç
2. "16x Prompt" şablonunu seç
3. Akıllı filtreler uygula (test dosyalarını hariç tut, ana mantığa odaklan)
4. Özel komutunu ekle
5. Kolay kopyalama için HTML olarak dışa aktar
```

### Kod İncelemesi İçin
```
1. Sadece değiştirilmiş dosyaları göstermek için Git filtresi kullan
2. "Code Review" şablonunu seç
3. Potansiyel sorunları bulmak için kalite filtrelerini uygula
4. Takım paylaşımı için DOCX olarak dışa aktar
```

### Dokümantasyon İçin
```
1. Ana dosyalar ve dokümantasyon için filtrele
2. "Documentation" şablonunu kullan
3. Sözdizimi vurgulamalı HTML olarak dışa aktar
4. Güzel web sayfasını paylaş
```

## ⚙️ Yapılandırma

CodeFuser, `config/default_settings.json` aracılığıyla oldukça yapılandırılabilir:

```json
{
  "project_types": {
    ".NET": [".cs", ".cshtml", ".csproj", ".json"],
    "Python": [".py", ".pyx", ".pyi"],
    "JavaScript": [".js", ".jsx", ".ts", ".tsx"]
  },
  "ignore_folders": ["node_modules", ".git", "bin", "obj"],
  "output_settings": {
    "default_format": "html",
    "available_formats": ["txt", "docx", "pdf", "html"]
  },
  "interface": {
    "fullscreen": true,
    "theme": "modern"
  }
}
```

## 📊 Alternatiflerle Karşılaştırma

| Özellik | CodeFuser | 16x Prompt | PasteMax |
|---------|-----------|------------|----------|
| Şablonlar | ✅ 5+ Yerleşik | ❌ Temel | ❌ Yok |
| Git Entegrasyonu | ✅ Tam | ❌ Yok | ❌ Yok |
| Akıllı Filtreler | ✅ 30+ Filtre | ❌ Temel | ❌ Temel |
| Dışa Aktarma Formatları | ✅ 4 Format | ❌ Sadece Metin | ❌ Sadece Metin |
| Çok Dilli | ✅ TR/EN | ❌ Sadece EN | ❌ Sadece EN |
| Gelişmiş Arayüz | ✅ Modern | ❌ Temel | ❌ Temel |

## 🛠️ Kaynak Koddan Derleme

### Bağımsız EXE Derle
```bash
python build_exe.py
```

### VSCode Eklentisi Derle
```bash
cd vscode-extension
npm install
npm run compile
vsce package
```

## 🤝 Katkıda Bulunma

Katkılarınızı memnuniyetle karşılıyoruz! Lütfen rehber için [CONTRIBUTING.md](CONTRIBUTING.md) dosyasına bakın.

### Geliştirme Kurulumu
```bash
git clone https://github.com/yourusername/codefuser.git
cd codefuser
pip install -r requirements.txt
python -m pytest tests/
```

## 📝 Lisans

Bu proje MIT Lisansı altında lisanslanmıştır - detaylar için [LICENSE](LICENSE) dosyasına bakın.

## 🙏 Teşekkürler

- 16x Prompt ve PasteMax'ten ilham alınmıştır
- Python, Tkinter ve modern web teknolojileri ile geliştirilmiştir
- Yerel geliştirici topluluğu için Türkçe dil desteği

## 🗺️ Yol Haritası

### 🚀 Versiyon 1.1 (2024 Q2)
- [ ] **Gelişmiş Özel Filtreler**: Sürükle-bırak arayüzü ile görsel filtre oluşturucu
- [ ] **Yapay Zeka Entegrasyonu**: Doğrudan ChatGPT/Claude API entegrasyonu
- [ ] **Toplu İşleme**: Birden fazla projeyi eş zamanlı işleme
- [ ] **Dışa Aktarma Zamanlaması**: Otomatik periyodik dışa aktarmalar
- [ ] **Bulut Depolama**: Google Drive, Dropbox, OneDrive entegrasyonu

### 🎯 Versiyon 1.2 (2024 Q3)
- [ ] **İşbirliği Özellikleri**: Takımla şablon ve filtre paylaşımı
- [ ] **Proje Profilleri**: Proje konfigürasyonlarını kaydet ve geri yükle
- [ ] **Gelişmiş Arama**: Dışa aktarılan dosyalarda tam metin arama
- [ ] **Eklenti Sistemi**: Üçüncü taraf uzantı desteği
- [ ] **Mobil Companion**: Mobil cihazlarda dışa aktarılanları görüntüleme

### 🔮 Versiyon 2.0 (2024 Q4)
- [ ] **Web Arayüzü**: Tarayıcı tabanlı versiyon
- [ ] **Gerçek Zamanlı İşbirliği**: Canlı düzenleme ve paylaşım
- [ ] **Yapay Zeka Destekli Analiz**: Otomatik kod kalitesi önerileri
- [ ] **Kurumsal Özellikler**: SSO, denetim logları, uyumluluk
- [ ] **Çoklu Dil Genişletmesi**: Fransızca, Almanca, İspanyolca, Japonca

### 💡 Topluluk İstekleri
- [ ] **Veritabanı Entegrasyonu**: Veritabanlarındaki kodlara bağlantı
- [ ] **Docker Desteği**: Konteynerleştirilmiş dağıtımlar
- [ ] **Jupyter Notebook**: Veri bilimi iş akışları ile entegrasyon
- [ ] **Daha Fazla IDE Uzantısı**: IntelliJ, Sublime Text, Atom
- [ ] **API Erişimi**: Otomasyon için RESTful API

**Özellikler için oy verin**: [GitHub Tartışmalarımızda](https://github.com/yourusername/codefuser/discussions)!

## 📞 Destek

- **GitHub Sorunları**: [Hata bildir veya özellik iste](https://github.com/yourusername/codefuser/issues)
- **Tartışmalar**: [Topluluk tartışmaları](https://github.com/yourusername/codefuser/discussions)
- **Dokümantasyon**: [Tam dokümantasyon](https://github.com/yourusername/codefuser/wiki)

---

**Geliştirici topluluğu için ❤️ ile yapıldı**

*CodeFuser - Kodunu birleştir, yapay zekânı besle*