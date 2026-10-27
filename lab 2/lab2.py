import tkinter as tk
from tkinter import messagebox
from editor import Editor

def main():
    root = tk.Tk()
    root.title("Лабораторна робота 2 (Варіант 6)")
    root.geometry("800x600")

    # Полотно для малювання
    canvas = tk.Canvas(root, bg="white")
    canvas.pack(fill=tk.BOTH, expand=True)

    # Підключаю логіку редактора
    editor = Editor(canvas)

    # Створення головного меню
    menubar = tk.Menu(root)

    # 1. Меню "Файл"
    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="Вихід", command=root.quit)
    menubar.add_cascade(label="Файл", menu=file_menu)

    # 2. Меню "Об'єкти"
    tool_var = tk.IntVar()
    tool_var.set(2)  # 2 - це прямокутник (активний за замовчуванням)

    objects_menu = tk.Menu(menubar, tearoff=0)
    objects_menu.add_radiobutton(label="Крапка", variable=tool_var, value=0, command=lambda: editor.set_tool(0))
    objects_menu.add_radiobutton(label="Лінія", variable=tool_var, value=1, command=lambda: editor.set_tool(1))
    objects_menu.add_radiobutton(label="Прямокутник", variable=tool_var, value=2, command=lambda: editor.set_tool(2))
    objects_menu.add_radiobutton(label="Еліпс", variable=tool_var, value=3, command=lambda: editor.set_tool(3))

    menubar.add_cascade(label="Об'єкти", menu=objects_menu)

    # 3. Меню "Довідка"
    help_menu = tk.Menu(menubar, tearoff=0)
    help_menu.add_command(label="Про програму", command=lambda: messagebox.showinfo("Довідка", "Лабораторна робота №2\nВиконала: Лінчевська Анастасія\nВаріант: 6"))
    menubar.add_cascade(label="Довідка", menu=help_menu)

    root.config(menu=menubar)
    
    # Запуск програми
    root.mainloop()

if __name__ == "__main__":
    main()