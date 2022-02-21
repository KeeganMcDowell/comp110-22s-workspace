"""A view of the mountain tops with a small lake out in front.

I created the 'primer' function in order to take reused components and be able to call them (ln 16-24).
Clouds were added at random x and y coordinates (ln 98-99) using randint and the turtle circle function.
"""

__author__ = "730234932"

from turtle import Turtle, colormode, done, tracer, update
from random import randint


MAX_SPEED: int = 0


def primer(a_turtle: Turtle, x: float, y: float) -> None:
    """Items that would have been used in setting up each component."""
    a_turtle.penup()
    a_turtle.setheading(0.0)
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.speed(MAX_SPEED)
    a_turtle.hideturtle()
    a_turtle.begin_fill()


def sun(a_sun: Turtle, x: float, y: float, angle: float) -> None:
    """Draws the yellow sun in the sky, starting at x, y."""
    primer(a_sun, x, y)

    a_sun.color("black", "yellow")

    i: int = 0
    while i < 50:
        side_length: int = 50
        a_sun.forward(side_length)
        a_sun.left(angle)
        i += 1
    
    a_sun.end_fill()


def mountain_tops(a_mountain: Turtle, x: float, y: float, angle: float) -> None:
    """Drawing the triangular outline of mountain tops, starting at x, y."""
    primer(a_mountain, x, y)

    a_mountain.color("black", "brown")

    i: int = 0
    while i < 2:
        side_length: int = 230
        a_mountain.forward(side_length)
        a_mountain.left(angle)
        i += 1
    
    a_mountain.end_fill()


def lake(a_lake: Turtle, x: float, y: float, width: float, height: float) -> None:
    """Draws a small lake in front of the mountains, starting at x, y."""
    primer(a_lake, x, y)

    a_lake.color("black", "blue")

    i: int = 0
    for i in range(2):
        angle: int = 90
        a_lake.forward(width)
        a_lake.left(angle)
        a_lake.forward(height)
        a_lake.left(angle)

    a_lake.end_fill()


def field(a_field: Turtle, x: float, y: float, width: float, height: float) -> None:
    """Drawing the green areas of grass around the mountains, starting at x, y."""
    primer(a_field, x, y)

    colormode(255)
    a_field.color(5, 94, 11)

    i: int = 0
    for i in range(2):
        angle: int = 90
        a_field.forward(width)
        a_field.left(angle)
        a_field.forward(height)
        a_field.left(angle)

    a_field.end_fill()


def clouds(a_cloud: Turtle, radius: float) -> None:
    """Draws white circular clouds placed randomly at the top of the scene."""
    i: int = 0
    number_of_clouds: int = 8
    while i < number_of_clouds:
        x: float = randint(-350, 125)
        y: float = randint(150, 275)
        primer(a_cloud, x, y)

        a_cloud.color("black", "white")

        a_cloud.circle(radius)
        
        a_cloud.end_fill()
        i += 1


def main() -> None:
    """The entrypoint of my mountain view."""
    tracer(0, 0)
    mountain_view: Turtle = Turtle()
    sun(mountain_view, 150, 200, 70)
    mountain_tops(mountain_view, -350, -50, 120)
    mountain_tops(mountain_view, -180, -50, 120)
    mountain_tops(mountain_view, -50, -50, 120)
    lake(mountain_view, -350, -200, 530, 150)
    field(mountain_view, -350, -350, 530, 150)
    field(mountain_view, -350, -350, 230, 300)
    clouds(mountain_view, 25)
    update()
    done()


if __name__ == "__main__":
    main()