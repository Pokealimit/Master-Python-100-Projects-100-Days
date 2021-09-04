import turtle as t
from random import choice, randint
import numpy as np

def random_pen_colour() -> tuple:
    R = randint(0, 255)
    G = randint(0, 255)
    B = randint(0, 255)
    return (R,G,B)

def drawSpirograph(number_of_circles: int) -> tuple:
    return np.linspace(0,360,number_of_circles)


if __name__ == "__main__":
    tim = t.Turtle()
    tim.speed("fastest")
    r = 50
    t.colormode(255)

    angles = drawSpirograph(20)

    for angle in angles:
        tim.color(random_pen_colour())
        tim.setheading(angle)
        tim.circle(r)


    screen = t.Screen()
    screen.exitonclick()
