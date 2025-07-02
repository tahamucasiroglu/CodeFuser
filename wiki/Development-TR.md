# 👨‍💻 Geliştirme Rehberi

CodeFuser v2.0'a katkıda bulunma, işlevselliği genişletme ve özel entegrasyonlar oluşturma için kapsamlı rehber.

## 🚀 Başlangıç

### Geliştirme Ortamı Kurulumu

#### Ön Koşullar
```bash
# Gerekli Yazılımlar
- Python 3.8+ (3.9+ önerilen)
- Git
- Kod Editörü (VS Code, PyCharm, vb.)
- Virtual Environment aracı (venv, conda, virtualenv)

# İsteğe Bağlı Araçlar
- Docker (konteynerleştirilmiş geliştirme için)
- Node.js (web tabanlı uzantılar için)
- PostgreSQL/SQLite (veritabanı özellikler için)
```

#### Clone ve Kurulum
```bash
# Depoyu fork'la
# Fork'unu clone et
git clone https://github.com/your-username/CodeFuser.git
cd CodeFuser

# Virtual environment oluştur
python -m venv venv

# Virtual environment'ı aktifleştir
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# Bağımlılıkları yükle
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Geliştirme modunda yükle
pip install -e .
```

#### Geliştirme Bağımlılıkları
```txt
# requirements-dev.txt
pytest>=7.0.0
pytest-cov>=4.0.0
black>=22.0.0
flake8>=5.0.0
mypy>=1.0.0
pre-commit>=2.20.0
sphinx>=5.0.0
sphinx-rtd-theme>=1.0.0
```

### Proje Yapısı

#### Temel Mimari
```
CodeFuser/
├── src/                          # Ana kaynak kodu
│   ├── __init__.py
│   ├── main_app.py              # Ana uygulama giriş noktası
│   ├── file_tree_widget.py     # Dosya ağacı bileşeni
│   ├── file_prompt_dialog.py   # Özel prompt dialogu
│   ├── export_manager.py       # Export işlevselliği
│   ├── template_manager.py     # Şablon sistemi
│   ├── git_integration.py      # Git özellikleri
│   ├── smart_filters.py        # Filtreleme sistemi
│   └── utils/                   # Yardımcı modüller
│       ├── file_utils.py
│       ├── config_manager.py
│       └── localization.py
├── config/                      # Yapılandırma dosyaları
│   ├── default_settings.json
│   └── user_settings.json
├── templates/                   # Yerleşik şablonlar
│   ├── 16x_prompt.json
│   ├── claude_project.json
│   └── ...
├── locales/                     # Uluslararasılaştırma
│   ├── en.json
│   └── tr.json
├── tests/                       # Test paketi
│   ├── unit/
│   ├── integration/
│   └── fixtures/
├── docs/                        # Dokümantasyon
├── assets/                      # Statik varlıklar
├── main.py                      # Giriş noktası
├── build_exe.py                # Build scripti
└── requirements.txt
```

#### Modül Bağımlılıkları
```python
# Temel Bağımlılıklar
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import json
import os
import subprocess
from pathlib import Path
from typing import Dict, List, Optional, Union

# Export Bağımlılıkları
from docx import Document
from reportlab.pdfgen import canvas
import html
import base64

# Git Entegrasyonu
import git
from git import Repo, InvalidGitRepositoryError

# Şablon Sistemi
import jinja2
from jinja2 import Template, Environment
```

## 🏗️ Mimari Genel Bakış

### Temel Bileşenler

#### 1. Ana Uygulama (main_app.py)
```python
class CodeFuserApp:
    """Ana uygulama kontrolcüsü"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.config_manager = ConfigManager()
        self.template_manager = TemplateManager()
        self.export_manager = ExportManager()
        self.file_tree = FileTreeWidget(self.root)
        
    def initialize_ui(self):
        """Ana kullanıcı arayüzünü kur"""
        pass
        
    def handle_export(self):
        """Export işlemlerini yönet"""
        pass
```

#### 2. Dosya Ağacı Widget'ı (file_tree_widget.py)
```python
class FileTreeWidget:
    """Özel prompt'lar ile gelişmiş dosya ağacı"""
    
    def __init__(self, parent):
        self.parent = parent
        self.selected_files = set()
        self.file_prompts = {}  # Dosya-özel prompt'lar
        
    def populate_tree(self, root_path: str):
        """Ağacı dosya ve klasörlerle doldur"""
        pass
        
    def handle_document_icon_click(self, file_path: str):
        """Özel prompt ikon tıklamalarını işle"""
        pass
        
    def apply_row_color(self, file_path: str):
        """Dosya durumuna göre renk kodlama uygula"""
        pass
```

#### 3. Export Manager (export_manager.py)
```python
class ExportManager:
    """Tüm export işlemlerini yönet"""
    
    def __init__(self):
        self.supported_formats = ['txt', 'html', 'docx', 'pdf']
        
    def export_to_format(self, format_type: str, data: dict, output_path: str):
        """Veriyi belirtilen formata export et"""
        exporters = {
            'txt': self._export_txt,
            'html': self._export_html,
            'docx': self._export_docx,
            'pdf': self._export_pdf
        }
        return exporters[format_type](data, output_path)
```

