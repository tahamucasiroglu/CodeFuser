# 🔧 Troubleshooting Guide

Comprehensive troubleshooting guide for CodeFuser v2.0 - solve common issues and optimize performance.

## 🚨 Common Issues

### Installation and Startup Issues

#### Windows EXE Won't Start
```
Symptoms: Double-click CodeFuser.exe but nothing happens
Solutions:
1. Run as Administrator
2. Check Windows Defender/Antivirus exclusions
3. Verify Windows version compatibility (Windows 10/11)
4. Check for missing Visual C++ Redistributables
5. Run from Command Prompt to see error messages
```

#### Python Version Issues
```bash
# Check Python version
python --version

# Required: Python 3.8+
# If version is too old:
# - Install Python 3.8+ from python.org
# - Update PATH environment variable
# - Restart terminal/command prompt
```

#### Missing Dependencies
```bash
# Install required packages
pip install -r requirements.txt

# If specific package fails:
pip install --upgrade pip
pip install package_name --no-cache-dir

# For development setup:
pip install -e .
```

### Interface and Display Issues

#### Fullscreen Mode Problems
```json
// Fix in user_settings.json
{
  "interface": {
    "fullscreen": false,
    "window_size": "1200x800",
    "remember_window_state": true
  }
}
```

#### Font and Text Display Issues
```json
{
  "interface": {
    "font_size": 10,
    "high_dpi_scaling": "auto",
    "theme": "modern"
  }
}
```

#### Colors Not Displaying Correctly
```json
{
  "interface": {
    "colors": {
      "selected_file": "#fff3a0",
      "selected_with_prompt": "#d4f5d4",
      "prompt_only": "#ffcccc",
      "background": "#f8f9fa"
    }
  }
}
```

### File Tree and Selection Issues

#### Files Not Showing Up
```
Check these settings:
1. Project type selection (Python, JavaScript, etc.)
2. File extension filters
3. Ignore patterns in configuration
4. Maximum file scan limits
5. Hidden file visibility
```

#### File Tree Loading Slowly
```json
{
  "performance": {
    "max_files_scan": 5000,
    "scan_timeout_seconds": 30,
    "parallel_scanning": true,
    "max_worker_threads": 2
  }
}
```

#### Custom Prompts Not Saving
```
Common causes:
1. File permissions in config directory
2. JSON syntax errors in user_settings.json
3. File path encoding issues
4. Insufficient disk space
```

### Export and Output Issues

#### Export Fails with Large Projects
```json
{
  "performance": {
    "memory_limit_mb": 1024,
    "max_export_size_mb": 100
  },
  "output_settings": {
    "chunk_large_files": true,
    "compress_output": true
  }
}
```

#### PDF Export Problems
```json
{
  "format_settings": {
    "pdf": {
      "embed_fonts": true,
      "fallback_font": "Arial",
      "reduce_file_size": true,
      "image_quality": "medium"
    }
  }
}
```

#### HTML Export Not Opening
```
Solutions:
1. Check default browser settings
2. Try different browser
3. Verify HTML file isn't corrupted
4. Check file permissions
5. Test in private/incognito mode
```

#### DOCX Export Issues
```json
{
  "format_settings": {
    "docx": {
      "compatibility_mode": "2016",
      "embed_fonts": false,
      "use_fallback_fonts": true
    }
  }
}
```

### Git Integration Issues

#### Git Not Detected
```bash
# Verify Git installation
git --version

# Check Git in PATH
echo $PATH  # Linux/Mac
echo %PATH%  # Windows

# Initialize Git repo if needed
git init
```

#### Git Status Not Updating
```json
{
  "git_integration": {
    "refresh_interval_seconds": 5,
    "auto_detect_repository": true,
    "cache_git_status": false
  }
}
```

#### Large Repository Performance
```json
{
  "git_integration": {
    "shallow_analysis": true,
    "max_files_analyze": 1000,
    "skip_binary_files": true,
    "use_git_filters": true
  }
}
```

### Template and Prompt Issues

#### Templates Not Loading
```
Check:
1. Template directory exists
2. JSON syntax is valid
3. File permissions
4. Template file encoding (UTF-8)
5. Required template fields present
```

