from turtle import Turtle

TEXT_ALIGNMENT = "center"
TEXT_FONT = ("Courier", 20, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highest_score = self.get_highest_score()
        self.hideturtle()
        self.teleport(-20, 275)
        self.color("white")
        self.updating_score()

    def increase_score(self) -> None:
        self.score += 1
        self.updating_score()

    def updating_score(self) -> None:
        self.clear()
        self.write(f"Score : {self.score}\tHighest score : {self.highest_score}", align=TEXT_ALIGNMENT, font=TEXT_FONT)

    def reset_score(self) -> None:
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("score_data.txt", "w") as file:
                file.write(str(self.highest_score))
        self.score = 0
        self.updating_score()

    @staticmethod
    def get_highest_score() -> int:
        with open("score_data.txt", "r") as file:
            highest_score = int(file.read())
        return highest_score
