# importing our used modules
from turtle import Turtle
import random

# Our global variables to have a better control over our program
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    # initializing our class
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1,stretch_len=2)
        self.color(random.choice(COLORS))
        self.goto(x=300,y=random.randint(-250,250))
        self.speed(3)

    # moving to the left automatically
    def move_left(self,speed ):
        self.goto(self.xcor()-speed,self.ycor())
