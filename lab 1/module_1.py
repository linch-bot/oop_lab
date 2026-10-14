import tkinter as tk
import utils

def open_dialog(parent_window, open_next_callback):
    # Callback-функции заховані всередині модуля
    def on_next():
        dialog.destroy() 
        open_next_callback() 

    def on_cancel():
        dialog.destroy()

    # Створюємо вікно діалогу
    dialog = tk.Toplevel(parent_window)
    dialog.title("Вікно 1")
    utils.center_window(dialog, 250, 100)
    # Робимо вікно модальним (блокує головне)
    dialog.transient(parent_window)
    dialog.grab_set()

    # Кнопки [Далі] і [Відміна]
    btn_next = tk.Button(dialog, text="Далі >", command=on_next)
    btn_next.pack(side=tk.LEFT, padx=20, pady=20)

    btn_cancel = tk.Button(dialog, text="Відміна", command=on_cancel)
    btn_cancel.pack(side=tk.RIGHT, padx=20, pady=20)