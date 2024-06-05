from turtle import Turtle, Screen

runner = Turtle()
number_of_angles = 3

for i in range(number_of_angles):
    angle = 360/ number_of_angles
    runner.forward(100)
    runner.right(angle)

def square():
    for i in range(4):
        runner.forward(100)
        runner.right(90)

def triangle():
    for i in range(3):
        runner.forward(100)
        runner.right(120)

def pentagon():
    for i in range(5):
        runner.forward(100)
        runner.right(72)

def hexagon():
    for i in range(6):
        runner.forward(100)
        runner.right(60)

def heptagon():
    for i in range(7):
        runner.forward(100)
        runner.right(51.5)

def octagon():
    for i in range(8):
        runner.forward(100)
        runner.right(45)

def nonagon():
    for i in range(9):
        runner.forward(100)
        runner.right(40)

def decagon():
    for i in range(10):
        runner.forward(100)
        runner.right(36)

square()
triangle()
pentagon()
hexagon()
heptagon()
octagon()
nonagon()
decagon()


screen = Screen()
screen.exitonclick()