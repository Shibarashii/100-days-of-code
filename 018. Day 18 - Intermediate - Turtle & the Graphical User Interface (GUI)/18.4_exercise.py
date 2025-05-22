import random
from turtle import Turtle, Screen
import turtle as t

t.colormode(255)
turtle = Turtle()
turtle.pensize(15)
turtle.speed("fastest")
MOVE_DISTANCE = 20


def move_right():
    turtle.right(90)
    turtle.forward(MOVE_DISTANCE)


def move_left():
    turtle.left(90)
    turtle.forward(MOVE_DISTANCE)


def move_backward():
    turtle.backward(MOVE_DISTANCE)


def move_forward():
    turtle.forward(MOVE_DISTANCE)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b  # Automatically a tuple even without the parentheses


move_list = [move_right, move_left, move_backward, move_forward]


while True:
    turtle.color(random_color())
    move = random.choice(move_list)
    move()


