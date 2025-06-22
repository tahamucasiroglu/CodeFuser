#!/usr/bin/env python3
"""
CodeFuser Test Script
Quick test to verify all components are working
"""

import sys
import os
from pathlib import Path

def test_imports():
    """Test all critical imports"""
    print("🧪 Testing imports...")
    
    issues = []
    
    try:
        import tkinter as tk
        print("✅ tkinter - OK")
    except ImportError as e:
        issues.append(f"❌ tkinter - {e}")
    
    try:
        from PIL import Image, ImageTk
        print("✅ PIL (Pillow) - OK")
    except ImportError as e:
        issues.append(f"❌ PIL (Pillow) - {e}")
    
    try:
        import docx
        print("✅ python-docx - OK")
    except ImportError as e:
        issues.append(f"❌ python-docx - {e}")
    
    try:
        import reportlab
        print("✅ reportlab - OK")
    except ImportError as e:
        issues.append(f"❌ reportlab - {e}")
    
    return issues

def test_file_structure():
    """Test file structure"""
    print("\n📁 Testing file structure...")
    
    issues = []
    required_files = [
        'main.py',
        'src/main_window.py',
        'src/config_manager.py',
        'src/file_scanner.py',
        'src/output_manager.py',
        'src/template_engine.py',
        'src/git_integration.py',
        'src/smart_filters.py',
        'src/ui_components.py',
        'src/file_tree_widget.py',
        'src/settings_window.py',
        'src/localization_manager.py',
        'config/default_settings.json',
        'locales/en.json',
        'locales/tr.json',
        'requirements.txt',
        'README.md',
        'LICENSE'
    ]
    
    for file_path in required_files:
        full_path = Path(file_path)
        if full_path.exists():
            print(f"✅ {file_path}")
        else:
            issues.append(f"❌ Missing: {file_path}")
    
    return issues

def test_config():
    """Test configuration loading"""
    print("\n⚙️ Testing configuration...")
    
    issues = []
    
    try:
        sys.path.insert(0, str(Path(__file__).parent / 'src'))
        from config_manager import ConfigManager
        
        config = ConfigManager()
        project_types = config.get_project_types()
        
        if project_types:
            print(f"✅ Config loaded - {len(project_types)} project types")
        else:
            issues.append("❌ No project types found in config")
            
    except Exception as e:
        issues.append(f"❌ Config loading failed: {e}")
    
    return issues

def test_localization():
    """Test localization"""
    print("\n🌍 Testing localization...")
    
    issues = []
    
    try:
        from localization_manager import LocalizationManager
        from config_manager import ConfigManager
        
        config = ConfigManager()
        loc = LocalizationManager(config)
        
        # Test English
        loc.set_language('en')
        app_title = loc.get('app_title')
        
        if app_title:
            print(f"✅ English localization - {app_title}")
        else:
            issues.append("❌ English localization failed")
        
        # Test Turkish
        loc.set_language('tr')
        app_title_tr = loc.get('app_title')
        
        if app_title_tr:
            print(f"✅ Turkish localization - {app_title_tr}")
        else:
            issues.append("❌ Turkish localization failed")
            
    except Exception as e:
        issues.append(f"❌ Localization test failed: {e}")
    
    return issues

def test_logo():
    """Test logo file"""
    print("\n🖼️ Testing logo...")
    
    issues = []
    
    logo_path = Path('assets/CodeFuser Logo.png')
    if logo_path.exists():
        print(f"✅ Logo found: {logo_path}")
        
        # Test if PIL can open it
        try:
            from PIL import Image
            img = Image.open(logo_path)
            print(f"✅ Logo format valid: {img.size} {img.format}")
        except Exception as e:
            issues.append(f"❌ Logo format error: {e}")
    else:
        issues.append(f"❌ Logo not found: {logo_path}")
    
    return issues

def main():
    """Run all tests"""
    print("🚀 CodeFuser Application Test")
    print("=" * 50)
    
    all_issues = []
    
    # Run tests
    all_issues.extend(test_imports())
    all_issues.extend(test_file_structure())
    all_issues.extend(test_config())
    all_issues.extend(test_localization())
    all_issues.extend(test_logo())
    
    print("\n" + "=" * 50)
    print("📊 Test Results:")
    
    if not all_issues:
        print("🎉 All tests passed! CodeFuser is ready to run.")
        print("\n💡 To start the application:")
        print("   python main.py")
        return True
    else:
        print(f"❌ Found {len(all_issues)} issues:")
        for issue in all_issues:
            print(f"   {issue}")
        
        print("\n💡 To fix issues:")
        print("   pip install -r requirements.txt")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)