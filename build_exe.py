#!/usr/bin/env python3
"""
CodeFuser Windows EXE Builder
Bağımsız çalışan tek dosya Windows EXE oluşturur
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path

def install_requirements():
    """Gerekli paketleri yükle"""
    print("📦 Gerekli paketler kontrol ediliyor...")
    
    required_packages = {
        'PyInstaller': 'pyinstaller',
        'Pillow': 'pillow', 
        'python-docx': 'python-docx',
        'reportlab': 'reportlab'
    }
    
    for display_name, pip_name in required_packages.items():
        try:
            __import__(pip_name.replace('-', '_').lower())
            print(f"✅ {display_name} yüklü")
        except ImportError:
            print(f"📥 {display_name} yükleniyor...")
            try:
                subprocess.run([sys.executable, '-m', 'pip', 'install', pip_name], 
                             check=True, capture_output=True)
                print(f"✅ {display_name} yüklendi")
            except subprocess.CalledProcessError as e:
                print(f"❌ {display_name} yüklenemedi: {e}")
                return False
    
    return True

def create_icon():
    """Icon dosyası oluştur"""
    png_path = Path('assets/CodeFuser Logo.png')
    ico_path = Path('assets/CodeFuser.ico')
    
    if ico_path.exists():
        print("✅ Icon dosyası mevcut")
        return True
    
    if not png_path.exists():
        print("⚠️  Logo bulunamadı, icon olmadan devam")
        return False
    
    try:
        from PIL import Image
        print("🎨 Icon oluşturuluyor...")
        
        img = Image.open(png_path)
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        
        ico_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
        img.save(ico_path, format='ICO', sizes=ico_sizes)
        
        print("✅ Icon oluşturuldu")
        return True
        
    except Exception as e:
        print(f"⚠️  Icon oluşturulamadı: {e}")
        return False

def create_spec_file():
    """PyInstaller spec dosyası oluştur"""
    
    spec_content = '''# -*- mode: python ; coding: utf-8 -*-

import os
from pathlib import Path

block_cipher = None

# Tüm src dosyalarını ekle
src_modules = []
src_path = Path('src')
if src_path.exists():
    for py_file in src_path.glob('*.py'):
        if py_file.name != '__init__.py':
            module_name = py_file.stem
            src_modules.append(module_name)

a = Analysis(
    ['main.py'],
    pathex=['.', 'src'],
    binaries=[],
    datas=[
        ('config', 'config'),
        ('locales', 'locales'), 
        ('assets', 'assets'),
        ('templates', 'templates'),
    ],
    hiddenimports=src_modules + [
        'main_window',
        'config_manager',
        'localization_manager',
        'template_engine',
        'file_scanner',
        'output_manager',
        'file_tree_widget',
        'settings_window',
        'git_integration',
        'smart_filters',
        'ui_components',
        'utils',
        'tkinter',
        'tkinter.ttk',
        'tkinter.filedialog',
        'tkinter.messagebox',
        'tkinter.scrolledtext',
        '_tkinter',
        'PIL',
        'PIL.Image',
        'PIL.ImageTk',
        'PIL.ImageDraw',
        'PIL.ImageFont',
        'PIL._tkinter_finder',
        'docx',
        'docx.document',
        'docx.shared',
        'docx.enum',
        'docx.enum.text',
        'docx.enum.style',
        'docx.oxml',
        'docx.oxml.shared',
        'lxml',
        'lxml.etree',
        'reportlab',
        'reportlab.pdfgen',
        'reportlab.pdfgen.canvas',
        'reportlab.lib',
        'reportlab.lib.styles',
        'reportlab.lib.units',
        'reportlab.lib.pagesizes',
        'reportlab.lib.colors',
        'reportlab.platypus',
        'reportlab.platypus.paragraph',
        'reportlab.platypus.tables',
        'reportlab.pdfbase',
        'reportlab.pdfbase.ttfonts',
        'json',
        'pathlib',
        'threading',
        'queue',
        'datetime',
        'webbrowser',
        'platform',
        'subprocess',
        'glob',
        're',
        'typing',
        'dataclasses',
        'collections',
        'itertools',
        'functools',
        'copy',
        'html',
        'urllib',
        'urllib.parse',
        'encodings',
        'encodings.utf_8',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'matplotlib',
        'numpy',
        'scipy',
        'pandas',
        'pytest',
        'IPython',
        'jupyter',
        'notebook',
        'PyQt5',
        'PyQt6',
        'PySide2',
        'PySide6',
        'wx',
        'kivy',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

# Tüm src dosyalarını pure modüller olarak ekle
for py_file in Path('src').glob('*.py'):
    if py_file.name != '__init__.py':
        a.pure.append((py_file.stem, str(py_file), 'PYMODULE'))

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='CodeFuser',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # GUI uygulaması
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='assets/CodeFuser.ico' if os.path.exists('assets/CodeFuser.ico') else None,
    onefile=True,  # Tek dosya
    windowed=True   # Windows GUI
)
'''
    
    with open('CodeFuser.spec', 'w', encoding='utf-8') as f:
        f.write(spec_content)
    
    print("✅ Spec dosyası oluşturuldu")
    return True

def build_executable():
    """EXE dosyasını derle"""
    print("🔨 EXE derleniyor...")
    
    # Eski build klasörlerini temizle
    for folder in ['build', 'dist']:
        if Path(folder).exists():
            shutil.rmtree(folder)
            print(f"🗑️  {folder} klasörü temizlendi")
    
    try:
        result = subprocess.run([
            sys.executable, '-m', 'PyInstaller',
            '--clean',
            '--noconfirm', 
            'CodeFuser.spec'
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            exe_path = Path('dist/CodeFuser.exe')
            if exe_path.exists():
                size_mb = exe_path.stat().st_size / 1024 / 1024
                print(f"✅ EXE oluşturuldu: {size_mb:.1f} MB")
                return True
            else:
                print("❌ EXE dosyası bulunamadı")
                return False
        else:
            print(f"❌ Derleme hatası:\n{result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Derleme hatası: {e}")
        return False

def create_portable_package():
    """Taşınabilir paket oluştur"""
    print("📦 Taşınabilir paket hazırlanıyor...")
    
    # Release klasörü oluştur
    release_dir = Path('CodeFuser_Portable')
    if release_dir.exists():
        shutil.rmtree(release_dir)
    release_dir.mkdir()
    
    # EXE'yi kopyala
    exe_source = Path('dist/CodeFuser.exe')
    if exe_source.exists():
        shutil.copy2(exe_source, release_dir / 'CodeFuser.exe')
        
        # README oluştur (Türkçe ve İngilizce)
        readme_content = """
