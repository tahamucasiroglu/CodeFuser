# Contributing to CodeFuser

We love your input! We want to make contributing to CodeFuser as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

## Development Process

We use GitHub to host code, to track issues and feature requests, as well as accept pull requests.

### Pull Requests
1. Fork the repo and create your branch from `main`
2. If you've added code that should be tested, add tests
3. If you've changed APIs, update the documentation
4. Ensure the test suite passes
5. Make sure your code lints
6. Issue that pull request!

### Development Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/codefuser.git
cd codefuser

# Install dependencies
pip install -r requirements.txt

# Run tests
python -m pytest tests/

# Run the application
python main.py
```

### VSCode Extension Development

```bash
cd vscode-extension
npm install
npm run compile
npm run watch  # For development
```

## Any contributions you make will be under the MIT Software License
When you submit code changes, your submissions are understood to be under the same [MIT License](LICENSE) that covers the project.

## Report bugs using GitHub's [issue tracker](https://github.com/yourusername/codefuser/issues)

**Great Bug Reports** tend to have:

- A quick summary and/or background
- Steps to reproduce
  - Be specific!
  - Give sample code if you can
- What you expected would happen
- What actually happens
- Notes (possibly including why you think this might be happening, or stuff you tried that didn't work)

## Feature Requests

We love feature requests! Please provide:

- **Is your feature request related to a problem?** A clear description of what the problem is
- **Describe the solution you'd like** A clear description of what you want to happen
- **Describe alternatives you've considered** Any alternative solutions or features you've considered
- **Additional context** Screenshots, mockups, or any other context

## Coding Style

### Python Code
- Follow PEP 8
- Use meaningful variable names
- Add docstrings to functions and classes
- Keep functions small and focused

### TypeScript/JavaScript (VSCode Extension)
- Use TypeScript for type safety
- Follow ESLint rules
- Use meaningful variable names
- Add JSDoc comments for functions

### Example Python Code Style
```python
def scan_files(self, directory: Path, extensions: List[str]) -> List[Dict[str, Any]]:
    """
    Scan directory for files with specified extensions.
    
    Args:
        directory: Path to scan
        extensions: List of file extensions to include
        
    Returns:
        List of file information dictionaries
    """
    files = []
    # Implementation here...
    return files
```

## Code Organization

### Python Structure
```
src/
├── main_window.py          # Main GUI window
├── config_manager.py       # Configuration management
├── file_scanner.py         # File scanning logic
├── output_manager.py       # Export functionality
├── template_engine.py      # Template system
├── git_integration.py      # Git features
├── smart_filters.py        # Advanced filtering
└── ui_components.py        # UI components
```

### Adding New Features

#### New Template
1. Add template to `template_engine.py`
2. Update `get_available_templates()`
3. Add to default templates dictionary
4. Update documentation

#### New Filter
1. Add filter to `smart_filters.py`
2. Update `get_available_filters()`
3. Implement filter logic
4. Add to filter categories

#### New Export Format
1. Create formatter class in `output_manager.py`
2. Inherit from `OutputFormatter`
3. Implement `format_output()` method
4. Register in `OutputManager.__init__()`

## Testing

### Running Tests
```bash
python -m pytest tests/ -v
```

### Writing Tests
- Write tests for new features
- Test error conditions
- Use descriptive test names
- Follow AAA pattern (Arrange, Act, Assert)

Example test:
```python
def test_file_scanner_finds_python_files():
    # Arrange
    scanner = FileScanner(config_manager)
    test_dir = Path("test_data")
    
    # Act
    files = scanner.scan_directory(test_dir, [".py"])
    
    # Assert
    assert len(files) > 0
    assert all(f["path"].suffix == ".py" for f in files)
```

## Internationalization

Adding a new language:

1. Create `locales/{language_code}.json`
2. Copy structure from `locales/en.json`
3. Translate all strings
4. Update `localization_manager.py`
5. Test the interface

Example locale file:
```json
{
  "app_title": "CodeFuser",
  "main_screen": {
    "select_folder": "Select Folder",
    "browse": "Browse",
    "scan_files": "Scan Files"
  }
}
```

## Release Process

1. Update version in relevant files
2. Update CHANGELOG.md
3. Create git tag: `git tag v1.0.0`
4. Push tag: `git push origin v1.0.0`
5. GitHub Actions will build and create release

## Questions?

Don't hesitate to ask questions in [GitHub Discussions](https://github.com/yourusername/codefuser/discussions)!

## License

By contributing, you agree that your contributions will be licensed under the MIT License.