import turtle
from turtle import Turtle, Screen
import random

circleTur = Turtle()
turtle.colormode(255)
circleTur.speed("fastest")


def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colours = (r, g, b)
    return colours


for i in range(100):
    circleTur.color(randomColor())
    circleTur.circle(100)
    circleTur.right(4)

screen = Screen()
screen.exitonclick()
