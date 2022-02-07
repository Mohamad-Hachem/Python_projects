# importing our modules
import turtle
import pandas as pd
from labels import Labels

# initialising my screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
# shaping our turtle to have image shape
turtle.shape(image)

# initializing my labels
labels = Labels()

# starting our game
answer = screen.textinput(title="Guess the State", prompt="What's another state name")
states_score = 0
states = pd.read_csv('50_states.csv')
list_states = states.state.to_list()

# starting my while loop
while states_score <= 50 and answer != 'q':
    answer = answer.title()

    # checking if the answer is right and post it on the map
    if (answer in list_states) and (answer not in labels.states_labels):
        # retrieving the coordinates
        coordinates = states[states.state == answer]
        # adding a state
        labels.add_state(int(coordinates.x),int(coordinates.y),answer)
        # increasing score
        states_score += 1

    # asking the user again
    answer = screen.textinput(title=f"{states_score}/50 States Correct", prompt="What's another state name\nPress 'q' to quit")

# generating a file containing the states that are not guessed
def generate_left_states():
    missing_states = []
    for state in states.state.to_list():
        if state not in labels.states_labels:
            missing_states.append(state)
    # creating a dataframe and write it into a file
    data_missing_state = pd.DataFrame(missing_states)
    data_missing_state.to_csv("missing_states.csv")


# finishing the program
if states_score == 50:
    print("Well done you won!!!!")
else:
    print("you still have some stuff to learn check the generated file of states for you to learn")
    generate_left_states()

# exit only on click
screen.exitonclick()

# how did we get the coordinates
def get_coordinates():
    # we are going to collect the X, Y by the following function
    def get_mouse_click_coor(x, y):
        print(x, y)

    # starting an event listener (mouse click) then get the coordination of the click on the map
    # we do that to be able to collect the coordinates to use in my csv file
    turtle.onscreenclick(fun=get_mouse_click_coor)

    # we will keep the program on going to collect the coordinates
    # usually we keep this function at the end of our program
    turtle.mainloop()