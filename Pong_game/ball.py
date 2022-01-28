# importing my modules
from turtle import Turtle
from random import choice
import time

# Global variables
RIGHT, LEFT, UP, DOWN = 2, -2, 2, -2


# initialising my ball class
class Ball(Turtle):

    # initialising
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color("white")
        self.penup()
        self.x_direction, self.y_direction = choice([LEFT,RIGHT]), choice([UP,DOWN])

    # moving my ball
    def moving(self):
        new_x = self.xcor() + self.x_direction
        new_y = self.ycor() + self.y_direction
        self.goto(new_x, new_y)

    # collision detect with walls
    def wall_collision(self):
        if(self.ycor() >= 280 or self.ycor() <= -280):
           if self.y_direction == UP:
              self.y_direction = DOWN
           else:
              self.y_direction = UP

    # collision detect with paddels
    def paddle_collision(self, paddle):
        """this function takes a paddle and check if there is a collision with ball"""
        # if the ball is at 50 distance and x = 340 that means it touches the paddle
        if self.distance(paddle) <= 50 and (self.xcor() >= 340 or self.xcor() <= -340):
            if self.x_direction == RIGHT:
                self.x_direction = LEFT
            else:
                self.x_direction = RIGHT
        # if it is not touching the paddle and goes to far that means the other player scores a point
        elif self.distance(paddle) > 50 and self.distance(paddle) < 200 and (self.xcor() >= 400 or self.xcor() <= -400):
            self.goto(0, 0)
            time.sleep(1)
            if self.y_direction == DOWN:
                self.y_direction = UP
            else:
                self.y_direction = DOWN

            if self.x_direction == LEFT:
                self.x_direction = RIGHT
            else:
                self.x_direction = LEFT

            return True
