from turtle import Turtle
from random import randint

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("blue")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.speed("fastest")
        self.move_food()

    def move_food(self):
        self.hideturtle()
        x_pos = randint(-260, 260)
        y_pos = randint(-260, 260)
        self.teleport(x_pos, y_pos)
        self.showturtle()