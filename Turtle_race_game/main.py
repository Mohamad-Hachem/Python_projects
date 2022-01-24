# TODO: 1. import the necessary modules to work with
import turtle as t
import random
# import colorgram as col not important just cool module to work with

# TODO: 2. Start by working on the screen criteria before starting because dim are important
screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet",prompt="which turtle will win? Enter your color:")
print(user_bet)

# TODO: 3.Start working on the race
# we declared 2 lists 1. is the turtles' colors (colors) 2. is the list of turtles objects (turtles)
colors = ["red","orange","black","green","blue","purple"]
turtles = []

# initialise the race to False
is_race_on = False

# Creating the turtles
for i in range(6):
    turtle = t.Turtle("turtle")
    turtle.penup()
    turtle.color(colors[i])
    turtles.append(turtle)

#positioning the turtles
for turtle in turtles:
    turtle.goto(x=-230,y=-100+30*turtles.index(turtle))

# making sure that the user locked his/her answer before starting the race
if user_bet:
    is_race_on = True

# starting the race
while(is_race_on):
    # iterating the turtles one by one and give them a random forward to move
    for turtle in turtles:
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
        # checking if after moving the turtle passed the finish line
        if(turtle.xcor() >= 230):
            # if yes making sure to end the race and annonce the winner
            is_race_on = False
            winning_color = turtle.pencolor()
            print(f"the winner is {turtle.pencolor()}")
            # checking if the user's bet was right or no and report back to him
            if(winning_color == user_bet):
                print("Congrats you won")
            else:
                print("you lost")

# press on the screen to end the project
screen.exitonclick()