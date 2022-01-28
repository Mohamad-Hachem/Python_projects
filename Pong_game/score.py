# importing my modules
from turtle import Turtle

# declaring our class
class Score(Turtle):

    # initialising
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.left_score = 0
        self.right_score = 0
        self.write_score()
    # writing on the board
    def write_score(self):
        self.goto(-100, y=200)
        self.write(self.left_score, align="center",font=("Courie", 50, "normal"))
        self.goto(100, y=200)
        self.write(self.right_score, align="center", font=("Courie", 50, "normal"))

    # incrementing scores left
    def increment_score_left(self):
        self.clear()
        self.left_score += 1
        self.write_score()

    # incrementing scores right
    def increment_score_right(self):
        self.clear()
        self.right_score += 1
        self.write_score()