#### 4. Şablon Manager (template_manager.py)
```python
class TemplateManager:
    """Şablon sistemi yönetimi"""
    
    def __init__(self):
        self.templates = {}
        self.load_templates()
        
    def load_templates(self):
        """Tüm mevcut şablonları yükle"""
        pass
        
    def render_template(self, template_name: str, variables: dict) -> str:
        """Şablonu değişkenlerle render et"""
        pass
        
    def validate_template(self, template_data: dict) -> bool:
        """Şablon yapısını doğrula"""
        pass
```

### Tasarım Desenleri

#### 1. Observer Deseni
```python
class EventManager:
    """Merkezi olay yönetimi"""
    
    def __init__(self):
        self.listeners = {}
        
    def subscribe(self, event_type: str, callback):
        """Olaylara abone ol"""
        if event_type not in self.listeners:
            self.listeners[event_type] = []
        self.listeners[event_type].append(callback)
        
    def notify(self, event_type: str, data=None):
        """Tüm dinleyicileri bilgilendir"""
        for callback in self.listeners.get(event_type, []):
            callback(data)
```

#### 2. Strategy Deseni
```python
class ExportStrategy:
    """Temel export stratejisi"""
    
    def export(self, data: dict, output_path: str):
        raise NotImplementedError
        
class HTMLExportStrategy(ExportStrategy):
    """HTML export implementasyonu"""
    
    def export(self, data: dict, output_path: str):
        # HTML-özel export mantığı
        pass
```

#### 3. Factory Deseni
```python
class ExportFactory:
    """Exporter'ları oluşturan factory"""
    
    @staticmethod
    def create_exporter(format_type: str) -> ExportStrategy:
        exporters = {
            'html': HTMLExportStrategy,
            'pdf': PDFExportStrategy,
            'docx': DOCXExportStrategy,
            'txt': TXTExportStrategy
        }
        return exporters[format_type]()
```

## 🔧 Geliştirme İş Akışı

### Kod Stili ve Standartları

#### Python Stil Rehberi
```python
# Formatlama için Black kullan
black src/ tests/

# Linting için flake8 kullan
flake8 src/ tests/

# Tip kontrolü için mypy kullan
mypy src/

# Düzgün formatlanmış kod örneği
def process_files(
    file_paths: List[str], 
    output_format: str,
    template_name: Optional[str] = None
) -> Dict[str, Any]:
    """
    Export için dosyaları işle.
    
    Args:
        file_paths: İşlenecek dosya yollarının listesi
        output_format: Hedef export formatı
        template_name: Kullanılacak opsiyonel şablon
        
    Returns:
        İşlenmiş veri içeren dictionary
        
    Raises:
        ValueError: Format desteklenmiyorsa
        FileNotFoundError: Dosyalar mevcut değilse
    """
    if output_format not in SUPPORTED_FORMATS:
        raise ValueError(f"Desteklenmeyen format: {output_format}")
        
    result = {
        "files": [],
        "metadata": {},
        "statistics": {}
    }
    
    for file_path in file_paths:
        if not Path(file_path).exists():
            raise FileNotFoundError(f"Dosya bulunamadı: {file_path}")
            
        # Dosyayı işle...
        
    return result
```

#### Git İş Akışı
```bash
# Feature geliştirme iş akışı
git checkout main
git pull origin main
git checkout -b feature/new-export-format

# Değişiklik yap...
git add .
git commit -m "feat: yeni export format desteği ekle

- XML export işlevselliği ekle
- Export manager'ı güncelle
- XML export için testler ekle"

# Push ve PR oluştur
git push origin feature/new-export-format
# GitHub'da pull request oluştur
```

#### Pre-commit Hook'ları
```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: 22.3.0
    hooks:
      - id: black
        language_version: python3.9

  - repo: https://github.com/pycqa/flake8
    rev: 4.0.1
    hooks:
      - id: flake8

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v0.950
    hooks:
      - id: mypy
```

### Test Stratejisi

#### Birim Testleri
```python
# tests/unit/test_template_manager.py
import pytest
from src.template_manager import TemplateManager

class TestTemplateManager:
    
    @pytest.fixture
    def template_manager(self):
        return TemplateManager()
        
    def test_load_templates(self, template_manager):
        """Şablon yüklemeyi test et"""
        template_manager.load_templates()
        assert len(template_manager.templates) > 0
        
    def test_render_template(self, template_manager):
        """Şablon render'ını test et"""
        template_data = {
            "name": "Test Şablonu",
            "prompt": "{{PROJECT_NAME}} güvenlik sorunları için analiz et",
            "variables": {
                "PROJECT_NAME": {"type": "string", "default": "TestProject"}
            }
        }
        
        rendered = template_manager.render_template(template_data, {
            "PROJECT_NAME": "MyApp"
        })
        
        assert "MyApp güvenlik sorunları için analiz et" in rendered
        
    def test_invalid_template(self, template_manager):
        """Geçersiz şablon validasyonunu test et"""
        invalid_template = {"name": "Geçersiz"}  # Gerekli alanlar eksik
        
        with pytest.raises(ValueError):
            template_manager.validate_template(invalid_template)
```

