# 🎨 Templates Guide

Master CodeFuser's powerful template system to create consistent, professional AI-ready code outputs.

## 🎯 Template Overview

Templates provide pre-written, professionally crafted prompts that guide AI analysis in specific directions. They save time and ensure consistent results across projects.

### Built-in Templates

| Template | Best For | AI Tools | Use Case |
|----------|----------|----------|----------|
| **16x Prompt** | General analysis | All | Comprehensive code review |
| **Claude Project** | Claude AI | Claude | Project setup and analysis |
| **Code Review** | Team reviews | All | Structured code inspection |
| **Documentation** | Docs generation | All | API and code documentation |
| **Cursor Rules** | IDE setup | Cursor IDE | Development environment |

## 📝 Built-in Templates Deep Dive

### 🔥 16x Prompt Template

**Purpose**: The most popular AI analysis format, providing comprehensive code examination.

**Template Content**:
```
You are an expert software engineer. Please analyze the provided codebase and deliver insights in the following structured format:

## 1. **Architecture Overview**
- Overall system design and patterns
- Key components and their relationships
- Technology stack analysis

## 2. **Code Quality Assessment**
- Code organization and structure
- Naming conventions and readability
- Documentation quality

## 3. **Security Analysis**
- Potential security vulnerabilities
- Authentication and authorization
- Data validation and sanitization

## 4. **Performance Considerations**
- Bottlenecks and optimization opportunities
- Resource usage patterns
- Scalability concerns

## 5. **Best Practices Compliance**
- Industry standard adherence
- Framework-specific best practices
- Code maintainability

## 6. **Testing Strategy**
- Test coverage analysis
- Testing patterns and quality
- Missing test scenarios

## 7. **Dependencies and Libraries**
- Third-party library usage
- Version management
- Security of dependencies

## 8. **Error Handling**
- Exception handling patterns
- Error logging and monitoring
- Graceful failure mechanisms

## 9. **Database and Data Layer**
- Data model design
- Query optimization
- Data integrity

## 10. **API Design** (if applicable)
- RESTful design principles
- API documentation
- Versioning strategy

## 11. **Configuration Management**
- Environment-specific settings
- Secret management
- Configuration validation

## 12. **Logging and Monitoring**
- Logging strategy and implementation
- Monitoring and alerting
- Performance metrics

## 13. **Deployment and DevOps**
- Deployment strategy
- CI/CD pipeline
- Infrastructure as code

## 14. **Scalability and Reliability**
- Horizontal scaling capability
- Fault tolerance
- Load distribution

## 15. **Maintenance and Technical Debt**
- Code debt assessment
- Refactoring opportunities
- Long-term maintainability

## 16. **Recommendations**
- Priority improvements
- Action items with timelines
- Implementation strategies

Please provide specific examples from the code where relevant and prioritize findings by impact and urgency.
```

**Best Used With**:
- File-specific prompts for targeted analysis
- HTML export for easy reading
- Large codebases requiring comprehensive review

### 🤖 Claude Project Template

**Purpose**: Optimized for Claude AI's project feature, providing structured context.

**Template Content**:
```
This is a codebase for {{PROJECT_NAME}} project. Please analyze this codebase to understand:

## Project Context
{{PROJECT_DESCRIPTION}}

## Analysis Goals
- Understand the overall architecture and design patterns
- Identify key functionality and business logic
- Review code quality and potential improvements
- Assess security considerations
- Evaluate performance and scalability aspects

## Key Areas of Focus
1. **Core Functionality**: Main business logic and features
2. **Data Flow**: How data moves through the system
3. **Integration Points**: External APIs, databases, services
4. **Error Handling**: Exception management and recovery
5. **Testing**: Test coverage and quality

## Specific Questions
- What are the main architectural patterns used?
- Are there any potential security vulnerabilities?
- What are the performance bottlenecks?
- How maintainable and extensible is the code?
- What improvements would you recommend?

Please provide a comprehensive analysis with specific code examples and actionable recommendations.

## Code Structure
The following files represent the key components of the system:
{{FILE_LIST}}

Each file may have specific analysis instructions. Please pay attention to any file-specific prompts provided.
```

**Best Used With**:
- Claude AI platform
- Project setup and initial analysis
- Team onboarding and knowledge transfer

### 🔍 Code Review Template

**Purpose**: Structured template for thorough code reviews and team collaboration.

