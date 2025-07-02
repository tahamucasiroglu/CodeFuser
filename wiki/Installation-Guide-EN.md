# 🔧 Installation Guide

Complete installation guide for CodeFuser v2.0 across all platforms and methods.

## 🎯 Quick Decision Guide

**Choose your installation method:**

| Method | Best For | Requirements | Time |
|--------|----------|-------------|------|
| **[Standalone EXE](#-method-1-standalone-windows-exe)** | Windows users, beginners | Windows 10/11 | 2 minutes |
| **[Python Source](#-method-2-python-source)** | Developers, all platforms | Python 3.8+ | 5 minutes |
| **[VSCode Extension](#-method-3-vscode-extension)** | VSCode users | VSCode + Node.js | 3 minutes |

## 📥 Method 1: Standalone Windows EXE

### ✨ Advantages
- **Zero dependencies** - No Python installation needed
- **Instant setup** - Download, extract, run
- **Portable** - Copy to any Windows machine
- **Professional** - Includes bilingual documentation

### 📋 System Requirements
- Windows 10 or Windows 11 (64-bit)
- 4 GB RAM (recommended)
- 100 MB free disk space
- .NET Framework (included with Windows)

### 🚀 Installation Steps

#### Step 1: Download
1. Go to [CodeFuser Releases](https://github.com/tahamucasiroglu/CodeFuser/releases/latest)
2. Download `CodeFuser_Portable.zip` (approximately 25 MB)
3. **Windows Defender Warning**: This is normal for new EXE files

#### Step 2: Extract
1. Right-click the downloaded ZIP file
2. Select "Extract All..." or "Extract Here"
3. Open the extracted `CodeFuser_Portable` folder

#### Step 3: Run
1. Double-click `CodeFuser.exe`
2. **Security Warning**: Click "More info" → "Run anyway" if prompted
3. Application starts immediately! 🎉

#### Step 4: First Launch Setup
1. **Language Selection**: Choose Turkish or English
2. **Folder Selection**: Click "Browse" to select your first project
3. **File Scanning**: Click "Scan Files" to discover code files
4. **Ready to use!**

### 📁 What's Included
```
CodeFuser_Portable/
├── CodeFuser.exe (22MB standalone executable)
├── OKUBENI.txt (Turkish documentation)
├── README.txt (English documentation)
└── BAŞLANGIÇ - QUICK START.txt (Bilingual quick reference)
```

### 🔧 Troubleshooting EXE Installation

#### "Windows Protected Your PC"
```
Solution:
1. Click "More info"
2. Click "Run anyway"
3. This is normal for new executables
```

#### "Application Failed to Start"
```
Possible causes:
1. Antivirus blocking - Add CodeFuser to exceptions
2. Corrupted download - Re-download the ZIP file
3. Missing .NET Framework - Update Windows
```

#### "Out of Memory" Error
```
Solution:
1. Close other applications
2. Restart your computer
3. Ensure 4+ GB RAM available
```

## 🐍 Method 2: Python Source

### ✨ Advantages
- **Cross-platform** - Works on Windows, macOS, Linux
- **Latest features** - Get updates immediately
- **Customizable** - Modify source code
- **Development** - Contribute to the project

### 📋 System Requirements
- Python 3.8 or higher
- pip package manager
- Git (optional, for cloning)
- 50 MB free disk space

### 🚀 Installation Steps

#### Step 1: Install Python
**Windows:**
1. Download from [python.org](https://python.org)
2. **Important**: Check "Add Python to PATH" during installation
3. Verify: Open Command Prompt, type `python --version`

**macOS:**
```bash
# Using Homebrew (recommended)
brew install python

# Or download from python.org
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip git
```

#### Step 2: Download CodeFuser
**Option A: Git Clone (Recommended)**
```bash
git clone https://github.com/tahamucasiroglu/CodeFuser.git
cd CodeFuser
```

**Option B: ZIP Download**
1. Go to [CodeFuser Repository](https://github.com/tahamucasiroglu/CodeFuser)
2. Click "Code" → "Download ZIP"
3. Extract and navigate to folder

#### Step 3: Install Dependencies
```bash
# Install required packages
pip install -r requirements.txt

# If you get permission errors on macOS/Linux:
pip3 install --user -r requirements.txt
```

#### Step 4: Run Application
```bash
# Start CodeFuser
python main.py

# On some systems:
python3 main.py
```

### 📦 Dependencies Installed
```
tkinter (GUI framework)
Pillow>=8.0.0 (Image processing)
python-docx>=0.8.11 (DOCX export)
reportlab>=3.6.0 (PDF export)
```

### 🔧 Troubleshooting Python Installation

#### "Python not found" or "pip not found"
```bash
# Windows - Add to PATH
setx PATH "%PATH%;C:\Python39;C:\Python39\Scripts"

# macOS/Linux - Add to shell profile
echo 'export PATH="/usr/local/bin/python3:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

#### "ModuleNotFoundError: No module named 'tkinter'"
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# CentOS/RHEL
sudo yum install tkinter

# macOS (Homebrew)
brew install python-tk
```

#### "Permission denied" errors
```bash
# Use --user flag
pip install --user -r requirements.txt

# Or use virtual environment (recommended)
python -m venv codefuser_env
source codefuser_env/bin/activate  # Linux/macOS
# codefuser_env\Scripts\activate  # Windows
pip install -r requirements.txt
```

## 🆚 Method 3: VSCode Extension

### ✨ Advantages
- **Integrated workflow** - Use directly in VSCode
- **Context-aware** - Works with current project
- **Quick export** - Right-click integration
- **Familiar interface** - VSCode commands

### 📋 System Requirements
- Visual Studio Code 1.70+
- Node.js 16+ (for development)
- CodeFuser Python installation (dependency)

### 🚀 Installation Steps

#### Step 1: Install Prerequisites
1. **Install VSCode**: Download from [code.visualstudio.com](https://code.visualstudio.com)
2. **Install CodeFuser Python**: Follow [Method 2](#-method-2-python-source) above

#### Step 2: Build Extension (Temporary - Until Marketplace)
```bash
# Navigate to extension directory
cd vscode-extension

# Install dependencies
npm install

# Compile TypeScript
npm run compile

# Package extension
npm install -g vsce
vsce package

# Install the generated .vsix file
# In VSCode: Ctrl+Shift+P → "Install from VSIX"
```

#### Step 3: Use Extension
**Quick Export:**
1. Right-click any folder in VSCode Explorer
2. Select "CodeFuser: Quick Export Selected Files"
3. Follow the prompts

**Command Palette:**
1. Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS)
2. Type "CodeFuser"
3. Choose from available commands

### 🔧 VSCode Extension Commands
```
CodeFuser: Quick Export Selected Files
CodeFuser: Open Configuration
CodeFuser: Export Current Workspace
CodeFuser: Set Custom Template
```

## 🏗️ Building Standalone EXE (Advanced)

### For Developers Who Want to Create Their Own EXE

#### Prerequisites
```bash
pip install pyinstaller
```

#### Build Process
```bash
# Ensure you're in the CodeFuser directory
cd CodeFuser

# Run the build script
python build_exe.py
```

#### Build Output
```
CodeFuser_Portable/
├── CodeFuser.exe (Generated executable)
├── OKUBENI.txt (Turkish README)
├── README.txt (English README)
└── BAŞLANGIÇ - QUICK START.txt (Quick start)
```

### 🔧 Build Troubleshooting

#### "PyInstaller not found"
```bash
pip install pyinstaller>=4.10
```

#### "Missing modules" in EXE
```bash
# Edit build_exe.py to add missing modules to hiddenimports
```

#### Large EXE size
```bash
# This is normal - EXE includes:
# - Python interpreter
# - All dependencies
# - GUI libraries
# - Export libraries
```

## 🌐 Platform-Specific Notes

### Windows
- **Antivirus**: May flag new EXE files - add exceptions
- **Permissions**: Run as administrator if file access issues
- **Fonts**: Uses system fonts for PDF generation

### macOS
- **Gatekeeper**: May block unsigned applications
- **Homebrew**: Recommended for Python installation
- **Tkinter**: May require additional installation steps

### Linux
- **Package managers**: Use distribution-specific commands
- **Display server**: Requires X11 or Wayland
- **Fonts**: Install additional fonts for PDF export

## 🔄 Updating CodeFuser

### Standalone EXE
1. Download new version from Releases
2. Extract to replace old version
3. Settings and templates are preserved

### Python Source
```bash
# Git method
git pull origin main
pip install -r requirements.txt

# ZIP method
# Download new ZIP, extract, reinstall dependencies
```

### VSCode Extension
```bash
# Rebuild and reinstall
cd vscode-extension
npm run compile
vsce package
# Install new .vsix file
```

## 🆘 Getting Help

If you encounter issues during installation:

1. **Check the [Troubleshooting Guide](Troubleshooting-EN)**
2. **Search [GitHub Issues](https://github.com/tahamucasiroglu/CodeFuser/issues)**
3. **Create a new issue** with:
   - Your operating system
   - Installation method used
   - Complete error message
   - Steps to reproduce

---

**Installation complete?** Continue to [Getting Started Guide](Getting-Started-EN) →