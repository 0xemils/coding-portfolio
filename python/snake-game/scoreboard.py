from turtle import Turtle
import os

ALIGNMENT = "center"
FONT = ("Courier", 27, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())

        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 250)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"SCORE: {self.score} | High score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def add_score(self):
        self.score += 1
        self.update_score()
