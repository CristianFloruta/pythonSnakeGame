from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.color("white")
        self.speed("fastest")
        x_coord = randint(-280, 280)
        y_coord = randint(-280, 280)
        self.goto(x_coord, y_coord)
        self.reset_location()

    def reset_location(self):
        x_coord = randint(-280, 280)
        y_coord = randint(-280, 280)
        self.goto(x_coord, y_coord)
