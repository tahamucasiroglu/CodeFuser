#!/usr/bin/env python3
"""
CodeFuser Standalone EXE Builder
Bu script PyInstaller kullanarak CodeFuser'ı tek dosyalık exe haline getirir
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path

def create_exe():
    """Create standalone executable"""
    
    # Ensure we're in the right directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    # Create spec file for PyInstaller
    spec_content = '''# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('config', 'config'),
        ('locales', 'locales'),
        ('assets', 'assets'),
        ('src/*.py', 'src'),
    ],
    hiddenimports=[
        'tkinter',
        'tkinter.ttk',
        'tkinter.filedialog',
        'tkinter.messagebox',
        'PIL',
        'PIL.Image',
        'PIL.ImageTk',
        'docx',
        'reportlab',
        'reportlab.pdfgen',
        'reportlab.lib',
        'reportlab.platypus',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

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
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='assets/CodeFuser.ico'
)
'''
    
    # Write spec file
    with open('CodeFuser.spec', 'w', encoding='utf-8') as f:
        f.write(spec_content)
    
    print("🚀 Building CodeFuser executable...")
    print("📦 Installing required packages...")
    
    # Install required packages
    required_packages = [
        'PyInstaller',
        'python-docx',
        'reportlab',
        'Pillow'
    ]
    
    for package in required_packages:
        try:
            subprocess.run([sys.executable, '-m', 'pip', 'install', package], check=True)
            print(f"✅ {package} installed")
        except subprocess.CalledProcessError:
            print(f"❌ Failed to install {package}")
            return False
    
    # Convert PNG logo to ICO if needed
    png_logo = Path('assets/CodeFuser Logo.png')
    ico_path = Path('assets/CodeFuser.ico')
    
    if png_logo.exists() and not ico_path.exists():
        try:
            from PIL import Image
            print("🖼️  Converting PNG logo to ICO format...")
            
            img = Image.open(png_logo)
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
            
            # Create multiple sizes for ICO
            sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
            images = []
            for size in sizes:
                resized = img.resize(size, Image.Resampling.LANCZOS)
                images.append(resized)
            
            img.save(ico_path, format='ICO', sizes=[(img.width, img.height) for img in images])
            print(f"✅ ICO icon created: {ico_path}")
            
        except Exception as e:
            print(f"⚠️  Could not convert PNG to ICO: {e}")
            print("⚠️  Continuing without icon...")
    
    elif not png_logo.exists() and not ico_path.exists():
        print("⚠️  No logo files found, continuing without icon...")
    
    # Build with PyInstaller
    try:
        print("🔨 Building executable...")
        subprocess.run([
            sys.executable, '-m', 'PyInstaller',
            '--clean',
            '--noconfirm',
            'CodeFuser.spec'
        ], check=True)
        
        print("✅ Build completed!")
        print(f"📁 Executable created: {Path('dist/CodeFuser.exe').absolute()}")
        
        # Create portable package
        create_portable_package()
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Build failed: {e}")
        return False

def create_portable_package():
    """Create a portable package with all necessary files"""
    
    print("📦 Creating portable package...")
    
    # Create release directory
    release_dir = Path('release')
    if release_dir.exists():
        shutil.rmtree(release_dir)
    release_dir.mkdir()
    
    # Copy executable
    exe_source = Path('dist/CodeFuser.exe')
    if exe_source.exists():
        shutil.copy2(exe_source, release_dir / 'CodeFuser.exe')
    
    # Copy config files
    config_files = [
        'config/default_settings.json',
        'locales/tr.json',
        'locales/en.json'
    ]
    
    for file_path in config_files:
        source = Path(file_path)
        if source.exists():
            dest = release_dir / file_path
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, dest)
    
    # Create README for portable version
    readme_content = """# CodeFuser Portable

## Quick Start
1. Double-click CodeFuser.exe to start
2. Select a project folder
3. Choose file types and filters
4. Add your prompt or select a template
5. Export to your preferred format!

## Features
- 🎯 Smart Templates (16x Prompt, Cursor Rules, etc.)
- 🔍 Advanced Filters (Git integration, Smart analysis)
- 📄 Multiple Export Formats (TXT, HTML, DOCX, PDF)
- 🌍 Multi-Language Support (Turkish/English)

## Requirements
- Windows 10/11
- No Python installation required!

## Support
- GitHub: https://github.com/yourusername/codefuser
- Issues: https://github.com/yourusername/codefuser/issues

Generated with CodeFuser Build System
"""
    
    with open(release_dir / 'README.txt', 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print(f"✅ Portable package created: {release_dir.absolute()}")

if __name__ == "__main__":
    print("🚀 CodeFuser EXE Builder")
    print("=" * 50)
    
    if create_exe():
        print("\n✅ Build process completed successfully!")
        print("📁 Check the 'release' folder for the portable package")
    else:
        print("\n❌ Build process failed!")
        sys.exit(1)