#### Entegrasyon Testleri
```python
# tests/integration/test_export_workflow.py
import pytest
import tempfile
from pathlib import Path
from src.main_app import CodeFuserApp

class TestExportWorkflow:
    
    @pytest.fixture
    def app(self):
        return CodeFuserApp()
        
    @pytest.fixture
    def sample_project(self):
        """Test için örnek proje oluştur"""
        with tempfile.TemporaryDirectory() as temp_dir:
            project_dir = Path(temp_dir)
            
            # Örnek dosyalar oluştur
            (project_dir / "main.py").write_text("print('Merhaba Dünya')")
            (project_dir / "utils.py").write_text("def helper(): pass")
            
            yield project_dir
            
    def test_full_export_workflow(self, app, sample_project):
        """Tam export iş akışını test et"""
        # Kurulum
        app.file_tree.populate_tree(str(sample_project))
        app.file_tree.select_all_files()
        
        # Şablon ayarla ve export et
        app.set_template("16x_prompt")
        
        with tempfile.NamedTemporaryFile(suffix=".html") as output_file:
            result = app.export_manager.export_to_format(
                "html", 
                app.get_export_data(),
                output_file.name
            )
            
            assert result.success
            assert Path(output_file.name).exists()
            
            # İçeriği doğrula
            content = Path(output_file.name).read_text()
            assert "Merhaba Dünya" in content
            assert "16x Prompt" in content
```

#### Test Yapılandırması
```ini
# pytest.ini
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = 
    --cov=src
    --cov-report=html
    --cov-report=term-missing
    --cov-fail-under=80
```

## 🔌 Plugin Geliştirme

### Plugin Mimarisi

#### Plugin Arayüzü
```python
# src/plugins/base_plugin.py
from abc import ABC, abstractmethod
from typing import Dict, Any

class BasePlugin(ABC):
    """Tüm plugin'ler için temel sınıf"""
    
    def __init__(self):
        self.name = ""
        self.version = "1.0.0"
        self.description = ""
        
    @abstractmethod
    def initialize(self, app_context: Dict[str, Any]):
        """Plugin'i uygulama bağlamı ile başlat"""
        pass
        
    @abstractmethod
    def get_capabilities(self) -> Dict[str, Any]:
        """Plugin yeteneklerini döndür"""
        pass
        
    def cleanup(self):
        """Kaynakları temizle"""
        pass
```

#### Export Plugin Örneği
```python
# plugins/xml_exporter.py
from src.plugins.base_plugin import BasePlugin
import xml.etree.ElementTree as ET

class XMLExportPlugin(BasePlugin):
    """XML export plugin'i"""
    
    def __init__(self):
        super().__init__()
        self.name = "XML Exporter"
        self.version = "1.0.0"
        self.description = "Kod analizini XML formatına export et"
        
    def initialize(self, app_context):
        """XML export yeteneğini kaydet"""
        export_manager = app_context['export_manager']
        export_manager.register_format('xml', self.export_xml)
        
    def get_capabilities(self):
        return {
            "export_formats": ["xml"],
            "features": ["structured_data", "schema_validation"]
        }
        
    def export_xml(self, data: dict, output_path: str):
        """Veriyi XML formatına export et"""
        root = ET.Element("code_analysis")
        
        # Metadata ekle
        metadata = ET.SubElement(root, "metadata")
        ET.SubElement(metadata, "generated_at").text = data.get("timestamp", "")
        ET.SubElement(metadata, "total_files").text = str(data.get("file_count", 0))
        
        # Dosyaları ekle
        files_elem = ET.SubElement(root, "files")
        for file_data in data.get("files", []):
            file_elem = ET.SubElement(files_elem, "file")
            file_elem.set("path", file_data["path"])
            
            if file_data.get("custom_prompt"):
                prompt_elem = ET.SubElement(file_elem, "custom_prompt")
                prompt_elem.text = file_data["custom_prompt"]
                
            content_elem = ET.SubElement(file_elem, "content")
            content_elem.text = file_data["content"]
            
        # Dosyaya yaz
        tree = ET.ElementTree(root)
        tree.write(output_path, encoding="utf-8", xml_declaration=True)
```

#### Plugin Manifest'i
```json
{
  "name": "XML Exporter",
  "version": "1.0.0",
  "description": "Kod analizini XML formatına export et",
  "author": "Geliştirici Adı",
  "entry_point": "xml_exporter.XMLExportPlugin",
  "dependencies": {
    "python": ">=3.8",
    "packages": []
  },
  "capabilities": {
    "export_formats": ["xml"],
    "hooks": ["pre_export", "post_export"]
  },
  "configuration": {
    "xml_schema": "schema.xsd",
    "validation": true,
    "pretty_print": true
  }
}
```

### Özel Şablon Geliştirme

