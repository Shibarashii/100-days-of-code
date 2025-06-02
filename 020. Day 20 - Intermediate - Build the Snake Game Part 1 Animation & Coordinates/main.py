from turtle import Turtle, Screen
from snake import Snake
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

screen.onkey(fun=snake.right, key="d")
screen.onkey(fun=snake.left, key="a")
screen.onkey(fun=snake.up, key="w")
screen.onkey(fun=snake.down, key="s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    screen.listen()
    snake.move()


screen.exitonclick()
