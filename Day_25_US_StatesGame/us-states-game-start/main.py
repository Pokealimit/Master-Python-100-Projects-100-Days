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
    # state_row = States[States["state"].str.contains(answer_state.lower(), case=False)]
    if answer_state in all_states:
    # print(state_row)
    # if not state_row.empty:
        # coordinate = (state_row.iloc[0]['x'], state_row.iloc[0]['y'])
        # state_turtle.goto(coordinate)
        # state_turtle.write(state_row.iloc[0]['state'], align="center", font=("Courier", 18, "normal"))
        # state_turtle.write(state_row.state.item(), align="center", font=("Courier", 18, "normal"))
        state_data = States[States.state == answer_state]
        state_turtle.goto(int(state_data.x), int(state_data.y))
        state_turtle.write(answer_state)
        correct_guesses += 1
        guessed_states.append(answer_state)

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")

        break

# Create CSV


# screen.exitonclick()