import tkinter as tk
from tkinter import ttk
from pathlib import Path
from typing import Dict, List, Set, Optional, Callable
import os


class FileTreeWidget(tk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        
        self.selected_files: Set[str] = set()
        self.all_files: List[Dict[str, any]] = []
        self.filtered_files: List[Dict[str, any]] = []
        self.on_selection_change: Optional[Callable[[int], None]] = None
        
        # Virtual scrolling variables
        self.item_height = 30
        self.visible_items = 20
        self.scroll_position = 0
        self.search_timer = None
        
        self._create_widgets()
        self._setup_bindings()
    
    def _create_widgets(self):
        # Header frame with search and counter
        header_frame = tk.Frame(self, bg='white', height=40)
        header_frame.pack(fill=tk.X, padx=5, pady=5)
        header_frame.pack_propagate(False)
        
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
        
        # File counter
        self.counter_label = tk.Label(
            header_frame,
            text="0 / 0 files selected",
            bg='white',
            fg='#FF6B6B',
            font=('Segoe UI', 10, 'bold')
        )
        self.counter_label.pack(side=tk.RIGHT, padx=(10, 0))
        
        # Main listbox with scrollbar (much faster than custom widgets)
        list_frame = tk.Frame(self, bg='#f8f9fa')
        list_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=(0, 5))
        
        # Create listbox and scrollbar
        self.scrollbar = ttk.Scrollbar(list_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.listbox = tk.Listbox(
            list_frame,
            yscrollcommand=self.scrollbar.set,
            selectmode=tk.NONE,
            font=('Segoe UI', 10),
            bg='#f8f9fa',
            selectbackground='#e3f2fd',
            activestyle='none',
            borderwidth=0,
            highlightthickness=0
        )
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.config(command=self.listbox.yview)
        
        # Control buttons frame
        control_frame = tk.Frame(self, bg='white', height=40)
        control_frame.pack(fill=tk.X, padx=5)
        control_frame.pack_propagate(False)
        
        # Select/Deselect buttons
        tk.Button(
            control_frame,
            text="Select All",
            command=self.select_all,
            bg='#4CAF50',
            fg='white',
            relief=tk.FLAT,
            font=('Segoe UI', 9),
            padx=10
        ).pack(side=tk.LEFT, padx=(0, 5), pady=5)
        
        tk.Button(
            control_frame,
            text="Deselect All", 
            command=self.deselect_all,
            bg='#FF9800',
            fg='white',
            relief=tk.FLAT,
            font=('Segoe UI', 9),
            padx=10
        ).pack(side=tk.LEFT, padx=(0, 5), pady=5)
        
        tk.Button(
            control_frame,
            text="Remove Selected",
            command=self._remove_selected,
            bg='#F44336',
            fg='white', 
            relief=tk.FLAT,
            font=('Segoe UI', 9),
            padx=10
        ).pack(side=tk.LEFT, pady=5)
        
        # Empty state label
        self.empty_label = tk.Label(
            list_frame,
            text="No files scanned yet. Please select a folder first and click 'Scan Files' button.",
            bg='#f8f9fa',
            fg='#666666',
            font=('Segoe UI', 11),
            wraplength=400
        )
    
    def _setup_bindings(self):
        # Bind search with debouncing
        self.search_var.trace('w', self._on_search_changed)
        
        # Bind listbox events
        self.listbox.bind('<Button-1>', self._on_listbox_click)
        self.listbox.bind('<Double-Button-1>', self._on_listbox_double_click)
        
        # Bind mouse wheel
        self.listbox.bind("<MouseWheel>", self._on_mousewheel)
    
    def _on_search_focus_in(self, event):
        if self.search_entry.get() == "Filter files and folders by name":
            self.search_entry.delete(0, tk.END)
            self.search_entry.config(fg='black')
    
    def _on_search_focus_out(self, event):
        if not self.search_entry.get():
            self.search_entry.insert(0, "Filter files and folders by name")
            self.search_entry.config(fg='#999999')
    
    def _on_search_changed(self, *args):
        # Debounce search to avoid lag
        if self.search_timer:
            self.after_cancel(self.search_timer)
        self.search_timer = self.after(300, self._filter_files)
    
    def _on_mousewheel(self, event):
        self.listbox.yview_scroll(int(-1*(event.delta/120)), "units")
    
    def _on_listbox_click(self, event):
        index = self.listbox.nearest(event.y)
        if 0 <= index < len(self.filtered_files):
            file_info = self.filtered_files[index]
            file_path = file_info['relative_path']
            
            # Toggle selection
            if file_path in self.selected_files:
                self.selected_files.remove(file_path)
            else:
                self.selected_files.add(file_path)
            
            self._update_display()
            self._update_counter()
    
    def _on_listbox_double_click(self, event):
        # Double click could be used for other actions
        pass
    
    def populate_tree(self, files: List[Dict[str, any]]):
        """Populate the tree with files"""
        self.all_files = files.copy()
        self.filtered_files = files.copy()
        self.selected_files.clear()
        
        if not files:
            self.listbox.pack_forget()
            self.empty_label.pack(expand=True)
            self._update_counter()
            return
        else:
            self.empty_label.pack_forget()
            self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self._update_display()
        self._update_counter()
    
    def _filter_files(self):
        """Filter files based on search text"""
        search_text = self.search_var.get().lower()
        
        if search_text == "filter files and folders by name" or not search_text:
            self.filtered_files = self.all_files.copy()
        else:
            # Fast filtering using list comprehension
            self.filtered_files = [
                f for f in self.all_files 
                if search_text in Path(f['relative_path']).name.lower()
            ]
        
        self._update_display()
    
    def _update_display(self):
        """Update the listbox display efficiently"""
        self.listbox.delete(0, tk.END)
        
        for file_info in self.filtered_files:
            file_path = file_info['relative_path']
            file_name = Path(file_path).name
            
            # Get file icon
            icon = self._get_file_icon(Path(file_name).suffix.lower())
            
            # Format display text
            selected_marker = "☑️" if file_path in self.selected_files else "☐"
            
            # Show directory structure with indentation
            depth = len(Path(file_path).parts) - 1
            indent = "  " * depth
            
            display_text = f"{selected_marker} {indent}{icon} {file_name}"
            
            self.listbox.insert(tk.END, display_text)
            
            # Color selected items
            if file_path in self.selected_files:
                self.listbox.itemconfig(tk.END, {'bg': '#e3f2fd'})
    
    def _get_file_icon(self, extension: str) -> str:
        """Get file icon based on extension"""
        icons = {
            '.py': '🐍', '.js': '📜', '.ts': '📘', '.jsx': '⚛️', '.tsx': '⚛️',
            '.html': '🌐', '.css': '🎨', '.json': '📋', '.xml': '📄', '.txt': '📝',
            '.md': '📖', '.yml': '⚙️', '.yaml': '⚙️', '.cs': '🔷', '.java': '☕',
            '.cpp': '🔧', '.c': '🔧', '.h': '📎', '.hpp': '📎', '.go': '🐹',
            '.rs': '🦀', '.rb': '💎', '.php': '🐘', '.swift': '🦉', '.kt': '🟣',
        }
        return icons.get(extension, '📄')
    
    def _update_counter(self):
        """Update the file counter"""
        total = len(self.all_files)
        selected = len(self.selected_files)
        self.counter_label.config(text=f"{selected} / {total} files selected")
        
        if self.on_selection_change:
            self.on_selection_change(selected)
    
    def _remove_selected(self):
        """Remove selected files from the list"""
        if not self.selected_files:
            return
        
        # Remove selected files from all_files
        self.all_files = [f for f in self.all_files if f['relative_path'] not in self.selected_files]
        
        # Clear selection since files are removed
        self.selected_files.clear()
        
        # Refilter and update display
        self._filter_files()
        self._update_counter()
        
        # Show empty message if no files left
        if not self.all_files:
            self.listbox.pack_forget()
            self.empty_label.pack(expand=True)
    
    def select_all(self):
        """Select all visible files"""
        for file_info in self.filtered_files:
            self.selected_files.add(file_info['relative_path'])
        
        self._update_display()
        self._update_counter()
    
    def deselect_all(self):
        """Deselect all files"""
        self.selected_files.clear()
        self._update_display()
        self._update_counter()
    
    def get_selected_files(self) -> List[str]:
        """Get list of selected file paths"""
        return list(self.selected_files)
    
    def get_file_count(self) -> int:
        """Get total number of files"""
        return len(self.all_files)