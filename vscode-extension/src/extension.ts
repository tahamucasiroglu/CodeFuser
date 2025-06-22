import * as vscode from 'vscode';
import * as fs from 'fs';
import * as path from 'path';

export function activate(context: vscode.ExtensionContext) {
    console.log('CodeFuser extension is now active!');

    // Register main command
    let openPanelCommand = vscode.commands.registerCommand('codefuser.openPanel', () => {
        CodeFuserPanel.createOrShow(context.extensionUri);
    });

    // Register quick export command
    let quickExportCommand = vscode.commands.registerCommand('codefuser.quickExport', async (uri: vscode.Uri) => {
        if (uri) {
            await quickExportFiles(uri);
        }
    });

    context.subscriptions.push(openPanelCommand, quickExportCommand);
}

async function quickExportFiles(uri: vscode.Uri) {
    const config = vscode.workspace.getConfiguration('codefuser');
    const outputFormat = config.get<string>('defaultOutputFormat', 'txt');
    
    try {
        // Get files to export
        const files = await getFilesFromUri(uri);
        
        if (files.length === 0) {
            vscode.window.showWarningMessage('No files found to export');
            return;
        }

        // Ask for output location
        const outputUri = await vscode.window.showSaveDialog({
            defaultUri: vscode.Uri.file(path.join(uri.fsPath, `codefuser_export.${outputFormat}`)),
            filters: {
                'Text files': ['txt'],
                'HTML files': ['html'],
                'Word documents': ['docx'],
                'PDF files': ['pdf']
            }
        });

        if (outputUri) {
            await exportFiles(files, outputUri, outputFormat);
            vscode.window.showInformationMessage(`Files exported to ${outputUri.fsPath}`);
        }
    } catch (error) {
        vscode.window.showErrorMessage(`Export failed: ${error}`);
    }
}

async function getFilesFromUri(uri: vscode.Uri): Promise<string[]> {
    const stat = await vscode.workspace.fs.stat(uri);
    const files: string[] = [];

    if (stat.type === vscode.FileType.File) {
        files.push(uri.fsPath);
    } else if (stat.type === vscode.FileType.Directory) {
        const entries = await vscode.workspace.fs.readDirectory(uri);
        for (const [name, type] of entries) {
            if (type === vscode.FileType.File && shouldIncludeFile(name)) {
                files.push(path.join(uri.fsPath, name));
            }
        }
    }

    return files;
}

function shouldIncludeFile(filename: string): boolean {
    const extensions = ['.js', '.ts', '.tsx', '.jsx', '.py', '.cs', '.java', '.cpp', '.c', '.h', '.html', '.css', '.scss'];
    const ignoreFiles = ['.env', '.gitignore', 'package-lock.json', 'yarn.lock'];
    
    return extensions.some(ext => filename.endsWith(ext)) && !ignoreFiles.includes(filename);
}

async function exportFiles(files: string[], outputUri: vscode.Uri, format: string) {
    let content = `# CodeFuser Export\n# Generated: ${new Date().toISOString()}\n# Total Files: ${files.length}\n\n`;
    
    for (const file of files) {
        try {
            const fileContent = fs.readFileSync(file, 'utf8');
            const relativePath = vscode.workspace.asRelativePath(file);
            
            content += `\n=== FILE: ${relativePath} ===\n`;
            content += `\n${fileContent}\n`;
        } catch (error) {
            console.error(`Error reading file ${file}:`, error);
        }
    }
    
    fs.writeFileSync(outputUri.fsPath, content, 'utf8');
}

class CodeFuserPanel {
    public static currentPanel: CodeFuserPanel | undefined;
    public static readonly viewType = 'codefuser';

    private readonly _panel: vscode.WebviewPanel;
    private readonly _extensionUri: vscode.Uri;
    private _disposables: vscode.Disposable[] = [];

    public static createOrShow(extensionUri: vscode.Uri) {
        const column = vscode.window.activeTextEditor
            ? vscode.window.activeTextEditor.viewColumn
            : undefined;

        if (CodeFuserPanel.currentPanel) {
            CodeFuserPanel.currentPanel._panel.reveal(column);
            return;
        }

        const panel = vscode.window.createWebviewPanel(
            CodeFuserPanel.viewType,
            'CodeFuser',
            column || vscode.ViewColumn.One,
            {
                enableScripts: true,
                localResourceRoots: [vscode.Uri.joinPath(extensionUri, 'media')]
            }
        );

        CodeFuserPanel.currentPanel = new CodeFuserPanel(panel, extensionUri);
    }

