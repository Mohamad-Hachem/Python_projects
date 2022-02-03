import time
from turtle import Screen
from player import Player
from car_manager import CarManager , MOVE_INCREMENT
from scoreboard import Scoreboard

# initializing a screen and setting it up
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# initializing the player
player = Player()

# initializing level scoreboard
score_board = Scoreboard()

# function to keep the cars moving
def moving_cars(cars_list,speed):
    """this function takes a list of cars and makes them move to the left"""
    for i in cars_list:
        i.move_left(speed)


# function to make sure there is no collisions
def collision(player, cars_list):
    """this function takes 2 parameters a player and a list of cars it returns a boolean if there is any collision"""
    for i in cars_list:
        if(player.distance(i) <= 22):
            return True
    return False


# starting the Game
game_is_on = True
cars = 0
cars_list = []
while game_is_on:
    score_board.write_score()
    time.sleep(0.1)
    screen.onkey(fun=player.move_up, key="Up")
    screen.update()
    # creating our cars to see them play
    moving_cars(cars_list,MOVE_INCREMENT)
    if(cars%6 == 0):
        car = CarManager()
        cars_list.append(car)
        cars += 1
    else:
        cars += 1

    # checking if there is any collision with the obstacles
    if collision(player,cars_list):
        score_board.end_game()
        game_is_on = False

    # checking if the player crossed the finish line
    if(player.finish()):
        MOVE_INCREMENT += 10
        score_board.score_increment()




screen.exitonclick()