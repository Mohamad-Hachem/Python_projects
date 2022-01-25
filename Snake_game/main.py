# importing our needed modules
from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

# initialising the screen that we will have the snake on
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# we will turn our tracer off so we can update when we feel it is the right time
screen.tracer(0)

# initialising the snake
snake = Snake()

# initialising food
food = Food()

# initialising score
score = Score()

# start listening for key presses
screen.listen()
screen.onkey(fun=snake.move_up, key="Up")
screen.onkey(fun=snake.move_down, key="Down")
screen.onkey(fun=snake.move_left, key="Left")
screen.onkey(fun=snake.move_right, key="Right")

# Start our game
games_is_on = True

while games_is_on:

    # updating the screen
    screen.update()
    time.sleep(0.1)

    # letting the snake to move
    snake.move()

    # detecting if there is any collision with food
    if(snake.head.distance(food) < 15):
        food.refresh()
        snake.extend()
        score.increment_score()

    # detect collision with wall
    if(snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300):
        games_is_on = False
        score.game_over()

    # detect if the head has any collision with its body
    for part in snake.snake_body[1:]:
        if(snake.head.distance(part) < 10):
            games_is_on = False
            score.game_over()

screen.exitonclick()
