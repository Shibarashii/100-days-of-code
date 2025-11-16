from turtle import Turtle
from typing import Tuple
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LENGTH = 2
WIDTH = 1


class CarManager():
    def __init__(self):
        self.cars: list[Turtle] = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def spawn_car(self):
        if random.randint(1, 6) == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=LENGTH, stretch_wid=WIDTH)
            new_car.penup()
            new_car.color(self._generate_random_color())
            new_car.goto(300, self._generate_random_y())
            new_car.setheading(180)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.move_speed)

    def increase_move_speed(self):
        self.move_speed += MOVE_INCREMENT

    def _generate_random_color(self):
        return random.choice(COLORS)

    def _generate_random_y(self):
        return random.randint(-250, 250)
