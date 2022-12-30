from turtle import Turtle


class GameOver(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

    def inform(self):
        """
        create a turtle object
        :return: Write "Game Over" on the game screen!
        """
        self.write(arg="GAME OVER!", align="center", font=("Courier", 24, "bold"), )
