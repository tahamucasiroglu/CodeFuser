import tkinter as tk
from tkinter import ttk, font
import math
from typing import Callable, Optional, List, Tuple


class ModernButton(tk.Button):
    def __init__(self, parent, **kwargs):
        # Extract custom parameters
        self.bg_color = kwargs.pop('bg_color', '#2196F3')
        self.hover_color = kwargs.pop('hover_color', '#1976D2')
        self.text_color = kwargs.pop('text_color', 'white')
        self.border_radius = kwargs.pop('border_radius', 10)
        
        # Default styling
        kwargs['relief'] = tk.FLAT
        kwargs['bg'] = self.bg_color
        kwargs['fg'] = self.text_color
        kwargs['activebackground'] = self.hover_color
        kwargs['activeforeground'] = self.text_color
        kwargs['cursor'] = 'hand2'
        kwargs['font'] = kwargs.get('font', ('Segoe UI', 10))
        kwargs['padx'] = kwargs.get('padx', 20)
        kwargs['pady'] = kwargs.get('pady', 10)
        
        super().__init__(parent, **kwargs)
        
        self.bind('<Enter>', self._on_enter)
        self.bind('<Leave>', self._on_leave)
    
    def _on_enter(self, event):
        self.config(bg=self.hover_color)
    
    def _on_leave(self, event):
        self.config(bg=self.bg_color)


class AnimatedProgressBar(tk.Canvas):
    def __init__(self, parent, width=400, height=30, bg_color='#E0E0E0', 
                 fill_color='#2196F3', text_color='black', **kwargs):
        super().__init__(parent, width=width, height=height, 
                        bg='white', highlightthickness=0, **kwargs)
        
        self.width = width
        self.height = height
        self.bg_color = bg_color
        self.fill_color = fill_color
        self.text_color = text_color
        self.progress = 0
        self.is_indeterminate = False
        self.animation_step = 0
        
        self._draw_background()
        self._draw_progress()
    
    def _draw_background(self):
        self.create_rectangle(0, 0, self.width, self.height, 
                            fill=self.bg_color, outline='', tags='bg')
    
    def _draw_progress(self):
        self.delete('progress')
        self.delete('text')
        
        if self.is_indeterminate:
            # Draw animated indeterminate progress
            bar_width = self.width * 0.3
            position = (self.animation_step % (self.width + bar_width)) - bar_width
            self.create_rectangle(position, 0, position + bar_width, self.height,
                                fill=self.fill_color, outline='', tags='progress')
        else:
            # Draw determinate progress
            progress_width = int(self.width * self.progress / 100)
            if progress_width > 0:
                self.create_rectangle(0, 0, progress_width, self.height,
                                    fill=self.fill_color, outline='', tags='progress')
            
            # Draw percentage text
            text = f"{int(self.progress)}%"
            self.create_text(self.width // 2, self.height // 2, 
                           text=text, fill=self.text_color, 
                           font=('Segoe UI', 10, 'bold'), tags='text')
    
    def set_progress(self, value: float):
        self.progress = max(0, min(100, value))
        self.is_indeterminate = False
        self._draw_progress()
    
    def set_indeterminate(self, value: bool = True):
        self.is_indeterminate = value
        if value:
            self._animate_indeterminate()
    
    def _animate_indeterminate(self):
        if self.is_indeterminate:
            self.animation_step += 5
            self._draw_progress()
            self.after(20, self._animate_indeterminate)


