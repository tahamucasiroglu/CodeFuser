import tkinter as tk
from tkinter import ttk
from pathlib import Path
from typing import Dict, List, Set, Optional, Callable
import os


class FileTreeWidget(tk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        
        self.selected_files: Set[str] = set()
        self.file_items: Dict[str, str] = {}  # path -> item_id mapping
        self.item_paths: Dict[str, str] = {}  # item_id -> path mapping
        self.file_data: Dict[str, dict] = {}  # path -> file_info mapping
        self.on_selection_change: Optional[Callable[[int], None]] = None
        
        self._create_widgets()
        self._setup_styles()
    
    def _create_widgets(self):
        # Header frame with search and counter
        header_frame = tk.Frame(self, bg='white')
        header_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Search box
        search_frame = tk.Frame(header_frame, bg='white')
        search_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        search_icon = tk.Label(search_frame, text="🔍", bg='white', font=('Segoe UI', 12))
        search_icon.pack(side=tk.LEFT, padx=(0, 5))
        
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(
            search_frame,
            textvariable=self.search_var,
            relief=tk.FLAT,
            bg='#f0f0f0',
            font=('Segoe UI', 10)
        )
        self.search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=3)
        self.search_entry.insert(0, "Filter files and folders by name")
        self.search_entry.bind('<FocusIn>', self._on_search_focus_in)
        self.search_entry.bind('<FocusOut>', self._on_search_focus_out)
        self.search_var.trace('w', lambda *args: self._filter_tree())
        
        # File counter
        self.counter_label = tk.Label(
            header_frame,
            text="0 / 0 files selected",
            bg='white',
            fg='#FF6B6B',
            font=('Segoe UI', 10, 'bold')
        )
        self.counter_label.pack(side=tk.RIGHT, padx=(10, 0))
        
        # Main content frame
        content_frame = tk.Frame(self, bg='#f8f9fa')
        content_frame.pack(fill=tk.BOTH, expand=True, padx=5)
        
        # Create main container with scrollbar
        tree_container = tk.Frame(content_frame)
        tree_container.pack(fill=tk.BOTH, expand=True)
        
        # Create scrollable frame
        self.canvas = tk.Canvas(tree_container, bg='#f8f9fa', highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(tree_container, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg='#f8f9fa')
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        
        # Bind mouse wheel
        self.canvas.bind("<MouseWheel>", self._on_mousewheel)
        
        # Empty state message
        self.empty_label = tk.Label(
            content_frame,
            text="No files selected. Use the checkboxes on the right of files to select them",
            bg='#f8f9fa',
            fg='#666666',
            font=('Segoe UI', 11),
            wraplength=400
        )
    
    def _setup_styles(self):
        pass  # No special styles needed for this simpler approach
    
    def _on_search_focus_in(self, event):
        if self.search_entry.get() == "Filter files and folders by name":
            self.search_entry.delete(0, tk.END)
            self.search_entry.config(fg='black')
    
    def _on_search_focus_out(self, event):
        if not self.search_entry.get():
            self.search_entry.insert(0, "Filter files and folders by name")
            self.search_entry.config(fg='#999999')
    
    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    def populate_tree(self, files: List[Dict[str, any]]):
        # Clear existing items
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        
        self.file_items.clear()
        self.item_paths.clear()
        self.file_data.clear()
        self.selected_files.clear()
        
        if not files:
            self.empty_label.pack(pady=50)
            self._update_counter(0, 0)
            return
        else:
            self.empty_label.pack_forget()
        
        # Store file data
        for file_info in files:
            self.file_data[file_info['relative_path']] = file_info
        
        # Build tree structure
        tree_data = {}
        for file_info in files:
            path = Path(file_info['relative_path'])
            parts = path.parts
            
            current = tree_data
            for i, part in enumerate(parts[:-1]):
                if part not in current:
                    current[part] = {'__files__': [], '__dirs__': {}}
                current = current[part]['__dirs__']
            
            # Add file to its parent directory
            if len(parts) > 0:
                current['__files__'] = current.get('__files__', [])
                current['__files__'].append(file_info)
        
        # Populate tree recursively
        self._populate_tree_recursive(self.scrollable_frame, tree_data, '', 0)
        
        # Update counter
        self._update_counter(0, len(files))
    
    def _populate_tree_recursive(self, parent: tk.Widget, data: dict, path_prefix: str, depth: int):
        # Add directories first
        for dir_name, dir_data in sorted(data.items()):
            if dir_name in ['__files__', '__dirs__']:
                continue
            
            dir_path = os.path.join(path_prefix, dir_name) if path_prefix else dir_name
            
            # Create directory frame
            dir_frame = tk.Frame(parent, bg='#f8f9fa')
            dir_frame.pack(fill=tk.X, padx=(depth * 20, 0), pady=1)
            
            # Directory icon and name
            dir_label = tk.Label(
                dir_frame,
                text=f"📁 {dir_name}",
                bg='#f8f9fa',
                font=('Segoe UI', 10),
                anchor='w'
            )
            dir_label.pack(side=tk.LEFT, fill=tk.X, expand=True)
            
            # Remove button for directory
            remove_btn = tk.Button(
                dir_frame,
                text='🗑️',
                font=('Segoe UI', 10),
                bg='#ff6b6b',
                fg='white',
                relief=tk.FLAT,
                cursor='hand2',
                padx=5,
                pady=2,
                command=lambda dp=dir_path: self._remove_directory(dp)
            )
            remove_btn.pack(side=tk.RIGHT, padx=(5, 0))
            
            # Container for subdirectories and files
            sub_container = tk.Frame(parent, bg='#f8f9fa')
            sub_container.pack(fill=tk.X)
            
            # Recursively add subdirectories and files
            if '__dirs__' in dir_data:
                self._populate_tree_recursive(sub_container, dir_data['__dirs__'], dir_path, depth + 1)
            if '__files__' in dir_data:
                for file_info in sorted(dir_data['__files__'], key=lambda f: f['relative_path']):
                    self._add_file_item(sub_container, file_info, depth + 1)
        
        # Add files in root level
        if '__files__' in data:
            for file_info in sorted(data['__files__'], key=lambda f: f['relative_path']):
                self._add_file_item(parent, file_info, depth)
    
    def _add_file_item(self, parent: tk.Widget, file_info: dict, depth: int):
        file_path = file_info['relative_path']
        file_name = Path(file_path).name
        
        # Determine file icon based on extension
        ext = Path(file_name).suffix.lower()
        icon = self._get_file_icon(ext)
        
        # Create file frame
        file_frame = tk.Frame(parent, bg='#f8f9fa')
        file_frame.pack(fill=tk.X, padx=(depth * 20, 0), pady=1)
        
        # Checkbox
        var = tk.BooleanVar(value=file_path in self.selected_files)
        checkbox = tk.Checkbutton(
            file_frame,
            variable=var,
            bg='#f8f9fa',
            activebackground='#f8f9fa',
            command=lambda fp=file_path, v=var: self._toggle_selection(fp, v.get())
        )
        checkbox.pack(side=tk.LEFT, padx=(0, 5))
        
        # File icon and name
        file_label = tk.Label(
            file_frame,
            text=f"{icon} {file_name}",
            bg='#f8f9fa',
            font=('Segoe UI', 10),
            anchor='w'
        )
        file_label.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # Remove button
        remove_btn = tk.Button(
            file_frame,
            text='🗑️',
            font=('Segoe UI', 10),
            bg='#ff6b6b',
            fg='white',
            relief=tk.FLAT,
            cursor='hand2',
            padx=5,
            pady=2,
            command=lambda fp=file_path: self._remove_file(fp)
        )
        remove_btn.pack(side=tk.RIGHT, padx=(5, 0))
        
        # Store references
        self.file_items[file_path] = file_frame
        self.item_paths[str(file_frame)] = file_path
        
        # Store checkbox reference
        setattr(file_frame, 'checkbox_var', var)
    
    def _get_file_icon(self, extension: str) -> str:
        icons = {
            '.py': '🐍',
            '.js': '📜',
            '.ts': '📘',
            '.jsx': '⚛️',
            '.tsx': '⚛️',
            '.html': '🌐',
            '.css': '🎨',
            '.json': '📋',
            '.xml': '📄',
            '.txt': '📝',
            '.md': '📖',
            '.yml': '⚙️',
            '.yaml': '⚙️',
            '.cs': '🔷',
            '.java': '☕',
            '.cpp': '🔧',
            '.c': '🔧',
            '.h': '📎',
            '.hpp': '📎',
            '.go': '🐹',
            '.rs': '🦀',
            '.rb': '💎',
            '.php': '🐘',
            '.swift': '🦉',
            '.kt': '🟣',
        }
        return icons.get(extension, '📄')
    
    def _toggle_selection(self, file_path: str, selected: bool):
        if selected:
            self.selected_files.add(file_path)
        else:
            self.selected_files.discard(file_path)
        
        # Update counter
        total_files = len(self.file_data)
        selected_count = len(self.selected_files)
        self._update_counter(selected_count, total_files)
        
        # Trigger callback
        if self.on_selection_change:
            self.on_selection_change(selected_count)
    
    def _remove_file(self, file_path: str):
        # Remove from selection
        self.selected_files.discard(file_path)
        
        # Remove from data
        if file_path in self.file_data:
            del self.file_data[file_path]
        
        # Remove widget
        if file_path in self.file_items:
            widget = self.file_items[file_path]
            widget.destroy()
            del self.file_items[file_path]
        
        # Update counter
        total_files = len(self.file_data)
        selected_count = len(self.selected_files)
        self._update_counter(selected_count, total_files)
        
        # Show empty message if needed
        if total_files == 0:
            self.empty_label.pack(pady=50)
        
        # Trigger callback
        if self.on_selection_change:
            self.on_selection_change(selected_count)
    
    def _remove_directory(self, dir_path: str):
        # Find all files in this directory
        files_to_remove = []
        for file_path in self.file_data.keys():
            if file_path.startswith(dir_path + '/') or file_path.startswith(dir_path + '\\'):
                files_to_remove.append(file_path)
        
        # Remove all files in directory
        for file_path in files_to_remove:
            self._remove_file(file_path)
    
    def _update_counter(self, selected: int, total: int):
        self.counter_label.config(text=f"{selected} / {total} files selected")
    
    def _filter_tree(self):
        search_text = self.search_var.get().lower()
        
        if search_text == "filter files and folders by name":
            search_text = ""
        
        # Simple filter: hide/show file frames based on search
        for file_path, frame in self.file_items.items():
            file_name = Path(file_path).name.lower()
            if not search_text or search_text in file_name:
                frame.pack(fill=tk.X, padx=(0, 0), pady=1)
            else:
                frame.pack_forget()
    
    def get_selected_files(self) -> List[str]:
        return list(self.selected_files)
    
    def select_all(self):
        for file_path in self.file_data.keys():
            self.selected_files.add(file_path)
            if file_path in self.file_items:
                frame = self.file_items[file_path]
                checkbox_var = getattr(frame, 'checkbox_var', None)
                if checkbox_var:
                    checkbox_var.set(True)
        
        self._update_counter(len(self.selected_files), len(self.file_data))
        
        if self.on_selection_change:
            self.on_selection_change(len(self.selected_files))
    
    def deselect_all(self):
        for file_path in self.file_data.keys():
            if file_path in self.file_items:
                frame = self.file_items[file_path]
                checkbox_var = getattr(frame, 'checkbox_var', None)
                if checkbox_var:
                    checkbox_var.set(False)
        
        self.selected_files.clear()
        self._update_counter(0, len(self.file_data))
        
        if self.on_selection_change:
            self.on_selection_change(0)