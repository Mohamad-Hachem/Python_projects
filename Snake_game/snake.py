from turtle import Turtle

# creating our constants so we have more control over our game and not have to go and search in the code for changes
STARTING_POSITIONS = [(0, 0),(-20, 0),(-40, 0)]
MOVE_DISTANCE = 20
up, down, left, right = 90, 270, 180, 0

class Snake:
    # creating our class
    def __init__(self):
        self.snake_body = []
        self.initialising()
        self.head = self.snake_body[0]

    #creating the body of our snake
    def initialising(self):
        # creating turtles and appending them to snake body
        for _ in range(3):
            self.add_turtle()

        # positioning the snake body
        for i in range(len(self.snake_body)):
            self.snake_body[i].goto(STARTING_POSITIONS[i])

    # adding a turtle to the body (making the body bigger)
    def add_turtle(self):
        new_turtle = Turtle("square")
        new_turtle.penup()
        new_turtle.color("white")
        self.snake_body.append(new_turtle)

    # extending the snake body (when the snake eats)
    def extend(self):
        self.add_turtle()
        # telling my new turtle to join snake body by taking the position of the previous tale
        self.snake_body[-1].goto(self.snake_body[-2].xcor(), self.snake_body[-2].ycor())

    # creating a move function that will keep our snake moving
    def move(self):
        #  snake moving making every turtle follow the one before it
        for i in range(len(self.snake_body) - 1, 0, -1):
            x_cor = self.snake_body[i - 1].xcor()
            y_cor = self.snake_body[i - 1].ycor()
            self.snake_body[i].goto(x=x_cor, y=y_cor)
        # we will only move the head and the body will follow
        self.snake_body[0].forward(MOVE_DISTANCE)

    # creating a series of functions of movements for our snakes up ,down ,left ,right
    def move_up(self):
        if(self.head.heading() != down):
            self.head.setheading(90)

    def move_right(self):
        if (self.head.heading() != left):
            self.head.setheading(0)

    def move_left(self):
        if (self.head.heading() != right):
            self.head.setheading(180)

    def move_down(self):
        if (self.head.heading() != up):
            self.head.setheading(270)
