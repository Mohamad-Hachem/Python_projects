# importing modules needed
from turtle import Turtle

# Global variables so we have a quick access on initial placement without having to look into the code
POSITION_X, POSITION_Y = 0, 270

# creating our class score
class Score(Turtle):
    # initialising our class
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(POSITION_X , POSITION_Y)
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.write(arg=f"current score: {self.score}", move=False, align="center", font=('Arial',16,'normal'))

    # incrementing and updating the score each time the snake eats
    def increment_score(self):
        self.clear()
        self.score += 1
        super().write(arg=f"current score: {self.score}", move=False, align="center", font=('Arial',16,'normal'))

    # ending the game
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(arg=f"Game over!", move=False, align="center", font=('Arial',16,'normal'))