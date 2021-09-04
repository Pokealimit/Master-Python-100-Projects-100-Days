import turtle as t
import random as r

is_race_on = False
screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

start_x = -238
start_y = -80

r.shuffle(colors)

turtle_list = []
i = 0
for color in colors:
    turtle_list.append(t.Turtle(shape="turtle"))
    turtle_list[i].color(color)
    turtle_list[i].penup()
    turtle_list[i].goto(x=start_x, y=start_y)
    i += 1
    start_y += 30

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_dist = r.randint(0,10)
        turtle.forward(rand_dist)
    

screen.exitonclick()