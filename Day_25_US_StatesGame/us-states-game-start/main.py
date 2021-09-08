import turtle, pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

state_turtle = turtle.Turtle()
state_turtle.hideturtle()
state_turtle.penup()

# To get the coordinates of the 50 states on the gif manually
# def get_mouse_click_coord(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coord)

# turtle.mainloop()

# Read States Names and Coordinates from CSV
States = pandas.read_csv("50_states.csv")
all_states = States['state'].to_list()

# print(States)

correct_guesses = 0
# game_is_on = True
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title = f"{correct_guesses}/50 States Correct", prompt = "What's another state's name?").title()
    if answer_state in all_states:
        state_data = States[States.state == answer_state]
        state_turtle.goto(int(state_data.x), int(state_data.y))
        state_turtle.write(answer_state)
        correct_guesses += 1
        guessed_states.append(answer_state)

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # Create CSV
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break


