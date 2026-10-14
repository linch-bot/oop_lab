import tkinter as tk
import utils

def open_dialog(parent_window, open_prev_callback):
    def on_back():
        dialog.destroy()
        open_prev_callback()

    def on_ok():
        print("Натиснуто 'Так' у другому вікні")
        dialog.destroy()

    def on_cancel():
        dialog.destroy()

    dialog = tk.Toplevel(parent_window)
    dialog.title("Вікно 2")
    utils.center_window(dialog, 300, 100)
    dialog.transient(parent_window)
    dialog.grab_set()

    btn_back = tk.Button(dialog, text="< Назад", command=on_back)
    btn_back.pack(side=tk.LEFT, padx=10, pady=20)

    btn_ok = tk.Button(dialog, text="Так", command=on_ok)
    btn_ok.pack(side=tk.LEFT, padx=10, pady=20)

    btn_cancel = tk.Button(dialog, text="Відміна", command=on_cancel)
    btn_cancel.pack(side=tk.RIGHT, padx=10, pady=20)