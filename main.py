#!/usr/bin/env python3
"""
CodeFuser - The Ultimate Code Aggregation Tool with AI Integration
Main entry point for the application
"""

import sys
import os
from pathlib import Path

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
    
    # Add src directory to Python path
    src_path = Path(__file__).parent / 'src'
    sys.path.insert(0, str(src_path))
    
    try:
        from main_window import MainWindow
        app = MainWindow()
        app.run()
        
    except ImportError as e:
        print(f"❌ Error importing modules: {e}")
        print("💡 Make sure you're in the CodeFuser directory")
        sys.exit(1)
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()