# 🐙 Git Integration Guide

Leverage CodeFuser's powerful Git integration to focus on changed code, track development progress, and optimize your AI analysis workflow.

## 🎯 Git Integration Overview

CodeFuser seamlessly integrates with Git repositories to provide intelligent file filtering based on version control status, helping you focus on what's changed and what matters most.

### Key Features

| Feature | Description | Use Case |
|---------|-------------|----------|
| **Status Detection** | Show Git status for each file | Quick identification of changes |
| **Change Filtering** | Filter by modification status | Focus on recent development |
| **Branch Comparison** | Compare files across branches | Feature branch analysis |
| **Commit Range Analysis** | Analyze specific commit ranges | Release preparation |
| **Author Filtering** | Filter by commit author | Individual contributor focus |
| **Ignore Integration** | Respect .gitignore patterns | Clean file lists |

## 📊 Git Status Indicators

### Status Symbols
```
M  - Modified (tracked file changed)
A  - Added (new file staged)
D  - Deleted (file removed)
R  - Renamed (file moved/renamed)
C  - Copied (file copied)
?  - Untracked (new file not in Git)
!  - Ignored (matches .gitignore)
U  - Unmerged (merge conflict)
```

### Visual Display
Files in the file tree show Git status:
```
☑️ 📄 M  🐍 auth.py          (Modified file)
☐ 📝✨ A  📜 new_feature.js   (Added file with custom prompt)
☑️ 📄 ?  🎨 styles.css       (Untracked file)
```

## 🔧 Git Configuration

### Basic Git Settings
```json
{
  "git_integration": {
    "enabled": true,
    "auto_detect_repository": true,
    "show_git_status": true,
    "status_indicators": {
      "modified": "M",
      "added": "A",
      "deleted": "D",
      "renamed": "R",
      "copied": "C",
      "untracked": "?",
      "ignored": "!",
      "unmerged": "U"
    },
    "include_untracked": true,
    "ignore_git_ignored": true,
    "refresh_interval_seconds": 5
  }
}
```

### Advanced Git Configuration
```json
{
  "git_advanced": {
    "branch_comparison": {
      "enabled": true,
      "default_base_branch": "main",
      "show_ahead_behind": true,
      "auto_detect_base": true
    },
    "commit_analysis": {
      "enabled": true,
      "max_commits_analyze": 100,
      "include_merge_commits": false
    },
    "performance": {
      "cache_git_status": true,
      "cache_duration_seconds": 30,
      "parallel_git_commands": true
    }
  }
}
```

## 🔍 Git-Based Filtering

### Status-Based Filters

#### Modified Files Only
```json
{
  "git_filters": {
    "modified_only": {
      "description": "Show only modified files",
      "include_status": ["M", "A", "D", "R"],
      "exclude_status": ["?", "!"]
    }
  }
}
```

#### Recent Changes
```json
{
  "git_filters": {
    "recent_changes": {
      "description": "Files changed in last 7 days",
      "time_range": {
        "since": "7 days ago",
        "until": "now"
      },
      "include_status": ["M", "A", "R"]
    }
  }
}
```

#### Staged Changes
```json
{
  "git_filters": {
    "staged_changes": {
      "description": "Files ready for commit",
      "git_command": "git diff --cached --name-only",
      "include_untracked_staged": true
    }
  }
}
```

### Branch-Based Filtering

#### Feature Branch Changes
```json
{
  "branch_filters": {
    "feature_branch_changes": {
      "description": "Changes in current feature branch",
      "base_branch": "develop",
      "current_branch": "feature/new-auth",
      "comparison_type": "diff"
    }
  }
}
```

#### Release Preparation
```json
{
  "release_filters": {
    "release_changes": {
      "description": "Changes since last release",
      "base_ref": "v1.0.0",
      "current_ref": "HEAD",
      "include_new_files": true
    }
  }
}
```

### Commit-Based Filtering

#### Commit Range Analysis
```json
{
  "commit_filters": {
    "commit_range": {
      "description": "Files changed in specific commits",
      "from_commit": "abc123",
      "to_commit": "def456",
      "include_merge_commits": false
    }
  }
}
```

#### Author-Specific Changes
```json
{
  "author_filters": {
    "my_changes": {
      "description": "Files I've modified",
      "authors": ["john.doe@company.com"],
      "time_range": "last 30 days",
      "min_commits": 1
    }
  }
}
```

## 🚀 Common Git Workflows

### 1. Code Review Workflow

