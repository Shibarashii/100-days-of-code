from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.show_score()

    def add_score(self):
        self.score += 1
        self.show_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER",
                   align=ALIGNMENT,
                   font=FONT)

    def show_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}",
                   align=ALIGNMENT,
                   font=FONT)
