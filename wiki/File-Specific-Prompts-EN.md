# 🎯 File-Specific Prompts Guide

**The revolutionary feature that makes CodeFuser v2.0 the most powerful AI code analysis tool.**

## 🔥 What Makes This Revolutionary?

### Before CodeFuser v2.0
```
Traditional tools: "Here's my entire codebase, analyze it"
Result: Generic analysis across all files
```

### With CodeFuser v2.0
```
CodeFuser v2.0: "Here's my codebase with specific instructions for each file"
├── auth.py → "Focus on security vulnerabilities and authentication flows"
├── api.py → "Check for rate limiting and input validation" 
├── database.py → "Analyze query performance and connection handling"
└── utils.py → "Review helper functions for potential optimizations"
Result: Targeted, precise analysis for each component
```

## 📋 Step-by-Step Tutorial

### Step 1: Understanding the Interface
1. **Scan your project** to see all files in the file tree
2. **Look for the 📄 icons** next to each file name
3. **Notice the checkbox layout**: `☑️   📄  🐍 filename.py`
4. **Observe the spacing** - checkboxes and icons are properly separated

### Step 2: Adding Your First File-Specific Prompt
1. **Find a critical file** (like `main.py` or `app.py`)
2. **Click the 📄 icon** next to that file
3. **A dialog window opens** with:
   - File name and path at the top
   - Large text area for your prompt
   - Character counter
   - Example prompts button
   - Save/Cancel buttons

### Step 3: Writing Effective Prompts
```
✅ GOOD Examples:
- "Analyze the error handling in this authentication module"
- "Check for SQL injection vulnerabilities in these database queries"
- "Review the caching logic for potential race conditions"
- "Examine the API endpoints for proper input validation"

❌ POOR Examples:
- "Look at this file" (too generic)
- "Fix bugs" (not specific enough)
- "Make it better" (no actionable direction)
```

### Step 4: Using the Visual Feedback System
After adding prompts, notice how file backgrounds change:

- 🟢 **Green**: `☑️   📝✨  🐍 auth.py` - Selected + Custom Prompt *(Perfect!)*
- 🟡 **Yellow**: `☑️   📄   🐍 utils.py` - Selected Only *(Good)*
- 🔴 **Red**: `☐   📝✨  🐍 old_code.py` - Prompt Only *(Warning!)*

## 🎨 Advanced Techniques

### Multi-Layer Prompting Strategy
```
Layer 1 - General Template: "Code Review"
Layer 2 - File-Specific Prompts:
├── security.py → "Focus on authentication and authorization"
├── payment.py → "Check for financial transaction security"
├── logging.py → "Review for sensitive data exposure"
└── config.py → "Verify secure configuration management"
```

### Domain-Specific Prompt Patterns

#### 🔒 Security Analysis
```
auth.py → "Analyze authentication mechanisms for:
- Password policy enforcement
- Session management security
- Multi-factor authentication implementation
- Protection against timing attacks"

api.py → "Review API security for:
- Input validation and sanitization
- Rate limiting implementation
- CORS configuration
- Authentication token handling"
```

#### ⚡ Performance Optimization
```
database.py → "Examine database operations for:
- N+1 query problems
- Missing indexes
- Connection pool efficiency
- Transaction boundary optimization"

cache.py → "Analyze caching strategy for:
- Cache invalidation logic
- Memory usage patterns
- Race condition prevention
- TTL configuration effectiveness"
```

#### 🧪 Code Quality Review
```
models.py → "Review data models for:
- Proper validation rules
- Relationship definitions
- Index optimization opportunities
- Migration compatibility"

utils.py → "Examine utility functions for:
- Code reusability
- Error handling completeness
- Performance bottlenecks
- Documentation quality"
```

## 🎯 Pro Tips and Best Practices

### ✅ Do This for Maximum Impact

#### 1. **Be Contextually Specific**
```
Instead of: "Review this file"
Write: "Analyze the payment processing logic for PCI compliance and error handling"
```

