import tkinter as tk
import utils

def open_dialog(parent_window, update_text_callback):
    # Callback-функции заховані всередині модуля
    def on_ok():
        selection = listbox.curselection()
        if selection:
            selected_group = listbox.get(selection[0])
            update_text_callback(selected_group) 
        dialog.destroy() 

    def on_cancel():
        dialog.destroy()

    
    dialog = tk.Toplevel(parent_window)
    dialog.title("Вікно 3 (Список)")
    utils.center_window(dialog, 300, 250)
    dialog.transient(parent_window)
    dialog.grab_set()

    
    listbox = tk.Listbox(dialog, font=("Arial", 11))
    listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    
    groups = ["ІМ-55", "ІМ-52", "ІМ-53", "ІМ-54", "ІМ_55", "ІМ-о51"]
    for group in groups:
        listbox.insert(tk.END, group)

    
    btn_frame = tk.Frame(dialog)
    btn_frame.pack(fill=tk.X, pady=10)

    
    btn_ok = tk.Button(btn_frame, text="Так", command=on_ok)
    btn_ok.pack(side=tk.LEFT, padx=30)

    btn_cancel = tk.Button(btn_frame, text="Відміна", command=on_cancel)
    btn_cancel.pack(side=tk.RIGHT, padx=30)