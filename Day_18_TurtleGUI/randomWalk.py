from turtle import Turtle, Screen, colormode
from random import randint

def random_pen_colour() -> tuple:
        R = randint(0, 255)
        G = randint(0, 255)
        B = randint(0, 255)

        return (R,G,B)

def random_walk(r):
    for _ in range(50):
        r.pencolor(random_pen_colour())
        dir = randint(0,1)
        if dir == 1:
            r.right(90)
            # r.forward(20)
        else:
            r.left(90)
            # r.forward(20)
        
        r.forward(20)


if __name__ == "__main__":
    t = Turtle()
    colormode(255)
    t.pensize(10)
    t.speed(4)
    random_walk(t)
    

    screen = Screen()
    screen.exitonclick()

