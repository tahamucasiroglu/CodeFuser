import json
import os
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
import shutil


@dataclass
class ProjectType:
    name: str
    extensions: List[str]


class ConfigManager:
    def __init__(self):
        self.base_dir = Path(__file__).parent.parent
        self.config_dir = self.base_dir / "config"
        self.default_settings_path = self.config_dir / "default_settings.json"
        self.user_settings_path = self.config_dir / "user_settings.json"
        
        self._default_settings = self._load_default_settings()
        self._user_settings = self._load_user_settings()
        self._merged_settings = self._merge_settings()
    
    def _load_default_settings(self) -> Dict[str, Any]:
        with open(self.default_settings_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def _load_user_settings(self) -> Dict[str, Any]:
        if self.user_settings_path.exists():
            try:
                with open(self.user_settings_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return {}
        return {}
    
    def _merge_settings(self) -> Dict[str, Any]:
        merged = self._default_settings.copy()
        self._deep_merge(merged, self._user_settings)
        return merged
    
    def _deep_merge(self, base: Dict[str, Any], update: Dict[str, Any]) -> None:
        for key, value in update.items():
            if key in base and isinstance(base[key], dict) and isinstance(value, dict):
                self._deep_merge(base[key], value)
            else:
                base[key] = value
    
    def get(self, key: str, default: Any = None) -> Any:
        keys = key.split('.')
        value = self._merged_settings
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def set(self, key: str, value: Any) -> None:
        keys = key.split('.')
        
        if not self._user_settings:
            self._user_settings = {}
        
        current = self._user_settings
        for k in keys[:-1]:
            if k not in current:
                current[k] = {}
            current = current[k]
        
        current[keys[-1]] = value
        self._save_user_settings()
        self._merged_settings = self._merge_settings()
    
    def _save_user_settings(self) -> None:
        with open(self.user_settings_path, 'w', encoding='utf-8') as f:
            json.dump(self._user_settings, f, ensure_ascii=False, indent=4)
    
    def reset_to_defaults(self) -> None:
        if self.user_settings_path.exists():
            self.user_settings_path.unlink()
        self._user_settings = {}
        self._merged_settings = self._default_settings.copy()
    
    def get_project_types(self) -> Dict[str, List[str]]:
        return self.get('project_types', {})
    
    def add_project_type(self, name: str, extensions: List[str]) -> None:
        project_types = self.get_project_types()
        project_types[name] = extensions
        self.set('project_types', project_types)
    
    def get_ignored_folders(self) -> List[str]:
        return self.get('ignore_folders', [])
    
    def get_ignored_files(self) -> List[str]:
        return self.get('ignore_files', [])
    
    def get_language(self) -> str:
        return self.get('language', 'tr')
    
    def set_language(self, language: str) -> None:
        self.set('language', language)
    
    def get_output_format(self) -> str:
        return self.get('output_settings.default_format', 'txt')
    
    def get_available_formats(self) -> List[str]:
        return self.get('output_settings.available_formats', ['txt'])
    
    def export_settings(self, filepath: Path) -> None:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self._merged_settings, f, ensure_ascii=False, indent=4)
    
    def import_settings(self, filepath: Path) -> None:
        with open(filepath, 'r', encoding='utf-8') as f:
            imported_settings = json.load(f)
        
        self._user_settings = imported_settings
        self._save_user_settings()
        self._merged_settings = self._merge_settings()