#### Şablon Yapısı
```json
{
  "name": "Güvenlik Denetimi Şablonu",
  "description": "Kapsamlı güvenlik analizi şablonu",
  "version": "1.0.0",
  "author": "Güvenlik Ekibi",
  "category": "security",
  "variables": {
    "COMPLIANCE_FRAMEWORK": {
      "type": "select",
      "options": ["OWASP", "NIST", "ISO27001", "PCI-DSS"],
      "default": "OWASP",
      "description": "Güvenlik uyum çerçevesi"
    },
    "SECURITY_LEVEL": {
      "type": "select",
      "options": ["basic", "standard", "comprehensive"],
      "default": "standard",
      "description": "Güvenlik analizi derinliği"
    },
    "FOCUS_AREAS": {
      "type": "multiselect",
      "options": [
        "authentication", "authorization", "input_validation",
        "data_protection", "session_management", "error_handling"
      ],
      "default": ["authentication", "authorization"],
      "description": "Odaklanılacak güvenlik alanları"
    }
  },
  "conditional_sections": {
    "include_compliance_check": "{{COMPLIANCE_FRAMEWORK}} != 'custom'",
    "include_advanced_analysis": "{{SECURITY_LEVEL}} == 'comprehensive'"
  },
  "prompt": "# {{PROJECT_NAME}} için Güvenlik Analizi\\n\\n{{COMPLIANCE_FRAMEWORK}} uyumuna odaklanan {{SECURITY_LEVEL}} güvenlik denetimi yapın.\\n\\n## Analiz Kapsamı\\n{{#each FOCUS_AREAS}}\\n- {{this}}\\n{{/each}}\\n\\n{{#if include_compliance_check}}\\n## Uyum Gereksinimleri\\nKodun {{COMPLIANCE_FRAMEWORK}} standartlarını karşıladığından emin olun.\\n{{/if}}\\n\\n{{#if include_advanced_analysis}}\\n## Gelişmiş Güvenlik Analizi\\n- Tehdit modelleme\\n- Saldırı yüzeyi analizi\\n- Kriptografik implementasyon incelemesi\\n{{/if}}\\n\\nÖnem derecesi ve çözüm adımlarıyla spesifik bulgular sağlayın."
}
```

#### Şablon Motor Entegrasyonu
```python
# src/template_engine.py
from jinja2 import Environment, FileSystemLoader, Template
from typing import Dict, Any

class TemplateEngine:
    """Gelişmiş şablon render motoru"""
    
    def __init__(self, template_dirs: List[str]):
        self.env = Environment(loader=FileSystemLoader(template_dirs))
        self.env.globals.update({
            'project_name': self._get_project_name,
            'current_date': self._get_current_date,
            'file_count': self._get_file_count
        })
        
    def render_template(self, template_data: dict, context: dict) -> str:
        """Gelişmiş özelliklerle şablon render et"""
        template = Template(template_data['prompt'])
        
        # Koşullu bölümleri işle
        processed_context = self._process_conditionals(
            template_data, context
        )
        
        # Yerleşik değişkenleri ekle
        processed_context.update(self._get_builtin_variables(context))
        
        return template.render(**processed_context)
        
    def _process_conditionals(self, template_data: dict, context: dict) -> dict:
        """Koşullu şablon bölümlerini işle"""
        result = context.copy()
        
        for condition_name, condition_expr in template_data.get('conditional_sections', {}).items():
            # Koşulu değerlendir
            try:
                condition_result = self._evaluate_condition(condition_expr, context)
                result[condition_name] = condition_result
            except Exception as e:
                logger.warning(f"Koşul {condition_name} değerlendirilemedi: {e}")
                result[condition_name] = False
                
        return result
```

## 🌐 API Geliştirme

### REST API Arayüzü

#### API Server Kurulumu
```python
# src/api/server.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import threading

class CodeFuserAPI:
    """CodeFuser için REST API"""
    
    def __init__(self, app_instance):
        self.app = Flask(__name__)
        CORS(self.app)
        self.codefuser_app = app_instance
        self.setup_routes()
        
    def setup_routes(self):
        """API rotalarını kur"""
        
        @self.app.route('/api/v1/scan', methods=['POST'])
        def scan_project():
            """Proje dizinini tara"""
            data = request.json
            project_path = data.get('path')
            
            if not project_path:
                return jsonify({'error': 'Proje yolu gerekli'}), 400
                
            try:
                files = self.codefuser_app.scan_directory(project_path)
                return jsonify({
                    'success': True,
                    'files': files,
                    'count': len(files)
                })
            except Exception as e:
                return jsonify({'error': str(e)}), 500
                
        @self.app.route('/api/v1/export', methods=['POST'])
        def export_analysis():
            """Kod analizini export et"""
            data = request.json
            
            try:
                result = self.codefuser_app.export_manager.export_to_format(
                    data.get('format', 'html'),
                    data.get('export_data'),
                    data.get('output_path')
                )
                
                return jsonify({
                    'success': True,
                    'output_path': result.output_path,
                    'file_size': result.file_size
                })
            except Exception as e:
                return jsonify({'error': str(e)}), 500
                
        @self.app.route('/api/v1/templates', methods=['GET'])
        def get_templates():
            """Mevcut şablonları getir"""
            templates = self.codefuser_app.template_manager.get_templates()
            return jsonify({
                'templates': [
                    {
                        'name': t.name,
                        'description': t.description,
                        'version': t.version,
                        'variables': t.variables
                    }
                    for t in templates
                ]
            })
            
    def start_server(self, host='localhost', port=5000):
        """API server'ı ayrı thread'de başlat"""
        def run_server():
            self.app.run(host=host, port=port, debug=False)
            
        server_thread = threading.Thread(target=run_server, daemon=True)
        server_thread.start()
        return server_thread
```

