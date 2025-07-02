#!/usr/bin/env python3
"""
CodeFuser - The Ultimate Code Aggregation Tool with AI Integration
Main entry point for the application
"""

import sys
import os
from pathlib import Path

# PyInstaller frozen app fix
if getattr(sys, 'frozen', False):
    # PyInstaller ile derlenmiş - tüm modüller root'ta
    sys.path.insert(0, sys._MEIPASS)
else:
    # Normal Python - src klasöründen import et
    src_path = Path(__file__).parent / 'src'
    if src_path.exists():
        sys.path.insert(0, str(src_path))

def check_dependencies():
    """Check if all required dependencies are available"""
    missing_deps = []
    
    try:
        import tkinter
    except ImportError:
        missing_deps.append("tkinter (Python GUI library)")
    
    try:
        from PIL import Image, ImageTk
    except ImportError:
        missing_deps.append("Pillow (pip install Pillow)")
    
    try:
        import docx
    except ImportError:
        missing_deps.append("python-docx (pip install python-docx)")
    
    try:
        import reportlab
    except ImportError:
        missing_deps.append("reportlab (pip install reportlab)")
    
    if missing_deps:
        print("❌ Missing dependencies:")
        for dep in missing_deps:
            print(f"  - {dep}")
        print("\n💡 Install missing dependencies with:")
        print("pip install -r requirements.txt")
        return False
    
    return True

def main():
    """Main application entry point"""
    print("🚀 Starting CodeFuser...")
    
    # Check dependencies first
    if not check_dependencies():
        sys.exit(1)
    
    try:
        # Debug bilgisi
        if getattr(sys, 'frozen', False):
            print(f"📁 Running from: {sys._MEIPASS}")
            print(f"📁 Executable: {sys.executable}")
        
        from main_window import MainWindow
        app = MainWindow()
        app.run()
        
    except ImportError as e:
        print(f"❌ Error importing modules: {e}")
        print("💡 Module search paths:")
        for p in sys.path[:5]:
            print(f"   - {p}")
        import traceback
        traceback.print_exc()
        if getattr(sys, 'frozen', False):
            input("\nPress Enter to exit...")
        sys.exit(1)
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        if getattr(sys, 'frozen', False):
            input("\nPress Enter to exit...")
        sys.exit(1)

if __name__ == "__main__":
    main()