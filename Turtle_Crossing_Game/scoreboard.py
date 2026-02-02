from turtle import Turtle
FONT = ("Courier", 24, "normal")
ROAD_LINES_Y_CORDS = [250, 200, 150, 100, 50, 0, -250, -200, -150, -100, -50]

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.setheading(180)
        self.update_screen()

    def draw_lines(self):
        for y_cord in ROAD_LINES_Y_CORDS:
            self.teleport(300, y_cord)
            self.color("gray30")
            while self.xcor() > -300:
                self.forward(10)
                self.penup()
                self.forward(10)
                self.pendown()

    def write_level(self):
        self.color("white")
        self.teleport(-280, 270)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def write_instruction(self):
        self.color("darkgray")
        self.teleport(-280, -280)
        self.write("Key: Space", align="left", font=("Courier", 12, "normal"))

    def update_screen(self):
        self.clear()
        self.write_level()
        self.draw_lines()
        self.write_instruction()

    def write_game_over(self):
        self.color("white")
        self.teleport(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)