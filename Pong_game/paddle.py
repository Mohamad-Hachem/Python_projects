# TODO: 2. creating my paddle class
# import my needed module
from turtle import Turtle

# Global variables for better code control
HEIGHT, WIDTH = 1, 5
LEFT, RIGHT = -350, 350


# initializing my paddle class
class Paddle(Turtle):

    # initializing
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shape()
        self.shapesize(WIDTH, HEIGHT)
        self.penup()
        self.speed("fastest")

    # setting positioning
    def position(self, position='right'):
        """This function takes a string 'left' or 'right' to set the postion of the paddle that you want"""
        if position == 'left':
            self.setposition(LEFT, y=0)
        elif position == 'right':
            self.setposition(RIGHT, y=0)
        else:  # making our class a bit defensive
            print("you entered a wrong position we will put the paddle on the right by default")
            self.setposition(RIGHT, y=0)

    # Moving my Paddle functions
    def move_up(self):
        self.goto(x=self.xcor(), y=self.ycor()+20)

    def move_down(self):
        self.goto(x=self.xcor(), y=self.ycor()-20)