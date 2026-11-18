import tkinter as tk
from abc import ABC, abstractmethod

# абстрактний базовий клас 
class Shape(ABC):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    @abstractmethod
    def draw(self, canvas):
        pass

    @abstractmethod
    def draw_rubber_band(self, canvas, x2, y2):
        pass

# успадкування для крапки
class Dot(Shape):
    def draw(self, canvas):
        # малюю крапку як маленький овал
        canvas.create_oval(self.x1-2, self.y1-2, self.x1+2, self.y1+2, fill="black", outline="black")

    def draw_rubber_band(self, canvas, x2, y2):
        pass # Крапка ставиться миттєво, гумовий слід не потрібен

# успадкування для лінії
class Line(Shape):
    def draw(self, canvas):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill="black")

    def draw_rubber_band(self, canvas, x2, y2):
        # Пунктирна чорна лінія 
        canvas.create_line(self.x1, self.y1, x2, y2, fill="black", dash=(4, 4), tags="rubber")

# успадкування для прямокутника
class Rectangle(Shape):
    fill_color = "lightgreen"

    def _get_bbox(self, x2, y2):
        # Ввід від центру до одного з кутів 
        dx = abs(x2 - self.x1)
        dy = abs(y2 - self.y1)
        return self.x1 - dx, self.y1 - dy, self.x1 + dx, self.y1 + dy

    def draw(self, canvas):
        # чорний контур, світло-зелене заповнення 
        x_min, y_min, x_max, y_max = self._get_bbox(self.x2, self.y2)
        canvas.create_rectangle(x_min, y_min, x_max, y_max, outline="black", fill=self.fill_color)

    def draw_rubber_band(self, canvas, x2, y2):
        # пунктирна чорна лінія 
        x_min, y_min, x_max, y_max = self._get_bbox(x2, y2)
        canvas.create_rectangle(x_min, y_min, x_max, y_max, outline="black", dash=(4, 4), tags="rubber")

# успадкування для еліпса
class Ellipse(Shape):
    fill_color = ""
    
    def draw(self, canvas):
        # ввід по двом протилежним кутам, без заповнення 
        canvas.create_oval(self.x1, self.y1, self.x2, self.y2, outline="black", fill=self.fill_color)

    def draw_rubber_band(self, canvas, x2, y2):
        # пунктирна чорна лінія
        canvas.create_oval(self.x1, self.y1, x2, y2, outline="black", dash=(4, 4), tags="rubber")

# Лінія з кружечками (множинне успадкування від Line та Ellipse)
class LineWithCircles(Line, Ellipse):
    fill_color = "white"  # біле заповнення для кружечків на кінцях
    radius = 5

    def draw(self, canvas):
        orig_x1, orig_y1, orig_x2, orig_y2 = self.x1, self.y1, self.x2, self.y2
        r = self.radius

        # малюю основну лінію через метод класу Line
        Line.draw(self, canvas)

        # малюю перший кружечок через метод класу Ellipse
        self.x1, self.y1, self.x2, self.y2 = orig_x1 - r, orig_y1 - r, orig_x1 + r, orig_y1 + r
        Ellipse.draw(self, canvas)

        # малюю другий кружечок через метод класу Ellipse
        self.x1, self.y1, self.x2, self.y2 = orig_x2 - r, orig_y2 - r, orig_x2 + r, orig_y2 + r
        Ellipse.draw(self, canvas)

        # відновлюю початкові координати об'єкта
        self.x1, self.y1, self.x2, self.y2 = orig_x1, orig_y1, orig_x2, orig_y2

    def draw_rubber_band(self, canvas, x2, y2):
        orig_x1, orig_y1 = self.x1, self.y1
        r = self.radius

        Line.draw_rubber_band(self, canvas, x2, y2)

        self.x1, self.y1 = orig_x1 - r, orig_y1 - r
        Ellipse.draw_rubber_band(self, canvas, orig_x1 + r, orig_y1 + r)

        self.x1, self.y1 = x2 - r, y2 - r
        Ellipse.draw_rubber_band(self, canvas, x2 + r, y2 + r)

        self.x1, self.y1 = orig_x1, orig_y1


# каркас куба (множинне успадкування від Line та Rectangle)
class Cube(Line, Rectangle):
    fill_color = ""  # прозорий фон

    def _get_cube_coords(self, x2, y2):
        # координати переднього прямокутника
        ax1, ay1, ax2, ay2 = self._get_bbox(x2, y2)
        # зміщення для заднього прямокутника
        dx = abs(x2 - self.x1)
        dy = abs(y2 - self.y1)
        shift_x = max(15, dx // 2)
        shift_y = -max(15, dy // 2)
        return (ax1, ay1, ax2, ay2), shift_x, shift_y

    def draw(self, canvas):
        orig_x1, orig_y1, orig_x2, orig_y2 = self.x1, self.y1, self.x2, self.y2
        (ax1, ay1, ax2, ay2), sx, sy = self._get_cube_coords(orig_x2, orig_y2)

        # 1. задній прямокутник (через метод класу Rectangle)
        self.x1, self.y1 = orig_x1 + sx, orig_y1 + sy
        self.x2, self.y2 = orig_x2 + sx, orig_y2 + sy
        Rectangle.draw(self, canvas)

        # 2. передній прямокутник (через метод класу Rectangle)
        self.x1, self.y1, self.x2, self.y2 = orig_x1, orig_y1, orig_x2, orig_y2
        Rectangle.draw(self, canvas)

        # 3. 4 бічні ребра що з'єднують кути (через метод класу Line)
        corners = [
            (ax1, ay1, ax1 + sx, ay1 + sy),
            (ax2, ay1, ax2 + sx, ay1 + sy),
            (ax1, ay2, ax1 + sx, ay2 + sy),
            (ax2, ay2, ax2 + sx, ay2 + sy)
        ]
        for lx1, ly1, lx2, ly2 in corners:
            self.x1, self.y1, self.x2, self.y2 = lx1, ly1, lx2, ly2
            Line.draw(self, canvas)

        self.x1, self.y1, self.x2, self.y2 = orig_x1, orig_y1, orig_x2, orig_y2

    def draw_rubber_band(self, canvas, x2, y2):
        orig_x1, orig_y1 = self.x1, self.y1
        (ax1, ay1, ax2, ay2), sx, sy = self._get_cube_coords(x2, y2)

        # гумовий слід заднього та переднього прямокутників
        self.x1, self.y1 = orig_x1 + sx, orig_y1 + sy
        Rectangle.draw_rubber_band(self, canvas, x2 + sx, y2 + sy)

        self.x1, self.y1 = orig_x1, orig_y1
        Rectangle.draw_rubber_band(self, canvas, x2, y2)

        # гумовий слід 4 бічних ребер
        corners = [
            (ax1, ay1, ax1 + sx, ay1 + sy),
            (ax2, ay1, ax2 + sx, ay1 + sy),
            (ax1, ay2, ax1 + sx, ay2 + sy),
            (ax2, ay2, ax2 + sx, ay2 + sy)
        ]
        for lx1, ly1, lx2, ly2 in corners:
            self.x1, self.y1 = lx1, ly1
            Line.draw_rubber_band(self, canvas, lx2, ly2)

        self.x1, self.y1 = orig_x1, orig_y1