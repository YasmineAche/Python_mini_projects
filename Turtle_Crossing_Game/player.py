from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 50
FINISH_LINE_Y = 270


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_starting_position()
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        return False

    def go_to_starting_position(self):
        self.goto(STARTING_POSITION)
