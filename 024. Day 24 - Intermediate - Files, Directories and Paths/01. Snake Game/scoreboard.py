from turtle import Turtle
from pathlib import Path

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

path = Path(__file__).parent


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.load_highscore()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score} | Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_scoreboard()
        self.save_score()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def save_score(self):
        with open(path / "data.txt", "w") as file:
            file.write(str(self.highscore))

    def load_highscore(self):
        with open(path / "data.txt", "r") as file:
            content = file.read()
            self.highscore = int(content)
