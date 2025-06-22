from pathlib import Path
from typing import List, Dict, Any, Optional
from abc import ABC, abstractmethod
import datetime
from dataclasses import dataclass
from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted, PageBreak
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import textwrap


@dataclass
class OutputFile:
    file_path: str
    content: str


class OutputFormatter(ABC):
    def __init__(self, config_manager):
        self.config_manager = config_manager
    
    @abstractmethod
    def format_output(self, files: List[OutputFile], output_path: Path, prompt: str = "") -> None:
        pass
    
    def get_separator(self) -> str:
        return self.config_manager.get('output_settings.file_separator', '=== FILE: {filepath} ===')
    
    def get_prompt_placeholder(self) -> str:
        return self.config_manager.get('output_settings.prompt_placeholder', '[PROMPT]')
    
    def get_content_placeholder(self) -> str:
        return self.config_manager.get('output_settings.content_placeholder', '[CONTENT]')


class TextOutputFormatter(OutputFormatter):
    def format_output(self, files: List[OutputFile], output_path: Path, prompt: str = "") -> None:
        encoding = self.config_manager.get('encoding', 'utf-8')
        
        with open(output_path, 'w', encoding=encoding) as f:
            # Write header
            f.write(f"# CodeFuser Output\n")
            f.write(f"# Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"# Total Files: {len(files)}\n")
            f.write("\n" + "="*80 + "\n\n")
            
            # Write prompt if provided (once at the beginning)
            if prompt:
                f.write(f"{self.get_prompt_placeholder()}\n")
                f.write(f"{prompt}\n")
                f.write("\n" + "-"*80 + "\n\n")
            
            for idx, file_data in enumerate(files):
                # Write file separator
                separator = self.get_separator().format(filepath=file_data.file_path)
                f.write(f"\n{separator}\n")
                
                # Write content
                f.write(f"\n{self.get_content_placeholder()}\n")
                f.write(file_data.content)
                
                # Add spacing between files
                if idx < len(files) - 1:
                    f.write("\n\n")


class DocxOutputFormatter(OutputFormatter):
    def format_output(self, files: List[OutputFile], output_path: Path, prompt: str = "") -> None:
        doc = Document()
        
        # Add title
        title = doc.add_heading('CodeFuser Output', 0)
        title.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        
        # Add metadata
        doc.add_paragraph(f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        doc.add_paragraph(f"Total Files: {len(files)}")
        doc.add_paragraph("")
        
        # Add prompt if provided (once at the beginning)
        if prompt:
            prompt_heading = doc.add_heading(self.get_prompt_placeholder(), level=2)
            prompt_para = doc.add_paragraph(prompt)
            prompt_para.style.font.size = Pt(11)
            prompt_para.style.font.color.rgb = RGBColor(0, 0, 139)
            doc.add_paragraph("-" * 80)
            doc.add_paragraph("")
        
        for idx, file_data in enumerate(files):
            # Add file header
            file_header = doc.add_heading(file_data.file_path, level=2)
            
            # Add content
            content_heading = doc.add_heading(self.get_content_placeholder(), level=3)
            
            # Split content into smaller chunks for better handling
            content_lines = file_data.content.split('\n')
            for line in content_lines:
                if line.strip():
                    para = doc.add_paragraph(line)
                    para.style.font.name = 'Courier New'
                    para.style.font.size = Pt(9)
                else:
                    doc.add_paragraph("")
            
            # Add page break between files (except for the last one)
            if idx < len(files) - 1:
                doc.add_page_break()
        
        # Save document
        doc.save(str(output_path))


class PdfOutputFormatter(OutputFormatter):
    def __init__(self, config_manager):
        super().__init__(config_manager)
        self._register_fonts()
    
    def _register_fonts(self):
        # Try to register monospace fonts
        try:
            # This is a placeholder - in production, you'd want to handle font paths properly
            pass
        except:
            pass
    
    def format_output(self, files: List[OutputFile], output_path: Path, prompt: str = "") -> None:
        # Create PDF document
        doc = SimpleDocTemplate(
            str(output_path),
            pagesize=A4,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=18,
        )
        
        # Container for the 'Flowable' objects
        elements = []
        
        # Define styles
        styles = getSampleStyleSheet()
        
        # Custom styles
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            textColor='darkblue',
            alignment=TA_LEFT,
        )
        
        file_header_style = ParagraphStyle(
            'FileHeader',
            parent=styles['Heading2'],
            fontSize=14,
            textColor='darkgreen',
            spaceAfter=12,
        )
        
        code_style = ParagraphStyle(
            'Code',
            parent=styles['Code'],
            fontSize=8,
            fontName='Courier',
            leftIndent=0,
            rightIndent=0,
            spaceAfter=6,
        )
        
        # Add title
        elements.append(Paragraph("CodeFuser Output", title_style))
        elements.append(Spacer(1, 0.2*inch))
        
        # Add metadata
        metadata = f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}<br/>Total Files: {len(files)}"
        elements.append(Paragraph(metadata, styles['Normal']))
        elements.append(Spacer(1, 0.3*inch))
        
        # Add prompt if provided (once at the beginning)
        if prompt:
            elements.append(Paragraph(f"<b>{self.get_prompt_placeholder()}</b>", styles['Heading2']))
            elements.append(Paragraph(prompt, styles['Italic']))
            elements.append(Spacer(1, 0.3*inch))
            elements.append(Paragraph("-" * 80, styles['Normal']))
            elements.append(Spacer(1, 0.3*inch))
        
        # Process files
        for idx, file_data in enumerate(files):
            # Add file header
            elements.append(Paragraph(file_data.file_path, file_header_style))
            
            # Add content header
            elements.append(Paragraph(f"<b>{self.get_content_placeholder()}</b>", styles['Normal']))
            elements.append(Spacer(1, 0.05*inch))
            
            # Add content - wrap long lines
            wrapped_content = self._wrap_content(file_data.content, 100)
            content_pre = Preformatted(wrapped_content, code_style)
            elements.append(content_pre)
            
            # Add page break between files (except for the last one)
            if idx < len(files) - 1:
                elements.append(PageBreak())
        
        # Build PDF
        doc.build(elements)
    
    def _wrap_content(self, content: str, width: int = 100) -> str:
        lines = content.split('\n')
        wrapped_lines = []
        
        for line in lines:
            if len(line) > width:
                wrapped = textwrap.wrap(line, width=width, break_long_words=True, break_on_hyphens=False)
                wrapped_lines.extend(wrapped)
            else:
                wrapped_lines.append(line)
        
        return '\n'.join(wrapped_lines)


