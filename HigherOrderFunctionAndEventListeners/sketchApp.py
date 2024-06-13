from turtle import Turtle, Screen

toto = Turtle()
def move_forward():
    toto.forward(10)

def move_backwards():
    toto.backward(10)

def clockwise():
    toto.right(10)

def counterClockwise():
    toto.left(10)

def clear():
    toto.clear()
    toto.penup()
    toto.home()
    toto.pendown()

screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s",fun=move_backwards)
screen.onkey(key="a",fun=counterClockwise)
screen.onkey(key="d",fun=clockwise)
screen.onkey(key="c",fun=clear)
screen.exitonclick()