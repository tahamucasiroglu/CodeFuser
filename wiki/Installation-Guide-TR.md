# 📦 Kurulum Rehberi

CodeFuser v2.0'ı sisteminize kurmanın tüm yolları için kapsamlı rehber.

## 🎯 Kurulum Seçenekleri

| Kurulum Türü | Zorluk | Gereksinimler | En İyi Kullanım |
|---------------|---------|---------------|-----------------|
| **Windows EXE** | ⭐ Kolay | Hiçbiri | Windows kullanıcıları |
| **Python Kaynak** | ⭐⭐ Orta | Python 3.8+ | Geliştiriciler |
| **Git Clone** | ⭐⭐⭐ İleri | Git + Python | Katkıda bulunanlar |
| **Docker** | ⭐⭐ Orta | Docker | İzole ortam |

## 🖥️ Windows Taşınabilir EXE (Önerilen)

### ✨ Özellikler
- ✅ Kurulum gerektirmez
- ✅ Python gerektirmez
- ✅ Anında çalışır
- ✅ Tüm özellikler dahil
- ✅ Portable (USB'de taşınabilir)

### 📥 İndirme ve Kurulum

#### Adım 1: İndirme
```bash
# En son sürümü GitHub'dan indirin
https://github.com/tahamucasiroglu/CodeFuser/releases/latest

# CodeFuser_v2.0_Windows.zip dosyasını indirin
```

#### Adım 2: Çıkarma
```
1. İndirilen ZIP dosyasına sağ tıklayın
2. "Tümünü ayıkla..." seçeneğini seçin
3. İstediğiniz konumu seçin (örn: C:\Programs\CodeFuser)
4. "Ayıkla" butonuna tıklayın
```

#### Adım 3: Çalıştırma
```
1. Çıkarılan klasöre gidin
2. CodeFuser.exe dosyasına çift tıklayın
3. Windows güvenlik uyarısı çıkarsa "Daha fazla bilgi" → "Yine de çalıştır"
```

### 📁 Klasör Yapısı
```
CodeFuser_Portable/
├── CodeFuser.exe          # Ana program
├── config/                # Yapılandırma dosyaları
│   ├── default_settings.json
│   └── user_settings.json
├── templates/             # Şablon dosyaları
│   ├── 16x_prompt.json
│   ├── claude_project.json
│   └── ...
├── locales/              # Dil dosyaları
│   ├── en.json
│   └── tr.json
└── README.txt           # Kullanım kılavuzu
```

### 🛡️ Güvenlik Uyarıları

#### Windows Defender
```
Çözüm 1: Geçici olarak devre dışı bırak
1. Windows Güvenlik → Virüs ve tehdit koruması
2. Gerçek zamanlı korumayı geçici kapatın
3. CodeFuser'ı çalıştırın

Çözüm 2: Dışlama ekle (Önerilen)
1. Windows Güvenlik → Virüs ve tehdit koruması
2. Ayarları yönet → Dışlamalar ekle veya kaldır
3. "Dışlama ekle" → "Klasör"
4. CodeFuser klasörünü seçin
```

#### Diğer Antivirüs Programları
```
1. Antivirüs programınızı açın
2. Dışlamalar/İstisna listesi bölümünü bulun
3. CodeFuser klasörünü dışlamalara ekleyin
4. Ayarları kaydedin ve programı yeniden başlatın
```

## 🐍 Python Kaynak Kurulumu

### 📋 Gereksinimler
```bash
# Sistem Gereksinimleri
- Python 3.8 veya üzeri
- pip (Python paket yöneticisi)
- 200 MB boş disk alanı
- İnternet bağlantısı (kurulum için)

# İsteğe Bağlı
- Git (geliştirme için)
- Virtual environment aracı
```

### 🔧 Python Kurulumu

#### Windows
```bash
# Python'u python.org'dan indirin
https://www.python.org/downloads/

# Kurulum sırasında "Add to PATH" seçeneğini işaretleyin
```

#### macOS
```bash
# Homebrew ile
brew install python

# veya python.org'dan indirin
```

#### Linux (Ubuntu/Debian)
```bash
# Paket yöneticisi ile
sudo apt update
sudo apt install python3 python3-pip python3-venv

# CentOS/RHEL/Fedora
sudo yum install python3 python3-pip  # CentOS 7
sudo dnf install python3 python3-pip  # Fedora/CentOS 8+
```

### 📥 CodeFuser Kurulumu

#### Yöntem 1: Hızlı Kurulum
```bash
# En son sürümü indirin
curl -L -O https://github.com/tahamucasiroglu/CodeFuser/archive/refs/heads/main.zip

# Çıkarın
unzip main.zip
cd CodeFuser-main

# Bağımlılıkları yükleyin
pip install -r requirements.txt

# Çalıştırın
python main.py
```

#### Yöntem 2: Virtual Environment ile (Önerilen)
```bash
# Virtual environment oluşturun
python -m venv codefuser-env

# Aktifleştirin
# Windows
codefuser-env\Scripts\activate
# macOS/Linux
source codefuser-env/bin/activate

# CodeFuser'ı indirin
curl -L -O https://github.com/tahamucasiroglu/CodeFuser/archive/refs/heads/main.zip
unzip main.zip
cd CodeFuser-main

# Bağımlılıkları yükleyin
pip install --upgrade pip
pip install -r requirements.txt

# Çalıştırın
python main.py
```

#### Yöntem 3: Pip ile Kurulum (Gelecekte)
```bash
# Gelecekte PyPI'da mevcut olacak
pip install codefuser

# Çalıştırma
codefuser
```

### 🔧 Bağımlılık Sorunları

#### Yaygın Hatalar ve Çözümleri
```bash
# ModuleNotFoundError: No module named 'tkinter'
# Ubuntu/Debian
sudo apt-get install python3-tk

# CentOS/RHEL
sudo yum install tkinter  # CentOS 7
sudo dnf install python3-tkinter  # CentOS 8+

# macOS (Homebrew Python kullanıyorsanız)
brew install python-tk
```

```bash
# Microsoft Visual C++ 14.0 is required
# Windows'ta bu hata alırsanız:
# https://visualstudio.microsoft.com/visual-cpp-build-tools/
# Visual C++ Build Tools'u indirin ve yükleyin
```

```bash
# Permission denied hataları
# Windows
pip install --user -r requirements.txt

# macOS/Linux
pip install --user -r requirements.txt
# veya
sudo pip install -r requirements.txt
```

## 📂 Git Clone Kurulumu (Geliştiriciler)

### 🔨 Geliştirme Kurulumu

#### Ön Gereksinimler
```bash
# Git kurulumu
# Windows: https://git-scm.com/download/win
# macOS: brew install git
# Linux: sudo apt install git (Ubuntu) / sudo yum install git (CentOS)

# Python 3.8+ ve pip gerekli
```

#### Clone ve Kurulum
```bash
# Depoyu clone edin
git clone https://github.com/tahamucasiroglu/CodeFuser.git
cd CodeFuser

# Virtual environment oluşturun
python -m venv venv

# Aktifleştirin
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Geliştirme bağımlılıklarını yükleyin
pip install --upgrade pip
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Editable modda yükleyin
pip install -e .

# Çalıştırın
python main.py
```

#### Pre-commit Hook'ları (İsteğe Bağlı)
```bash
# Kod kalitesi için pre-commit hook'ları
pip install pre-commit
pre-commit install

# Manuel olarak çalıştırma
pre-commit run --all-files
```

### 🔄 Güncelleme

#### Git ile Güncelleme
```bash
# En son değişiklikleri çekin
git pull origin main

# Bağımlılıkları güncelleyin
pip install -r requirements.txt --upgrade
```

## 🐳 Docker Kurulumu

### 📦 Docker ile Çalıştırma

#### Dockerfile
```dockerfile
# Dockerfile (proje dizininde oluşturun)
FROM python:3.9-slim

# Çalışma dizini
WORKDIR /app

# Sistem bağımlılıkları
RUN apt-get update && apt-get install -y \
    python3-tk \
    && rm -rf /var/lib/apt/lists/*

# Python bağımlılıkları
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama kodları
COPY . .

# Port
EXPOSE 5000

# Başlangıç komutu
CMD ["python", "main.py"]
```

#### Docker Compose
```yaml
# docker-compose.yml
version: '3.8'

services:
  codefuser:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - ./projects:/app/projects
      - ./exports:/app/exports
      - ./config:/app/config
    environment:
      - DISPLAY=${DISPLAY}
    networks:
      - codefuser-network

networks:
  codefuser-network:
    driver: bridge
```

#### Çalıştırma
```bash
# Docker image oluşturma
docker build -t codefuser .

# Çalıştırma
docker run -p 5000:5000 -v $(pwd)/projects:/app/projects codefuser

# Docker Compose ile
docker-compose up -d
```

## 🔧 Kurulum Sonrası Yapılandırma

### ⚙️ İlk Çalıştırma

#### 1. Dil Ayarı
```json
# config/user_settings.json dosyasını düzenleyin
{
  "interface": {
    "language": "tr",  // "en" için İngilizce
    "fullscreen": true
  }
}
```

#### 2. Proje Türleri
```json
{
  "project_types": {
    "Python": [".py", ".pyx", ".pyi", ".ipynb"],
    "JavaScript": [".js", ".jsx", ".ts", ".tsx"],
    "Web": [".html", ".css", ".scss", ".sass"]
  }
}
```

#### 3. Export Ayarları
```json
{
  "output_settings": {
    "default_format": "html",
    "default_location": "~/Documents/CodeFuser_Exports"
  }
}
```

### 🎯 Test Kurulumu

#### Basit Test
```bash
# Program başlatma testi
python main.py

# Komut satırından test
python -c "
import sys
print(f'Python Sürümü: {sys.version}')

try:
    import tkinter
    print('✅ Tkinter mevcut')
except ImportError:
    print('❌ Tkinter eksik')

try:
    from docx import Document
    print('✅ python-docx mevcut')
except ImportError:
    print('❌ python-docx eksik')
"
```

#### Örnek Proje ile Test
```bash
# Test projesi oluşturun
mkdir test_project
cd test_project

echo 'print("Merhaba CodeFuser!")' > main.py
echo 'def helper(): pass' > utils.py

# CodeFuser ile test edin
# 1. CodeFuser'ı başlatın
# 2. test_project klasörünü seçin
# 3. Dosyaları seçin ve HTML'e export edin
```

## 🔍 Sorun Giderme

### ❗ Yaygın Kurulum Sorunları

#### Windows EXE Sorunları
```
Problem: EXE çalışmıyor
Çözüm:
1. Windows Defender'ı kontrol edin
2. Yönetici olarak çalıştırın
3. Visual C++ Redistributable yükleyin
4. Windows 10/11 kullandığınızdan emin olun
```

#### Python Kurulum Sorunları
```bash
# Python PATH sorunu
# Windows'ta Python bulunamıyor
where python
# Çıktı yoksa Python PATH'e eklenmemiş

# Çözüm: Python'u PATH'e manuel ekleyin
# Sistem Özellikleri → Gelişmiş → Ortam Değişkenleri
# PATH'e Python klasörünü ekleyin
```

#### Bağımlılık Hatları
```bash
# pip güncel değil
pip install --upgrade pip

# Paket yükleme hatası
pip install --no-cache-dir paket_adi

# İzin sorunu
pip install --user paket_adi
```

#### tkinter Eksik (Linux)
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# CentOS/RHEL
sudo yum install tkinter

# Arch Linux
sudo pacman -S tk
```

### 🔧 Performans Optimizasyonu

#### Düşük Sistem Kaynakları
```json
# config/user_settings.json
{
  "performance": {
    "max_files_scan": 1000,
    "scan_timeout_seconds": 15,
    "max_worker_threads": 2,
    "memory_limit_mb": 256
  }
}
```

#### Ağ Sürücüsü Kullanımı
```json
{
  "performance": {
    "network_timeout_seconds": 60,
    "cache_network_files": true,
    "batch_file_operations": true
  }
}
```

## 📱 Platform-Özel Notlar

### 🖥️ Windows

#### Desteklenen Sürümler
- ✅ Windows 10 (1903 ve üzeri)
- ✅ Windows 11
- ⚠️ Windows 8.1 (sınırlı destek)
- ❌ Windows 7 (desteklenmiyor)

#### Özel Gereksinimler
```
- .NET Framework 4.7.2 veya üzeri
- Visual C++ 2015-2019 Redistributable
- PowerShell 5.1 veya üzeri (Windows 10'da dahil)
```

### 🍎 macOS

#### Desteklenen Sürümler
- ✅ macOS 10.15 (Catalina) ve üzeri
- ✅ macOS 11 (Big Sur)
- ✅ macOS 12 (Monterey)
- ✅ macOS 13 (Ventura)

#### Homebrew Kurulumu
```bash
# Homebrew ile tam kurulum
brew install python
brew install python-tk
pip3 install codefuser
```

#### Notarization Uyarısı
```
macOS Gatekeeper uyarısı çıkarsa:
1. Sistem Tercihleri → Güvenlik ve Gizlilik
2. "Yine de aç" butonuna tıklayın
```

### 🐧 Linux

#### Desteklenen Dağıtımlar
- ✅ Ubuntu 18.04+
- ✅ Debian 10+
- ✅ CentOS 7+
- ✅ Fedora 30+
- ✅ Arch Linux
- ✅ openSUSE Leap 15+

#### Paket Manager Kurulumu
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip python3-tk python3-venv

# CentOS 7
sudo yum install python3 python3-pip tkinter
sudo yum groupinstall "Development Tools"

# Fedora
sudo dnf install python3 python3-pip python3-tkinter python3-devel

# Arch Linux
sudo pacman -S python python-pip tk

# openSUSE
sudo zypper install python3 python3-pip python3-tk
```

#### AppImage (Gelecekte)
```bash
# Gelecekte AppImage olarak da mevcut olacak
wget https://github.com/tahamucasiroglu/CodeFuser/releases/latest/CodeFuser-x86_64.AppImage
chmod +x CodeFuser-x86_64.AppImage
./CodeFuser-x86_64.AppImage
```

## 📋 Kurulum Kontrol Listesi

### ✅ Kurulum Öncesi
- [ ] Sistem gereksinimlerini kontrol ettiniz
- [ ] Yeterli disk alanı mevcut (min 500 MB)
- [ ] İnternet bağlantısı aktif
- [ ] Antivirüs ayarları kontrol edildi

### ✅ Kurulum Sırasında
- [ ] Doğru kurulum yöntemi seçildi
- [ ] Tüm bağımlılıklar yüklendi
- [ ] Hata mesajları kaydedildi
- [ ] Kurulum tamamlandı

### ✅ Kurulum Sonrası
- [ ] Program başarıyla çalışıyor
- [ ] Temel özellikler test edildi
- [ ] Dil ayarı yapıldı
- [ ] Export ayarları yapılandırıldı
- [ ] Örnek proje ile test edildi

## 🚀 Sonraki Adımlar

Kurulum tamamlandıktan sonra:

1. **[Hızlı Başlangıç](Getting-Started-TR)** - İlk projenizi analiz edin
2. **[Yapılandırma](Configuration-TR)** - Ayarları özelleştirin
3. **[Şablonlar](Templates-Guide-TR)** - Güçlü şablonları keşfedin
4. **[Akıllı Filtreler](Smart-Filters-TR)** - Filtreleme özelliklerini öğrenin

## 📞 Yardım ve Destek

Kurulum sorunları yaşıyorsanız:

- **[Sorun Giderme](Troubleshooting-TR)** - Yaygın sorunlar ve çözümleri
- **[GitHub Issues](https://github.com/tahamucasiroglu/CodeFuser/issues)** - Bug bildirimi
- **[GitHub Discussions](https://github.com/tahamucasiroglu/CodeFuser/discussions)** - Topluluk desteği

---

**Kuruluma hazır mısınız?** Sisteminize uygun kurulum yöntemini seçin ve CodeFuser v2.0 ile kod analizine başlayın!

*Kurulum tamamlandıktan sonra [Hızlı Başlangıç](Getting-Started-TR) rehberine geçin →*