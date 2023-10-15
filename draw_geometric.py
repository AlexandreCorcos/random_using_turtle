from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
full_rotate = 360
colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "gray", "black", "white", "cyan",
          "magenta", "teal", "navy", "maroon", "olive", "lime", "aqua", "silver"]

for x in range(3, 11):
    angle = full_rotate / x
    print(x, angle)
    tim.color(random.choice(colors))

    for _ in range(x):
        tim.forward(100)
        tim.right(angle)

screen = Screen()
screen.exitonclick()
