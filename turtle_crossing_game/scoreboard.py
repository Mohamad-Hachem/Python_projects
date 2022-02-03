# importing needed module
from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    # initializing Score
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x=-280,y=250)
        self.level = 0
        self.write_score()

    # writing my score
    def write_score(self):
        """this method takes nothing and simply update the score"""
        self.clear()
        self.write(arg=f"Level : {self.level}", align="left", font=FONT)

    # increasing score
    def score_increment(self):
        self.level += 1

    # ending the game
    def end_game(self):
        self.goto(0,0)
        self.write(arg=f"Game over you reached :level {self.level}", align="center", font=("Courier", 12, "normal"))
