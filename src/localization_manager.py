import json
from pathlib import Path
from typing import Dict, Any, Optional
import re

from utils import get_locale_path


class LocalizationManager:
    def __init__(self, config_manager):
        self.config_manager = config_manager
        self.current_language = self.config_manager.get_language()
        self.translations = self._load_translations()
        self.fallback_language = "en"
        self.fallback_translations = self._load_translations(self.fallback_language)
    
    def _load_translations(self, language: Optional[str] = None) -> Dict[str, Any]:
        if language is None:
            language = self.current_language
        
        try:
            locale_file = get_locale_path(f"{language}.json")
            with open(locale_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError, IOError) as e:
            print(f"⚠️ Locale loading error for {language}: {e}")
            return self._get_fallback_translations(language)
    
    def _get_fallback_translations(self, language: str) -> Dict[str, Any]:
        """Fallback translations when locale files are not found"""
        if language == 'tr':
            return {
                "language_name": "Türkçe",
                "app_title": "CodeFuser - Kod Birleştirme Aracı",
                "select_folder": "Klasör Seç",
                "scan_files": "Dosyaları Tara",
                "export": "Dışa Aktar",
                "settings": "Ayarlar",
                "about": "Hakkında",
                "file": "Dosya",
                "edit": "Düzenle",
                "view": "Görünüm",
                "help": "Yardım",
                "project_folder": "Proje Klasörü:",
                "file_types": "Dosya Türleri:",
                "filters": "Filtreler:",
                "output_format": "Çıktı Formatı:",
                "prompt_template": "Prompt Şablonu:",
                "custom_prompt": "Özel Prompt:",
                "export_button": "Dışa Aktar",
                "cancel": "İptal",
                "ok": "Tamam",
                "error": "Hata",
                "warning": "Uyarı",
                "info": "Bilgi",
                "success": "Başarılı",
                "loading": "Yükleniyor...",
                "scanning": "Taranıyor...",
                "exporting": "Dışa aktarılıyor...",
                "done": "Tamamlandı",
                "no_folder_selected": "Klasör seçilmedi",
                "no_files_found": "Dosya bulunamadı",
                "export_successful": "Dışa aktarma başarılı",
                "export_failed": "Dışa aktarma başarısız"
            }
        else:  # English
            return {
                "language_name": "English",
                "app_title": "CodeFuser - Code Aggregation Tool",
                "select_folder": "Select Folder",
                "scan_files": "Scan Files",
                "export": "Export",
                "settings": "Settings",
                "about": "About",
                "file": "File",
                "edit": "Edit",
                "view": "View",
                "help": "Help",
                "project_folder": "Project Folder:",
                "file_types": "File Types:",
                "filters": "Filters:",
                "output_format": "Output Format:",
                "prompt_template": "Prompt Template:",
                "custom_prompt": "Custom Prompt:",
                "export_button": "Export",
                "cancel": "Cancel",
                "ok": "OK",
                "error": "Error",
                "warning": "Warning",
                "info": "Info",
                "success": "Success",
                "loading": "Loading...",
                "scanning": "Scanning...",
                "exporting": "Exporting...",
                "done": "Done",
                "no_folder_selected": "No folder selected",
                "no_files_found": "No files found",
                "export_successful": "Export successful",
                "export_failed": "Export failed"
            }
    
    def get(self, key: str, **kwargs) -> str:
        keys = key.split('.')
        value = self._get_nested_value(self.translations, keys)
        
        if value is None and self.current_language != self.fallback_language:
            value = self._get_nested_value(self.fallback_translations, keys)
        
        if value is None:
            return key
        
        if kwargs:
            try:
                return value.format(**kwargs)
            except (KeyError, ValueError):
                return value
        
        return value
    
    def _get_nested_value(self, data: Dict[str, Any], keys: list) -> Optional[str]:
        current = data
        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return None
        return current if isinstance(current, str) else None
    
    def set_language(self, language: str) -> bool:
        try:
            locale_file = get_locale_path(f"{language}.json")
            # Test if file exists by trying to open it
            with open(locale_file, 'r', encoding='utf-8') as f:
                pass
            
            self.current_language = language
            self.translations = self._load_translations()
            self.config_manager.set_language(language)
            return True
        except FileNotFoundError:
            return False
    
    def get_available_languages(self) -> Dict[str, str]:
        languages = {}
        # Default languages when files not found
        default_languages = {
            'tr': 'Türkçe',
            'en': 'English'
        }
        
        for lang_code in default_languages:
            try:
                translations = self._load_translations(lang_code)
                lang_name = translations.get('language_name', default_languages[lang_code])
                languages[lang_code] = lang_name
            except:
                languages[lang_code] = default_languages[lang_code]
        
        return languages
    
    def add_translation(self, language: str, key: str, value: str) -> None:
        locale_file = self.locales_dir / f"{language}.json"
        
        if locale_file.exists():
            with open(locale_file, 'r', encoding='utf-8') as f:
                translations = json.load(f)
        else:
            translations = {}
        
        keys = key.split('.')
        current = translations
        
        for k in keys[:-1]:
            if k not in current:
                current[k] = {}
            current = current[k]
        
        current[keys[-1]] = value
        
        with open(locale_file, 'w', encoding='utf-8') as f:
            json.dump(translations, f, ensure_ascii=False, indent=4)
        
        if language == self.current_language:
            self.translations = translations
    
    def validate_translations(self) -> Dict[str, list]:
        all_keys = set()
        language_keys = {}
        
        for locale_file in self.locales_dir.glob("*.json"):
            lang_code = locale_file.stem
            translations = self._load_translations(lang_code)
            keys = self._extract_keys(translations)
            language_keys[lang_code] = keys
            all_keys.update(keys)
        
        missing_keys = {}
        for lang_code, keys in language_keys.items():
            missing = all_keys - keys
            if missing:
                missing_keys[lang_code] = sorted(list(missing))
        
        return missing_keys
    
    def _extract_keys(self, data: Dict[str, Any], prefix: str = "") -> set:
        keys = set()
        
        for key, value in data.items():
            full_key = f"{prefix}.{key}" if prefix else key
            
            if isinstance(value, dict):
                keys.update(self._extract_keys(value, full_key))
            else:
                keys.add(full_key)
        
        return keys


class TranslationHelper:
    @staticmethod
    def pluralize(count: int, singular: str, plural: str) -> str:
        return singular if count == 1 else plural
    
    @staticmethod
    def format_file_size(size_bytes: int) -> str:
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.2f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.2f} TB"