import turtle as t
from random import choice, randint
import numpy as np

def random_pen_colour() -> tuple:
    R = randint(0, 255)
    G = randint(0, 255)
    B = randint(0, 255)
    return (R,G,B)


if __name__ == "__main__":
    tim = t.Turtle()
    tim.speed(10)
    r = 50
    t.colormode(255)

    angles = np.linspace(0,360,36)

    for angle in angles:
        tim.pencolor(random_pen_colour())
        tim.setheading(angle)
        tim.circle(r)


    screen = t.Screen()
    screen.exitonclick()
