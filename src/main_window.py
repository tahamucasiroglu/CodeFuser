import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from pathlib import Path
import threading
from typing import List, Optional, Dict, Any
import json

from ui_components import (
    ModernButton, AnimatedProgressBar, ModernEntry, 
    ModernScrolledText, AnimatedLabel, ModernCheckbox, ModernCombobox
)
from file_tree_widget import FileTreeWidget
from settings_window import SettingsWindow
from config_manager import ConfigManager
from localization_manager import LocalizationManager
from file_scanner import FileScanner, FileScannerProgress
from output_manager import OutputManager


class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.config_manager = ConfigManager()
        self.localization = LocalizationManager(self.config_manager)
        self.file_scanner = FileScanner(self.config_manager)
        self.output_manager = OutputManager(self.config_manager)
        
        self.selected_folder = None
        self.scanned_files = []
        self.is_processing = False
        
        self._setup_window()
        self._create_menu()
        self._create_widgets()
        self._apply_theme()
    
    def _setup_window(self):
        self.root.title(self.localization.get('app_title'))
        
        # Get screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Check if fullscreen is enabled in settings
        fullscreen_enabled = self.config_manager.get('interface.fullscreen', True)
        
        if fullscreen_enabled:
            # Start maximized/fullscreen
            self.root.state('zoomed')  # Windows
            try:
                self.root.attributes('-zoomed', True)  # Linux
            except:
                pass
        else:
            # Set window size and center it
            window_size = self.config_manager.get('interface.window_size', '900x700')
            width, height = map(int, window_size.split('x'))
            
            x = (screen_width - width) // 2
            y = (screen_height - height) // 2
            
            self.root.geometry(f"{width}x{height}+{x}+{y}")
        
        self.root.minsize(800, 600)
        
        # Set icon if available
        try:
            icon_path = Path(__file__).parent.parent / 'assets' / 'icon.ico'
            if icon_path.exists():
                self.root.iconbitmap(str(icon_path))
        except:
            pass
    
    def _create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label=self.localization.get('menu.file'), menu=file_menu)
        file_menu.add_command(label="Exit", command=self.root.quit)
        
        # Settings menu
        settings_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label=self.localization.get('menu.settings'), menu=settings_menu)
        settings_menu.add_command(label=self.localization.get('menu.settings'), 
                                command=self._open_settings)
        
        # Language menu
        language_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label=self.localization.get('menu.language'), menu=language_menu)
        
        for lang_code, lang_name in self.localization.get_available_languages().items():
            language_menu.add_radiobutton(
                label=lang_name,
                command=lambda lc=lang_code: self._change_language(lc),
                variable=tk.StringVar(value=self.localization.current_language),
                value=lang_code
            )
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label=self.localization.get('menu.help'), menu=help_menu)
        help_menu.add_command(label=self.localization.get('menu.about'), 
                            command=self._show_about)
    
    def _create_widgets(self):
        # Main container with padding
        main_frame = tk.Frame(self.root, bg='white')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Folder selection section
        folder_frame = tk.LabelFrame(
            main_frame, 
            text=self.localization.get('main_screen.select_folder'),
            bg='white', 
            font=('Segoe UI', 11, 'bold')
        )
        folder_frame.pack(fill=tk.X, pady=(0, 10))
        
        folder_inner = tk.Frame(folder_frame, bg='white')
        folder_inner.pack(padx=10, pady=10)
        
        self.folder_path_var = tk.StringVar()
        self.folder_entry = ModernEntry(
            folder_inner, 
            placeholder=self.localization.get('main_screen.select_folder'),
            textvariable=self.folder_path_var,
            state='readonly',
            width=50
        )
        self.folder_entry.pack(side=tk.LEFT, padx=(0, 10))
        
        self.browse_button = ModernButton(
            folder_inner,
            text=self.localization.get('main_screen.browse'),
            command=self._browse_folder
        )
        self.browse_button.pack(side=tk.LEFT)
        
        # Scan files button
        self.scan_button = ModernButton(
            folder_inner,
            text=self.localization.get('main_screen.scan_files'),
            command=self._scan_files,
            bg_color='#4CAF50',
            hover_color='#45A049'
        )
        self.scan_button.pack(side=tk.LEFT, padx=(10, 0))
        
        # Project type selection
        type_frame = tk.LabelFrame(
            main_frame,
            text=self.localization.get('main_screen.project_type'),
            bg='white',
            font=('Segoe UI', 11, 'bold')
        )
        type_frame.pack(fill=tk.X, pady=(0, 10))
        
        type_inner = tk.Frame(type_frame, bg='white')
        type_inner.pack(padx=10, pady=10)
        
        # Project type combobox
        project_types = list(self.config_manager.get_project_types().keys())
        self.project_type_var = tk.StringVar(value=project_types[0] if project_types else '')
        
        self.project_type_combo = ModernCombobox(
            type_inner,
            textvariable=self.project_type_var,
            values=project_types,
            state='readonly',
            width=30
        )
        self.project_type_combo.pack(side=tk.LEFT, padx=(0, 20))
        self.project_type_combo.bind('<<ComboboxSelected>>', self._on_project_type_changed)
        
        # Custom extensions entry
        tk.Label(
            type_inner,
            text=self.localization.get('main_screen.custom_extensions'),
            bg='white',
            font=('Segoe UI', 10)
        ).pack(side=tk.LEFT, padx=(0, 5))
        
        self.custom_extensions_var = tk.StringVar()
        self.custom_extensions_entry = ModernEntry(
            type_inner,
            placeholder=".py, .txt, .md",
            textvariable=self.custom_extensions_var,
            width=30
        )
        self.custom_extensions_entry.pack(side=tk.LEFT)
        
        # Options frame
        options_frame = tk.Frame(main_frame, bg='white')
        options_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Include ignored checkbox
        self.include_ignored_var = tk.BooleanVar(value=False)
        self.include_ignored_check = ModernCheckbox(
            options_frame,
            text=self.localization.get('settings.include_ignored'),
            variable=self.include_ignored_var,
            bg='white'
        )
        self.include_ignored_check.pack(side=tk.LEFT, padx=(0, 20))
        
        # Output format selection
        tk.Label(
            options_frame,
            text=self.localization.get('main_screen.output_format'),
            bg='white',
            font=('Segoe UI', 10)
        ).pack(side=tk.LEFT, padx=(0, 5))
        
        self.output_format_var = tk.StringVar(value=self.config_manager.get_output_format())
        self.output_format_combo = ModernCombobox(
            options_frame,
            textvariable=self.output_format_var,
            values=self.output_manager.get_available_formats(),
            state='readonly',
            width=10
        )
        self.output_format_combo.pack(side=tk.LEFT)
        
        # File selection section
        file_selection_frame = tk.LabelFrame(
            main_frame,
            text=self.localization.get('main_screen.file_selection'),
            bg='white',
            font=('Segoe UI', 11, 'bold')
        )
        file_selection_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # File tree widget
        self.file_tree = FileTreeWidget(file_selection_frame, bg='white')
        self.file_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=(5, 10))
        self.file_tree.on_selection_change = self._on_file_selection_change
        
        # Prompt section
        prompt_frame = tk.LabelFrame(
            main_frame,
            text=self.localization.get('main_screen.prompt_text'),
            bg='white',
            font=('Segoe UI', 11, 'bold')
        )
        prompt_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        self.prompt_text = ModernScrolledText(
            prompt_frame,
            height=6,
            bg='white',
            font=('Segoe UI', 10)
        )
        self.prompt_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Insert placeholder
        self.prompt_text.insert('1.0', self.localization.get('main_screen.prompt_placeholder'))
        self.prompt_text.config(fg='#999999')
        
        # Bind focus events for placeholder
        self.prompt_text.text.bind('<FocusIn>', self._on_prompt_focus_in)
        self.prompt_text.text.bind('<FocusOut>', self._on_prompt_focus_out)
        
        # Progress section
        progress_frame = tk.Frame(main_frame, bg='white')
        progress_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.progress_bar = AnimatedProgressBar(progress_frame, width=760, height=25)
        self.progress_bar.pack()
        
        self.progress_label = AnimatedLabel(
            progress_frame,
            text="",
            bg='white',
            font=('Segoe UI', 9)
        )
        self.progress_label.pack(pady=(5, 0))
        
        # Action buttons
        button_frame = tk.Frame(main_frame, bg='white')
        button_frame.pack(fill=tk.X)
        
        self.start_button = ModernButton(
            button_frame,
            text=self.localization.get('main_screen.start_process'),
            command=self._start_process,
            bg_color='#4CAF50',
            hover_color='#45A049',
            state=tk.DISABLED
        )
        self.start_button.pack(side=tk.RIGHT, padx=(10, 0))
        
        self.cancel_button = ModernButton(
            button_frame,
            text=self.localization.get('main_screen.cancel'),
            command=self._cancel_process,
            bg_color='#F44336',
            hover_color='#DA190B',
            state=tk.DISABLED
        )
        self.cancel_button.pack(side=tk.RIGHT)
        
        # Update extensions display
        self._on_project_type_changed()
    
    def _on_prompt_focus_in(self, event):
        if self.prompt_text.get('1.0', 'end-1c') == self.localization.get('main_screen.prompt_placeholder'):
            self.prompt_text.delete('1.0', tk.END)
            self.prompt_text.config(fg='black')
    
    def _on_prompt_focus_out(self, event):
        if not self.prompt_text.get('1.0', 'end-1c').strip():
            self.prompt_text.insert('1.0', self.localization.get('main_screen.prompt_placeholder'))
            self.prompt_text.config(fg='#999999')
    
    def _browse_folder(self):
        folder = filedialog.askdirectory(
            title=self.localization.get('main_screen.select_folder')
        )
        if folder:
            self.selected_folder = Path(folder)
            self.folder_path_var.set(str(self.selected_folder))
            # Clear file tree when new folder is selected
            self.file_tree.populate_tree([])
            self.scanned_files = []
    
    def _scan_files(self):
        if not self.selected_folder:
            messagebox.showwarning(
                self.localization.get('app_title'),
                self.localization.get('messages.select_folder_first')
            )
            return
        
        # Get extensions
        if self.project_type_var.get() == 'Custom' or not self.project_type_var.get():
            extensions_text = self.custom_extensions_var.get()
            extensions = [ext.strip() for ext in extensions_text.split(',') if ext.strip()]
        else:
            extensions = self.config_manager.get_project_types().get(self.project_type_var.get(), [])
        
        if not extensions:
            messagebox.showwarning(
                self.localization.get('app_title'),
                "Please select a project type or enter custom extensions"
            )
            return
        
        # Disable UI during scanning
        self.scan_button.config(state=tk.DISABLED)
        self.start_button.config(state=tk.DISABLED)
        
        # Start scanning in background thread
        thread = threading.Thread(
            target=self._scan_files_thread,
            args=(extensions, self.include_ignored_var.get())
        )
        thread.daemon = True
        thread.start()
    
    def _scan_files_thread(self, extensions: List[str], include_ignored: bool):
        try:
            # Update progress
            self.root.after(0, lambda: self.progress_label.start_animation(self.localization.get('progress.scanning')))
            self.root.after(0, lambda: self.progress_bar.set_indeterminate(True))
            
            # Scan files
            files = self.file_scanner.scan_directory(
                self.selected_folder,
                extensions,
                include_ignored,
                self._update_progress
            )
            
            # Convert FileInfo objects to dicts for file tree
            file_dicts = [
                {
                    'path': f.path,
                    'relative_path': f.relative_path,
                    'size': f.size
                }
                for f in files
            ]
            
            self.scanned_files = file_dicts
            
            # Update file tree
            self.root.after(0, lambda: self.file_tree.populate_tree(file_dicts))
            
            # Stop progress
            self.root.after(0, lambda: self.progress_bar.set_indeterminate(False))
            self.root.after(0, lambda: self.progress_bar.set_progress(100))
            self.root.after(0, lambda: self.progress_label.stop_animation(f"Found {len(files)} files"))
            
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror(
                self.localization.get('app_title'),
                self.localization.get('progress.error', error=str(e))
            ))
        finally:
            # Re-enable UI
            self.root.after(0, lambda: self.scan_button.config(state=tk.NORMAL))
            self.root.after(0, lambda: self.start_button.config(state=tk.NORMAL))
            self.root.after(0, lambda: self.progress_bar.set_progress(0))
            self.root.after(0, lambda: self.progress_label.config(text=""))
    
    
    def _on_file_selection_change(self, selected_count: int):
        # Update UI based on selection
        if selected_count > 0:
            self.start_button.config(state=tk.NORMAL)
        else:
            self.start_button.config(state=tk.DISABLED)
    
    def _on_project_type_changed(self, event=None):
        project_type = self.project_type_var.get()
        if project_type and project_type != 'Custom':
            extensions = self.config_manager.get_project_types().get(project_type, [])
            self.custom_extensions_var.set(', '.join(extensions))
            self.custom_extensions_entry.entry.config(state='readonly')
        else:
            self.custom_extensions_entry.entry.config(state='normal')
            self.custom_extensions_var.set('')
    
    def _start_process(self):
        # Get selected files from file tree
        selected_files = self.file_tree.get_selected_files()
        
        if not selected_files:
            messagebox.showwarning(
                self.localization.get('app_title'),
                "Please select at least one file to process"
            )
            return
        
        # Get prompt
        prompt_text = self.prompt_text.get('1.0', 'end-1c')
        if prompt_text == self.localization.get('main_screen.prompt_placeholder'):
            prompt_text = ""
        
        # Disable UI
        self._set_ui_state(False)
        self.is_processing = True
        
        # Get only selected files
        files_to_process = [f for f in self.scanned_files if f['relative_path'] in selected_files]
        
        # Start processing in background thread
        thread = threading.Thread(
            target=self._process_files,
            args=(files_to_process, prompt_text)
        )
        thread.daemon = True
        thread.start()
    
    def _process_files(self, files: List[Dict[str, Any]], prompt: str):
        try:
            # Update progress
            self.progress_label.start_animation(self.localization.get('progress.generating'))
            self.progress_bar.set_progress(50)
            
            if not files:
                self.root.after(0, lambda: messagebox.showinfo(
                    self.localization.get('app_title'),
                    "No files selected"
                ))
                return
            
            # Generate output
            self.progress_label.config(text=self.localization.get('progress.generating'))
            self.progress_bar.set_indeterminate(False)
            self.progress_bar.set_progress(90)
            
            # Create output file
            output_format = self.output_format_var.get()
            output_filename = f"codefuser_output.{output_format}"
            output_path = self.selected_folder / output_filename
            
            output_path = self.output_manager.create_output(
                files,
                output_path,
                output_format,
                prompt
            )
            
            # Complete
            self.progress_bar.set_progress(100)
            self.progress_label.stop_animation(self.localization.get('progress.completed'))
            
            self.root.after(0, lambda: messagebox.showinfo(
                self.localization.get('app_title'),
                self.localization.get('messages.output_saved', filepath=str(output_path))
            ))
            
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror(
                self.localization.get('app_title'),
                self.localization.get('progress.error', error=str(e))
            ))
        finally:
            self.root.after(0, lambda: self._set_ui_state(True))
            self.is_processing = False
    
    def _update_progress(self, progress: FileScannerProgress):
        percentage = progress.get_progress_percentage()
        self.root.after(0, lambda: self.progress_bar.set_progress(percentage))
        
        if progress.current_file:
            self.root.after(0, lambda: self.progress_label.config(
                text=self.localization.get('progress.processing', filename=progress.current_file)
            ))
    
    def _cancel_process(self):
        if self.is_processing:
            self.file_scanner.stop_scanning()
            self.is_processing = False
            self._set_ui_state(True)
            self.progress_label.stop_animation("Cancelled")
            self.progress_bar.set_progress(0)
    
    def _set_ui_state(self, enabled: bool):
        state = tk.NORMAL if enabled else tk.DISABLED
        
        self.browse_button.config(state=state)
        self.scan_button.config(state=state)
        self.project_type_combo.config(state='readonly' if enabled else 'disabled')
        self.output_format_combo.config(state='readonly' if enabled else 'disabled')
        self.start_button.config(state=state if enabled and self.file_tree.get_selected_files() else tk.DISABLED)
        self.cancel_button.config(state=tk.NORMAL if not enabled else tk.DISABLED)
        
        if enabled:
            self.progress_bar.set_progress(0)
            self.progress_label.config(text="")
    
    def _open_settings(self):
        settings_window = SettingsWindow(self.root, self.config_manager, self.localization)
    
    def _change_language(self, language_code: str):
        self.localization.set_language(language_code)
        messagebox.showinfo(
            self.localization.get('app_title'),
            "Please restart the application for language changes to take effect."
        )
    
    def _show_about(self):
        about_text = f"""CodeFuser v1.0.0

A modern tool for collecting and merging project files with custom prompts.

Created with ❤️ using Python and Tkinter

© 2024 CodeFuser Team"""
        
        messagebox.showinfo(self.localization.get('menu.about'), about_text)
    
    def _apply_theme(self):
        # Apply modern theme colors
        self.root.configure(bg='white')
        
        # Configure ttk styles
        style = ttk.Style()
        style.theme_use('clam')
    
    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = MainWindow()
    app.run()