#### Variable Substitution Not Working
```json
// Verify variable syntax in templates
{
  "prompt": "Analyze {{PROJECT_NAME}} for security issues",
  "variables": {
    "PROJECT_NAME": {
      "type": "string",
      "default": "{{AUTO_DETECT}}"
    }
  }
}
```

#### Custom Template Errors
```bash
# Validate template JSON
python -m json.tool template.json

# Check for common issues:
# - Missing required fields
# - Invalid variable references
# - Circular dependencies
```

## ⚡ Performance Issues

### Slow File Scanning

#### Large Project Optimization
```json
{
  "performance": {
    "max_files_scan": 5000,
    "parallel_scanning": true,
    "max_worker_threads": 4,
    "exclude_large_files": true,
    "max_file_size_mb": 5
  }
}
```

#### Network Drive Performance
```json
{
  "performance": {
    "network_timeout_seconds": 60,
    "cache_network_files": true,
    "batch_file_operations": true
  }
}
```

### Memory Usage Issues

#### High Memory Consumption
```json
{
  "performance": {
    "memory_limit_mb": 512,
    "garbage_collection_interval": 100,
    "clear_cache_threshold_mb": 200
  }
}
```

#### Memory Leaks
```
Solutions:
1. Restart CodeFuser periodically
2. Clear cache manually
3. Reduce concurrent operations
4. Update to latest version
```

### UI Responsiveness

#### Slow Interface Updates
```json
{
  "performance": {
    "ui_update_interval_ms": 200,
    "defer_non_critical_updates": true,
    "batch_ui_updates": true
  }
}
```

#### Freezing During Operations
```json
{
  "performance": {
    "async_operations": true,
    "show_progress_bars": true,
    "allow_operation_cancellation": true
  }
}
```

## 🔒 Security and Privacy Issues

### File Access Problems

#### Permission Denied Errors
```bash
# Windows: Run as Administrator
# Linux/Mac: Check file permissions
chmod 755 /path/to/codefuser
chmod 644 /path/to/config/files
```

#### Antivirus False Positives
```
Solutions:
1. Add CodeFuser to antivirus exclusions
2. Use Windows Defender exclusions
3. Temporarily disable real-time protection
4. Submit false positive report to AV vendor
```

### Data Privacy Concerns

#### Sensitive File Detection
```json
{
  "security": {
    "scan_for_secrets": true,
    "secret_patterns": [
      "password", "api_key", "secret", "token"
    ],
    "exclude_suspicious_files": true,
    "warn_before_export": true
  }
}
```

#### Local Data Storage
```json
{
  "privacy": {
    "store_file_paths_only": true,
    "clear_cache_on_exit": true,
    "encrypt_sensitive_data": true,
    "log_level": "warning"
  }
}
```

## 🌐 Language and Localization Issues

### Language Not Switching

#### Locale Configuration
```json
{
  "interface": {
    "language": "tr",  // or "en"
    "auto_detect_language": false,
    "fallback_language": "en"
  }
}
```

#### Missing Translations
```
Check:
1. locales/tr.json exists
2. File encoding is UTF-8
3. JSON syntax is valid
4. All required keys present
```

### Text Encoding Issues

#### Special Characters Not Displaying
```json
{
  "output_settings": {
    "encoding": "utf-8",
    "normalize_unicode": true,
    "handle_special_chars": true
  }
}
```

## 🔄 Configuration Issues

### Settings Not Saving

#### Configuration File Issues
```bash
# Check file permissions
ls -la config/user_settings.json

# Verify JSON syntax
python -c "import json; json.load(open('config/user_settings.json'))"

# Reset to defaults if corrupted
mv user_settings.json user_settings.json.backup
# Restart CodeFuser to regenerate defaults
```

#### Invalid Configuration Values
```json
// Common validation issues:
{
  "window_size": "1200x800",    // Must be string format
  "max_files_scan": 10000,      // Must be integer
  "enabled": true,              // Must be boolean
  "file_extensions": [".py"]    // Must be array
}
```

### Team Configuration Conflicts

