from engine import Engine2D
from model import Circle, Triangle, Rectangle, Vector2

if __name__ == "__main__":
    engine = Engine2D()

    circle = Circle(Vector2(2, 3), 4)
    triangle = Triangle(Vector2(1, 0), Vector2(3, 4), Vector2(0, 3))
    rectangle = Rectangle(Vector2(2, 1), 3, 4)

    engine.add_drawable(circle)
    engine.add_drawable(triangle)
    engine.add_drawable(rectangle)

    engine.set_color("red")
    engine.draw()

    engine.set_color("blue")
    engine.add_drawable(Circle(Vector2(3, 4), 2))
    engine.add_drawable(Rectangle(Vector2(5, 5), 10, 20))
    engine.draw()
