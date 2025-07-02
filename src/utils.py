"""
Utility functions for CodeFuser
Handles resource paths for both development and PyInstaller builds
"""

import sys
import os
from pathlib import Path

def get_resource_path(relative_path):
    """Get absolute path to resource, works for dev and PyInstaller"""
    if getattr(sys, 'frozen', False):
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = Path(sys._MEIPASS)
    else:
        # Development mode
        base_path = Path(__file__).parent.parent
    
    return base_path / relative_path

def get_config_path(filename):
    """Get path to config file"""
    return get_resource_path(f'config/{filename}')

def get_locale_path(filename):
    """Get path to locale file"""
    return get_resource_path(f'locales/{filename}')

def get_asset_path(filename):
    """Get path to asset file"""
    return get_resource_path(f'assets/{filename}')

def get_template_path(filename):
    """Get path to template file"""
    return get_resource_path(f'templates/{filename}')

def ensure_dir(path):
    """Ensure directory exists"""
    Path(path).mkdir(parents=True, exist_ok=True)
    return path