#### API Client Kütüphanesi
```python
# src/api/client.py
import requests
from typing import Dict, List, Optional

class CodeFuserClient:
    """CodeFuser API için Python client'ı"""
    
    def __init__(self, base_url: str = "http://localhost:5000"):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        
    def scan_project(self, project_path: str) -> Dict:
        """Proje dizinini tara"""
        response = self.session.post(
            f"{self.base_url}/api/v1/scan",
            json={'path': project_path}
        )
        response.raise_for_status()
        return response.json()
        
    def export_analysis(
        self, 
        export_data: Dict,
        output_path: str,
        format_type: str = 'html'
    ) -> Dict:
        """Kod analizini export et"""
        response = self.session.post(
            f"{self.base_url}/api/v1/export",
            json={
                'export_data': export_data,
                'output_path': output_path,
                'format': format_type
            }
        )
        response.raise_for_status()
        return response.json()
        
    def get_templates(self) -> List[Dict]:
        """Mevcut şablonları getir"""
        response = self.session.get(f"{self.base_url}/api/v1/templates")
        response.raise_for_status()
        return response.json()['templates']

# Kullanım örneği
client = CodeFuserClient()
scan_result = client.scan_project('/path/to/project')
templates = client.get_templates()

export_data = {
    'files': scan_result['files'],
    'template': templates[0],
    'custom_prompts': {}
}

export_result = client.export_analysis(
    export_data, 
    '/path/to/output.html',
    'html'
)
```

## 📦 Build ve Dağıtım

### PyInstaller Yapılandırması

#### Build Script'i (build_exe.py)
```python
# build_exe.py
import PyInstaller.__main__
import sys
import os
from pathlib import Path

def build_executable():
    """Standalone executable oluştur"""
    
    # Yolları tanımla
    src_path = Path("src")
    main_file = "main.py"
    
    # PyInstaller argümanları
    args = [
        main_file,
        "--onefile",
        "--windowed",
        "--name=CodeFuser_v2.0",
        "--icon=assets/icon.ico",
        f"--distpath=dist/",
        f"--workpath=build/",
        "--clean",
        
        # Veri dosyalarını ekle
        "--add-data=config;config",
        "--add-data=templates;templates",
        "--add-data=locales;locales",
        "--add-data=assets;assets",
        
        # Gizli import'lar
        "--hidden-import=tkinter",
        "--hidden-import=tkinter.ttk",
        "--hidden-import=docx",
        "--hidden-import=reportlab",
        "--hidden-import=git",
        
        # Gereksiz modülleri hariç tut
        "--exclude-module=pytest",
        "--exclude-module=sphinx",
        "--exclude-module=black",
        
        # Optimizasyon
        "--optimize=2",
        "--strip",
    ]
    
    # Kaynak dosyalarını path'e ekle
    for py_file in src_path.glob("**/*.py"):
        args.append(f"--additional-hooks-dir={py_file.parent}")
    
    # PyInstaller'ı çalıştır
    PyInstaller.__main__.run(args)
    
    # Taşınabilir paket oluştur
    create_portable_package()

def create_portable_package():
    """Tüm kaynaklarla taşınabilir paket oluştur"""
    import shutil
    
    dist_dir = Path("dist")
    portable_dir = dist_dir / "CodeFuser_Portable"
    
    # Dizin yapısını oluştur
    portable_dir.mkdir(exist_ok=True)
    
    # Executable'ı kopyala
    exe_file = dist_dir / "CodeFuser_v2.0.exe"
    if exe_file.exists():
        shutil.copy2(exe_file, portable_dir / "CodeFuser.exe")
    
    # Kaynakları kopyala
    for resource_dir in ["config", "templates", "locales"]:
        if Path(resource_dir).exists():
            shutil.copytree(
                resource_dir, 
                portable_dir / resource_dir,
                dirs_exist_ok=True
            )
    
    # README oluştur
    readme_content = create_portable_readme()
    (portable_dir / "README.txt").write_text(readme_content, encoding='utf-8')
    
    print(f"Taşınabilir paket oluşturuldu: {portable_dir}")

def create_portable_readme():
    """Taşınabilir paket için README oluştur"""
    return """
CodeFuser v2.0 - Taşınabilir Sürüm
==================================

Bu taşınabilir sürümde:
- Kurulum gerektirmez
- Python gerektirmez  
- Tüm özellikler dahil
- Ayarlar config/ klasöründe saklanır

Kullanım:
1. CodeFuser.exe dosyasını çalıştırın
2. Proje klasörünüzü seçin
3. Dosyaları seçin ve analiz edin
4. Çıktıyı istediğiniz formatta export edin

Daha fazla bilgi için:
https://github.com/tahamucasiroglu/CodeFuser/wiki
"""

if __name__ == "__main__":
    build_executable()
```

