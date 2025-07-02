# 📊 Export Formats Guide

Complete guide to CodeFuser's four professional export formats and their optimization for different use cases.

## 🎯 Format Overview

| Format | Best For | File Size | AI Tools | Professional Use |
|--------|----------|-----------|----------|------------------|
| **HTML** | Viewing, AI copying | Medium | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **TXT** | Simple AI input | Small | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| **DOCX** | Documentation, sharing | Large | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **PDF** | Printing, archiving | Large | ⭐⭐ | ⭐⭐⭐⭐⭐ |

## 📄 TXT Format

### ✨ Best For
- **AI Tool Input**: Direct copy-paste to ChatGPT, Claude, etc.
- **Simple Processing**: Text analysis tools
- **Quick Review**: Fast reading without formatting
- **Version Control**: Clean diffs in Git

### 🔧 Structure
```
# CodeFuser Output
# Generated: 2024-01-15 14:30:25
# Total Files: 5

================================================================================

[PROMPT]
Analyze this codebase for security vulnerabilities and suggest improvements.

--------------------------------------------------------------------------------

=== FILE: src/auth.py ===

[CUSTOM PROMPT FOR THIS FILE]
Focus on authentication logic and session management security

[CONTENT]
def authenticate_user(username, password):
    # Implementation here...

=== FILE: src/api.py ===

[CONTENT]
class APIHandler:
    # Implementation here...
```

### ⚙️ Configuration Options
```json
{
  "format_settings": {
    "txt": {
      "line_ending": "auto",        // "windows", "unix", "auto"
      "encoding": "utf-8",          // "utf-8", "ascii", "latin1"
      "include_separators": true,   // File separators
      "separator_length": 80,       // Length of separator lines
      "include_timestamps": true,   // Generation metadata
      "include_file_stats": true    // File count and sizes
    }
  }
}
```

### 💡 Pro Tips
- **Perfect for AI**: No formatting distractions
- **Lightweight**: Smallest file size
- **Fast Loading**: Opens instantly in any text editor
- **Search Friendly**: Easy to search across content

## 🌐 HTML Format

### ✨ Best For
- **Interactive Viewing**: Browser-based review with navigation
- **AI Tool Integration**: Easy copying with syntax highlighting
- **Team Sharing**: Send via email or web hosting
- **Code Presentation**: Professional code showcasing

### 🎨 Features
- **Syntax Highlighting**: Prism.js integration with 100+ languages
- **Copy Buttons**: One-click copying for each file
- **Table of Contents**: Quick navigation between files
- **Statistics Dashboard**: File counts, sizes, languages
- **Responsive Design**: Works on desktop, tablet, mobile
- **Dark Theme**: Professional dark color scheme

### 🔧 Structure
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>CodeFuser Output</title>
    <!-- Prism.js for syntax highlighting -->
    <!-- Modern CSS styling -->
</head>
<body>
    <!-- Header with project info -->
    <div class="header">
        <h1>🚀 CodeFuser Output</h1>
        <div class="meta">Generated on 2024-01-15</div>
    </div>
    
    <!-- Statistics dashboard -->
    <div class="stats">
        <div class="stat-item">
            <div class="stat-value">5</div>
            <div class="stat-label">Total Files</div>
        </div>
    </div>
    
    <!-- Prompt section -->
    <div class="prompt-section">
        <h2>🎯 Prompt Instructions</h2>
        <div class="prompt-content">Your prompt here...</div>
    </div>
    
    <!-- Table of contents -->
    <div class="toc">
        <h3>📋 Table of Contents</h3>
        <ul>
            <li><a href="#file1">src/auth.py</a></li>
        </ul>
    </div>
    
    <!-- File contents with syntax highlighting -->
    <div class="file-section" id="file1">
        <div class="file-header">
            <div class="file-path">📄 src/auth.py</div>
        </div>
        <!-- Custom prompt for this file -->
        <div class="custom-prompt">
            <h4>🎯 Custom Prompt for this file:</h4>
            <div>Focus on authentication security...</div>
        </div>
        <div class="file-content">
            <pre><code class="language-python">
def authenticate_user(username, password):
    # Code with syntax highlighting
            </code></pre>
        </div>
    </div>
</body>
</html>
```

### ⚙️ Configuration Options
```json
{
  "format_settings": {
    "html": {
      "syntax_highlighting": true,      // Enable Prism.js highlighting
      "theme": "tomorrow-night",        // Syntax theme
      "include_css": true,             // Embed CSS in HTML
      "copy_button": true,             // Add copy buttons
      "toc_navigation": true,          // Table of contents
      "responsive_design": true,       // Mobile-friendly
      "include_statistics": true,      // Stats dashboard
      "custom_css_file": null,         // Path to custom CSS
      "javascript_enabled": true,      // Interactive features
      "print_styles": true            // Print-friendly CSS
    }
  }
}
```

### 🎨 Customization Examples

#### Custom Color Scheme
```css
/* Add to custom CSS file */
.header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.file-section {
    border-left: 4px solid #667eea;
}

