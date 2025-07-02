# 🔍 Smart Filters Guide

Master CodeFuser's intelligent filtering system to focus on exactly the code that matters for your analysis.

## 🎯 Filter Overview

Smart Filters automatically analyze and categorize your code files, allowing you to focus on specific aspects of your project without manual file selection.

### Filter Categories

| Category | Purpose | Examples |
|----------|---------|----------|
| **Content Analysis** | Filter by code content | Functions, classes, TODOs |
| **File Types** | Filter by file characteristics | Tests, configs, documentation |
| **Git Integration** | Filter by version control status | Modified, staged, untracked |
| **Code Quality** | Filter by code metrics | Complexity, size, issues |
| **Language Specific** | Filter by programming language | Python modules, JS components |
| **Project Structure** | Filter by project organization | Source, tests, build files |

## 🧠 Content Analysis Filters

### Code Pattern Detection

#### Function and Class Detection
```json
{
  "content_filters": {
    "has_functions": {
      "description": "Files containing function definitions",
      "patterns": [
        "def\\s+\\w+\\s*\\(",      // Python functions
        "function\\s+\\w+\\s*\\(", // JavaScript functions
        "public\\s+\\w+\\s+\\w+\\s*\\(", // Java/C# methods
        "fn\\s+\\w+\\s*\\("        // Rust functions
      ]
    },
    "has_classes": {
      "description": "Files containing class definitions",
      "patterns": [
        "class\\s+\\w+",          // Most languages
        "interface\\s+\\w+",      // Interfaces
        "struct\\s+\\w+",         // Go/Rust structs
        "type\\s+\\w+\\s*="       // TypeScript types
      ]
    }
  }
}
```

#### Documentation and Comments
```json
{
  "documentation_filters": {
    "well_documented": {
      "description": "Files with good documentation",
      "criteria": {
        "docstring_ratio": "> 0.1",
        "comment_ratio": "> 0.05",
        "has_module_docstring": true
      }
    },
    "needs_documentation": {
      "description": "Files lacking documentation",
      "criteria": {
        "docstring_ratio": "< 0.05",
        "comment_ratio": "< 0.02",
        "has_public_functions": true
      }
    }
  }
}
```

#### TODO and FIXME Detection
```json
{
  "task_filters": {
    "has_todos": {
      "description": "Files with TODO comments",
      "patterns": [
        "TODO:",
        "FIXME:",
        "HACK:",
        "XXX:",
        "BUG:",
        "NOTE:"
      ]
    },
    "urgent_items": {
      "description": "Files with urgent tasks",
      "patterns": [
        "URGENT:",
        "CRITICAL:",
        "SECURITY:",
        "BREAKING:"
      ]
    }
  }
}
```

### Security Pattern Detection
```json
{
  "security_filters": {
    "potential_vulnerabilities": {
      "description": "Files with potential security issues",
      "patterns": [
        "eval\\(",                    // Code injection
        "exec\\(",                    // Code execution
        "input\\(",                   // User input
        "raw_input\\(",              // Raw input
        "os\\.system\\(",            // System commands
        "subprocess\\.",             // Process execution
        "sql\\s*=.*\\+",            // SQL concatenation
        "innerHTML\\s*=",            // XSS potential
        "document\\.write\\("        // DOM manipulation
      ]
    },
    "authentication_files": {
      "description": "Authentication and security related files",
      "patterns": [
        "password",
        "auth",
        "login",
        "session",
        "token",
        "crypto",
        "security",
        "permission"
      ],
      "filename_patterns": true
    }
  }
}
```

## 📁 File Type Filters

### Test File Detection
```json
{
  "test_filters": {
    "test_files": {
      "description": "Test and spec files",
      "patterns": [
        "**/test_*.py",
        "**/*_test.py",
        "**/*.test.js",
        "**/*.spec.js",
        "**/tests/**",
        "**/__tests__/**",
        "**/spec/**"
      ]
    },
    "mock_files": {
      "description": "Mock and fixture files",
      "patterns": [
        "**/mock*.py",
        "**/fixture*.py",
        "**/*mock*",
        "**/stubs/**"
      ]
    }
  }
}
```