#### Spec Dosyası Özelleştirmesi
```python
# codefuser.spec
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('config', 'config'),
        ('templates', 'templates'),
        ('locales', 'locales'),
        ('assets', 'assets'),
    ],
    hiddenimports=[
        'tkinter',
        'tkinter.ttk',
        'docx',
        'reportlab.pdfgen',
        'git',
        'jinja2',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'pytest',
        'sphinx',
        'black',
        'mypy',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='CodeFuser_v2.0',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='assets/icon.ico',
)
```

### CI/CD Pipeline

#### GitHub Actions İş Akışı
```yaml
# .github/workflows/build.yml
name: Build ve Release

on:
  push:
    tags:
      - 'v*'
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.8, 3.9, '3.10', 3.11]

    steps:
    - uses: actions/checkout@v3
    
    - name: Python ${{ matrix.python-version }} kurulumu
      uses: actions/setup-python@v3
      with:
        python-version: ${{ matrix.python-version }}
        
    - name: Bağımlılıkları yükle
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install -r requirements-dev.txt
        
    - name: Testleri çalıştır
      run: |
        pytest tests/ --cov=src --cov-report=xml
        
    - name: Coverage yükle
      uses: codecov/codecov-action@v3

  build-windows:
    needs: test
    runs-on: windows-latest
    if: startsWith(github.ref, 'refs/tags/')

    steps:
    - uses: actions/checkout@v3
    
    - name: Python kurulumu
      uses: actions/setup-python@v3
      with:
        python-version: '3.9'
        
    - name: Bağımlılıkları yükle
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install pyinstaller
        
    - name: Executable oluştur
      run: |
        python build_exe.py
        
    - name: Release arşivi oluştur
      run: |
        Compress-Archive -Path dist/CodeFuser_Portable/* -DestinationPath CodeFuser_v2.0_Windows.zip
        
    - name: Release artifact yükle
      uses: actions/upload-artifact@v3
      with:
        name: CodeFuser_Windows
        path: CodeFuser_v2.0_Windows.zip

  release:
    needs: [test, build-windows]
    runs-on: ubuntu-latest
    if: startsWith(github.ref, 'refs/tags/')

    steps:
    - name: Artifact'ları indir
      uses: actions/download-artifact@v3
      
    - name: Release Oluştur
      uses: softprops/action-gh-release@v1
      with:
        files: |
          CodeFuser_Windows/CodeFuser_v2.0_Windows.zip
        body: |
          ## CodeFuser v2.0 Release
          
          ### Yeni Özellikler
          - Dosya-özel özel prompt'lar
          - Gelişmiş Git entegrasyonu
          - İyileştirilmiş export formatları
          - Gelişmiş filtreleme sistemi
          
          ### İndirmeler
          - Windows Standalone: CodeFuser_v2.0_Windows.zip
          
          ### Kurulum
          1. Uygun paketi indirin
          2. İstenen konuma çıkarın
          3. CodeFuser.exe'yi çalıştırın (Windows)
```

## 📚 Dokümantasyon

### Kod Dokümantasyonu

#### Docstring Standartları
```python
def export_to_format(
    self,
    format_type: str,
    data: Dict[str, Any],
    output_path: str,
    options: Optional[Dict[str, Any]] = None
) -> ExportResult:
    """
    İşlenmiş veriyi belirtilen formata export et.
    
    Bu metod analiz edilmiş kod verisinin HTML, PDF, DOCX ve TXT
    dahil çeşitli çıktı formatlarına dönüştürülmesini yönetir.
    
    Args:
        format_type: Hedef export formatı ('html', 'pdf', 'docx', 'txt')
        data: Şunları içeren işlenmiş kod analizi verisi:
            - files: Dosya verisi dictionary'lerinin listesi
            - metadata: Analiz metadata'sı
            - template: Uygulanan şablon bilgisi
            - custom_prompts: Dosya-özel prompt'lar
        output_path: Çıktı dosyası için mutlak yol
        options: Opsiyonel format-özel yapılandırma:
            - html: {'syntax_highlighting': bool, 'theme': str}
            - pdf: {'page_size': str, 'font_size': int}
            - docx: {'font_family': str, 'include_toc': bool}
            - txt: {'encoding': str, 'line_ending': str}
    
    Returns:
        Şunları içeren ExportResult nesnesi:
            - success: İşlem başarısını gösteren Boolean
            - output_path: Oluşturulan dosyanın yolu
            - file_size: Oluşturulan dosyanın byte cinsinden boyutu
            - generation_time: Export için geçen süre
            - warnings: Karşılaşılan ölümcül olmayan sorunların listesi
    
    Raises:
        ValueError: format_type desteklenmiyorsa
        FileNotFoundError: Çıktı dizini mevcut değilse
        PermissionError: output_path için yetersiz izinler
        ExportError: Export işlemi başarısızsa
    
    Example:
        >>> exporter = ExportManager()
        >>> data = {
        ...     'files': [{'path': 'main.py', 'content': 'print("hello")'}],
        ...     'metadata': {'project_name': 'MyApp'},
        ...     'template': '16x_prompt'
        ... }
        >>> result = exporter.export_to_format('html', data, '/tmp/output.html')
        >>> print(f"Export {'başarılı' if result.success else 'başarısız'}")
        Export başarılı
    
    Note:
        Büyük export'lar (>100MB) önemli zaman ve bellek alabilir.
        Çok büyük kod tabanları için chunked export kullanmayı düşünün.
    
    See Also:
        - get_supported_formats(): Mevcut export formatlarının listesi
        - validate_export_data(): Export öncesi veriyi doğrula
        - ExportResult: Dönüş değeri yapısının detayları
    """
```