#### Pre-Commit Review
```
Scenario: Review changes before committing
Filter: Modified and staged files
Template: Code Review
Focus: Quality and standards compliance
```

**Configuration:**
```json
{
  "workflow": "pre_commit_review",
  "filters": {
    "git_status": ["M", "A"],
    "exclude_patterns": ["test_*", "*.md"],
    "max_files": 20
  },
  "template": "code_review",
  "export_format": "html"
}
```

#### Pull Request Review
```
Scenario: Review feature branch before merge
Filter: Branch comparison against main
Template: Code Review
Focus: Integration and impact analysis
```

**Configuration:**
```json
{
  "workflow": "pull_request_review",
  "git_comparison": {
    "base_branch": "main",
    "feature_branch": "feature/user-auth",
    "include_context_files": true
  },
  "template": "code_review",
  "file_prompts": {
    "pattern": "auth.*\\.py",
    "prompt": "Focus on security implications of authentication changes"
  }
}
```

### 2. Bug Investigation Workflow

#### Recent Changes Analysis
```
Scenario: Investigate recent bug introduction
Filter: Files changed in last week
Template: Bug Analysis
Focus: Identify potential causes
```

**Configuration:**
```json
{
  "workflow": "bug_investigation",
  "git_filters": {
    "time_range": "7 days",
    "exclude_tests": false,
    "include_config_changes": true
  },
  "template": "bug_analysis",
  "analysis_focus": "potential_issues"
}
```

#### Blame-Based Analysis
```
Scenario: Track responsibility for specific changes
Filter: Files modified by specific authors
Template: Change Impact Analysis
Focus: Understanding change context
```

### 3. Release Preparation Workflow

#### Release Diff Analysis
```
Scenario: Prepare release notes and review
Filter: Changes since last release tag
Template: Release Review
Focus: Feature completeness and stability
```

**Configuration:**
```json
{
  "workflow": "release_preparation",
  "git_comparison": {
    "base_ref": "v1.2.0",
    "current_ref": "HEAD",
    "group_by_feature": true
  },
  "template": "release_review",
  "include_statistics": true
}
```

### 4. Security Audit Workflow

#### Security-Focused Git Analysis
```
Scenario: Security audit of recent changes
Filter: Authentication and security-related files
Template: Security Audit
Focus: Vulnerability assessment
```

**Configuration:**
```json
{
  "workflow": "security_audit",
  "git_filters": {
    "modified_files": true,
    "security_patterns": [
      "**/auth/**",
      "**/security/**",
      "**/*password*",
      "**/*token*"
    ]
  },
  "template": "security_audit",
  "file_prompts": {
    "auto_generate": true,
    "focus": "security_vulnerabilities"
  }
}
```

## 📈 Git Analytics and Insights

### Commit Frequency Analysis
```json
{
  "git_analytics": {
    "commit_frequency": {
      "time_period": "last_30_days",
      "group_by": "author",
      "include_merge_commits": false,
      "file_types": [".py", ".js", ".ts"]
    }
  }
}
```

### Code Churn Analysis
```json
{
  "code_churn": {
    "description": "Files with high change frequency",
    "criteria": {
      "commits_per_week": "> 5",
      "lines_changed_per_commit": "> 50",
      "time_period": "last_quarter"
    },
    "risk_assessment": true
  }
}
```

### Hotspot Detection
```json
{
  "hotspot_analysis": {
    "description": "Files that change together frequently",
    "min_co_change_frequency": 0.7,
    "time_window": "6_months",
    "visualization": "dependency_graph"
  }
}
```

## 🔧 Advanced Git Features

### Submodule Support
```json
{
  "submodule_integration": {
    "enabled": true,
    "include_submodule_changes": true,
    "track_submodule_updates": true,
    "recursive_analysis": false
  }
}
```

### Git LFS Integration
```json
{
  "git_lfs": {
    "enabled": true,
    "track_lfs_files": false,
    "include_lfs_metadata": true,
    "lfs_file_handling": "reference_only"
  }
}
```

### Worktree Support
```json
{
  "worktree_support": {
    "enabled": true,
    "auto_detect_worktrees": true,
    "include_all_worktrees": false,
    "current_worktree_only": true
  }
}
```

## 🎛️ Git Filter Presets

### Development Presets
```json
{
  "git_presets": {
    "daily_review": {
      "description": "Review today's changes",
      "filters": {
        "since": "today",
        "author": "current_user",
        "exclude_merges": true
      }
    },
    "sprint_review": {
      "description": "Review sprint changes",
      "filters": {
        "since": "2 weeks ago",
        "include_team": true,
        "group_by_feature": true
      }
    },
    "hotfix_analysis": {
      "description": "Analyze hotfix changes",
      "filters": {
        "branch_pattern": "hotfix/*",
        "urgency": "high",
        "include_tests": true
      }
    }
  }
}
```