### Configuration Files
```json
{
  "config_filters": {
    "configuration_files": {
      "description": "Configuration and settings files",
      "extensions": [".json", ".yaml", ".yml", ".toml", ".ini", ".cfg", ".conf"],
      "filenames": [
        "config.py",
        "settings.py",
        "constants.py",
        "environment.js",
        "webpack.config.js",
        "package.json",
        "requirements.txt",
        "Dockerfile",
        ".env"
      ]
    },
    "build_files": {
      "description": "Build and deployment files",
      "patterns": [
        "Makefile",
        "gulpfile.js",
        "Gruntfile.js",
        "build.gradle",
        "pom.xml",
        "CMakeLists.txt",
        "setup.py",
        "pyproject.toml"
      ]
    }
  }
}
```

### Documentation Files
```json
{
  "documentation_filters": {
    "readme_files": {
      "description": "README and documentation files",
      "patterns": [
        "README*",
        "CHANGELOG*",
        "CONTRIBUTING*",
        "LICENSE*",
        "DOCS*",
        "*.md",
        "*.rst",
        "*.txt"
      ]
    },
    "api_documentation": {
      "description": "API documentation files",
      "patterns": [
        "**/docs/**",
        "**/api/**",
        "swagger.json",
        "openapi.yaml",
        "**/schema/**"
      ]
    }
  }
}
```

## 🎨 Language-Specific Filters

### Python Filters
```json
{
  "python_filters": {
    "django_files": {
      "description": "Django framework files",
      "patterns": [
        "**/models.py",
        "**/views.py",
        "**/forms.py",
        "**/admin.py",
        "**/urls.py",
        "**/settings.py",
        "**/migrations/**"
      ]
    },
    "flask_files": {
      "description": "Flask framework files",
      "patterns": [
        "app.py",
        "run.py",
        "**/routes/**",
        "**/blueprints/**",
        "**/templates/**"
      ]
    },
    "data_science": {
      "description": "Data science and ML files",
      "extensions": [".ipynb"],
      "patterns": [
        "**/analysis/**",
        "**/notebooks/**",
        "**/models/**",
        "**/data/**"
      ],
      "content_patterns": [
        "import pandas",
        "import numpy",
        "import sklearn",
        "import tensorflow",
        "import torch"
      ]
    }
  }
}
```

### JavaScript/TypeScript Filters
```json
{
  "javascript_filters": {
    "react_components": {
      "description": "React component files",
      "extensions": [".jsx", ".tsx"],
      "content_patterns": [
        "import React",
        "from 'react'",
        "useState",
        "useEffect",
        "Component"
      ]
    },
    "vue_components": {
      "description": "Vue.js component files",
      "extensions": [".vue"],
      "content_patterns": [
        "<template>",
        "<script>",
        "<style>"
      ]
    },
    "node_backend": {
      "description": "Node.js backend files",
      "patterns": [
        "**/routes/**",
        "**/controllers/**",
        "**/middleware/**",
        "**/models/**",
        "server.js",
        "app.js"
      ]
    }
  }
}
```

### Web Development Filters
```json
{
  "web_filters": {
    "frontend_files": {
      "description": "Frontend web files",
      "extensions": [".html", ".css", ".scss", ".sass", ".less"],
      "patterns": [
        "**/assets/**",
        "**/static/**",
        "**/public/**",
        "**/src/**"
      ]
    },
    "api_files": {
      "description": "API and backend files",
      "patterns": [
        "**/api/**",
        "**/endpoints/**",
        "**/routes/**",
        "**/controllers/**"
      ]
    }
  }
}
```

## 📊 Code Quality Filters

