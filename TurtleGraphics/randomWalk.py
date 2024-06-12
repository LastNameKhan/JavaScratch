from turtle import Turtle, Screen
import random

walking = Turtle()
colours = ["black", "red", "yellow", "blue", "teal", "green", "purple", "wheat", "DeepSkyBlue"]
direction = [0, 90, 180, 270]
distance = random.randint(0, 100)
walking.pensize(5)
walking.speed("fastest")

for i in range(200):
    walking.forward(30)
    walking.setheading(random.choice(direction))
    walking.color(random.choice(colours))


screen = Screen()
screen.exitonclick()