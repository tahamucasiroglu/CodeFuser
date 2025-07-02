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
        
        # README oluştur
        readme_content = """CodeFuser - Kod Birleştirme Aracı
=================================

🚀 HIZLI BAŞLANGIÇ:
1. CodeFuser.exe'ye çift tıklayın
2. Proje klasörünüzü seçin  
3. Dosya türlerini ve filtreleri ayarlayın
4. Şablon seçin veya özel prompt yazın
5. İstediğiniz formatta dışa aktarın!

✨ ÖZELLİKLER:
- 🎯 Akıllı Şablonlar (16x Prompt, Claude Project, vb.)
- 🔍 Gelişmiş Filtreler (Git entegrasyonu, akıllı analiz)  
- 📄 Çoklu Export Formatları (TXT, HTML, DOCX, PDF)
- 🌍 Çoklu Dil Desteği (Türkçe/İngilizce)
- 🚀 Python kurulumu gerektirmez!

💻 SİSTEM GEREKSİNİMLERİ:
- Windows 10/11 (64-bit)
- En az 100 MB boş disk alanı
- İnternet bağlantısı gerekmez

ℹ️ NOTLAR:
- İlk açılışta Windows Defender uyarısı verebilir
- "Yine de çalıştır" seçeneğini tıklayın
- Antivirus yazılımları yanlış pozitif uyarı verebilir

📧 DESTEK:
- GitHub: https://github.com/yourusername/codefuser
- E-posta: destek@codefuser.com

Sürüm: 2.0.0
Lisans: MIT
© 2024 CodeFuser - Tüm hakları saklıdır.
"""
        
        with open(release_dir / 'OKUBENI.txt', 'w', encoding='utf-8') as f:
            f.write(readme_content)
        
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