import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path
from typing import Optional, Callable


class FilePromptDialog:
    def __init__(self, parent, file_path: str, current_prompt: str = "", 
                 localization_manager=None):
        self.parent = parent
        self.file_path = file_path
        self.current_prompt = current_prompt
        self.localization = localization_manager
        self.result_prompt = None
        self.callback: Optional[Callable] = None
        
        self._create_dialog()
    
    def _create_dialog(self):
        """Dialog penceresini oluştur"""
        self.dialog = tk.Toplevel(self.parent)
        self.dialog.title(f"Özel Prompt - {Path(self.file_path).name}")
        self.dialog.geometry("640x640")
        self.dialog.resizable(True, True)
        self.dialog.transient(self.parent)
        self.dialog.grab_set()
        
        # Dialog'u merkeze yerleştir
        self.dialog.update_idletasks()
        x = (self.dialog.winfo_screenwidth() // 2) - (640 // 2)
        y = (self.dialog.winfo_screenheight() // 2) - (640 // 2)
        self.dialog.geometry(f"640x640+{x}+{y}")
        
        # Program ikonunu ayarla
        self._set_dialog_icon()
        
        self._create_widgets()
        self._setup_bindings()
    
    def _set_dialog_icon(self):
        """Dialog için program ikonunu ayarla"""
        try:
            # Icon dosyalarını dene
            icon_paths = [
                Path(__file__).parent.parent / 'assets' / 'CodeFuser.ico',
                Path(__file__).parent.parent / 'assets' / 'CodeFuser Logo.png',
                Path(__file__).parent.parent / 'assets' / 'icon.ico',
                Path(__file__).parent.parent / 'assets' / 'icon.png'
            ]
            
            for icon_path in icon_paths:
                if icon_path.exists():
                    if icon_path.suffix.lower() == '.ico':
                        self.dialog.iconbitmap(str(icon_path))
                        return
                    else:
                        # PNG dosyaları için PIL kullan
                        try:
                            from PIL import Image, ImageTk
                            img = Image.open(icon_path)
                            img = img.resize((32, 32), Image.Resampling.LANCZOS)
                            photo = ImageTk.PhotoImage(img)
                            self.dialog.iconphoto(False, photo)
                            # Reference tutmak için dialog'a bağla
                            self.dialog._icon_photo = photo
                            return
                        except ImportError:
                            continue
        except Exception:
            # Icon yüklenemezse devam et
            pass
    
    def _create_widgets(self):
        """Widget'ları oluştur"""
        # Ana container - padding olmadan
        container = tk.Frame(self.dialog, bg='white')
        container.pack(fill=tk.BOTH, expand=True)
        
        # Buton alanı - ÖNCE pack et ki altta kalabilsin
        button_container = tk.Frame(container, bg='white')
        button_container.pack(fill=tk.X, side=tk.BOTTOM, padx=20, pady=(0, 20))
        
        # İçerik alanı - geri kalan tüm alanı kapla
        content_frame = tk.Frame(container, bg='white')
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(20, 10))
        
        # Header
        header_frame = tk.Frame(content_frame, bg='white')
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        # File icon and name
        file_icon = tk.Label(header_frame, text="📄", bg='white', font=('Segoe UI', 20))
        file_icon.pack(side=tk.LEFT, padx=(0, 10))
        
        file_info_frame = tk.Frame(header_frame, bg='white')
        file_info_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        file_name = tk.Label(
            file_info_frame,
            text=Path(self.file_path).name,
            bg='white',
            font=('Segoe UI', 14, 'bold'),
            anchor='w'
        )
        file_name.pack(fill=tk.X)
        
        file_path_label = tk.Label(
            file_info_frame,
            text=self.file_path,
            bg='white',
            fg='#666666',
            font=('Segoe UI', 10),
            anchor='w'
        )
        file_path_label.pack(fill=tk.X)
        
        # Separator
        separator = tk.Frame(content_frame, height=1, bg='#e0e0e0')
        separator.pack(fill=tk.X, pady=(0, 20))
        
        # Instructions
        instructions = tk.Label(
            content_frame,
            text="Bu dosya için özel bir prompt girebilirsiniz. Bu prompt sadece bu dosya için kullanılacak ve genel prompta eklenerek AI'ya gönderilecektir.",
            bg='white',
            fg='#333333',
            font=('Segoe UI', 10),
            wraplength=560,
            justify=tk.LEFT
        )
        instructions.pack(fill=tk.X, pady=(0, 15))
        
        # Prompt frame
        prompt_frame = tk.Frame(content_frame, bg='white')
        prompt_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        prompt_label = tk.Label(
            prompt_frame,
            text="Özel Prompt:",
            bg='white',
            font=('Segoe UI', 11, 'bold'),
            anchor='w'
        )
        prompt_label.pack(fill=tk.X, pady=(0, 5))
        
        # Text area with scrollbar
        text_frame = tk.Frame(prompt_frame, bg='white')
        text_frame.pack(fill=tk.BOTH, expand=True)
        
        self.text_widget = tk.Text(
            text_frame,
            font=('Segoe UI', 10),
            bg='#f8f9fa',
            fg='#333333',
            relief=tk.FLAT,
            borderwidth=1,
            wrap=tk.WORD,
            undo=True,
            padx=10,
            pady=10
        )
        
        scrollbar = ttk.Scrollbar(text_frame, orient=tk.VERTICAL, command=self.text_widget.yview)
        self.text_widget.configure(yscrollcommand=scrollbar.set)
        
        self.text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Placeholder text
        self.placeholder_text = "Örnek: 'Bu dosyadaki güvenlik kontrollerini analiz et' veya 'Bu fonksiyonların performansını değerlendir'"
        if not self.current_prompt:
            self.text_widget.insert('1.0', self.placeholder_text)
            self.text_widget.config(fg='#999999')
        else:
            self.text_widget.insert('1.0', self.current_prompt)
            self.text_widget.config(fg='#333333')
        
        # Character counter
        self.char_counter = tk.Label(
            prompt_frame,
            text="0 karakter",
            bg='white',
            fg='#666666',
            font=('Segoe UI', 9),
            anchor='e'
        )
        self.char_counter.pack(fill=tk.X, pady=(5, 0))
        
        # Button frame - artık button_container içinde
        button_frame = tk.Frame(button_container, bg='white')
        button_frame.pack(fill=tk.X)
        
        # Example prompts button
        example_btn = tk.Button(
            button_frame,
            text="💡 Örnek Promptlar",
            command=self._show_examples,
            bg='#e3f2fd',
            fg='#1976d2',
            relief=tk.FLAT,
            font=('Segoe UI', 9),
            padx=15,
            pady=8,
            cursor='hand2'
        )
        example_btn.pack(side=tk.LEFT)
        
        # Action buttons
        btn_frame = tk.Frame(button_frame, bg='white')
        btn_frame.pack(side=tk.RIGHT)
        
        # Clear button
        if self.current_prompt:
            clear_btn = tk.Button(
                btn_frame,
                text="🗑️ Temizle",
                command=self._clear_prompt,
                bg='#fff3e0',
                fg='#f57c00',
                relief=tk.FLAT,
                font=('Segoe UI', 9),
                padx=15,
                pady=8,
                cursor='hand2'
            )
            clear_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # Cancel button
        cancel_btn = tk.Button(
            btn_frame,
            text="İptal",
            command=self._cancel,
            bg='#f5f5f5',
            fg='#333333',
            relief=tk.FLAT,
            font=('Segoe UI', 9),
            padx=20,
            pady=8,
            cursor='hand2'
        )
        cancel_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # Save button
        save_btn = tk.Button(
            btn_frame,
            text="✅ Kaydet",
            command=self._save_prompt,
            bg='#4CAF50',
            fg='white',
            relief=tk.FLAT,
            font=('Segoe UI', 9, 'bold'),
            padx=20,
            pady=8,
            cursor='hand2'
        )
        save_btn.pack(side=tk.LEFT)
        
        # Focus on text widget
        self.text_widget.focus_set()
        
        # Select all if there's existing content
        if self.current_prompt:
            self.text_widget.tag_add(tk.SEL, '1.0', tk.END)
    
    def _setup_bindings(self):
        """Event binding'leri ayarla"""
        self.text_widget.bind('<FocusIn>', self._on_text_focus_in)
        self.text_widget.bind('<FocusOut>', self._on_text_focus_out)
        self.text_widget.bind('<KeyRelease>', self._update_char_counter)
        self.text_widget.bind('<Button-1>', self._update_char_counter)
        
        # Keyboard shortcuts
        self.dialog.bind('<Control-Return>', lambda e: self._save_prompt())
        self.dialog.bind('<Escape>', lambda e: self._cancel())
        self.dialog.bind('<Control-a>', self._select_all)
        
        # Dialog close
        self.dialog.protocol("WM_DELETE_WINDOW", self._cancel)
    
    def _on_text_focus_in(self, event):
        """Text widget focus aldığında"""
        current_text = self.text_widget.get('1.0', tk.END).strip()
        if current_text == self.placeholder_text:
            self.text_widget.delete('1.0', tk.END)
            self.text_widget.config(fg='#333333')
        self._update_char_counter()
    
    def _on_text_focus_out(self, event):
        """Text widget focus kaybettiğinde"""
        current_text = self.text_widget.get('1.0', tk.END).strip()
        if not current_text:
            self.text_widget.insert('1.0', self.placeholder_text)
            self.text_widget.config(fg='#999999')
        self._update_char_counter()
    
    def _update_char_counter(self, event=None):
        """Karakter sayacını güncelle"""
        current_text = self.text_widget.get('1.0', tk.END).strip()
        if current_text == self.placeholder_text:
            char_count = 0
        else:
            char_count = len(current_text)
        
        self.char_counter.config(text=f"{char_count} karakter")
        
        # Color coding for length
        if char_count > 1000:
            self.char_counter.config(fg='#f44336')  # Red
        elif char_count > 500:
            self.char_counter.config(fg='#ff9800')  # Orange
        else:
            self.char_counter.config(fg='#666666')  # Gray
    
    def _select_all(self, event):
        """Tümünü seç"""
        self.text_widget.tag_add(tk.SEL, '1.0', tk.END)
        return 'break'
    
    def _show_examples(self):
        """Örnek promptları göster"""
        examples = [
            "Bu dosyadaki güvenlik açıklarını analiz et ve önerilerde bulun",
            "Bu kodun performansını değerlendir ve optimizasyon önerileri ver",
            "Bu dosyadaki hata yönetimi stratejilerini incele",
            "Bu kodun test edilebilirliğini değerlendir",
            "Bu dosyadaki kod kalitesini ve best practice uyumunu kontrol et",
            "Bu API endpoint'lerinin güvenlik kontrollerini analiz et",
            "Bu veritabanı işlemlerinin verimliliğini değerlendir",
            "Bu UI bileşeninin kullanıcı deneyimini analiz et"
        ]
        
        # Examples dialog
        examples_dialog = tk.Toplevel(self.dialog)
        examples_dialog.title("Örnek Promptlar")
        examples_dialog.geometry("500x400")
        examples_dialog.transient(self.dialog)
        examples_dialog.grab_set()
        
        # Center the dialog
        examples_dialog.update_idletasks()
        x = (examples_dialog.winfo_screenwidth() // 2) - (500 // 2)
        y = (examples_dialog.winfo_screenheight() // 2) - (400 // 2)
        examples_dialog.geometry(f"500x400+{x}+{y}")
        
        main_frame = tk.Frame(examples_dialog, bg='white', padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        title = tk.Label(
            main_frame,
            text="💡 Örnek Promptlar",
            bg='white',
            font=('Segoe UI', 14, 'bold')
        )
        title.pack(pady=(0, 15))
        
        # Scrollable listbox
        listbox_frame = tk.Frame(main_frame, bg='white')
        listbox_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        
        scrollbar = ttk.Scrollbar(listbox_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        listbox = tk.Listbox(
            listbox_frame,
            yscrollcommand=scrollbar.set,
            font=('Segoe UI', 10),
            bg='#f8f9fa',
            selectbackground='#e3f2fd',
            borderwidth=0,
            highlightthickness=1,
            highlightcolor='#2196F3'
        )
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=listbox.yview)
        
        for example in examples:
            listbox.insert(tk.END, example)
        
        def use_selected():
            selection = listbox.curselection()
            if selection:
                selected_text = examples[selection[0]]
                # Clear current text if it's placeholder
                current_text = self.text_widget.get('1.0', tk.END).strip()
                if current_text == self.placeholder_text:
                    self.text_widget.delete('1.0', tk.END)
                
                self.text_widget.insert(tk.END, selected_text)
                self.text_widget.config(fg='#333333')
                self._update_char_counter()
                examples_dialog.destroy()
        
        def on_double_click(event):
            use_selected()
        
        listbox.bind('<Double-Button-1>', on_double_click)
        
        # Buttons
        btn_frame = tk.Frame(main_frame, bg='white')
        btn_frame.pack(fill=tk.X)
        
        tk.Button(
            btn_frame,
            text="Kullan",
            command=use_selected,
            bg='#4CAF50',
            fg='white',
            relief=tk.FLAT,
            font=('Segoe UI', 9, 'bold'),
            padx=20,
            pady=8
        ).pack(side=tk.RIGHT)
        
        tk.Button(
            btn_frame,
            text="İptal",
            command=examples_dialog.destroy,
            bg='#f5f5f5',
            fg='#333333',
            relief=tk.FLAT,
            font=('Segoe UI', 9),
            padx=20,
            pady=8
        ).pack(side=tk.RIGHT, padx=(0, 10))
    
    def _clear_prompt(self):
        """Promptu temizle"""
        result = messagebox.askyesno(
            "Prompt Temizle",
            "Bu dosya için girilen özel promptu silmek istediğinizden emin misiniz?",
            parent=self.dialog
        )
        if result:
            self.result_prompt = ""
            self.dialog.destroy()
    
    def _save_prompt(self):
        """Promptu kaydet"""
        current_text = self.text_widget.get('1.0', tk.END).strip()
        
        if current_text == self.placeholder_text:
            current_text = ""
        
        self.result_prompt = current_text
        self.dialog.destroy()
    
    def _cancel(self):
        """İptal et"""
        self.result_prompt = None
        self.dialog.destroy()
    
    def show(self) -> Optional[str]:
        """Dialog'u göster ve sonucu döndür"""
        self.dialog.wait_window()
        return self.result_prompt


def show_file_prompt_dialog(parent, file_path: str, current_prompt: str = "", 
                          localization_manager=None) -> Optional[str]:
    """File prompt dialog'unu göster ve sonucu döndür"""
    dialog = FilePromptDialog(parent, file_path, current_prompt, localization_manager)
    return dialog.show()