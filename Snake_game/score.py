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
        self.high_score = self.read_data()
        self.update_scoreboard()

    # updating the score
    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"current score: {self.score} High Score: {self.high_score}", move=False, align="center", font=('Arial',16,'normal'))

    # incrementing and updating the score each time the snake eats
    def increment_score(self):
        self.score += 1
        self.update_scoreboard()

    # reseting the score board
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        with open("data.txt", mode='w') as file:
            file.write(f"{self.high_score}")
        self.update_scoreboard()

    # ending the game
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(arg=f"Game over!", move=False, align="center", font=('Arial',16,'normal'))

    # reading data from file
    def read_data(self):
        with open("data.txt") as file:
            return int(file.read())