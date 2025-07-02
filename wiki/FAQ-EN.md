# ❓ Frequently Asked Questions

## 🚀 General Questions

### What is CodeFuser?
CodeFuser is an AI-powered code aggregation tool that combines project files into AI-ready outputs with file-specific custom prompts, advanced filtering, and multiple export formats.

### What's new in v2.0?
The revolutionary **file-specific custom prompts** feature allows you to add individual instructions to each file, making AI analysis more targeted and effective. Plus standalone Windows EXE, enhanced UI, and improved color coding.

### Is CodeFuser free?
Yes! CodeFuser is completely free and open-source under the MIT License.

### What platforms does CodeFuser support?
- **Windows**: Standalone EXE (recommended) or Python source
- **macOS**: Python source
- **Linux**: Python source
- **VSCode**: Extension for all platforms

## 🎯 File-Specific Prompts

### How do file-specific prompts work?
Click the 📄 icon next to any file to add custom instructions for that specific file. These prompts are included in the export alongside the file content, giving AI tools targeted guidance for each component.

### What's the difference between general and file-specific prompts?
- **General prompt**: Applied to the entire project (from templates or custom input)
- **File-specific prompt**: Applied only to individual files for targeted analysis

### Can I use both general and file-specific prompts?
Yes! They work together. The general prompt provides overall context, while file-specific prompts give detailed instructions for each file.