### Quality Assurance Presets
```json
{
  "qa_presets": {
    "regression_risk": {
      "description": "Files with high regression risk",
      "criteria": {
        "change_frequency": "high",
        "test_coverage": "low",
        "complexity": "high"
      }
    },
    "stability_review": {
      "description": "Stability-critical files",
      "criteria": {
        "change_impact": "high",
        "dependency_count": "high",
        "bug_history": "exists"
      }
    }
  }
}
```

## 🔍 Git Integration Troubleshooting

### Common Issues

#### Git Not Detected
```bash
# Check Git installation
git --version

# Verify repository
git status

# Check CodeFuser Git settings
{
  "git_integration": {
    "enabled": true,
    "auto_detect_repository": true
  }
}
```

#### Slow Git Operations
```json
{
  "performance_optimization": {
    "git_cache": {
      "enabled": true,
      "cache_size_mb": 50,
      "cache_duration_minutes": 10
    },
    "parallel_operations": {
      "enabled": true,
      "max_concurrent": 3
    },
    "command_timeout_seconds": 30
  }
}
```

#### Large Repository Performance
```json
{
  "large_repo_optimization": {
    "partial_clone": true,
    "shallow_analysis": true,
    "max_files_analyze": 1000,
    "skip_binary_files": true,
    "use_git_filters": true
  }
}
```

### Git Command Customization
```json
{
  "custom_git_commands": {
    "status_command": "git status --porcelain",
    "diff_command": "git diff --name-only",
    "log_command": "git log --oneline --since='1 week ago'",
    "blame_command": "git blame --line-porcelain"
  }
}
```

## 💡 Git Integration Best Practices

### ✅ Effective Git Workflows

#### Start with Recent Changes
```
1. Use "modified files" filter as starting point
2. Add file-specific prompts to critical changes
3. Include context files if needed
4. Focus on changes that affect core functionality
```

#### Combine Git with Smart Filters
```
1. Git filter: Recently modified files
2. Smart filter: Exclude test files
3. Quality filter: Include only well-documented files
4. Result: High-quality, recently changed core code
```

#### Use Branch Comparisons
```
1. Compare feature branch against main
2. Focus on new functionality
3. Add security prompts to authentication changes
4. Add performance prompts to database changes
```

### ❌ Common Git Integration Mistakes

#### Ignoring Merge Commits
- Merge commits provide important context
- Include them for comprehensive analysis
- They show integration points

#### Focusing Only on Latest Changes
- Recent changes need historical context
- Include related unchanged files
- Consider dependency impacts

#### Overlooking Configuration Changes
- Config changes can have major impacts
- Include environment and build files
- They often explain behavioral changes

### 🎯 Git-Specific Prompt Strategies

#### For Modified Files
```
"This file was recently modified. Focus on:
1. What changed and why
2. Impact on dependent code
3. Potential side effects
4. Testing requirements"
```

#### For New Files
```
"This is a new file. Analyze:
1. Purpose and integration points
2. Code quality and standards compliance
3. Missing documentation or tests
4. Architecture fit"
```

#### For Deleted Files
```
"This file was removed. Consider:
1. What functionality was lost
2. Where was it moved (if applicable)
3. Impact on dependent code
4. Migration path for users"
```

## 🚀 Advanced Git Workflows

### Continuous Integration Integration
```json
{
  "ci_integration": {
    "pre_commit_analysis": {
      "enabled": true,
      "run_on_staged_files": true,
      "block_commit_on_issues": false
    },
    "pull_request_analysis": {
      "enabled": true,
      "comment_on_pr": true,
      "analysis_threshold": "high_impact_changes"
    }
  }
}
```

### Team Collaboration Features
```json
{
  "team_features": {
    "shared_git_filters": {
      "enabled": true,
      "sync_across_team": true,
      "filter_repository": "team-codefuser-filters"
    },
    "author_expertise_mapping": {
      "enabled": true,
      "expertise_database": "team_expertise.json",
      "suggest_reviewers": true
    }
  }
}
```

---

**Ready to supercharge your Git workflow?** Start with basic status filtering and gradually incorporate advanced branch comparisons and commit analysis!

*Continue to [Troubleshooting Guide](Troubleshooting-EN) for help with any Git integration issues →*