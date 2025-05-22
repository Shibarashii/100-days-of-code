from turtle import Turtle, Screen
import random
START_POS_X = -450
START_POS_Y = -150
screen = Screen()
screen.setup(width=1000, height=1000)

red_turtle = Turtle()
orange_turtle = Turtle()
yellow_turtle = Turtle()
green_turtle = Turtle()
blue_turtle = Turtle()
purple_turtle = Turtle()
turtles = {
    "red": red_turtle,
    "orange": orange_turtle,
    "yellow": yellow_turtle,
    "green": green_turtle,
    "blue": blue_turtle,
    "purple": purple_turtle
}

i = 0
for color in turtles:
    i += 1
    turtles[color].shape("turtle")
    turtles[color].shapesize(2)
    turtles[color].color(color)
    turtles[color].penup()
    turtles[color].goto(START_POS_X, START_POS_Y + i * 50)


guess = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Choose a color: ")

winner = ""
no_winner = True
while no_winner:
    for color in turtles:
        turtles[color].forward(random.randint(1, 20))
        if turtles[color].xcor() > 400:
            winner = turtles[color].pencolor()
            no_winner = False

if winner == guess:
    print(f"You got it right! {winner.capitalize()} won ")
else:
    print(f"You got it wrong! {winner.capitalize()} won ")


screen.exitonclick()