.custom-prompt {
    background: #e8f4fd;
    border: 2px solid #2196f3;
}
```

#### Dark Mode Override
```css
body {
    background: #1a1a1a;
    color: #e0e0e0;
}

.file-header {
    background: #2d2d2d;
    border-bottom: 1px solid #404040;
}
```

### 💡 Pro Tips
- **Best for AI Tools**: Syntax highlighting helps identify code structure
- **Copy Buttons**: Click to copy entire files or sections
- **Browser Bookmarks**: Save for quick reference
- **Team Sharing**: Host on internal servers or email

## 📝 DOCX Format

### ✨ Best For
- **Formal Documentation**: Corporate reports and documentation
- **Team Collaboration**: Comments and track changes in Word
- **Professional Sharing**: Client presentations and reviews
- **Template Integration**: Company document templates

### 🎨 Features
- **Professional Formatting**: Headers, styles, page breaks
- **Table of Contents**: Auto-generated with page numbers
- **Custom Prompt Styling**: Orange highlighting for file-specific prompts
- **Code Formatting**: Monospace font with proper indentation
- **Metadata**: Document properties and statistics
- **Print Ready**: Proper margins and page layout

### 🔧 Structure
```
CodeFuser Output
Generated: 2024-01-15 14:30:25
Total Files: 5

[PROMPT]
Your main prompt text here...
────────────────────────────────────────

📄 src/auth.py

🎯 Custom Prompt for this file:
Focus on authentication logic and session management security
────────────────────────

[CONTENT]
def authenticate_user(username, password):
    """Authenticate user credentials."""
    # Implementation code...

[Page Break]

📄 src/api.py
...
```

### ⚙️ Configuration Options
```json
{
  "format_settings": {
    "docx": {
      "font_family": "Courier New",        // Code font
      "font_size": 10,                     // Base font size
      "include_toc": true,                 // Table of contents
      "page_breaks_between_files": true,   // New page per file
      "header_footer": true,               // Page headers/footers
      "line_spacing": 1.15,               // Line spacing
      "margin_inches": 1.0,               // Page margins
      "highlight_prompts": true,           // Orange prompt styling
      "include_metadata": true,            // Document properties
      "watermark": null                    // Optional watermark text
    }
  }
}
```

### 📋 Template Integration
```json
{
  "docx_template": {
    "company_template": "templates/company_template.docx",
    "header_text": "Code Review - Confidential",
    "footer_text": "Generated by CodeFuser v2.0",
    "logo_path": "assets/company_logo.png",
    "custom_styles": {
      "code_style": "CodeBlock",
      "prompt_style": "PromptHighlight"
    }
  }
}
```

### 💡 Pro Tips
- **Track Changes**: Enable in Word for collaborative review
- **Comments**: Add review comments directly in Word
- **Version Control**: Save as different versions for iterations
- **PDF Export**: Convert to PDF from Word for final distribution

## 📄 PDF Format

### ✨ Best For
- **Archival**: Long-term storage and preservation
- **Printing**: High-quality printed documentation
- **Security**: Password protection and digital signatures
- **Distribution**: Consistent viewing across platforms

### 🎨 Features
- **Professional Layout**: Proper typography and spacing
- **Page Numbers**: Automatic pagination
- **Consistent Rendering**: Same appearance on all devices
- **Bookmarks**: PDF navigation bookmarks
- **Metadata**: PDF properties and search indexing
- **Print Optimization**: Proper margins and page breaks

### 🔧 Structure
```
┌─────────────────────────────────────────┐
│              CodeFuser Output            │
│         Generated: 2024-01-15           │
│             Total Files: 5              │
└─────────────────────────────────────────┘

[PROMPT]
Your main prompt text appears here with proper
formatting and line wrapping for readability.

────────────────────────────────────────────

📄 src/auth.py

[CONTENT]
def authenticate_user(username, password):
    """Authenticate user credentials."""
    # Code is properly formatted with
    # monospace font and indentation
                                    Page 1
