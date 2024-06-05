from turtle import Turtle, Screen

little_turtle = Turtle()
tri_turtle = Turtle()
tri_turtle.forward(200)

# Square
for i in range(4):
    little_turtle.forward(100)
    little_turtle.right(90)

# Trapezium
for i in range(6):
    tri_turtle.forward(100)
    tri_turtle.right(60)





screen = Screen()
screen.exitonclick()