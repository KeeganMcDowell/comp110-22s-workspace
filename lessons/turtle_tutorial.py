"""Turtle tutorial."""

from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

leo.penup()
leo.goto(-200, -150)
leo.pendown()


colormode(255)
leo.color(217, 51, 255)
leo.begin_fill()

leo.speed(50)
leo.hideturtle()

side_length: float = 400
i: int = 0
while (i < 3): 
    leo.forward(side_length)
    leo.left(120)
    i = i + 1

leo.end_fill()

bob: Turtle = Turtle()


bob.penup()
bob.goto(-200, -150)
bob.pendown()

colormode(255)
bob.color(110, 11, 132)

bob.speed(100)
bob.hideturtle()

i: int = 0
while (i < 3): 
    bob.forward(side_length)
    bob.left(120)
    i = i + 1

i: int = 0
while (i < 200): 
    side_length = side_length * .97
    bob.forward(side_length)
    bob.left(121)
    i = i + 1


done()