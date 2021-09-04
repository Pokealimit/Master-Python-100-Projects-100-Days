from turtle import Turtle, Screen, colormode
from random import randint

class differentShape:
    def __init__(self):
        self.tim = Turtle()
        colormode(255)
    
    def drawTriangle(self):
        self.tim.pencolor(self.random_pen_colour())
        for _ in range(3):
            self.tim.forward(100)
            self.tim.right(120)

    def drawSquare(self):
        self.tim.pencolor(self.random_pen_colour())
        for _ in range(4):
            self.tim.forward(100)
            self.tim.right(90)

    def drawPentagon(self):
        self.tim.pencolor(self.random_pen_colour())
        for _ in range(5):
            self.tim.forward(100)
            self.tim.right(72)

    def drawHexagon(self):
        self.tim.pencolor(self.random_pen_colour())
        for _ in range(6):
            self.tim.forward(100)
            self.tim.right(60)

    def drawHeptagon(self):
        self.tim.pencolor(self.random_pen_colour())
        for _ in range(7):
            self.tim.forward(100)
            self.tim.right(51.43)
    
    def drawOctagon(self):
        self.tim.pencolor(self.random_pen_colour())
        for _ in range(8):
            self.tim.forward(100)
            self.tim.right(45)

    def drawNonagon(self):
        self.tim.pencolor(self.random_pen_colour())
        for _ in range(9):
            self.tim.forward(100)
            self.tim.right(40)

    def drawDecagon(self):
            self.tim.pencolor(self.random_pen_colour())
            for _ in range(10):
                self.tim.forward(100)
                self.tim.right(36)

    def random_pen_colour(self) -> tuple:
        R = randint(0, 255)
        G = randint(0, 255)
        B = randint(0, 255)

        return (R,G,B)
        


if __name__ == "__main__":
    timmy = differentShape()
    timmy.drawTriangle()
    timmy.drawSquare()
    timmy.drawPentagon()
    timmy.drawHexagon()
    timmy.drawHeptagon()
    timmy.drawOctagon()
    timmy.drawNonagon()
    timmy.drawDecagon()
    screen = Screen()
    screen.exitonclick()
