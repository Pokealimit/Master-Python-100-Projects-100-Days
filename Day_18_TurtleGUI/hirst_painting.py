import colorgram
import turtle as t
import random as r
import numpy as np

colors = colorgram.extract('hirst_spot_painting.png',  2 ** 32)

color_list = []
for color in colors:
    R = color.rgb.r
    G = color.rgb.g
    B = color.rgb.b
    color_list.append((R,G,B))

for _ in range(4):
    color_list.pop(0)

tim = t.Turtle()
t.colormode(255)
tim.speed(10)
tim.penup()
tim.hideturtle()
inital_y = -235
tim.setpos(-235, inital_y)

for y in range(10):
    for x in range(10):
        tim.dot(20 , r.choice(color_list))
        tim.forward(50)

    inital_y += 50
    tim.setpos(-235, inital_y)

screen = t.Screen()
screen.exitonclick()