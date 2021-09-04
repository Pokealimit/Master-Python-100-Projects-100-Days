from turtle import Turtle, Screen, colormode
import random

def random_pen_colour() -> tuple:
        R = random.randint(0, 255)
        G = random.randint(0, 255)
        B = random.randint(0, 255)

        return (R,G,B)

def random_walk(r):
    directions = (0, 90, 180, 270)
    for _ in range(50):
        r.pencolor(random_pen_colour())
        r.setheading(random.choice(directions))
        r.forward(20)


if __name__ == "__main__":
    t = Turtle()
    colormode(255)
    t.pensize(10)
    t.speed(4)
    random_walk(t)

    screen = Screen()
    screen.exitonclick()

