import turtle
from paddle import Paddle
from turtle import Screen
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle(starting_position=(350, 0))
l_paddle = Paddle(starting_position=(-350, 0))

screen.listen()
screen.onkey(fun=r_paddle.move_up, key="w")
screen.onkey(fun=r_paddle.move_down, key="s")
screen.onkey(fun=l_paddle.move_up, key="Up")
screen.onkey(fun=l_paddle.move_down, key="Down")


ball = Ball()
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330:
        ball.bounce_x()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

screen.exitonclick()
