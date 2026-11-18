import tkinter as tk
from tkinter import messagebox
import os
from editor import MyEditor

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

    # callback для зміни заголовка 
    def update_title(tool_name):
        root.title(f"Лабораторна робота №4 (Варіант 6) - Поточний інструмент: {tool_name}")

    current_dir = os.path.dirname(os.path.abspath(__file__))

    # завантаження 6 іконок для Toolbar
    try:
        icon_dot = tk.PhotoImage(file=os.path.join(current_dir, "dot.png"))
        icon_line = tk.PhotoImage(file=os.path.join(current_dir, "line.png"))
        icon_rect = tk.PhotoImage(file=os.path.join(current_dir, "rect.png"))
        icon_ellipse = tk.PhotoImage(file=os.path.join(current_dir, "ellipse.png"))
        icon_line_circles = tk.PhotoImage(file=os.path.join(current_dir, "line_circles.png"))
        icon_cube = tk.PhotoImage(file=os.path.join(current_dir, "cube.png"))
    except tk.TclError as e:
        print(f"Помилка: Не знайдено файли картинок! Деталі: {e}")
        return

    # створення Toolbar 
    toolbar = tk.Frame(root, bd=1, relief=tk.RAISED)

    # посилання на динамічний об'єкт редактора зберігаю в атрибуті вікна
    root.editor = None
    
    btn_dot = tk.Button(toolbar, image=icon_dot, relief=tk.FLAT, command=lambda: root.editor.set_tool(0))
    btn_line = tk.Button(toolbar, image=icon_line, relief=tk.FLAT, command=lambda: root.editor.set_tool(1))
    btn_rect = tk.Button(toolbar, image=icon_rect, relief=tk.FLAT, command=lambda: root.editor.set_tool(2))
    btn_ellipse = tk.Button(toolbar, image=icon_ellipse, relief=tk.FLAT, command=lambda: root.editor.set_tool(3))
    btn_line_circles = tk.Button(toolbar, image=icon_line_circles, relief=tk.FLAT, command=lambda: root.editor.set_tool(4))
    btn_cube = tk.Button(toolbar, image=icon_cube, relief=tk.FLAT, command=lambda: root.editor.set_tool(5))

    for btn in (btn_dot, btn_line, btn_rect, btn_ellipse, btn_line_circles, btn_cube):
        btn.pack(side=tk.LEFT, padx=2, pady=2)

    # підказки для всіх 6 кнопок
    ToolTip(btn_dot, "Крапка")
    ToolTip(btn_line, "Лінія")
    ToolTip(btn_rect, "Прямокутник")
    ToolTip(btn_ellipse, "Еліпс")
    ToolTip(btn_line_circles, "Лінія з кружечками")
    ToolTip(btn_cube, "Каркас куба")

    toolbar.pack(side=tk.TOP, fill=tk.X)

    canvas = tk.Canvas(root, bg="white")
    canvas.pack(fill=tk.BOTH, expand=True)

   # динамічне створення об'єкта класу MyEditor (парний варіант 6)
    root.editor = MyEditor(canvas, on_tool_change=update_title)

    # функція знищення динамічного об'єкта MyEditor при виході
    def on_closing():
        if root.editor is not None:
            del root.editor
            root.editor = None
        root.destroy()

    # перехоплюю закриття вікна хрестиком
    root.protocol("WM_DELETE_WINDOW", on_closing)

    # створення головного меню 
    menubar = tk.Menu(root)

    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="Вихід", command=on_closing)
    menubar.add_cascade(label="Файл", menu=file_menu)

    objects_menu = tk.Menu(menubar, tearoff=0)
    objects_menu.add_command(label="Крапка", command=lambda: root.editor.set_tool(0))
    objects_menu.add_command(label="Лінія", command=lambda: root.editor.set_tool(1))
    objects_menu.add_command(label="Прямокутник", command=lambda: root.editor.set_tool(2))
    objects_menu.add_command(label="Еліпс", command=lambda: root.editor.set_tool(3))
    objects_menu.add_command(label="Лінія з кружечками", command=lambda: root.editor.set_tool(4))
    objects_menu.add_command(label="Каркас куба", command=lambda: root.editor.set_tool(5))
    menubar.add_cascade(label="Об'єкти", menu=objects_menu)

    help_menu = tk.Menu(menubar, tearoff=0)
    help_menu.add_command(label="Про програму", command=lambda: messagebox.showinfo("Довідка", "Лабораторна робота №4\nВиконала: Лінчевська Анастасія\nВаріант: 6"))
    menubar.add_cascade(label="Довідка", menu=help_menu)

    root.config(menu=menubar)
    
    # зберігаю посилання на іконки, щоб збирач сміття їх не видалив
    root.icons = [icon_dot, icon_line, icon_rect, icon_ellipse, icon_line_circles, icon_cube]
    
    root.mainloop()

if __name__ == "__main__":
    main()