### File Size and Complexity
```json
{
  "quality_filters": {
    "large_files": {
      "description": "Large files that may need refactoring",
      "criteria": {
        "lines": "> 500",
        "size_mb": "> 1"
      }
    },
    "small_files": {
      "description": "Very small files",
      "criteria": {
        "lines": "< 10",
        "size_kb": "< 1"
      }
    },
    "complex_files": {
      "description": "High complexity files",
      "criteria": {
        "functions": "> 20",
        "classes": "> 5",
        "nested_blocks": "> 4"
      }
    }
  }
}
```

### Code Health Indicators
```json
{
  "health_filters": {
    "potential_issues": {
      "description": "Files with potential code issues",
      "patterns": [
        "print\\(",                   // Debug prints
        "console\\.log\\(",          // Console logs
        "debugger;",                 // Debug statements
        "//\\s*TODO",               // TODO comments
        "#\\s*FIXME"                // FIXME comments
      ]
    },
    "unused_imports": {
      "description": "Files with potentially unused imports",
      "language_specific": {
        "python": ["^import \\w+$", "^from \\w+ import"],
        "javascript": ["^import .* from", "const .* = require"]
      }
    }
  }
}
```

## ⏰ Time-Based Filters

### Modification Time Filters
```json
{
  "time_filters": {
    "recently_modified": {
      "description": "Files modified in the last 7 days",
      "criteria": {
        "modified_days_ago": "< 7"
      }
    },
    "stale_files": {
      "description": "Files not modified in 6+ months",
      "criteria": {
        "modified_days_ago": "> 180"
      }
    },
    "active_development": {
      "description": "Files under active development",
      "criteria": {
        "modified_days_ago": "< 30",
        "commits_last_month": "> 3"
      }
    }
  }
}
```

## 🔧 Custom Filter Creation

### Simple Pattern Filter
```json
{
  "name": "Database Models",
  "description": "Database model and schema files",
  "type": "pattern",
  "criteria": {
    "filename_patterns": [
      "**/models/**",
      "**/schemas/**",
      "**/*model*.py",
      "**/*schema*.py"
    ],
    "content_patterns": [
      "class.*Model",
      "db\\.Model",
      "models\\.Model",
      "Schema"
    ]
  }
}
```

### Advanced Logic Filter
```json
{
  "name": "API Endpoints",
  "description": "REST API endpoint files",
  "type": "advanced",
  "criteria": {
    "and": [
      {
        "or": [
          {"filename_contains": "api"},
          {"filename_contains": "endpoint"},
          {"path_contains": "/api/"}
        ]
      },
      {
        "content_matches": [
          "@app\\.route",
          "@api\\.route",
          "app\\.get\\(",
          "app\\.post\\(",
          "router\\."
        ]
      },
      {
        "not": {
          "filename_contains": "test"
        }
      }
    ]
  }
}
```

### Composite Filter
```json
{
  "name": "Security Critical Files",
  "description": "Files that require security review",
  "type": "composite",
  "filters": [
    "authentication_files",
    "potential_vulnerabilities",
    "user_input_handlers"
  ],
  "logic": "OR"
}
```

## 🎛️ Filter Presets

### Development Workflow Presets
```json
{
  "presets": {
    "code_review": {
      "name": "Code Review Focus",
      "description": "Files most important for code review",
      "filters": [
        "recently_modified",
        "has_functions",
        "not test_files",
        "not configuration_files"
      ]
    },
    "security_audit": {
      "name": "Security Audit",
      "description": "Security-sensitive files",
      "filters": [
        "authentication_files",
        "potential_vulnerabilities",
        "user_input_handlers",
        "api_endpoints"
      ]
    },
    "performance_review": {
      "name": "Performance Review",
      "description": "Files affecting performance",
      "filters": [
        "database_queries",
        "large_files",
        "complex_algorithms",
        "api_endpoints"
      ]
    },
    "refactoring_candidates": {
      "name": "Refactoring Candidates",
      "description": "Files that may need refactoring",
      "filters": [
        "large_files",
        "complex_files",
        "has_todos",
        "potential_issues"
      ]
    }
  }
}
```

