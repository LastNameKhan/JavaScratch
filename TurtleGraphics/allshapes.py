from turtle import Turtle, Screen

runner = Turtle()
screen = Screen()
number_of_angles = 3

screen.setup(width=800, height=600, startx=200, starty=200)

for i in range(number_of_angles):
    angle = 360/ number_of_angles
    runner.forward(100)
    runner.right(angle)

def square():
    """To Print the Square"""
    for i in range(4):
        runner.forward(100)
        runner.right(90)

def triangle():
    """To Print the Triangle"""
    for i in range(3):
        runner.forward(100)
        runner.right(120)

def pentagon():
    """To Print the Pentagon"""
    for i in range(5):
        runner.forward(100)
        runner.right(72)

def hexagon():
    """To Print the hexagon"""
    for i in range(6):
        runner.forward(100)
        runner.right(60)

def heptagon():
    """To Print the heptagon"""
    for i in range(7):
        runner.forward(100)
        runner.right(51.5)

def octagon():
    """To Print the octagon"""
    for i in range(8):
        runner.forward(100)
        runner.right(45)

def nonagon():
    """To Print the nonagon"""
    for i in range(9):
        runner.forward(100)
        runner.right(40)

def decagon():
    """To Print the decagon"""
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