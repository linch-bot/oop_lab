import tkinter as tk
import module_1
import module_2
import module_3
import utils

# Функції-посередники для переходу між вікнами без взаємного імпорту модулів
def show_dialog_1():
    module_1.open_dialog(root, show_dialog_2)

def show_dialog_2():
    module_2.open_dialog(root, show_dialog_1)

# меню "Робота 1"
def run_work1():
    show_dialog_1()

def run_work2():
    module_3.open_dialog(root, update_main_text)

def update_main_text(text):
    result_label.config(text=f"Вибрано: {text}")

# Створення головного вікна
root = tk.Tk()
root.title("Лабораторна 1 - Головне вікно")
utils.center_window(root, 400, 300)

# Створення меню
menubar = tk.Menu(root)
root.config(menu=menubar)

menubar.add_command(label="Робота1", command=run_work1)
menubar.add_command(label="Робота2", command=run_work2)

#  результати з Роботи 2
result_label = tk.Label(root, text="Тут буде результат", font=("Arial", 12))
result_label.pack(pady=100) 

# Цикл очікування повідомлень 
if __name__ == "__main__":
    root.mainloop()