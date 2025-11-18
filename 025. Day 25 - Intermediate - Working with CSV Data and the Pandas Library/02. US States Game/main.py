from turtle import Turtle
from pathlib import Path
import turtle
import pandas as pd

root = Path(__file__).parent
image_path = root / "blank_states_img.gif"
data_path = root / "50_states.csv"
df = pd.read_csv(data_path)


img = str(image_path)
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(img)
turtle.shape(img)

scoreboard = Turtle()
correct_guesses = []

while len(correct_guesses) < 50:
    score = len(correct_guesses)
    scoreboard.clear()
    scoreboard.hideturtle()
    scoreboard.color("black")
    scoreboard.penup()
    scoreboard.goto(0, 300)
    scoreboard.write(f"Score: {score}", font=("Arial", 12))

    states_column = df["state"].to_list()

    answer_state = screen.textinput(
        title="Guess the state", prompt="What's another state's name?")
    if answer_state is not None:
        answer_state = answer_state.title()

    if answer_state == "Exit":
        states_to_learn = []
        for state in states_column:
            if state not in correct_guesses:
                states_to_learn.append(state)

        states_to_learn_df = pd.DataFrame(states_to_learn)
        states_to_learn_df.to_csv(root/"state_to_learn.csv")
        break

    if answer_state in states_column and answer_state not in correct_guesses:
        new_state = Turtle()
        new_state.hideturtle()
        new_state.color("black")
        new_state.penup()

        answer_state_row = df[df["state"] == answer_state]
        x = answer_state_row["x"].item()
        y = answer_state_row["y"].item()

        new_state.goto(x, y)
        new_state.write(answer_state)
        correct_guesses.append(answer_state)


screen.exitonclick()
