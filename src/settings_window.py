import tkinter as tk
from tkinter import ttk, messagebox
from typing import List, Dict, Any
from pathlib import Path

from ui_components import ModernButton, ModernCheckbox, ModernEntry


class SettingsWindow:
    def __init__(self, parent, config_manager, localization):
        self.parent = parent
        self.config_manager = config_manager
        self.localization = localization
        
        # Create window
        self.window = tk.Toplevel(parent)
        self.window.title(self.localization.get('settings.title'))
        self.window.geometry("600x500")
        self.window.resizable(True, True)
        
        # Make window modal
        self.window.transient(parent)
        self.window.grab_set()
        
        # Center window
        self._center_window()
        
        # Variables for settings
        self.temp_settings = {}
        
        self._create_widgets()
        self._load_current_settings()
    
    def _center_window(self):
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f'+{x}+{y}')
    
    def _create_widgets(self):
        # Main container
        main_frame = tk.Frame(self.window, bg='white', padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create notebook for tabs
        notebook = ttk.Notebook(main_frame)
        notebook.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        # General Settings Tab
        general_frame = tk.Frame(notebook, bg='white')
        notebook.add(general_frame, text="General")
        self._create_general_tab(general_frame)
        
        # File Settings Tab
        file_frame = tk.Frame(notebook, bg='white')
        notebook.add(file_frame, text="Files")
        self._create_file_tab(file_frame)
        
        # Interface Settings Tab
        interface_frame = tk.Frame(notebook, bg='white')
        notebook.add(interface_frame, text="Interface")
        self._create_interface_tab(interface_frame)
        
        # Project Types Tab
        projects_frame = tk.Frame(notebook, bg='white')
        notebook.add(projects_frame, text="Project Types")
        self._create_projects_tab(projects_frame)
        
        # Buttons frame
        buttons_frame = tk.Frame(main_frame, bg='white')
        buttons_frame.pack(fill=tk.X)
        
        # Action buttons
        ModernButton(
            buttons_frame,
            text=self.localization.get('settings.save'),
            command=self._save_settings,
            bg_color='#4CAF50',
            hover_color='#45A049'
        ).pack(side=tk.RIGHT, padx=(10, 0))
        
        ModernButton(
            buttons_frame,
            text="Cancel",
            command=self.window.destroy,
            bg_color='#757575',
            hover_color='#616161'
        ).pack(side=tk.RIGHT)
        
        ModernButton(
            buttons_frame,
            text=self.localization.get('settings.reset'),
            command=self._reset_to_defaults,
            bg_color='#FF9800',
            hover_color='#F57C00'
        ).pack(side=tk.LEFT)
    
    def _create_general_tab(self, parent):
        # Language settings
        lang_frame = tk.LabelFrame(parent, text="Language", bg='white', font=('Segoe UI', 11, 'bold'))
        lang_frame.pack(fill=tk.X, padx=10, pady=10)
        
        lang_inner = tk.Frame(lang_frame, bg='white')
        lang_inner.pack(padx=10, pady=10)
        
        tk.Label(lang_inner, text="Interface Language:", bg='white', font=('Segoe UI', 10)).pack(anchor='w')
        
        self.language_var = tk.StringVar(value=self.config_manager.get_language())
        lang_combo = ttk.Combobox(
            lang_inner,
            textvariable=self.language_var,
            values=['tr', 'en'],
            state='readonly',
            width=20
        )
        lang_combo.pack(anchor='w', pady=(5, 0))
        
        # Output settings
        output_frame = tk.LabelFrame(parent, text="Output Settings", bg='white', font=('Segoe UI', 11, 'bold'))
        output_frame.pack(fill=tk.X, padx=10, pady=10)
        
        output_inner = tk.Frame(output_frame, bg='white')
        output_inner.pack(padx=10, pady=10)
        
        tk.Label(output_inner, text="Default Output Format:", bg='white', font=('Segoe UI', 10)).pack(anchor='w')
        
        self.output_format_var = tk.StringVar(value=self.config_manager.get_output_format())
        format_combo = ttk.Combobox(
            output_inner,
            textvariable=self.output_format_var,
            values=['txt', 'docx', 'pdf'],
            state='readonly',
            width=20
        )
        format_combo.pack(anchor='w', pady=(5, 0))
        
        tk.Label(output_inner, text="Default Encoding:", bg='white', font=('Segoe UI', 10)).pack(anchor='w', pady=(10, 0))
        
        self.encoding_var = tk.StringVar(value=self.config_manager.get('encoding', 'utf-8'))
        encoding_combo = ttk.Combobox(
            output_inner,
            textvariable=self.encoding_var,
            values=['utf-8', 'utf-16', 'ascii', 'latin1'],
            state='readonly',
            width=20
        )
        encoding_combo.pack(anchor='w', pady=(5, 0))
        
        tk.Label(output_inner, text="Max File Size (MB):", bg='white', font=('Segoe UI', 10)).pack(anchor='w', pady=(10, 0))
        
        self.max_file_size_var = tk.StringVar(value=str(self.config_manager.get('max_file_size_mb', 10)))
        max_size_entry = tk.Entry(
            output_inner,
            textvariable=self.max_file_size_var,
            width=20
        )
        max_size_entry.pack(anchor='w', pady=(5, 0))
    
    def _create_file_tab(self, parent):
        # Ignored folders
        folders_frame = tk.LabelFrame(parent, text=self.localization.get('settings.ignored_folders'), 
                                     bg='white', font=('Segoe UI', 11, 'bold'))
        folders_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        folders_inner = tk.Frame(folders_frame, bg='white')
        folders_inner.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Folders listbox
        folders_list_frame = tk.Frame(folders_inner, bg='white')
        folders_list_frame.pack(fill=tk.BOTH, expand=True)
        
        folders_scrollbar = ttk.Scrollbar(folders_list_frame)
        folders_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.folders_listbox = tk.Listbox(
            folders_list_frame,
            yscrollcommand=folders_scrollbar.set,
            height=6
        )
        self.folders_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        folders_scrollbar.config(command=self.folders_listbox.yview)
        
        # Folders buttons
        folders_btn_frame = tk.Frame(folders_inner, bg='white')
        folders_btn_frame.pack(fill=tk.X, pady=(10, 0))
        
        self.new_folder_var = tk.StringVar()
        tk.Entry(
            folders_btn_frame,
            textvariable=self.new_folder_var,
            width=20
        ).pack(side=tk.LEFT, padx=(0, 5))
        
        tk.Button(
            folders_btn_frame,
            text=self.localization.get('settings.add_new'),
            command=self._add_ignored_folder,
            bg='#4CAF50',
            fg='white',
            relief=tk.FLAT
        ).pack(side=tk.LEFT, padx=(0, 5))
        
        tk.Button(
            folders_btn_frame,
            text=self.localization.get('settings.remove'),
            command=self._remove_ignored_folder,
            bg='#F44336',
            fg='white',
            relief=tk.FLAT
        ).pack(side=tk.LEFT)
        
        # Ignored files
        files_frame = tk.LabelFrame(parent, text=self.localization.get('settings.ignored_files'),
                                   bg='white', font=('Segoe UI', 11, 'bold'))
        files_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        files_inner = tk.Frame(files_frame, bg='white')
        files_inner.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Files listbox
        files_list_frame = tk.Frame(files_inner, bg='white')
        files_list_frame.pack(fill=tk.BOTH, expand=True)
        
        files_scrollbar = ttk.Scrollbar(files_list_frame)
        files_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.files_listbox = tk.Listbox(
            files_list_frame,
            yscrollcommand=files_scrollbar.set,
            height=6
        )
        self.files_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        files_scrollbar.config(command=self.files_listbox.yview)
        
        # Files buttons
        files_btn_frame = tk.Frame(files_inner, bg='white')
        files_btn_frame.pack(fill=tk.X, pady=(10, 0))
        
        self.new_file_var = tk.StringVar()
        tk.Entry(
            files_btn_frame,
            textvariable=self.new_file_var,
            width=20
        ).pack(side=tk.LEFT, padx=(0, 5))
        
        tk.Button(
            files_btn_frame,
            text=self.localization.get('settings.add_new'),
            command=self._add_ignored_file,
            bg='#4CAF50',
            fg='white',
            relief=tk.FLAT
        ).pack(side=tk.LEFT, padx=(0, 5))
        
        tk.Button(
            files_btn_frame,
            text=self.localization.get('settings.remove'),
            command=self._remove_ignored_file,
            bg='#F44336',
            fg='white',
            relief=tk.FLAT
        ).pack(side=tk.LEFT)
    
    def _create_interface_tab(self, parent):
        # Window settings
        window_frame = tk.LabelFrame(parent, text="Window Settings", bg='white', font=('Segoe UI', 11, 'bold'))
        window_frame.pack(fill=tk.X, padx=10, pady=10)
        
        window_inner = tk.Frame(window_frame, bg='white')
        window_inner.pack(padx=10, pady=10)
        
        # Fullscreen option
        self.fullscreen_var = tk.BooleanVar(value=self.config_manager.get('interface.fullscreen', True))
        tk.Checkbutton(
            window_inner,
            text="Start in fullscreen/maximized mode",
            variable=self.fullscreen_var,
            bg='white',
            font=('Segoe UI', 10)
        ).pack(anchor='w')
        
        # Animations option
        self.animations_var = tk.BooleanVar(value=self.config_manager.get('interface.animations', True))
        tk.Checkbutton(
            window_inner,
            text="Enable animations",
            variable=self.animations_var,
            bg='white',
            font=('Segoe UI', 10)
        ).pack(anchor='w', pady=(5, 0))
        
        # Window size (when not fullscreen)
        tk.Label(window_inner, text="Window Size (when not fullscreen):", bg='white', font=('Segoe UI', 10)).pack(anchor='w', pady=(10, 0))
        
        self.window_size_var = tk.StringVar(value=self.config_manager.get('interface.window_size', '900x700'))
        size_entry = tk.Entry(
            window_inner,
            textvariable=self.window_size_var,
            width=20
        )
        size_entry.pack(anchor='w', pady=(5, 0))
        
        tk.Label(window_inner, text="(Format: WIDTHxHEIGHT, e.g., 900x700)", bg='white', 
                font=('Segoe UI', 9), fg='#666666').pack(anchor='w', pady=(2, 0))
    
    def _create_projects_tab(self, parent):
        # Project types management
        projects_frame = tk.LabelFrame(parent, text="Project Types", bg='white', font=('Segoe UI', 11, 'bold'))
        projects_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        projects_inner = tk.Frame(projects_frame, bg='white')
        projects_inner.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Project types tree
        tree_frame = tk.Frame(projects_inner, bg='white')
        tree_frame.pack(fill=tk.BOTH, expand=True)
        
        tree_scroll = ttk.Scrollbar(tree_frame)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.projects_tree = ttk.Treeview(
            tree_frame,
            columns=('extensions',),
            show='tree headings',
            yscrollcommand=tree_scroll.set
        )
        self.projects_tree.heading('#0', text='Project Type')
        self.projects_tree.heading('extensions', text='Extensions')
        self.projects_tree.column('#0', width=200)
        self.projects_tree.column('extensions', width=300)
        
        self.projects_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        tree_scroll.config(command=self.projects_tree.yview)
        
        # Add/Edit form
        form_frame = tk.Frame(projects_inner, bg='white')
        form_frame.pack(fill=tk.X, pady=(10, 0))
        
        tk.Label(form_frame, text="Type Name:", bg='white', font=('Segoe UI', 10)).grid(row=0, column=0, sticky='w')
        self.project_name_var = tk.StringVar()
        tk.Entry(form_frame, textvariable=self.project_name_var, width=20).grid(row=0, column=1, padx=(5, 0))
        
        tk.Label(form_frame, text="Extensions:", bg='white', font=('Segoe UI', 10)).grid(row=1, column=0, sticky='w', pady=(5, 0))
        self.project_extensions_var = tk.StringVar()
        tk.Entry(form_frame, textvariable=self.project_extensions_var, width=40).grid(row=1, column=1, padx=(5, 0), pady=(5, 0))
        
        tk.Label(form_frame, text="(Comma separated: .py, .txt, .md)", bg='white', 
                font=('Segoe UI', 9), fg='#666666').grid(row=2, column=1, sticky='w', padx=(5, 0))
        
        # Buttons
        btn_frame = tk.Frame(form_frame, bg='white')
        btn_frame.grid(row=3, column=0, columnspan=2, pady=(10, 0), sticky='w')
        
        tk.Button(
            btn_frame,
            text="Add/Update",
            command=self._add_project_type,
            bg='#4CAF50',
            fg='white',
            relief=tk.FLAT
        ).pack(side=tk.LEFT, padx=(0, 5))
        
        tk.Button(
            btn_frame,
            text="Remove Selected",
            command=self._remove_project_type,
            bg='#F44336',
            fg='white',
            relief=tk.FLAT
        ).pack(side=tk.LEFT)
        
        # Bind tree selection
        self.projects_tree.bind('<<TreeviewSelect>>', self._on_project_select)
    
    def _load_current_settings(self):
        # Load ignored folders
        ignored_folders = self.config_manager.get_ignored_folders()
        for folder in ignored_folders:
            self.folders_listbox.insert(tk.END, folder)
        
        # Load ignored files
        ignored_files = self.config_manager.get_ignored_files()
        for file in ignored_files:
            self.files_listbox.insert(tk.END, file)
        
        # Load project types
        project_types = self.config_manager.get_project_types()
        for name, extensions in project_types.items():
            extensions_str = ', '.join(extensions)
            self.projects_tree.insert('', 'end', text=name, values=(extensions_str,))
    
    def _add_ignored_folder(self):
        folder = self.new_folder_var.get().strip()
        if folder and folder not in self.folders_listbox.get(0, tk.END):
            self.folders_listbox.insert(tk.END, folder)
            self.new_folder_var.set('')
    
    def _remove_ignored_folder(self):
        selection = self.folders_listbox.curselection()
        if selection:
            self.folders_listbox.delete(selection[0])
    
    def _add_ignored_file(self):
        file = self.new_file_var.get().strip()
        if file and file not in self.files_listbox.get(0, tk.END):
            self.files_listbox.insert(tk.END, file)
            self.new_file_var.set('')
    
    def _remove_ignored_file(self):
        selection = self.files_listbox.curselection()
        if selection:
            self.files_listbox.delete(selection[0])
    
    def _add_project_type(self):
        name = self.project_name_var.get().strip()
        extensions = self.project_extensions_var.get().strip()
        
        if not name or not extensions:
            messagebox.showwarning("Warning", "Please enter both name and extensions")
            return
        
        # Parse extensions
        ext_list = [ext.strip() for ext in extensions.split(',') if ext.strip()]
        
        # Check if already exists
        for item in self.projects_tree.get_children():
            if self.projects_tree.item(item, 'text') == name:
                # Update existing
                self.projects_tree.item(item, values=(extensions,))
                self.project_name_var.set('')
                self.project_extensions_var.set('')
                return
        
        # Add new
        self.projects_tree.insert('', 'end', text=name, values=(extensions,))
        self.project_name_var.set('')
        self.project_extensions_var.set('')
    
    def _remove_project_type(self):
        selection = self.projects_tree.selection()
        if selection:
            self.projects_tree.delete(selection[0])
    
    def _on_project_select(self, event):
        selection = self.projects_tree.selection()
        if selection:
            item = selection[0]
            name = self.projects_tree.item(item, 'text')
            extensions = self.projects_tree.item(item, 'values')[0]
            
            self.project_name_var.set(name)
            self.project_extensions_var.set(extensions)
    
    def _save_settings(self):
        try:
            # Save general settings
            self.config_manager.set_language(self.language_var.get())
            self.config_manager.set('output_settings.default_format', self.output_format_var.get())
            self.config_manager.set('encoding', self.encoding_var.get())
            self.config_manager.set('max_file_size_mb', int(self.max_file_size_var.get()))
            
            # Save interface settings
            self.config_manager.set('interface.fullscreen', self.fullscreen_var.get())
            self.config_manager.set('interface.animations', self.animations_var.get())
            self.config_manager.set('interface.window_size', self.window_size_var.get())
            
            # Save ignored folders
            folders = list(self.folders_listbox.get(0, tk.END))
            self.config_manager.set('ignore_folders', folders)
            
            # Save ignored files
            files = list(self.files_listbox.get(0, tk.END))
            self.config_manager.set('ignore_files', files)
            
            # Save project types
            project_types = {}
            for item in self.projects_tree.get_children():
                name = self.projects_tree.item(item, 'text')
                extensions_str = self.projects_tree.item(item, 'values')[0]
                extensions = [ext.strip() for ext in extensions_str.split(',') if ext.strip()]
                project_types[name] = extensions
            
            self.config_manager.set('project_types', project_types)
            
            messagebox.showinfo("Success", self.localization.get('messages.settings_saved'))
            self.window.destroy()
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save settings: {str(e)}")
    
    def _reset_to_defaults(self):
        if messagebox.askyesno("Confirm", self.localization.get('messages.confirm_reset')):
            self.config_manager.reset_to_defaults()
            messagebox.showinfo("Success", "Settings reset to defaults. Please restart the application.")
            self.window.destroy()