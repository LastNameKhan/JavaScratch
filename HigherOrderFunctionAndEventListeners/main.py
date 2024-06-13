import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)


screen.listen()
turtle.onkey(key="space", fun=move_forward)
screen.exitonclick()