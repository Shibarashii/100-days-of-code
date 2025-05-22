import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)

pagong = Turtle()
pagong.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def draw_circle(interval):
    interval_range = int(360 / interval)

    for i in range(interval_range):
        pagong.color(random_color())
        pagong.setheading(i * interval)
        pagong.circle(100)


draw_circle(int(input("Interval: ")))

screen = Screen()
screen.exitonclick()