**Template Content**:
```
# Code Review: {{PROJECT_NAME}}

## Review Context
- **Reviewer**: {{REVIEWER_NAME}}
- **Review Date**: {{REVIEW_DATE}}
- **Review Type**: {{REVIEW_TYPE}} (Pre-commit, Post-commit, Security, Performance)
- **Files Changed**: {{CHANGED_FILES_COUNT}} files

## Review Checklist

### 🔍 **Functionality**
- [ ] Code accomplishes intended functionality
- [ ] Logic is correct and efficient
- [ ] Edge cases are handled appropriately
- [ ] Business requirements are met

### 🏗️ **Design & Architecture**
- [ ] Code follows established design patterns
- [ ] Separation of concerns is maintained
- [ ] Dependencies are properly managed
- [ ] Interfaces are well-defined

### 📖 **Code Quality**
- [ ] Code is readable and well-documented
- [ ] Naming conventions are followed
- [ ] Functions/methods are appropriately sized
- [ ] Code duplication is minimized

### 🔒 **Security**
- [ ] Input validation is implemented
- [ ] Authentication/authorization is correct
- [ ] Sensitive data is properly handled
- [ ] SQL injection/XSS vulnerabilities checked

### ⚡ **Performance**
- [ ] No obvious performance bottlenecks
- [ ] Database queries are optimized
- [ ] Memory usage is reasonable
- [ ] Caching is used appropriately

### 🧪 **Testing**
- [ ] Unit tests are comprehensive
- [ ] Integration tests cover key flows
- [ ] Test data is appropriate
- [ ] Error scenarios are tested

### 📝 **Documentation**
- [ ] Code comments explain complex logic
- [ ] API documentation is updated
- [ ] README files are current
- [ ] Change logs are maintained

## Detailed Analysis

Please analyze each file and provide:

1. **Summary**: Brief overview of changes/functionality
2. **Strengths**: What's done well
3. **Issues**: Problems found (categorized by severity)
4. **Suggestions**: Specific improvement recommendations
5. **Questions**: Clarifications needed

## Risk Assessment
- **High Risk**: Critical issues that must be fixed
- **Medium Risk**: Important issues that should be addressed
- **Low Risk**: Minor improvements and suggestions

## Approval Status
- [ ] Approved (ready to merge)
- [ ] Approved with minor changes
- [ ] Requires significant changes
- [ ] Rejected (needs major rework)

## Action Items
List specific tasks with assignees and deadlines.
```

**Best Used With**:
- Team code reviews
- Pull request analysis
- Quality assurance processes
- DOCX export for formal documentation

### 📚 Documentation Template

**Purpose**: Generate comprehensive documentation from code analysis.

**Template Content**:
```
# {{PROJECT_NAME}} Documentation

Generate comprehensive documentation for this codebase including:

## 📋 **Project Overview**
- Purpose and main functionality
- Target audience and use cases
- Key features and capabilities
- Technology stack and dependencies

## 🏗️ **Architecture Documentation**
- System architecture diagram (describe in text)
- Component relationships and interactions
- Data flow and processing pipeline
- External integrations and dependencies

## 📖 **API Documentation**
For each API endpoint or public interface:
- Purpose and functionality
- Input parameters and validation
- Output format and examples
- Error responses and handling
- Authentication requirements

## 🔧 **Setup and Installation**
- System requirements
- Installation steps
- Configuration instructions
- Environment setup
- Database setup (if applicable)

## 💻 **Usage Examples**
- Basic usage scenarios
- Code examples with explanations
- Common use cases
- Best practices for integration

## 📁 **Code Structure**
For each major component/file:
- Purpose and responsibility
- Key classes/functions
- Dependencies and relationships
- Configuration options

## 🔌 **Integration Guide**
- How to integrate with external systems
- API usage examples
- SDK or library usage
- Third-party service integrations

## 🧪 **Testing Guide**
- Testing strategy and approach
- How to run tests
- Test data setup
- Coverage requirements

## 🚀 **Deployment Guide**
- Deployment requirements
- Environment configuration
- CI/CD pipeline setup
- Monitoring and logging

## 🔧 **Configuration Reference**
- All configuration options
- Environment variables
- Feature flags
- Performance tuning

## 📞 **Troubleshooting**
- Common issues and solutions
- Error messages and fixes
- Performance troubleshooting
- Debug information

## 🔄 **Maintenance**
- Regular maintenance tasks
- Update procedures
- Backup and recovery
- Security considerations

Please make the documentation clear, comprehensive, and suitable for both developers and end-users. Include specific code examples where helpful.
```

**Best Used With**:
- Documentation generation projects
- API documentation
- Team knowledge bases
- HTML export for web documentation

### ⚙️ Cursor Rules Template

**Purpose**: Generate IDE-specific configuration and rules for Cursor IDE.

