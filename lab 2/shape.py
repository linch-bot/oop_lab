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
        # Суцільна лінія синього кольору (варіант 6)
        canvas.create_line(self.x1, self.y1, x2, y2, fill="blue", tags="rubber")

# успадкування для прямокутника
class Rectangle(Shape):
    def draw(self, canvas):
        # чорний контур, жовте заповнення (варіант 6)
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, outline="black", fill="yellow")

    def draw_rubber_band(self, canvas, x2, y2):
        # суцільна лінія синього кольору
        canvas.create_rectangle(self.x1, self.y1, x2, y2, outline="blue", tags="rubber")

# успадкування для еліпса
class Ellipse(Shape):
    def _get_bbox(self, x2, y2):
        # математика вводу від центру до кута (варіант 6)
        # x1, y1 - це центр. радіус = різниця між центром і курсором
        dx = abs(x2 - self.x1)
        dy = abs(y2 - self.y1)
        return self.x1 - dx, self.y1 - dy, self.x1 + dx, self.y1 + dy

    def draw(self, canvas):
        # чорний контур, біле заповнення (варіант 6)
        x_min, y_min, x_max, y_max = self._get_bbox(self.x2, self.y2)
        canvas.create_oval(x_min, y_min, x_max, y_max, outline="black", fill="white")

    def draw_rubber_band(self, canvas, x2, y2):
        x_min, y_min, x_max, y_max = self._get_bbox(x2, y2)
        canvas.create_oval(x_min, y_min, x_max, y_max, outline="blue", tags="rubber")