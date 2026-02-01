from turtle import Turtle

TEXT_ALIGNMENT = "center"
TEXT_FONT = ("Courier", 20, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.teleport(-20, 275)
        self.color("white")
        self.updating_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.updating_score()

    def updating_score(self):
        self.write(f"Score : {self.score}", align=TEXT_ALIGNMENT, font=TEXT_FONT)

    def game_over(self):
        self.teleport(0,0)
        self.write(f"GAME OVER!", align=TEXT_ALIGNMENT, font=TEXT_FONT)
