from model import Circle, Triangle, Rectangle, Vector2
from engine import Engine2D


def test_engine_draw(capsys):
    engine = Engine2D()
    engine.add_drawable(Circle(Vector2(0, 1), 5))
    engine.add_drawable(Triangle(Vector2(0, 0), Vector2(1, 1), Vector2(2, 0)))
    engine.add_drawable(Rectangle(Vector2(1, 2), 3, 4))
    engine.draw()

    captured = capsys.readouterr()
    assert "Drawing Circle: (0, 1) with radius 5 in color black\n" in captured.out
    assert "Drawing Triangle: A (0, 0), B (1, 1), C (2, 0) in color black\n" in captured.out
    assert "Drawing Rectangle: Top left at (1, 2) with width 3 and height 4 in color black\n" in captured.out


def test_canvas_clear_after_draw():
    engine = Engine2D()
    engine.add_drawable(Circle(Vector2(0, 1), 5))
    engine.draw()

    assert len(engine.canvas) == 0


def test_color_change(capsys):
    engine = Engine2D()
    engine.set_color("blue")
    engine.add_drawable(Circle(Vector2(3, 4), 2))
    engine.draw()

    captured = capsys.readouterr()
    assert "Drawing Circle: (3, 4) with radius 2 in color blue\n" in captured.out

    engine.set_color("green")
    engine.add_drawable(Rectangle(Vector2(5, 5), 10, 20))
    engine.draw()

    captured = capsys.readouterr()
    assert "Drawing Rectangle: Top left at (5, 5) with width 10 and height 20 in color green\n" in captured.out
