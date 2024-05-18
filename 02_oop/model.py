from abc import ABC, abstractmethod
from dataclasses import dataclass


class Drawable(ABC):
    @abstractmethod
    def draw(self, color: str):
        pass


@dataclass
class Vector2:
    x: float
    y: float


class Circle(Drawable):
    def __init__(self, center: Vector2, radius: float):
        self.center = center
        self.radius = radius

    def draw(self, color: str):
        print(f"Drawing Circle: ({self.center.x}, {self.center.y}) with radius {self.radius} in color {color}")


class Triangle(Drawable):
    def __init__(self, a: Vector2, b: Vector2, c: Vector2):
        self.a = a
        self.b = b
        self.c = c

    def draw(self, color: str):
        print(f"Drawing Triangle: "
              f"A ({self.a.x}, {self.a.y}), B ({self.b.x}, {self.b.y}), C ({self.c.x}, {self.c.y}) "
              f"in color {color}")


class Rectangle(Drawable):
    def __init__(self, top_left: Vector2, width: float, height: float):
        self.top_left = top_left
        self.width = width
        self.height = height

    def draw(self, color: str):
        print(f"Drawing Rectangle: Top left at ({self.top_left.x}, {self.top_left.y}) "
              f"with width {self.width} and height {self.height} in color {color}")
