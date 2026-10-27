import tkinter as tk
from shape import Dot, Line, Rectangle, Ellipse

class Editor:
    def __init__(self, canvas):
        self.canvas = canvas
        self.shapes = []         # динамічний масив об'єктів
        self.max_shapes = 106    # Обмеження N = Ж + 100 = 106
        self.current_tool = 2    # 0-Крапка, 1-Лінія, 2-Прямокутник, 3-Еліпс
        self.is_drawing = False
        self.start_x = 0
        self.start_y = 0

        # Обробники подій миші
        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

    def set_tool(self, tool_id):
        self.current_tool = tool_id

    def on_press(self, event):
        if len(self.shapes) >= self.max_shapes:
            print("Досягнуто ліміт об'єктів (106)!")
            return
        
        self.is_drawing = True
        self.start_x = event.x
        self.start_y = event.y

        if self.current_tool == 0:  # Крапка ставиться по одному кліку
            dot = Dot(self.start_x, self.start_y, self.start_x, self.start_y)
            dot.draw(self.canvas)
            self.shapes.append(dot)
            self.is_drawing = False

    def on_drag(self, event):
        if not self.is_drawing: 
            return
        # Видалення старого гумового сліду перед малюванням нового
        self.canvas.delete("rubber")

        # тимчасовий гумовий слід 
        if self.current_tool == 1:
            Line(self.start_x, self.start_y, event.x, event.y).draw_rubber_band(self.canvas, event.x, event.y)
        elif self.current_tool == 2:
            Rectangle(self.start_x, self.start_y, event.x, event.y).draw_rubber_band(self.canvas, event.x, event.y)
        elif self.current_tool == 3:
            Ellipse(self.start_x, self.start_y, event.x, event.y).draw_rubber_band(self.canvas, event.x, event.y)

    def on_release(self, event):
        if not self.is_drawing: 
            return
        
        self.canvas.delete("rubber")
        self.is_drawing = False

        shape = None
        if self.current_tool == 1:
            shape = Line(self.start_x, self.start_y, event.x, event.y)
        elif self.current_tool == 2:
            shape = Rectangle(self.start_x, self.start_y, event.x, event.y)
        elif self.current_tool == 3:
            shape = Ellipse(self.start_x, self.start_y, event.x, event.y)

        # зберігаю готовий об'єкт у масив та відмальовую його
        if shape:
            shape.draw(self.canvas)
            self.shapes.append(shape)