#### 2. **Include Expected Outputs**
```
"Review the API authentication and provide:
1. Security vulnerability assessment
2. Recommended improvements
3. Code examples for fixes"
```

#### 3. **Use Action-Oriented Language**
```
✅ "Identify", "Analyze", "Review", "Check", "Examine"
❌ "Look at", "See", "Consider"
```

#### 4. **Reference Specific Technologies**
```
"Analyze this Django model for:
- Proper use of select_related() and prefetch_related()
- Index optimization for PostgreSQL
- Migration safety for production deployment"
```

### ❌ Common Mistakes to Avoid

#### 1. **Generic Prompts**
```
❌ "Make this better"
✅ "Optimize the database query performance in this module"
```

#### 2. **Overly Long Prompts**
Keep prompts under 500 characters for best results.

#### 3. **Unused Prompts**
Red background files have prompts but aren't selected - either select them or remove the prompt.

#### 4. **Inconsistent Prompt Styles**
Use similar structures across files for consistent analysis.

## 📊 Monitoring Your Prompt Strategy

### Understanding the Counter
The file counter shows: `"12 / 45 files selected • 8 with prompts • ⚠️ 2 unused prompts"`

- **12 / 45**: Total selection status
- **8 with prompts**: Files that have custom instructions
- **⚠️ 2 unused**: Files with prompts but not selected (red background)

### Optimization Targets
- **Green files**: 70-80% (core functionality with specific prompts)
- **Yellow files**: 15-25% (supporting files, general analysis)
- **Red files**: 0-5% (should be minimized)

## 🔧 Technical Features

### Dialog Window Features
- **640x640 optimal size** for comfortable prompt writing
- **Character counter** with color coding (green < 500, orange < 1000, red > 1000)
- **Example prompts library** with 8 pre-written examples
- **Auto-save functionality** preserves prompts between sessions
- **Keyboard shortcuts**: Ctrl+Enter to save, Ctrl+A to select all

### Integration with Export Formats

#### TXT Export
```
=== FILE: src/auth.py ===

[CUSTOM PROMPT FOR THIS FILE]
Analyze authentication mechanisms for security vulnerabilities

[CONTENT]
def authenticate_user(username, password):
    # ... code content ...
```

#### HTML Export
File-specific prompts appear in highlighted orange boxes above each file's content.

#### DOCX Export
Custom prompts are formatted as styled headings with orange text.

#### PDF Export  
Prompts are included as separate sections with distinct formatting.

## 🚀 Advanced Workflows

### Workflow 1: Security Audit
1. **Filter for security-critical files** (auth, api, crypto, etc.)
2. **Add security-specific prompts** to each file
3. **Use "Code Review" template** as base
4. **Export as DOCX** for formal documentation
5. **Generate comprehensive security report**

### Workflow 2: Performance Analysis
1. **Select performance-critical files** (database, cache, algorithms)
2. **Add performance-focused prompts** with specific metrics
3. **Use "16x Prompt" template** for detailed analysis
4. **Export as HTML** for interactive review
5. **Iterate based on AI feedback**

### Workflow 3: Code Review Process
1. **Use Git integration** to show only changed files
2. **Add review-specific prompts** based on change context
3. **Include testing prompts** for new functionality
4. **Export as multiple formats** for different stakeholders
5. **Track prompt effectiveness** over time

## 🔮 Future Enhancements (Coming Soon)

- **Prompt Templates**: Save and reuse prompt sets across projects
- **Smart Suggestions**: AI-powered prompt recommendations based on file content
- **Bulk Assignment**: Apply prompts to multiple files by pattern matching
- **Prompt History**: Track and reuse previously effective prompts
- **Team Sharing**: Share prompt strategies across development teams

---

**Ready to master file-specific prompts?** Start with a small project and gradually build your prompt library!

*Continue to [Templates Guide](Templates-Guide-EN) to learn about powerful template combinations →*