import tkinter as tk
from shape import Dot, Line, Rectangle, Ellipse, LineWithCircles, Cube

class MyEditor:
    def __init__(self, canvas, on_tool_change=None):
        self.canvas = canvas
        self.shapes = []
        self.max_shapes = 107  # ліміт об'єктів з 3-ї лаби 
        self.current_tool = 2 
        self.current_shape_class = Rectangle 
        self.is_drawing = False
        self.start_x = 0
        self.start_y = 0
        self.current_shape = None

        self.on_tool_change = on_tool_change

        # Словник інструментів
        self.tools = {
            0: (Dot, "Крапка"),
            1: (Line, "Лінія"),
            2: (Rectangle, "Прямокутник"),
            3: (Ellipse, "Еліпс"),
            4: (LineWithCircles, "Лінія з кружечками"),
            5: (Cube, "Каркас куба")
        }

        # обробники подій миші
        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)
        
        # одразу оновлюю заголовок при запуску для інструмента за замовчуванням
        self.set_tool(self.current_tool)

    def set_tool(self, tool_id):
        if tool_id in self.tools:
            self.current_tool = tool_id
            self.current_shape_class, tool_name = self.tools[tool_id]
            
            if self.on_tool_change:
                self.on_tool_change(tool_name)

    def on_press(self, event):
        if len(self.shapes) >= self.max_shapes:
            print(f"Досягнуто ліміт об'єктів ({self.max_shapes})!")
            return

        self.is_drawing = True
        self.start_x = event.x
        self.start_y = event.y
        
        # поліморфне створення екземпляра обраного класу без if-elif
        self.current_shape = self.current_shape_class(event.x, event.y, event.x, event.y)

    def on_drag(self, event):
        if not self.is_drawing or not self.current_shape:
            return

        self.canvas.delete("rubber")
        self.current_shape.draw_rubber_band(self.canvas, event.x, event.y)

    def on_release(self, event):
        if not self.is_drawing or not self.current_shape:
            return

        self.canvas.delete("rubber")
        self.is_drawing = False

        # фіксую кінцеві координати та малюю фігуру
        self.current_shape.x2 = event.x
        self.current_shape.y2 = event.y
        self.current_shape.draw(self.canvas)
        
        self.shapes.append(self.current_shape)
        self.current_shape = None

    def __del__(self):
        # деструктор для очищення пам'яті при знищенні динамічного об'єкта MyEditor
        self.shapes.clear()
        print("Динамічний об'єкт MyEditor успішно знищено.")