### What does the color coding mean?
- 🟢 **Green**: File is selected AND has custom prompt (optimal)
- 🟡 **Yellow**: File is selected but no custom prompt (good)
- 🔴 **Red**: File has custom prompt but NOT selected (warning - prompt won't be used)

### How long should file-specific prompts be?
Keep them under 500 characters for best results. The dialog shows character count with color coding (green < 500, orange < 1000, red > 1000).

### Can I save and reuse file-specific prompts?
Currently, prompts are saved per session. Prompt templates and cross-project reuse are planned for v2.1.

## 🔧 Installation & Setup

### Which installation method should I choose?
- **Beginners/Windows users**: Standalone EXE
- **Developers**: Python source
- **VSCode users**: VSCode extension

### Why does Windows Defender warn about the EXE?
This is normal for new executable files. CodeFuser is completely safe - the warning appears because the EXE is not yet digitally signed. Click "More info" → "Run anyway".

### Do I need Python for the standalone EXE?
No! The standalone EXE includes everything needed to run CodeFuser without any dependencies.

### Can I run CodeFuser on older Windows versions?
The standalone EXE requires Windows 10 or 11. For older versions, use the Python source method.

### Why is the EXE file so large (22MB)?
The EXE includes the Python interpreter, GUI libraries, export libraries (PDF, DOCX), and all dependencies to ensure it works without installation.

## 📊 Export & Output

### What export formats are supported?
- **TXT**: Simple text with separators
- **HTML**: Syntax-highlighted web page with copy functionality
- **DOCX**: Professional Word document
- **PDF**: Print-ready document with proper formatting

### Which format is best for AI tools?
- **HTML**: Best for viewing and copying to AI tools
- **TXT**: Simplest format, works with all AI tools
- **DOCX**: Good for formal documentation and team sharing

### How are file-specific prompts included in exports?
Each file's custom prompt appears in a clearly marked section before the file content in all export formats.

### Can I customize export formatting?
Basic customization is available through configuration files. Advanced formatting options are planned for future versions.

### Where are exported files saved?
By default, exports are saved to your Documents folder. You can choose a different location during the export process.

## 🔍 Filtering & Selection

### How do smart filters work?
Smart filters automatically categorize files based on content analysis, file types, Git status, and code patterns. Access them through the "Advanced Filters" section.

### What Git integration features are available?
- Show only modified files
- Filter by Git status (staged, unstaged, untracked)
- Compare branches
- Exclude ignored files

### Can I save filter configurations?
Filter preferences are saved automatically. Custom filter sets are planned for future versions.

### How do I exclude test files?
Use Smart Filters → "Exclude test files" to automatically filter out common test file patterns.

### Why don't I see all my files?
Check your file filters and search box. By default, some file types (like binaries) are excluded for better performance.

## 🎨 Templates & Customization

### What templates are included?
- **16x Prompt**: Popular AI analysis format
- **Claude Project**: Optimized for Claude AI
- **Code Review**: Structured code review format
- **Documentation**: Auto-documentation generation
- **Cursor Rules**: IDE-specific configurations

### Can I create custom templates?
Yes! Templates are JSON files with variable substitution. See the [Templates Guide](Templates-Guide-EN) for details.

### How do I share templates with my team?
Copy template JSON files to share. Team template management is planned for v2.2.

### Can I modify existing templates?
Yes, templates are stored in the `templates/` folder and can be edited directly.

## 🌍 Language & Localization

### What languages are supported?
Currently Turkish and English with full interface translation.

### How do I change the language?
Settings → Language → Select your preferred language. Restart may be required.

### Can I add a new language?
Yes! Language files are in the `locales/` folder. See the [Development Guide](Development-EN) for contribution instructions.

## 🐛 Troubleshooting

### CodeFuser won't start
1. **Standalone EXE**: Check Windows Defender, run as administrator
2. **Python source**: Verify Python installation and dependencies
3. **Check system requirements** and available memory

### Files aren't being detected
1. Verify the folder contains code files
2. Check file filters and exclusions
3. Ensure proper folder permissions

### Export fails
1. Check available disk space
2. Verify write permissions to output folder
3. Try a different export format

### UI appears corrupted or misaligned
1. Check display scaling settings
2. Try different screen resolution
3. Restart the application

### Performance is slow
1. Reduce number of selected files
2. Use smart filters to exclude unnecessary files
3. Close other memory-intensive applications

## 💡 Best Practices

### How many files should I select?
Start with 5-10 important files. Quality over quantity gives better AI analysis results.

### What makes a good file-specific prompt?
- Be specific and actionable
- Focus on the file's primary purpose
- Include expected output type
- Use technical terminology relevant to the code

### How do I organize large projects?
1. Use Git filters to focus on recent changes
2. Apply smart filters to exclude tests and dependencies
3. Create multiple exports for different purposes
4. Use file-specific prompts on core files only

### What's the best workflow for AI analysis?
1. Select core application files
2. Add specific prompts to critical components
3. Use appropriate template (16x Prompt for general analysis)
4. Export as HTML for easy AI tool integration
5. Iterate based on AI feedback

## 🔮 Future Features

### What's coming in v2.1?
- Prompt template libraries
- Bulk prompt assignment
- Prompt history and reuse
- Advanced export options

### When will the VSCode extension be in the marketplace?
We're working on marketplace submission. Currently available as a manual install.

### Will there be a web version?
A web interface is planned for v3.0 with real-time collaboration features.

### Can I request features?
Yes! Use [GitHub Discussions](https://github.com/tahamucasiroglu/CodeFuser/discussions) for feature requests.

## 🆘 Still Need Help?

### Community Support
- **GitHub Discussions**: [Ask questions](https://github.com/tahamucasiroglu/CodeFuser/discussions)
- **GitHub Issues**: [Report bugs](https://github.com/tahamucasiroglu/CodeFuser/issues)

### Documentation
- **[Getting Started Guide](Getting-Started-EN)**: Basic usage
- **[File-Specific Prompts Guide](File-Specific-Prompts-EN)**: Master the v2.0 feature
- **[Troubleshooting Guide](Troubleshooting-EN)**: Common issues and solutions

### Before Asking for Help
1. Check this FAQ
2. Search existing GitHub issues
3. Try the basic troubleshooting steps
4. Include system information and error messages in your report

---

**Question not answered here?** Check our [complete documentation](Home) or [ask the community](https://github.com/tahamucasiroglu/CodeFuser/discussions)!