#### API Dokümantasyonu
```python
# src/api/docs.py
from flask import Flask
from flask_restx import Api, Resource, fields

# Swagger ile API dokümantasyonu
api = Api(
    doc='/docs/',
    title='CodeFuser API',
    version='2.0',
    description='CodeFuser kod analiz aracı için REST API'
)

# Dokümantasyon için modelleri tanımla
scan_model = api.model('ScanRequest', {
    'path': fields.String(required=True, description='Proje dizin yolu'),
    'filters': fields.Raw(description='Opsiyonel filtreleme kriterleri'),
    'options': fields.Raw(description='Tarama seçenekleri')
})

scan_response = api.model('ScanResponse', {
    'success': fields.Boolean(description='İşlem başarı durumu'),
    'files': fields.List(fields.Raw, description='Bulunan dosyaların listesi'),
    'count': fields.Integer(description='Toplam dosya sayısı'),
    'statistics': fields.Raw(description='Tarama istatistikleri')
})

@api.route('/scan')
class ScanProject(Resource):
    @api.expect(scan_model)
    @api.marshal_with(scan_response)
    @api.doc(responses={
        200: 'Başarılı',
        400: 'Geçersiz istek verisi',
        500: 'İç sunucu hatası'
    })
    def post(self):
        """Kod dosyaları için proje dizinini tara"""
        pass
```

## 🔍 Gelişmiş Özellikler

### Özel Export Formatları

#### Yeni Exporter'lar Oluşturma
```python
# src/exporters/markdown_exporter.py
from .base_exporter import BaseExporter
from typing import Dict, Any

class MarkdownExporter(BaseExporter):
    """GitHub flavor ile Markdown formatına export"""
    
    def __init__(self):
        super().__init__()
        self.format_name = "markdown"
        self.file_extension = ".md"
        
    def export(self, data: Dict[str, Any], output_path: str) -> ExportResult:
        """Veriyi Markdown formatına export et"""
        try:
            content = self._generate_markdown(data)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(content)
                
            return ExportResult(
                success=True,
                output_path=output_path,
                file_size=os.path.getsize(output_path)
            )
            
        except Exception as e:
            return ExportResult(
                success=False,
                error=str(e)
            )
            
    def _generate_markdown(self, data: Dict[str, Any]) -> str:
        """Markdown içeriği oluştur"""
        lines = []
        
        # Başlık
        lines.append(f"# {data.get('project_name', 'Kod Analizi')}")
        lines.append("")
        lines.append(f"*Oluşturulma: {data.get('timestamp')}*")
        lines.append("")
        
        # İçindekiler
        lines.append("## İçindekiler")
        lines.append("")
        for i, file_data in enumerate(data.get('files', []), 1):
            file_path = file_data['path']
            anchor = file_path.replace('/', '').replace('.', '').lower()
            lines.append(f"{i}. [{file_path}](#{anchor})")
        lines.append("")
        
        # Prompt bölümü
        if data.get('prompt'):
            lines.append("## Analiz Prompt'u")
            lines.append("")
            lines.append("```")
            lines.append(data['prompt'])
            lines.append("```")
            lines.append("")
        
        # Dosya içerikleri
        for file_data in data.get('files', []):
            self._add_file_section(lines, file_data)
            
        return "\n".join(lines)
        
    def _add_file_section(self, lines: list, file_data: Dict[str, Any]):
        """Markdown'a bireysel dosya bölümü ekle"""
        file_path = file_data['path']
        anchor = file_path.replace('/', '').replace('.', '').lower()
        
        lines.append(f"## {file_path} {{#{anchor}}}")
        lines.append("")
        
        # Varsa özel prompt
        if file_data.get('custom_prompt'):
            lines.append("> **Özel Analiz Prompt'u:**")
            lines.append(f"> {file_data['custom_prompt']}")
            lines.append("")
        
        # Sözdizimi vurgulama için dili algıla
        language = self._detect_language(file_path)
        
        lines.append(f"```{language}")
        lines.append(file_data['content'])
        lines.append("```")
        lines.append("")
        lines.append("---")
        lines.append("")
        
    def _detect_language(self, file_path: str) -> str:
        """Dosya uzantısından programlama dilini algıla"""
        ext_map = {
            '.py': 'python',
            '.js': 'javascript',
            '.ts': 'typescript',
            '.jsx': 'jsx',
            '.tsx': 'tsx',
            '.html': 'html',
            '.css': 'css',
            '.scss': 'scss',
            '.java': 'java',
            '.cs': 'csharp',
            '.php': 'php',
            '.rb': 'ruby',
            '.go': 'go',
            '.rs': 'rust',
            '.cpp': 'cpp',
            '.c': 'c',
            '.sql': 'sql',
            '.json': 'json',
            '.xml': 'xml',
            '.yaml': 'yaml',
            '.yml': 'yaml',
        }
        
        ext = Path(file_path).suffix.lower()
        return ext_map.get(ext, 'text')
