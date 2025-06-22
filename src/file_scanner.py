import os
from pathlib import Path
from typing import List, Dict, Any, Callable, Optional, Set
from dataclasses import dataclass
from datetime import datetime
import fnmatch
import threading
from queue import Queue
import time


@dataclass
class FileInfo:
    path: Path
    relative_path: str
    size: int
    modified_time: datetime
    extension: str


class FileScannerProgress:
    def __init__(self):
        self.total_files = 0
        self.processed_files = 0
        self.current_file = ""
        self.is_scanning = True
        self.errors: List[Dict[str, str]] = []
        self._lock = threading.Lock()
    
    def update(self, processed: int = None, current_file: str = None, total: int = None):
        with self._lock:
            if processed is not None:
                self.processed_files = processed
            if current_file is not None:
                self.current_file = current_file
            if total is not None:
                self.total_files = total
    
    def add_error(self, file_path: str, error: str):
        with self._lock:
            self.errors.append({"file": file_path, "error": error})
    
    def get_progress_percentage(self) -> float:
        with self._lock:
            if self.total_files == 0:
                return 0.0
            return (self.processed_files / self.total_files) * 100


class FileScanner:
    def __init__(self, config_manager):
        self.config_manager = config_manager
        self.progress = FileScannerProgress()
        self._stop_scanning = False
    
    def scan_directory(
        self,
        directory: Path,
        extensions: List[str],
        include_ignored: bool = False,
        progress_callback: Optional[Callable[[FileScannerProgress], None]] = None
    ) -> List[FileInfo]:
        
        self._stop_scanning = False
        self.progress = FileScannerProgress()
        
        if not directory.exists() or not directory.is_dir():
            raise ValueError(f"Invalid directory: {directory}")
        
        ignored_folders = set(self.config_manager.get_ignored_folders()) if not include_ignored else set()
        ignored_files = set(self.config_manager.get_ignored_files()) if not include_ignored else set()
        max_file_size = self.config_manager.get('max_file_size_mb', 10) * 1024 * 1024
        
        # Normalize extensions
        extensions = [ext.lower() if ext.startswith('.') else f".{ext.lower()}" for ext in extensions]
        
        # First pass: count total files
        total_files = self._count_files(directory, extensions, ignored_folders, ignored_files)
        self.progress.update(total=total_files)
        
        # Second pass: collect files
        files = []
        file_queue = Queue()
        
        # Start scanner thread
        scanner_thread = threading.Thread(
            target=self._scan_worker,
            args=(directory, extensions, ignored_folders, ignored_files, max_file_size, file_queue)
        )
        scanner_thread.start()
        
        # Process files and update progress
        while scanner_thread.is_alive() or not file_queue.empty():
            if self._stop_scanning:
                break
                
            try:
                file_info = file_queue.get(timeout=0.1)
                files.append(file_info)
                self.progress.update(processed=len(files), current_file=file_info.relative_path)
                
                if progress_callback:
                    progress_callback(self.progress)
            except:
                continue
        
        scanner_thread.join()
        self.progress.is_scanning = False
        
        return sorted(files, key=lambda f: f.relative_path)
    
    def _count_files(
        self,
        directory: Path,
        extensions: List[str],
        ignored_folders: Set[str],
        ignored_files: Set[str]
    ) -> int:
        count = 0
        
        for root, dirs, files in os.walk(directory):
            # Filter out ignored directories
            dirs[:] = [d for d in dirs if d not in ignored_folders]
            
            for file in files:
                if self._should_include_file(file, extensions, ignored_files):
                    count += 1
        
        return count
    
    def _scan_worker(
        self,
        directory: Path,
        extensions: List[str],
        ignored_folders: Set[str],
        ignored_files: Set[str],
        max_file_size: int,
        file_queue: Queue
    ):
        for root, dirs, files in os.walk(directory):
            if self._stop_scanning:
                break
            
            # Filter out ignored directories
            dirs[:] = [d for d in dirs if d not in ignored_folders]
            
            root_path = Path(root)
            
            for file in files:
                if self._stop_scanning:
                    break
                
                if not self._should_include_file(file, extensions, ignored_files):
                    continue
                
                file_path = root_path / file
                
                try:
                    stat = file_path.stat()
                    
                    # Skip files that are too large
                    if stat.st_size > max_file_size:
                        self.progress.add_error(
                            str(file_path),
                            f"File too large: {stat.st_size / 1024 / 1024:.2f} MB"
                        )
                        continue
                    
                    file_info = FileInfo(
                        path=file_path,
                        relative_path=str(file_path.relative_to(directory)),
                        size=stat.st_size,
                        modified_time=datetime.fromtimestamp(stat.st_mtime),
                        extension=file_path.suffix.lower()
                    )
                    
                    file_queue.put(file_info)
                    
                except Exception as e:
                    self.progress.add_error(str(file_path), str(e))
    
    def _should_include_file(
        self,
        filename: str,
        extensions: List[str],
        ignored_files: Set[str]
    ) -> bool:
        # Check against ignored patterns
        for pattern in ignored_files:
            if fnmatch.fnmatch(filename.lower(), pattern.lower()):
                return False
        
        # Check extension
        if not extensions:  # If no extensions specified, include all
            return True
        
        file_ext = Path(filename).suffix.lower()
        return file_ext in extensions or filename.lower() in [ext.lower() for ext in extensions]
    
    def stop_scanning(self):
        self._stop_scanning = True
    
    def get_directory_statistics(self, files: List[FileInfo]) -> Dict[str, Any]:
        if not files:
            return {
                "total_files": 0,
                "total_size": 0,
                "extensions": {},
                "largest_file": None,
                "newest_file": None
            }
        
        total_size = sum(f.size for f in files)
        extensions = {}
        
        for file in files:
            ext = file.extension or "no_extension"
            if ext not in extensions:
                extensions[ext] = {"count": 0, "size": 0}
            extensions[ext]["count"] += 1
            extensions[ext]["size"] += file.size
        
        largest_file = max(files, key=lambda f: f.size)
        newest_file = max(files, key=lambda f: f.modified_time)
        
        return {
            "total_files": len(files),
            "total_size": total_size,
            "extensions": extensions,
            "largest_file": {
                "path": largest_file.relative_path,
                "size": largest_file.size
            },
            "newest_file": {
                "path": newest_file.relative_path,
                "modified": newest_file.modified_time.isoformat()
            }
        }