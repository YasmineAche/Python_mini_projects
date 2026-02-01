from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.penup()
        self.x_factor = 10
        self.y_factor = 10
        self.moving_speed = 0.2

    def move(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.y_factor = -self.y_factor
        x = self.xcor() + self.x_factor
        y = self.ycor() + self.y_factor
        self.goto(x, y)

    def check_collision(self, right_paddle, left_paddle):
        if (self.distance(right_paddle) < 50 and self.xcor() >= 325) or (self.distance(left_paddle) < 50 and self.xcor() <= -325):
            self.x_factor = -self.x_factor
            return True
        return False

    def increase_speed(self):
        self.moving_speed *= 0.9

    def losing_game(self):
        self.home()
        self.x_factor = -self.x_factor
        self.moving_speed = 0.2
