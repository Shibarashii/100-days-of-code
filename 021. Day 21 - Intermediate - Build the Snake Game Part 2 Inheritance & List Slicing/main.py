from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    # Detect collision with food
    if snake.head.distance(food) < 15:
        snake.extend()
        food.randomize_location()
        scoreboard.add_score()

    # Detect collision with food
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detection collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
