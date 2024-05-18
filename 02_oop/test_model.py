from model import Circle, Triangle, Rectangle, Vector2


def test_circle_draw(capsys):
    circle = Circle(Vector2(0, 1), 5)
    circle.draw("red")

    captured = capsys.readouterr()
    assert captured.out == "Drawing Circle: (0, 1) with radius 5 in color red\n"


def test_triangle_draw(capsys):
    triangle = Triangle(Vector2(0, 0), Vector2(1, 1), Vector2(2, 0))
    triangle.draw("blue")

    captured = capsys.readouterr()
    assert captured.out == "Drawing Triangle: A (0, 0), B (1, 1), C (2, 0) in color blue\n"


def test_rectangle_draw(capsys):
    rectangle = Rectangle(Vector2(1, 2), 3, 4)
    rectangle.draw("green")

    captured = capsys.readouterr()
    assert captured.out == "Drawing Rectangle: Top left at (1, 2) with width 3 and height 4 in color green\n"