    private constructor(panel: vscode.WebviewPanel, extensionUri: vscode.Uri) {
        this._panel = panel;
        this._extensionUri = extensionUri;

        this._update();

        this._panel.onDidDispose(() => this.dispose(), null, this._disposables);
    }

    public dispose() {
        CodeFuserPanel.currentPanel = undefined;

        this._panel.dispose();

        while (this._disposables.length) {
            const x = this._disposables.pop();
            if (x) {
                x.dispose();
            }
        }
    }

    private _update() {
        const webview = this._panel.webview;
        this._panel.title = 'CodeFuser';
        this._panel.webview.html = this._getHtmlForWebview(webview);
    }

    private _getHtmlForWebview(webview: vscode.Webview) {
        // Get logo URI
        const logoUri = webview.asWebviewUri(
            vscode.Uri.joinPath(this._extensionUri, 'assets', 'CodeFuser Logo.png')
        );
        
        return `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CodeFuser</title>
    <style>
        body {
            font-family: var(--vscode-font-family);
            color: var(--vscode-foreground);
            background-color: var(--vscode-editor-background);
            padding: 20px;
        }
        .header {
            text-align: center;
            margin-bottom: 30px;
        }
        .logo {
            font-size: 24px;
            font-weight: bold;
            color: var(--vscode-textLink-foreground);
        }
        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }
        .feature-card {
            border: 1px solid var(--vscode-panel-border);
            border-radius: 8px;
            padding: 20px;
            background: var(--vscode-editor-background);
        }
        .feature-title {
            font-weight: bold;
            margin-bottom: 10px;
            color: var(--vscode-textLink-foreground);
        }
        .btn {
            background: var(--vscode-button-background);
            color: var(--vscode-button-foreground);
            border: none;
            padding: 10px 20px;
            border-radius: 4px;
            cursor: pointer;
            margin: 5px;
        }
        .btn:hover {
            background: var(--vscode-button-hoverBackground);
        }
        .section {
            margin: 20px 0;
            padding: 20px;
            border: 1px solid var(--vscode-panel-border);
            border-radius: 8px;
        }
    </style>
</head>
<body>
    <div class="header">
        <img src="${logoUri}" alt="CodeFuser Logo" style="width: 64px; height: 64px; margin-bottom: 10px;">
        <div class="logo">🚀 CodeFuser</div>
        <p>Combine project files into a single output with AI prompts</p>
    </div>

    <div class="section">
        <h3>Quick Actions</h3>
        <button class="btn" onclick="openStandaloneApp()">📱 Open Standalone App</button>
        <button class="btn" onclick="exportCurrentWorkspace()">📤 Export Current Workspace</button>
        <button class="btn" onclick="showDocumentation()">📚 Documentation</button>
    </div>

    <div class="features">
        <div class="feature-card">
            <div class="feature-title">🎯 Smart Templates</div>
            <p>16x Prompt, Cursor Rules, Claude Project, Documentation templates with variable substitution</p>
        </div>
        <div class="feature-card">
            <div class="feature-title">🔍 Advanced Filters</div>
            <p>Git integration, Smart content analysis, File type detection, Custom filtering</p>
        </div>
        <div class="feature-card">
            <div class="feature-title">📄 Multiple Formats</div>
            <p>Export to TXT, HTML (with syntax highlighting), DOCX, PDF formats</p>
        </div>
        <div class="feature-card">
            <div class="feature-title">🌍 Multi-Language</div>
            <p>Turkish and English interface with extensible localization system</p>
        </div>
    </div>

    <div class="section">
        <h3>Usage</h3>
        <ol>
            <li>Right-click on any folder or file in Explorer</li>
            <li>Select "Quick Export Selected Files" for instant export</li>
            <li>Or use "Open CodeFuser" for full-featured interface</li>
            <li>Choose template, apply filters, and export!</li>
        </ol>
    </div>

    <script>
        const vscode = acquireVsCodeApi();

        function openStandaloneApp() {
            vscode.postMessage({
                command: 'openStandalone'
            });
        }

        function exportCurrentWorkspace() {
            vscode.postMessage({
                command: 'exportWorkspace'
            });
        }

        function showDocumentation() {
            vscode.postMessage({
                command: 'showDocs'
            });
        }
    </script>
</body>
</html>`;
    }
}

export function deactivate() {}