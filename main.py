#!/usr/bin/env python3
"""
CodeFuser - A modern tool for collecting and merging project files with custom prompts.
"""

import sys
import os
from pathlib import Path

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from main_window import MainWindow


def main():
    try:
        app = MainWindow()
        app.run()
    except Exception as e:
        print(f"Error starting CodeFuser: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()