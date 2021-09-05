from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

initial_coord = [(0,0),(-20,0),(-40,0)]
turtle_list = []

for position in initial_coord:
    tim = Turtle("square")
    tim.color("white")
    tim.penup()
    tim.goto(position)
    turtle_list.append(tim)



screen.exitonclick()