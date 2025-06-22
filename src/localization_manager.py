import json
from pathlib import Path
from typing import Dict, Any, Optional
import re


class LocalizationManager:
    def __init__(self, config_manager):
        self.config_manager = config_manager
        self.base_dir = Path(__file__).parent.parent
        self.locales_dir = self.base_dir / "locales"
        self.current_language = self.config_manager.get_language()
        self.translations = self._load_translations()
        self.fallback_language = "en"
        self.fallback_translations = self._load_translations(self.fallback_language)
    
    def _load_translations(self, language: Optional[str] = None) -> Dict[str, Any]:
        if language is None:
            language = self.current_language
        
        locale_file = self.locales_dir / f"{language}.json"
        
        if locale_file.exists():
            try:
                with open(locale_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return {}
        return {}
    
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
        locale_file = self.locales_dir / f"{language}.json"
        
        if locale_file.exists():
            self.current_language = language
            self.translations = self._load_translations()
            self.config_manager.set_language(language)
            return True
        return False
    
    def get_available_languages(self) -> Dict[str, str]:
        languages = {}
        for locale_file in self.locales_dir.glob("*.json"):
            lang_code = locale_file.stem
            
            translations = self._load_translations(lang_code)
            lang_name = translations.get('language_name', lang_code.upper())
            languages[lang_code] = lang_name
        
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