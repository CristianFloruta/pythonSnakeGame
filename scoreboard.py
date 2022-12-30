from turtle import Turtle

TEXT_COLOR = "white"
ALIGNMENT = "center"
FONT = ("Courier", 14, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.speed("fastest")
        self.goto(x=0, y=280)
        self.color(TEXT_COLOR)
        self.update_score()
        self.hideturtle()


    def update_score(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def score_count(self):
        self.score += 1
        self.clear()
        self.update_score()
