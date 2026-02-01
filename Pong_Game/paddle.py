from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        self.x_position = x
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.teleport(self.x_position, 0)

    def move_up(self):
        self.setheading(90)
        if self.ycor() < 230:
            self.forward(20)

    def move_down(self):
        self.setheading(270)
        if self.ycor() > -230:
            self.forward(20)