import turtle as t

tim = t.Turtle()
screen = t.Screen()

def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.backward(10)
def turn_cw():
    tim.right(10)
def turn_ccw():
    tim.left(10)

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_cw, "d")
screen.onkey(turn_ccw, "a")
screen.onkey(tim.reset, "c")

screen.exitonclick()