**Template Content**:
```
# Cursor IDE Rules for {{PROJECT_NAME}}

Based on this codebase analysis, generate Cursor IDE rules and configuration:

## 🎯 **Project-Specific Rules**

### Code Style and Formatting
- Indentation preferences (spaces/tabs, size)
- Line length limits
- Naming conventions for variables, functions, classes
- File organization patterns

### Language-Specific Settings
For each language in the project:
- Linter configuration
- Formatter settings
- Language server options
- Extension recommendations

### AI Assistant Configuration
- Preferred coding patterns for AI suggestions
- Context preferences for code completion
- Code review focus areas
- Documentation style preferences

## 🔧 **Workspace Settings**

### File Associations
- File type mappings
- Syntax highlighting preferences
- Icon themes for different file types

### Search and Navigation
- Ignore patterns for search
- File watcher configurations
- Quick open preferences

### Git Integration
- Ignore patterns
- Commit message templates
- Branch naming conventions
- Pre-commit hooks

## 📝 **Code Templates and Snippets**

Generate snippets for:
- Common function templates
- Class structure templates
- Test file templates
- Documentation templates

## 🛠️ **Debugging Configuration**
- Launch configurations
- Environment variables
- Debugging preferences
- Breakpoint templates

## 📦 **Extension Recommendations**
Based on the technology stack:
- Essential extensions for the project
- Optional productivity extensions
- Theme and UI extensions
- Language-specific extensions

## 🔍 **Linting and Validation Rules**
- ESLint/TSLint configuration
- Python linting rules
- Custom validation rules
- Code quality metrics

## 🧪 **Testing Integration**
- Test runner configuration
- Test file patterns
- Coverage reporting
- Test debugging setup

Generate the complete `.cursor-rules` file content that would be optimal for this specific project.
```

**Best Used With**:
- Cursor IDE setup
- Team development environment standardization
- Project onboarding
- TXT export for direct IDE configuration

## 🛠️ Creating Custom Templates

### Template File Structure

Templates are stored as JSON files in the `templates/` directory:

```json
{
  "name": "My Custom Template",
  "description": "Description of what this template does",
  "version": "1.0.0",
  "author": "Your Name",
  "category": "custom",
  "variables": {
    "PROJECT_NAME": {
      "type": "string",
      "default": "{{AUTO_DETECT}}",
      "description": "Name of the project"
    },
    "ANALYSIS_TYPE": {
      "type": "select",
      "options": ["security", "performance", "quality", "architecture"],
      "default": "quality",
      "description": "Type of analysis to perform"
    },
    "REVIEWER_NAME": {
      "type": "string",
      "default": "{{USER_NAME}}",
      "description": "Name of the person doing the review"
    }
  },
  "prompt": "Your template content here...\n\nUse {{PROJECT_NAME}} for variable substitution.\nAnalysis type: {{ANALYSIS_TYPE}}\nReviewer: {{REVIEWER_NAME}}"
}
```

### Variable Types

#### String Variables
```json
{
  "PROJECT_NAME": {
    "type": "string",
    "default": "My Project",
    "description": "Project name",
    "required": true
  }
}
```

#### Select Variables
```json
{
  "ANALYSIS_TYPE": {
    "type": "select",
    "options": ["security", "performance", "quality"],
    "default": "quality",
    "description": "Type of analysis"
  }
}
```

#### Boolean Variables
```json
{
  "INCLUDE_TESTS": {
    "type": "boolean",
    "default": true,
    "description": "Include test files in analysis"
  }
}
```

#### Auto-Detect Variables
```json
{
  "PROJECT_NAME": {
    "type": "string",
    "default": "{{AUTO_DETECT}}",
    "description": "Auto-detected from folder name"
  }
}
```

### Built-in Variable Substitutions

CodeFuser provides several built-in variables:

```
{{PROJECT_NAME}}        - Auto-detected project name
{{USER_NAME}}          - Current user name
{{DATE}}               - Current date (YYYY-MM-DD)
{{TIME}}               - Current time (HH:MM:SS)
{{TIMESTAMP}}          - ISO timestamp
{{FILE_COUNT}}         - Number of selected files
{{FILE_LIST}}          - List of selected files
{{PROJECT_DESCRIPTION}} - Auto-detected or user-provided
{{REVIEWER_NAME}}      - Current user or specified
{{REVIEW_DATE}}        - Current date formatted
{{CHANGED_FILES_COUNT}} - Number of files (for Git integration)
```

### Custom Template Examples

#### Security Audit Template
```json
{
  "name": "Security Audit",
  "description": "Comprehensive security analysis template",
  "version": "1.0.0",
  "category": "security",
  "variables": {
    "SECURITY_LEVEL": {
      "type": "select",
      "options": ["basic", "standard", "comprehensive", "enterprise"],
      "default": "standard",
      "description": "Level of security analysis"
    },
    "COMPLIANCE_STANDARD": {
      "type": "select",
      "options": ["OWASP", "PCI-DSS", "GDPR", "SOX", "HIPAA"],
      "default": "OWASP",
      "description": "Compliance standard to check against"
    }
  },
  "prompt": "# Security Audit: {{PROJECT_NAME}}\n\nPerform a {{SECURITY_LEVEL}} security analysis focusing on {{COMPLIANCE_STANDARD}} compliance.\n\n## Analysis Scope\n- Authentication and authorization mechanisms\n- Input validation and sanitization\n- Data encryption and protection\n- Session management\n- Error handling and information disclosure\n- Dependency vulnerabilities\n\nProvide specific findings with severity ratings and remediation steps."
}
```

