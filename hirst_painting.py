import turtle as t
import random

color_list = [(240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41),
              (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]
a = 0
screen = t.Screen()
# screen.setup(1000, 800)
t.colormode(255)
tim = t.Turtle()
tim.speed(0)
tim.hideturtle()


def print_dot():
    for _ in range(10):
        # tim.color(random_color())
        tim.pendown()
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(100)


for _ in range(10):
    a += 80
    tim.penup()
    tim.goto((-screen.window_width() / 2 + 40, -screen.window_height() / 2 + a))
    print(tim.pos())
    print_dot()

screen.exitonclick()
