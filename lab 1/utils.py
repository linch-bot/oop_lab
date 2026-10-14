def center_window(window, width, height):
    # Оновлюємо інформацію про вікно
    window.update_idletasks()
    
    # Отримуємо ширину та висоту екрану
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    # Вираховуємо координати X та Y для центрування
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))
    
    window.geometry(f"{width}x{height}+{x}+{y}")