from turtle import Turtle, Screen

pagong = Turtle()

screen = Screen()


def turn_right():
    pagong.right(10)


def turn_left():
    pagong.left(10)


def move_forward():
    pagong.forward(10)


def move_backward():
    pagong.backward(10)


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=pagong.clear)
screen.exitonclick()


