from turtle import Turtle, Screen
import random

timmy = Turtle()

timmy.penup()
timmy.goto(0, 0)
timmy.pendown()
colors = ["red4", "orange4", "yellow4", "green4", "blue4", "indigo", "purple4", "pink4"]


for i in range(3, 20):
    color = random.choice(colors)
    timmy.color(color)

    for j in range(i):
        angle = 360 / i
        timmy.forward(100)
        timmy.right(angle)


screen = Screen()
screen.exitonclick()