#### Shared Settings Issues
```json
{
  "team": {
    "shared_config_location": "//server/shared/config.json",
    "allow_local_overrides": true,
    "conflict_resolution": "local_wins"
  }
}
```

## 🧪 Development and Advanced Issues

### Plugin Development

#### Plugin Not Loading
```python
# Check plugin structure
plugins/
├── __init__.py
├── my_plugin.py
└── manifest.json

# Verify manifest.json
{
  "name": "My Plugin",
  "version": "1.0.0",
  "entry_point": "my_plugin.main"
}
```

#### API Integration Issues
```python
# Debug API calls
import logging
logging.basicConfig(level=logging.DEBUG)

# Check API endpoints
try:
    response = api_call()
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")
```

### Custom Export Formats

#### Export Format Development
```python
class CustomExporter:
    def __init__(self):
        self.format_name = "custom"
        
    def export(self, data, output_path):
        try:
            # Implementation here
            pass
        except Exception as e:
            logging.error(f"Export failed: {e}")
            raise
```

## 🔍 Debugging Tools

### Enable Debug Mode

#### Verbose Logging
```json
{
  "debug": {
    "enabled": true,
    "log_level": "DEBUG",
    "log_file": "codefuser_debug.log",
    "include_stack_traces": true
  }
}
```

#### Performance Profiling
```json
{
  "profiling": {
    "enabled": true,
    "profile_file_operations": true,
    "profile_ui_updates": true,
    "profile_exports": true
  }
}
```

### Log Analysis

#### Common Log Patterns
```bash
# Find errors in logs
grep "ERROR" codefuser.log

# Find performance issues
grep "SLOW" codefuser.log

# Find memory issues
grep "MEMORY" codefuser.log
```

#### Log Location
```
Windows EXE: CodeFuser_Portable/logs/
Python: ./logs/
Debug Mode: ./debug/
```

## 📞 Getting Help

### Information to Collect

#### System Information
```bash
# Operating System
uname -a  # Linux/Mac
systeminfo  # Windows

# Python version
python --version

# CodeFuser version
# Check About dialog or --version flag
```

#### Configuration Export
```json
// Export current configuration for support
{
  "system_info": "...",
  "configuration": "...",
  "recent_errors": "...",
  "performance_metrics": "..."
}
```

### Error Reporting

#### Bug Report Template
```markdown
**Environment:**
- OS: Windows 10/11, macOS, Linux
- CodeFuser Version: 2.0.x
- Python Version: 3.x.x

**Issue Description:**
- What were you trying to do?
- What happened instead?
- Error messages (if any)

**Steps to Reproduce:**
1. Step one
2. Step two
3. Step three

**Configuration:**
- Attach user_settings.json
- Mention any custom templates/plugins

**Logs:**
- Attach relevant log files
- Include debug output if available
```

### Community Resources

#### Documentation
- [GitHub Wiki](https://github.com/tahamucasiroglu/CodeFuser/wiki)
- [Configuration Guide](Configuration-EN)
- [Templates Guide](Templates-Guide-EN)

#### Support Channels
- [GitHub Issues](https://github.com/tahamucasiroglu/CodeFuser/issues)
- [Discussions](https://github.com/tahamucasiroglu/CodeFuser/discussions)

## 🚀 Performance Optimization

### Best Practices

#### Project Setup
```
✅ Do:
- Use appropriate project type filters
- Configure ignore patterns properly
- Set reasonable file size limits
- Enable Git integration for relevant projects

❌ Don't:
- Scan entire system drives
- Include massive binary files
- Use overly complex filter patterns
- Run on network drives without caching
```

#### Export Optimization
```
✅ Do:
- Choose appropriate export format
- Use file-specific prompts strategically
- Test with small projects first
- Monitor memory usage

❌ Don't:
- Export thousands of files at once
- Use high DPI images in exports
- Export to network locations directly
- Ignore export format limitations
```

---

**Still having issues?** Check the [Development Guide](Development-EN) for advanced troubleshooting or [report a bug](https://github.com/tahamucasiroglu/CodeFuser/issues) on GitHub!

*Continue to [Development Guide](Development-EN) for contributor information and advanced customization →*