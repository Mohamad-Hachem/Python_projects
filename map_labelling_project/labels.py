# importing our modules
from turtle import Turtle

class Labels:

    # initializing our labels list
    def __init__(self):
        self.states = []
        self.states_labels = []

    # adding a label
    def add_state(self, x, y, answer):
        label = Turtle()
        label.penup()
        label.hideturtle()
        label.speed(2)
        label.goto(x,y)
        label.write(arg=answer, align='left')
        self.states_labels.append(answer)
        self.states.append(label)