class ModernEntry(tk.Frame):
    def __init__(self, parent, placeholder='', **kwargs):
        super().__init__(parent, bg='white')
        
        self.placeholder = placeholder
        self.placeholder_color = '#999999'
        self.text_color = kwargs.pop('fg', 'black')
        
        # Create the entry widget
        self.entry = tk.Entry(self, relief=tk.FLAT, **kwargs)
        self.entry.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Bind events
        self.entry.bind('<FocusIn>', self._on_focus_in)
        self.entry.bind('<FocusOut>', self._on_focus_out)
        
        # Set placeholder
        self._show_placeholder()
    
    def _show_placeholder(self):
        if not self.entry.get():
            self.entry.insert(0, self.placeholder)
            self.entry.config(fg=self.placeholder_color)
    
    def _on_focus_in(self, event):
        if self.entry.get() == self.placeholder:
            self.entry.delete(0, tk.END)
            self.entry.config(fg=self.text_color)
    
    def _on_focus_out(self, event):
        if not self.entry.get():
            self._show_placeholder()
    
    def get(self):
        text = self.entry.get()
        return '' if text == self.placeholder else text
    
    def set(self, value):
        self.entry.delete(0, tk.END)
        if value:
            self.entry.insert(0, value)
            self.entry.config(fg=self.text_color)
        else:
            self._show_placeholder()


class ModernScrolledText(tk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent)
        
        # Create text widget with scrollbar
        self.text = tk.Text(self, wrap=tk.WORD, relief=tk.FLAT, **kwargs)
        self.scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, 
                                      command=self.text.yview)
        
        self.text.configure(yscrollcommand=self.scrollbar.set)
        
        # Pack widgets
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    def get(self, *args, **kwargs):
        return self.text.get(*args, **kwargs)
    
    def insert(self, *args, **kwargs):
        return self.text.insert(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        return self.text.delete(*args, **kwargs)
    
    def config(self, **kwargs):
        return self.text.config(**kwargs)


class AnimatedLabel(tk.Label):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.dots = 0
        self.base_text = ""
        self.is_animating = False
    
    def start_animation(self, base_text: str):
        self.base_text = base_text
        self.is_animating = True
        self._animate()
    
    def stop_animation(self, final_text: str = ""):
        self.is_animating = False
        self.config(text=final_text or self.base_text)
    
    def _animate(self):
        if self.is_animating:
            dots = "." * (self.dots % 4)
            self.config(text=f"{self.base_text}{dots}")
            self.dots += 1
            self.after(500, self._animate)


class ModernCheckbox(tk.Frame):
    def __init__(self, parent, text='', variable=None, **kwargs):
        super().__init__(parent, bg=kwargs.get('bg', 'white'))
        
        self.var = variable or tk.BooleanVar()
        
        # Create custom checkbox
        self.checkbox = tk.Canvas(self, width=20, height=20, 
                                 bg=kwargs.get('bg', 'white'), 
                                 highlightthickness=0)
        self.checkbox.pack(side=tk.LEFT, padx=(0, 5))
        
        # Create label
        self.label = tk.Label(self, text=text, bg=kwargs.get('bg', 'white'),
                            font=kwargs.get('font', ('Segoe UI', 10)))
        self.label.pack(side=tk.LEFT)
        
        # Draw checkbox
        self._draw_checkbox()
        
        # Bind events
        self.checkbox.bind('<Button-1>', self._toggle)
        self.label.bind('<Button-1>', self._toggle)
        
        # Watch variable changes
        self.var.trace('w', lambda *args: self._draw_checkbox())
    
    def _draw_checkbox(self):
        self.checkbox.delete('all')
        
        # Draw border
        self.checkbox.create_rectangle(2, 2, 18, 18, 
                                     outline='#666666', width=2)
        
        # Draw checkmark if checked
        if self.var.get():
            self.checkbox.create_line(5, 10, 8, 13, fill='#2196F3', width=2)
            self.checkbox.create_line(8, 13, 15, 6, fill='#2196F3', width=2)
    
    def _toggle(self, event=None):
        self.var.set(not self.var.get())


class ModernCombobox(ttk.Combobox):
    def __init__(self, parent, **kwargs):
        # Apply modern styling
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure combobox style
        style.configure('Modern.TCombobox',
                       fieldbackground='white',
                       background='white',
                       bordercolor='#CCCCCC',
                       arrowcolor='#666666',
                       lightcolor='white',
                       darkcolor='white')
        
        kwargs['style'] = 'Modern.TCombobox'
        super().__init__(parent, **kwargs)