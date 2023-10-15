import turtle as t
from random import random, choice, randint

tim = t.Turtle()
t.colormode(255)
tim.pensize(1)
tim.speed(0)
pos_ang = 0


def random_color():
    r = randint(1, 255)
    g = randint(1, 255)
    b = randint(1, 255)
    r_color = (r, g, b)
    return r_color


for _ in range(72):
    pos_ang += 5
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(pos_ang)


screen = t.Screen()
screen.exitonclick()
