from turtle import Turtle, Screen

rick_turtle = Turtle()

for i in range(15):
    rick_turtle.forward(10)
    rick_turtle.penup()
    rick_turtle.forward(10)
    rick_turtle.pendown()




screen = Screen()
screen.exitonclick()