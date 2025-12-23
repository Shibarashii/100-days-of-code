import turtle
from paddle import Paddle
from turtle import Screen
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle(starting_position=(350, 0))
l_paddle = Paddle(starting_position=(-350, 0))
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")
screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")


ball = Ball()
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()
        ball.move_speed *= 0.9

    # Detect right paddle misses
    if ball.xcor() > 400:
        ball.reset()
        scoreboard.l_point()

    # Detect left paddle misses
    if ball.xcor() < -400:
        ball.reset()
        scoreboard.r_point()


screen.exitonclick()