═══════════════════════════════════════════════════════════════════════════════
                            CodeFuser v2.0.0
        AI-Destekli Kod Birleştirme ve Analiz Aracı / AI-Powered Code Aggregation Tool
═══════════════════════════════════════════════════════════════════════════════

🇹🇷 TÜRKÇE KILAVUZ
═══════════════════

🚀 HIZLI BAŞLANGIÇ:
───────────────────
1. CodeFuser.exe dosyasına çift tıklayın
2. Proje klasörünüzü seçin (Browse düğmesi ile)
3. "Scan Files" düğmesine tıklayarak dosyaları tarayın
4. İstediğiniz dosyaları seçin (checkbox'ları işaretleyin)
5. Dosya bazında özel prompt'lar ekleyin (📄 ikonuna tıklayarak)
6. Genel prompt yazın veya hazır şablonlardan birini seçin
7. Çıktı formatını seçin (TXT, HTML, DOCX, PDF)
8. "Start Process" düğmesine tıklayın!

✨ YENİ ÖZELLİKLER v2.0:
─────────────────────────
🎯 Dosya Bazında Özel Prompt'lar
   • Her dosyanın yanındaki 📄 ikonuna tıklayın
   • O dosya için özel talimatlar yazın
   • Özel prompt'u olan dosyalar 📝✨ işareti ile gösterilir
   • "Bu dosyadaki güvenlik açıklarını analiz et" gibi spesifik istekler

🧠 Akıllı Şablonlar
   • 16x Prompt Style: Popüler AI analiz formatı
   • Claude Project Setup: Claude Projects için hazır format
   • Code Review: Detaylı kod inceleme şablonu
   • Custom: Kendi prompt'unuzu yazın

🔍 Gelişmiş Filtreler
   • Git Integration: Sadece değişen dosyalar, branch karşılaştırma
   • Smart Filters: Test dosyalarını hariç tutma, dosya boyutu filtreleme
   • Custom Filters: Özel uzantı ve klasör filtreleri

📊 Çoklu Export Formatları
   • TXT: Basit metin formatı
   • HTML: İnteraktif web sayfası (syntax highlighting ile)
   • DOCX: Microsoft Word belgesi
   • PDF: Profesyonel PDF raporu

🌍 Çoklu Dil Desteği
   • Türkçe ve İngilizce arayüz
   • Dil değiştirme: Settings > Language

💡 KULLANIM İPUÇLARI:
────────────────────
• Büyük projeler için: Advanced Filters kullanarak gereksiz dosyaları filtreleyin
• AI analizi için: Dosya bazında özel prompt'lar ile spesifik sorular sorun
• Kod incelemesi için: "Code Review" şablonunu kullanın
• Claude kullanıyorsanız: "Claude Project" şablonunu tercih edin
• Arama kutusu ile dosyaları hızlıca filtreleyin

⚠️ ÖNEMLİ NOTLAR:
─────────────────
• İlk açılışta Windows Defender veya antivirus uyarısı normal
• "Yine de çalıştır" / "Run anyway" seçeneğini tıklayın
• Uygulama tamamen güvenlidir ve açık kaynak kodludur
• İnternet bağlantısı gerektirmez, tamamen offline çalışır
• Python kurulumu gerekmez, tüm bağımlılıklar dahil

💻 SİSTEM GEREKSİNİMLERİ:
──────────────────────────
• Windows 10/11 (64-bit)
• En az 4 GB RAM önerilen
• 100 MB boş disk alanı
• .NET Framework (Windows ile birlikte gelir)

📧 DESTEK VE İLETİŞİM:
─────────────────────
• GitHub: https://github.com/yourusername/codefuser
• Issues: https://github.com/yourusername/codefuser/issues
• E-posta: destek@codefuser.com
• Telegram: @codefuser_support

═══════════════════════════════════════════════════════════════════════════════

🇬🇧 ENGLISH GUIDE
═════════════════

🚀 QUICK START:
──────────────
1. Double-click CodeFuser.exe
2. Select your project folder (using Browse button)
3. Click "Scan Files" to discover files
4. Select desired files (check the checkboxes)
5. Add file-specific prompts (click 📄 icon next to files)
6. Write general prompt or choose from templates
7. Select output format (TXT, HTML, DOCX, PDF)
8. Click "Start Process"!

✨ NEW FEATURES v2.0:
────────────────────
🎯 File-Specific Custom Prompts
   • Click the 📄 icon next to any file
   • Write specific instructions for that file
   • Files with custom prompts show 📝✨ indicator
   • Example: "Analyze security vulnerabilities in this file"

🧠 Smart Templates
   • 16x Prompt Style: Popular AI analysis format
   • Claude Project Setup: Ready format for Claude Projects
   • Code Review: Detailed code inspection template
   • Custom: Write your own prompt

🔍 Advanced Filters
   • Git Integration: Only changed files, branch comparison
   • Smart Filters: Exclude test files, file size filtering
   • Custom Filters: Custom extension and folder filters

📊 Multiple Export Formats
   • TXT: Simple text format
   • HTML: Interactive web page (with syntax highlighting)
   • DOCX: Microsoft Word document
   • PDF: Professional PDF report

🌍 Multi-Language Support
   • Turkish and English interface
   • Change language: Settings > Language

💡 USAGE TIPS:
─────────────
• For large projects: Use Advanced Filters to exclude unnecessary files
• For AI analysis: Use file-specific prompts for targeted questions
• For code review: Use the "Code Review" template
• For Claude users: Prefer the "Claude Project" template
• Use search box to quickly filter files

⚠️ IMPORTANT NOTES:
──────────────────
• Windows Defender or antivirus warnings on first run are normal
• Click "Run anyway" to proceed
• Application is completely safe and open-source
• No internet connection required, works completely offline
• No Python installation needed, all dependencies included

💻 SYSTEM REQUIREMENTS:
──────────────────────
• Windows 10/11 (64-bit)
• Minimum 4 GB RAM recommended
• 100 MB free disk space
• .NET Framework (comes with Windows)

📧 SUPPORT & CONTACT:
────────────────────
• GitHub: https://github.com/yourusername/codefuser
• Issues: https://github.com/yourusername/codefuser/issues
• Email: support@codefuser.com
• Telegram: @codefuser_support

═══════════════════════════════════════════════════════════════════════════════

📋 EXAMPLE WORKFLOWS / ÖRNEK KULLANIM SENARYOLARI:

🎯 AI Code Analysis / AI Kod Analizi:
1. Select Python files / Python dosyalarını seçin
2. Use "16x Prompt" template / "16x Prompt" şablonunu kullanın
3. Add file-specific prompts for critical files / Kritik dosyalar için özel prompt ekleyin
4. Export as HTML for easy reading / Kolay okuma için HTML olarak export edin

🔍 Code Review / Kod İnceleme:
1. Use Git filters to see only changed files / Sadece değişen dosyaları görmek için Git filtreleri
2. Select "Code Review" template / "Code Review" şablonunu seçin
3. Add specific review questions per file / Dosya başına özel inceleme soruları ekleyin
4. Export as DOCX for formal documentation / Resmi dokümantasyon için DOCX export

🤖 Claude Project Setup / Claude Proje Kurulumu:
1. Select all relevant source files / Tüm ilgili kaynak dosyaları seçin
2. Use "Claude Project" template / "Claude Project" şablonunu kullanın
3. Add context-specific prompts / Bağlam-özel prompt'lar ekleyin
4. Export as TXT for Claude upload / Claude'a yüklemek için TXT export

═══════════════════════════════════════════════════════════════════════════════

🆚 VERSION HISTORY / SÜRÜM GEÇMİŞİ:

v2.0.0 (Current):
• ✨ File-specific custom prompts / Dosya bazında özel prompt'lar
• 🎨 Enhanced UI with document icons / Belge ikonları ile gelişmiş arayüz
• 🔧 Improved template system / Gelişmiş şablon sistemi
• 🌐 Better localization support / Daha iyi yerelleştirme desteği

v1.0.0:
• 🚀 Initial release / İlk sürüm
• 📄 Basic file aggregation / Temel dosya birleştirme
• 🎯 Template support / Şablon desteği
• 🔍 Git integration / Git entegrasyonu

═══════════════════════════════════════════════════════════════════════════════

📄 LICENSE / LİSANS:
MIT License - Free to use, modify, and distribute
MIT Lisansı - Kullanım, değiştirme ve dağıtım serbesttir

© 2024 CodeFuser Team - All rights reserved
© 2024 CodeFuser Ekibi - Tüm hakları saklıdır

═══════════════════════════════════════════════════════════════════════════════

Happy Coding! / Mutlu Kodlamalar! 🚀✨
"""
        
        # Her iki dilde de dosya oluştur
        with open(release_dir / 'OKUBENI.txt', 'w', encoding='utf-8') as f:
            f.write(readme_content)
        
        with open(release_dir / 'README.txt', 'w', encoding='utf-8') as f:
            f.write(readme_content)
        
        # Ayrıca kısa bir başlangıç dosyası da oluşturalım
        quick_start = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                               CodeFuser v2.0.0                              ║
║                    🚀 AI-Powered Code Aggregation Tool 🚀                   ║
╚══════════════════════════════════════════════════════════════════════════════╝

🇹🇷 TÜRKÇE:
• Detaylı kullanım kılavuzu için: OKUBENI.txt dosyasını açın
• Başlangıç: CodeFuser.exe'ye çift tıklayın
• Yardım: Program içindeki Help menüsünü kullanın

🇬🇧 ENGLISH:  
• For detailed usage guide: Open README.txt file
• Quick start: Double-click CodeFuser.exe
• Help: Use the Help menu inside the program

═══════════════════════════════════════════════════════════════════════════════

⚠️  İlk çalıştırmada Windows Defender uyarısı normal! "Yine de çalıştır" tıklayın.
⚠️  Windows Defender warning on first run is normal! Click "Run anyway".

═══════════════════════════════════════════════════════════════════════════════
        """
        
        with open(release_dir / 'BAŞLANGIÇ - QUICK START.txt', 'w', encoding='utf-8') as f:
            f.write(quick_start)
        
        print(f"✅ Paket hazırlandı: {release_dir}")
        print(f"📁 EXE boyutu: {exe_source.stat().st_size / 1024 / 1024:.1f} MB")
        
        return True
    else:
        print("❌ EXE dosyası bulunamadı")
        return False

def main():
    """Ana işlev"""
    print("🚀 CodeFuser Windows EXE Builder")
    print("=" * 50)
    
    # Çalışma dizinini kontrol et
    if not Path('main.py').exists():
        print("❌ main.py bulunamadı! CodeFuser ana dizininde çalıştırın.")
        return False
    
    # Adımları gerçekleştir
    steps = [
        ("Gereksinimleri yükle", install_requirements),
        ("Icon dosyası oluştur", create_icon),
        ("Spec dosyası oluştur", create_spec_file), 
        ("EXE derle", build_executable),
        ("Taşınabilir paket oluştur", create_portable_package)
    ]
    
    for step_name, step_func in steps:
        print(f"\n📌 {step_name}...")
        if not step_func():
            print(f"❌ {step_name} başarısız!")
            return False
    
    print("\n" + "=" * 50)
    print("✅ Windows EXE başarıyla oluşturuldu!")
    print("\n📁 Oluşturulan dosyalar:")
    print("   - CodeFuser_Portable/CodeFuser.exe")
    print("\n🎉 Artık CodeFuser'ı Python olmadan çalıştırabilirsiniz!")
    print("💡 EXE'yi başka bilgisayarlara kopyalayabilirsiniz!")
    
    return True

if __name__ == "__main__":
    success = main()
    input("\nPress Enter to exit...")
    sys.exit(0 if success else 1)