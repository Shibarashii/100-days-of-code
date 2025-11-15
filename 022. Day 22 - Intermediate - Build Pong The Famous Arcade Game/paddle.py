from turtle import Turtle
from typing import Tuple

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
WIDTH = 5
LENGTH = 1


class Paddle(Turtle):
    def __init__(self, starting_position: Tuple[int, int]):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=WIDTH, stretch_len=LENGTH)
        self.penup()
        self.goto(starting_position)

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
