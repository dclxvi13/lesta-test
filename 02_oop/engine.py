from model import Drawable


class Engine2D:
    def __init__(self):
        self.canvas: list[Drawable] = []
        self.current_color: str = "black"

    def add_drawable(self, item: Drawable):
        self.canvas.append(item)

    def set_color(self, color: str):
        self.current_color = color

    def draw(self):
        for item in self.canvas:
            item.draw(self.current_color)

        self.canvas.clear()
