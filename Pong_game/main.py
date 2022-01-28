# importing our needed modules
from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from score import Score

# TODO: 1. Create my screen and set it up
# initialising my screen
screen = Screen()

# setting some criteria for my screen
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# initialising my paddles
right_paddle = Paddle()
right_paddle.position('right')
left_paddle = Paddle()
left_paddle.position('left')

# making the screen listen for keys
screen.listen()
screen.onkey(fun=right_paddle.move_up, key="Up")
screen.onkey(fun=right_paddle.move_down, key="Down")
screen.onkey(fun=left_paddle.move_up, key="W")
screen.onkey(fun=left_paddle.move_down, key="S")

# initialising my ball
ball = Ball()

# initialising score
score = Score()

# creating variables that we will use in the game
game_is_on = True

# starting my game
while game_is_on:
    screen.update()
    ball.wall_collision()
    if ball.paddle_collision(left_paddle):
        score.increment_score_right()
    if ball.paddle_collision(right_paddle):
        score.increment_score_left()
    ball.moving()
    sleep(0.001)
    if (score.left_score == 3 or score.right_score == 3):
        game_is_on = False
        break

# checking who one and put it in the console
if(score.left_score > score.right_score):
    print("left player wins")
else:
    print("right player wins")

# we will keep this at the bottom sense it symbolise the end of our program
# Making sure that the program ends with a mouse click
screen.exitonclick()
