from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-220, 250)
        self.write(f"Level  {self.score}", align="center", font=(FONT))

    def next_level(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.color("black")
        self.goto(0, 0)
        self.write("Game Over", align="center", font=(FONT))
