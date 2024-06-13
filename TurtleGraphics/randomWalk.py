import turtle
from turtle import Turtle, Screen
import random

walking = Turtle()
turtle.colormode(255)

def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


direction = [0, 90, 180, 270]
distance = random.randint(0, 100)
walking.pensize(5)
walking.speed("fastest")

for i in range(1000):
    walking.forward(30)
    walking.setheading(random.choice(direction))
    walking.color(randomColor())


screen = Screen()
screen.exitonclick()