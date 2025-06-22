#!/usr/bin/env python3
"""
Convert PNG logo to ICO format for Windows executable
"""

from PIL import Image
import os

def convert_png_to_ico():
    """Convert CodeFuser Logo.png to .ico format for Windows"""
    
    logo_path = "assets/CodeFuser Logo.png"
    ico_path = "assets/CodeFuser.ico"
    
    if not os.path.exists(logo_path):
        print(f"Error: {logo_path} not found!")
        return False
    
    try:
        # Open the PNG image
        img = Image.open(logo_path)
        
        # Convert to RGBA if not already
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        
        # Create multiple sizes for ICO (Windows best practice)
        sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
        
        # Create resized versions
        images = []
        for size in sizes:
            resized = img.resize(size, Image.Resampling.LANCZOS)
            images.append(resized)
        
        # Save as ICO with multiple sizes
        img.save(ico_path, format='ICO', sizes=[(img.width, img.height) for img in images])
        
        print(f"✅ Successfully converted {logo_path} to {ico_path}")
        print(f"📁 ICO file created with {len(sizes)} sizes: {', '.join([f'{s[0]}x{s[1]}' for s in sizes])}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error converting image: {e}")
        return False

if __name__ == "__main__":
    print("🖼️  CodeFuser Icon Converter")
    print("=" * 40)
    convert_png_to_ico()