### Project Type Presets
```json
{
  "project_presets": {
    "web_application": {
      "include": [
        "frontend_files",
        "api_files",
        "database_models",
        "authentication_files"
      ],
      "exclude": [
        "test_files",
        "build_files",
        "documentation_files"
      ]
    },
    "data_science": {
      "include": [
        "notebooks",
        "data_analysis",
        "model_files",
        "visualization"
      ],
      "exclude": [
        "raw_data",
        "cache_files",
        "temporary_files"
      ]
    },
    "mobile_app": {
      "include": [
        "ui_components",
        "business_logic",
        "api_integration",
        "native_modules"
      ],
      "exclude": [
        "generated_files",
        "build_artifacts",
        "assets"
      ]
    }
  }
}
```

## 🚀 Advanced Filter Features

### Dynamic Filters
```json
{
  "dynamic_filters": {
    "modified_since_last_release": {
      "description": "Files changed since last Git tag",
      "git_command": "git diff --name-only $(git describe --tags --abbrev=0)..HEAD"
    },
    "files_by_author": {
      "description": "Files by specific author",
      "git_command": "git log --author='{{AUTHOR}}' --name-only --pretty=format: | sort -u"
    }
  }
}
```

### Machine Learning Filters
```json
{
  "ml_filters": {
    "code_similarity": {
      "description": "Find similar code patterns",
      "algorithm": "cosine_similarity",
      "threshold": 0.8
    },
    "complexity_prediction": {
      "description": "Predict file complexity",
      "model": "trained_complexity_model",
      "threshold": "high"
    }
  }
}
```

### Performance Optimization
```json
{
  "filter_performance": {
    "caching": {
      "enabled": true,
      "cache_duration": "1 hour",
      "cache_size_mb": 50
    },
    "parallel_processing": {
      "enabled": true,
      "max_threads": 4
    },
    "early_termination": {
      "enabled": true,
      "max_files_per_filter": 1000
    }
  }
}
```

## 💡 Filter Best Practices

### ✅ Effective Filter Strategies

#### Start Broad, Narrow Down
```
1. Begin with project type preset
2. Add specific technology filters
3. Apply quality filters
4. Use Git filters for recent changes
5. Add file-specific prompts to remaining files
```

#### Layer Filters for Precision
```
Base Layer: Project structure (src files only)
Tech Layer: Language specific (Python files)
Quality Layer: Well-documented files
Focus Layer: Recently modified files
```

#### Combine with File-Specific Prompts
```
1. Use filters to select relevant files
2. Add targeted prompts to critical files
3. Use general template for overall analysis
4. Export in appropriate format
```

### ❌ Common Filter Mistakes

#### Over-Filtering
- Don't exclude too many files
- Important context might be lost
- Keep some supporting files

#### Under-Filtering
- Don't include everything
- Quality over quantity for AI analysis
- Focus on what matters most

#### Ignoring Context
- Some "unimportant" files provide crucial context
- Configuration files often affect behavior
- Test files show intended usage

## 🔍 Filter Troubleshooting

### No Files Match Filter
```
1. Check filter syntax and patterns
2. Verify file extensions match
3. Review exclude patterns
4. Test with simpler filters first
```

### Too Many Files Selected
```
1. Add more specific patterns
2. Use exclude filters
3. Combine multiple filters with AND logic
4. Set file count limits
```

### Filter Performance Issues
```
1. Enable caching
2. Reduce pattern complexity
3. Use early termination
4. Profile filter execution time
```

---

**Ready to filter like a pro?** Start with the built-in presets and gradually create custom filters for your specific needs!

*Continue to [Git Integration](Git-Integration-EN) to learn about combining filters with version control →*