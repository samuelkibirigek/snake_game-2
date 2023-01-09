from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-295, 265)
        self.color("white")
        self.score = 0
        self.the_score()

    def the_score(self):
        self.clear()
        self.write(f"Score: {self.score}", font=("Courier", 24, "normal"))

    def increment_score(self):
        self.score += 1
        self.the_score()

    def game_over(self):
        self.write("GAME OVER!", align="center", font=("Courier", 24, "normal"))