```

### AI Entegrasyon Özellikleri

#### OpenAI Entegrasyonu
```python
# src/ai/openai_integration.py
import openai
from typing import Dict, List, Optional

class OpenAIIntegration:
    """Gelişmiş analiz için OpenAI API entegrasyonu"""
    
    def __init__(self, api_key: str):
        openai.api_key = api_key
        
    def analyze_code_quality(
        self, 
        code_content: str, 
        file_path: str,
        custom_prompt: Optional[str] = None
    ) -> Dict[str, Any]:
        """GPT modelleri kullanarak kod kalitesini analiz et"""
        
        base_prompt = f"""
        Aşağıdaki kodu kalite, güvenlik ve en iyi uygulamalar açısından analiz edin:
        
        Dosya: {file_path}
        
        Odak alanları:
        - Kod yapısı ve organizasyonu
        - Potansiyel buglar ve sorunlar
        - Güvenlik açıkları
        - Performans optimizasyonları
        - En iyi uygulama uyumu
        
        Kod:
        ```
        {code_content}
        ```
        """
        
        if custom_prompt:
            base_prompt += f"\n\nEk talimatlar: {custom_prompt}"
            
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Uzman kod inceleyicisi ve güvenlik analisti olarak hareket edin."},
                    {"role": "user", "content": base_prompt}
                ],
                max_tokens=2000,
                temperature=0.1
            )
            
            return {
                'success': True,
                'analysis': response.choices[0].message.content,
                'tokens_used': response.usage.total_tokens,
                'model': response.model
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
            
    def generate_documentation(
        self, 
        code_files: List[Dict[str, str]]
    ) -> Dict[str, Any]:
        """Kod dosyaları için dokümantasyon oluştur"""
        
        combined_code = "\n\n".join([
            f"// {file_data['path']}\n{file_data['content']}"
            for file_data in code_files
        ])
        
        prompt = f"""
        Bu kod tabanı için kapsamlı dokümantasyon oluşturun:
        
        {combined_code}
        
        Şunları dahil edin:
        1. Genel bakış ve amaç
        2. Mimari açıklaması
        3. API dokümantasyonu
        4. Kullanım örnekleri
        5. Kurulum talimatları
        """
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Teknik dokümantasyon uzmanı olarak hareket edin."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=4000,
                temperature=0.2
            )
            
            return {
                'success': True,
                'documentation': response.choices[0].message.content,
                'tokens_used': response.usage.total_tokens
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
```

## 🤝 Katkıda Bulunma Rehberi

### Katkı Süreci

#### 1. Fork ve Clone
```bash
# GitHub'da depoyu fork'la
# Fork'unu clone et
git clone https://github.com/your-username/CodeFuser.git
cd CodeFuser

# Upstream remote ekle
git remote add upstream https://github.com/tahamucasiroglu/CodeFuser.git
```

#### 2. Geliştirme Kurulumu
```bash
# Virtual environment oluştur
python -m venv venv
source venv/bin/activate  # Linux/Mac
# veya
venv\Scripts\activate  # Windows

# Geliştirme modunda yükle
pip install -e .[dev]

# Pre-commit hook'larını yükle
pre-commit install
```

#### 3. Değişiklik Yap
```bash
# Feature branch oluştur
git checkout -b feature/amazing-feature

# Değişikliklerini yap
# Test yaz
# Dokümantasyonu güncelle

# Testleri çalıştır
pytest tests/

# Linting çalıştır
black src/ tests/
flake8 src/ tests/
mypy src/
```

#### 4. Pull Request Gönder
```bash
# Değişiklikleri commit et
git add .
git commit -m "feat: harika özellik ekle

- Yeni işlevselliği implement et
- Kapsamlı testler ekle
- Dokümantasyonu güncelle"

# Fork'una push et
git push origin feature/amazing-feature

# GitHub'da pull request oluştur
```

### Kod İnceleme Süreci

#### İnceleme Kontrol Listesi
```markdown
- [ ] Kod proje stil rehberini takip ediyor
- [ ] Tüm testler geçiyor
- [ ] Yeni özellikler testlere sahip
- [ ] Dokümantasyon güncellenmiş
- [ ] Breaking değişiklikler dokümante edilmiş
- [ ] Performans etkisi düşünülmüş
- [ ] Güvenlik etkileri incelenmiş
```

#### İnceleme Rehberi
- Yapıcı ve yardımcı ol
- Kişiye değil koda odaklan
- Spesifik iyileştirmeler öner
- İyi uygulamaları takdir et
- Değişiklikleri yerel olarak test et

---

**Katkıda bulunmaya hazır mısınız?** [Açık issue'ları](https://github.com/tahamucasiroglu/CodeFuser/issues) kontrol edin veya dahil olmak için [tartışma başlatın](https://github.com/tahamucasiroglu/CodeFuser/discussions)!

*Geliştirme sorunları için yardım almak üzere [Sorun Giderme Rehberi](Troubleshooting-TR)'ne devam edin →*