class OutputManager:
    def __init__(self, config_manager):
        self.config_manager = config_manager
        self.formatters = {
            'txt': TextOutputFormatter(config_manager),
            'docx': DocxOutputFormatter(config_manager),
            'pdf': PdfOutputFormatter(config_manager)
        }
    
    def create_output(
        self,
        files: List[Dict[str, Any]],
        output_path: Path,
        format: str,
        prompt: str = ""
    ) -> Path:
        
        if format not in self.formatters:
            raise ValueError(f"Unsupported output format: {format}")
        
        # Convert file data to OutputFile objects
        output_files = []
        encoding = self.config_manager.get('encoding', 'utf-8')
        
        for file_info in files:
            try:
                with open(file_info['path'], 'r', encoding=encoding) as f:
                    content = f.read()
                
                output_file = OutputFile(
                    file_path=file_info['relative_path'],
                    content=content
                )
                output_files.append(output_file)
            except Exception as e:
                # Log error but continue with other files
                print(f"Error reading file {file_info['path']}: {e}")
                continue
        
        # Ensure output path has correct extension
        output_path = output_path.with_suffix(f'.{format}')
        
        # Format and save output
        formatter = self.formatters[format]
        formatter.format_output(output_files, output_path, prompt)
        
        return output_path
    
    def get_available_formats(self) -> List[str]:
        return list(self.formatters.keys())
    
    def estimate_output_size(self, files: List[Dict[str, Any]], format: str) -> int:
        # Rough estimation based on file count and format
        total_size = sum(f.get('size', 0) for f in files)
        
        # Add overhead based on format
        overhead_multipliers = {
            'txt': 1.1,   # 10% overhead for separators and prompts
            'docx': 1.5,  # 50% overhead for XML structure
            'pdf': 2.0    # 100% overhead for PDF structure
        }
        
        multiplier = overhead_multipliers.get(format, 1.2)
        return int(total_size * multiplier)