from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color("gray")
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.clear()
        self.draw_line()
        self.write_instructions()
        self.teleport(-60, 250)
        self.write(self.left_score, align="center", font=("Courier", 50, "bold"))
        self.teleport(60, 250)
        self.write(self.right_score, align="center", font=("Courier", 50, "bold"))

    def draw_line(self):
        self.teleport(0, -250)
        self.pensize(2)
        self.setheading(90)
        for _ in range(26):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)

    def write_instructions(self):
        self.teleport(-340, -280)
        self.write("Left player: W/S \nRight player: ↑/↓\nStop game: Q", align="center", font=("Courier", 10, "bold"))
