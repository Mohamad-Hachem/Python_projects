# we will import the modules that are needed
from turtle import Turtle

# Our global variables
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280

# Creating a player class
class Player(Turtle):

    # initializing the player
    def __init__(self):
        super().__init__()
        self.penup()
        self.left(90)
        self.shape("turtle")
        self.goto(STARTING_POSITION)

    # moving up function
    def move_up(self):
        """This function takes nothing: it simply makes the turtle go up"""
        self.goto(self.xcor(), self.ycor()+MOVE_DISTANCE)

    # arrived to finish line
    def finish(self):
        if(self.ycor() >= 280):
            self.goto(STARTING_POSITION)
            return True
        return False


