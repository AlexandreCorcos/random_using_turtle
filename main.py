import turtle as t
from random import random, choice, randint

tim = t.Turtle()
t.colormode(255)
tim.pensize(15)
tim.speed(0)


def random_color():
    r = randint(1, 255)
    g = randint(1, 255)
    b = randint(1, 255)
    r_color = (r, g, b)
    return r_color


direction = [0, 90, 180, 270]

while True:
# for i in range(100):
    steps = 30
    angle = 90
    tim.fd(steps)
    tim.color(random_color())
    tim.rt(choice(direction))

screen = Screen()
screen.exitonclick()