┌─────────────────────────────────────────┐
│                                         │
│              [New File]                 │
│                                         │
└─────────────────────────────────────────┘
```

### ⚙️ Configuration Options
```json
{
  "format_settings": {
    "pdf": {
      "page_size": "A4",                  // "A4", "Letter", "Legal"
      "orientation": "portrait",          // "portrait", "landscape"
      "font_size": 9,                    // Base font size
      "line_height": 1.2,                // Line spacing
      "margins": {                       // Page margins in inches
        "top": 1.0,
        "bottom": 1.0,
        "left": 1.0,
        "right": 1.0
      },
      "include_page_numbers": true,       // Page numbering
      "include_bookmarks": true,          // PDF navigation
      "syntax_highlighting": false,       // Keep false for better printing
      "page_breaks_between_files": true,  // New page per file
      "header_text": "CodeFuser Export",  // Page header
      "footer_text": "Confidential",     // Page footer
      "watermark": null,                 // Optional watermark
      "security": {                      // PDF security options
        "password_protect": false,
        "allow_printing": true,
        "allow_copying": true,
        "allow_editing": false
      }
    }
  }
}
```

### 🔒 Security Features
```json
{
  "pdf_security": {
    "owner_password": "admin_password",
    "user_password": "view_password",
    "permissions": {
      "print": "high_quality",          // "none", "low_quality", "high_quality"
      "copy": false,                    // Allow text copying
      "edit": false,                    // Allow document editing
      "annotate": true,                 // Allow comments/annotations
      "fill_forms": false,              // Allow form filling
      "extract": false,                 // Allow content extraction
      "assemble": false                 // Allow page assembly
    }
  }
}
```

### 💡 Pro Tips
- **Print Preview**: Always check PDF before printing
- **Font Embedding**: Ensures consistent appearance
- **Compression**: Smaller file sizes with quality preservation
- **Bookmarks**: Use for easy navigation in large documents

## 🚀 Advanced Export Features

### File-Specific Prompt Integration

All formats include file-specific prompts:

#### TXT Format
```
[CUSTOM PROMPT FOR THIS FILE]
Analyze authentication mechanisms for security vulnerabilities
```

#### HTML Format
```html
<div class="custom-prompt">
    <h4>🎯 Custom Prompt for this file:</h4>
    <div class="custom-prompt-content">
        Analyze authentication mechanisms for security vulnerabilities
    </div>
</div>
```

#### DOCX Format
- Orange highlighted text box
- Distinct styling from main content
- Proper spacing and formatting

#### PDF Format
- Separate formatted section
- Consistent typography
- Clear visual separation

### Batch Export
```json
{
  "batch_export": {
    "enabled": true,
    "formats": ["html", "docx", "pdf"],
    "output_directory": "exports/",
    "filename_template": "{project}_{format}_{timestamp}"
  }
}
```

### Export Automation
```json
{
  "automation": {
    "auto_export_on_scan": false,
    "scheduled_exports": {
      "enabled": false,
      "frequency": "daily",
      "time": "18:00",
      "formats": ["html"]
    },
    "git_hook_export": {
      "enabled": false,
      "on_commit": true,
      "on_push": false
    }
  }
}
```

## 📊 Format Comparison

### File Sizes (Example 50 files, 10MB total code)
- **TXT**: 10.2 MB (minimal overhead)
- **HTML**: 12.5 MB (CSS + JavaScript)
- **DOCX**: 15.8 MB (XML structure + formatting)
- **PDF**: 18.3 MB (embedded fonts + layout)

### Generation Speed
- **TXT**: ~1 second (fastest)
- **HTML**: ~3 seconds (syntax highlighting)
- **DOCX**: ~5 seconds (document structure)
- **PDF**: ~8 seconds (layout rendering)

### AI Tool Compatibility
- **TXT**: Perfect - direct copy-paste
- **HTML**: Excellent - copy buttons + highlighting
- **DOCX**: Good - can copy from Word
- **PDF**: Limited - copy may lose formatting

## 🔧 Troubleshooting Export Issues

### Common Problems

#### Large File Export Fails
```json
{
  "performance": {
    "max_export_size_mb": 100,
    "chunk_large_files": true,
    "memory_limit_mb": 512
  }
}
```

#### Font Issues in PDF
```json
{
  "pdf_fonts": {
    "embed_fonts": true,
    "fallback_font": "Arial",
    "code_font": "Courier New",
    "custom_fonts_path": "fonts/"
  }
}
```

#### HTML Not Displaying Correctly
- Check browser compatibility
- Verify CSS loading
- Test JavaScript features
- Validate HTML structure

#### DOCX Formatting Issues
- Check Word version compatibility
- Verify template structure
- Test custom styles
- Review font availability

---

**Ready to export?** Choose the format that best fits your workflow and start creating professional code documentation! 

*Continue to [Templates Guide](Templates-Guide-EN) to learn about combining templates with export formats →*