#### Performance Analysis Template
```json
{
  "name": "Performance Analysis",
  "description": "Code performance optimization template",
  "version": "1.0.0",
  "category": "performance",
  "variables": {
    "TARGET_ENVIRONMENT": {
      "type": "select",
      "options": ["development", "staging", "production"],
      "default": "production",
      "description": "Target environment for analysis"
    },
    "PERFORMANCE_GOALS": {
      "type": "string",
      "default": "< 100ms response time",
      "description": "Performance targets"
    }
  },
  "prompt": "# Performance Analysis: {{PROJECT_NAME}}\n\nAnalyze code performance for {{TARGET_ENVIRONMENT}} environment.\n\n## Performance Goals\n{{PERFORMANCE_GOALS}}\n\n## Analysis Areas\n1. Algorithm complexity and optimization\n2. Database query performance\n3. Memory usage and garbage collection\n4. I/O operations and blocking calls\n5. Caching strategies\n6. Concurrency and parallel processing\n\nProvide specific optimization recommendations with expected impact."
}
```

## 🔧 Template Management

### Installing Custom Templates

1. **Create Template File**: Save as `templates/my_template.json`
2. **Restart CodeFuser**: Templates are loaded at startup
3. **Select Template**: Available in template dropdown

### Sharing Templates

#### Team Template Repository
```json
{
  "team_templates": {
    "repository_url": "https://github.com/yourteam/codefuser-templates",
    "auto_update": true,
    "templates": [
      "security_audit.json",
      "performance_review.json",
      "architecture_analysis.json"
    ]
  }
}
```

#### Template Package
```json
{
  "template_package": {
    "name": "Company Templates v1.0",
    "templates": [
      {
        "file": "security_audit.json",
        "category": "security"
      },
      {
        "file": "code_review.json",
        "category": "review"
      }
    ]
  }
}
```

### Template Validation

Templates are validated for:
- **JSON Syntax**: Valid JSON structure
- **Required Fields**: name, description, prompt
- **Variable Syntax**: Proper {{VARIABLE}} format
- **Circular References**: No self-referencing variables

### Template Testing

```json
{
  "template_test": {
    "template_file": "my_template.json",
    "test_variables": {
      "PROJECT_NAME": "Test Project",
      "ANALYSIS_TYPE": "security"
    },
    "expected_output": "Generated prompt should contain..."
  }
}
```

## 🚀 Advanced Template Features

### Conditional Content
```json
{
  "prompt": "# Analysis for {{PROJECT_NAME}}\n\n{{IF INCLUDE_TESTS}}## Test Analysis\nAnalyze test coverage and quality.{{ENDIF}}\n\n{{IF SECURITY_FOCUS}}## Security Review\nFocus on security vulnerabilities.{{ENDIF}}"
}
```

### Template Inheritance
```json
{
  "extends": "base_template.json",
  "override_variables": {
    "ANALYSIS_TYPE": "security"
  },
  "additional_prompt": "\n\n## Additional Security Checks\n..."
}
```

### Multi-Language Templates
```json
{
  "name": "Code Review",
  "localized": {
    "en": {
      "name": "Code Review",
      "description": "Comprehensive code review template"
    },
    "tr": {
      "name": "Kod İncelemesi",
      "description": "Kapsamlı kod inceleme şablonu"
    }
  }
}
```

## 💡 Template Best Practices

### ✅ Do This
- **Clear Descriptions**: Explain what the template does
- **Logical Variables**: Use meaningful variable names
- **Structured Prompts**: Organize with headers and sections
- **Specific Instructions**: Be clear about expected outputs
- **Version Control**: Track template changes
- **Test Templates**: Validate with sample projects

### ❌ Avoid This
- **Generic Prompts**: Too broad or vague instructions
- **Too Many Variables**: Keep it simple and focused
- **Circular Dependencies**: Variables referencing themselves
- **Overly Long Prompts**: Keep under 2000 characters
- **Hardcoded Values**: Use variables for flexibility

### 🎯 Template Categories

Organize templates by purpose:
- **Analysis**: General code analysis templates
- **Security**: Security-focused templates
- **Performance**: Performance optimization templates
- **Documentation**: Documentation generation templates
- **Review**: Code review and quality templates
- **Custom**: Organization-specific templates

---

**Ready to create powerful templates?** Start with the built-in templates and customize them for your specific needs!

*Continue to [Smart Filters](Smart-Filters-EN) to learn about combining templates with advanced filtering →*