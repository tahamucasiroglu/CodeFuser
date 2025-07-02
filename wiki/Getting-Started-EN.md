# 📖 Getting Started with CodeFuser v2.0

Welcome to CodeFuser! This guide will help you get up and running with the most powerful AI-driven code aggregation tool.

## 🚀 Quick Start (5 Minutes)

### Step 1: Download and Install
Choose your preferred installation method:

#### 📥 Option A: Standalone EXE (Recommended)
1. Go to [Releases](https://github.com/tahamucasiroglu/CodeFuser/releases/latest)
2. Download `CodeFuser_Portable.zip`
3. Extract the ZIP file
4. Double-click `CodeFuser.exe` - Done! ✨

#### 🐍 Option B: Python Source
```bash
git clone https://github.com/tahamucasiroglu/CodeFuser.git
cd CodeFuser
pip install -r requirements.txt
python main.py
```

### Step 2: First Project
1. **Select Folder**: Click "Browse" and choose your project directory
2. **Scan Files**: Click "Scan Files" to discover all code files
3. **Select Files**: Check the boxes next to files you want to include
4. **Choose Template**: Select "16x Prompt" for AI analysis
5. **Process**: Click "Start Process" and select output format

## 🎯 Understanding File-Specific Prompts (v2.0 Feature)

### What Are File-Specific Prompts?
Instead of giving the same instruction to all files, you can now provide targeted instructions for each file.

### How to Use Them
1. **Find the Icon**: Look for 📄 icons next to each file
2. **Click to Customize**: Click the 📄 icon to open the prompt dialog
3. **Write Instructions**: Add specific instructions for that file
4. **See Visual Feedback**: Files with prompts show 📝✨ and colored backgrounds

### Color Coding System
- 🟢 **Green Background**: File is selected AND has custom prompt (Perfect!)
- 🟡 **Yellow Background**: File is selected but no custom prompt (Good)
- 🔴 **Red Background**: File has custom prompt but NOT selected (Warning!)

## 📊 Understanding the Interface

### Main Window Components
1. **Toolbar**: Browse, scan, settings, and language options
2. **File Tree**: Shows all discovered files with checkboxes
3. **Template Area**: Choose from pre-built templates or create custom
4. **Prompt Editor**: Write your main instructions
5. **Export Options**: Select output format and location
6. **Status Bar**: Shows progress and file counts

### File Tree Features
- **Search Box**: Filter files by name (top of file tree)
- **Select All/None**: Bulk selection buttons
- **File Counter**: Shows "X / Y files selected • Z with prompts"
- **Remove Selected**: Remove unwanted files from list

## 🎨 Your First AI Analysis

### Example: Security Review
1. **Select Python files** in your web application
2. **Add file-specific prompts**:
   - `auth.py` → "Focus on authentication vulnerabilities"
   - `api.py` → "Check for SQL injection and XSS"
   - `utils.py` → "Review input validation functions"
3. **Choose "Code Review" template**
4. **Export as HTML** for easy reading
5. **Copy to your AI tool** (ChatGPT, Claude, etc.)

### Example: Performance Analysis
1. **Select core application files**
2. **Add targeted prompts**:
   - `database.py` → "Analyze query efficiency and N+1 problems"
   - `cache.py` → "Review caching strategy effectiveness"
   - `main.py` → "Check for bottlenecks in main execution flow"
3. **Use "16x Prompt" template**
4. **Export as TXT** for AI input

## ⚡ Pro Tips for Beginners

### ✅ Do This
- **Start small**: Begin with 3-5 important files
- **Be specific**: Write clear, actionable prompts for each file
- **Use templates**: They provide excellent starting points
- **Check colors**: Green files = optimal setup
- **Export as HTML**: Best for viewing and copying

### ❌ Avoid This
- **Don't select everything**: Quality over quantity
- **Don't use generic prompts**: Be specific for each file
- **Don't ignore red files**: They have unused prompts
- **Don't skip templates**: They save time and improve results

## 🔧 Basic Configuration

### Language Settings
- **Switch Languages**: Settings → Language → Turkish/English
- **Restart Required**: Some changes need app restart

### Default Preferences
- **Output Format**: Choose your preferred export format
- **File Filters**: Set up common exclusions (tests, docs, etc.)
- **Template**: Set your most-used template as default

## 🆘 Need Help?

### Common First-Time Issues
1. **"No files found"**: Check if folder has code files, adjust filters
2. **"Export failed"**: Check write permissions, available disk space
3. **"Template error"**: Ensure template has valid placeholder syntax

### Getting Support
- **📖 Check the Wiki**: Most questions are answered here
- **🐛 Report Issues**: [GitHub Issues](https://github.com/tahamucasiroglu/CodeFuser/issues)
- **💡 Ask Questions**: [GitHub Discussions](https://github.com/tahamucasiroglu/CodeFuser/discussions)

## 🎓 Next Steps

Once you're comfortable with the basics:

1. **[🎯 Master File-Specific Prompts](File-Specific-Prompts-EN)** - Deep dive into v2.0's killer feature
2. **[🎨 Learn Templates](Templates-Guide-EN)** - Create and customize templates
3. **[🔍 Explore Smart Filters](Smart-Filters-EN)** - Advanced file filtering
4. **[🐙 Use Git Integration](Git-Integration-EN)** - Work with version control

---

**Ready to fuse your code with AI precision?** 🚀

*Continue to [File-Specific Prompts Guide](File-Specific-Prompts-EN) →*