import tkinter as tk
from tkinter import messagebox
import os
from editor import Editor

# клас для спливаючих підказок (Tooltips) 
class ToolTip(object):
    def __init__(self, widget, text='widget info'):
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.tw = None

    def enter(self, event=None):
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25
        self.tw = tk.Toplevel(self.widget)
        self.tw.wm_overrideredirect(True) 
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, justify='left',
                         background='#ffffe0', relief='solid', borderwidth=1,
                         font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def leave(self, event=None):
        if self.tw:
            self.tw.destroy()
            self.tw = None

def main():
    root = tk.Tk()
    root.geometry("800x600")

    # callback для зміни заголовка (варіант 7)
    def update_title(tool_name):
        root.title(f"Лабораторна робота №3 (Варіант 7) - Поточний інструмент: {tool_name}")

    current_dir = os.path.dirname(os.path.abspath(__file__))

    # завантаження звичайних файлів картинок
    try:
        icon_dot = tk.PhotoImage(file=os.path.join(current_dir, "dot.png"))
        icon_line = tk.PhotoImage(file=os.path.join(current_dir, "line.png"))
        icon_rect = tk.PhotoImage(file=os.path.join(current_dir, "rect.png"))
        icon_ellipse = tk.PhotoImage(file=os.path.join(current_dir, "ellipse.png"))
    except tk.TclError as e:
        print(f"Помилка: Не знайдено файли картинок! Деталі: {e}")
        return

    # створення Toolbar 
    toolbar = tk.Frame(root, bd=1, relief=tk.RAISED)
    
    btn_dot = tk.Button(toolbar, image=icon_dot, relief=tk.FLAT, command=lambda: editor.set_tool(0))
    btn_line = tk.Button(toolbar, image=icon_line, relief=tk.FLAT, command=lambda: editor.set_tool(1))
    btn_rect = tk.Button(toolbar, image=icon_rect, relief=tk.FLAT, command=lambda: editor.set_tool(2))
    btn_ellipse = tk.Button(toolbar, image=icon_ellipse, relief=tk.FLAT, command=lambda: editor.set_tool(3))

    btn_dot.pack(side=tk.LEFT, padx=2, pady=2)
    btn_line.pack(side=tk.LEFT, padx=2, pady=2)
    btn_rect.pack(side=tk.LEFT, padx=2, pady=2)
    btn_ellipse.pack(side=tk.LEFT, padx=2, pady=2)
    
    ToolTip(btn_dot, "Крапка")
    ToolTip(btn_line, "Лінія")
    ToolTip(btn_rect, "Прямокутник")
    ToolTip(btn_ellipse, "Еліпс")

    toolbar.pack(side=tk.TOP, fill=tk.X)

    canvas = tk.Canvas(root, bg="white")
    canvas.pack(fill=tk.BOTH, expand=True)

    editor = Editor(canvas, on_tool_change=update_title)

    # створення головного меню 
    menubar = tk.Menu(root)

    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="Вихід", command=root.quit)
    menubar.add_cascade(label="Файл", menu=file_menu)

    objects_menu = tk.Menu(menubar, tearoff=0)
    objects_menu.add_command(label="Крапка", command=lambda: editor.set_tool(0))
    objects_menu.add_command(label="Лінія", command=lambda: editor.set_tool(1))
    objects_menu.add_command(label="Прямокутник", command=lambda: editor.set_tool(2))
    objects_menu.add_command(label="Еліпс", command=lambda: editor.set_tool(3))
    menubar.add_cascade(label="Об'єкти", menu=objects_menu)

    help_menu = tk.Menu(menubar, tearoff=0)
    help_menu.add_command(label="Про програму", command=lambda: messagebox.showinfo("Довідка", "Лабораторна робота №3\nВиконала: Лінчевська Анастасія\nВаріант: 7"))
    menubar.add_cascade(label="Довідка", menu=help_menu)

    root.config(menu=menubar)
    
    # зберігаю посилання на іконки, щоб збирач сміття їх не видалив
    root.icon_dot = icon_dot
    root.icon_line = icon_line
    root.icon_rect = icon_rect
    root.icon_ellipse = icon_ellipse
    
    root.mainloop()

if __name__ == "__main__":
    main()