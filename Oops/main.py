from turtle import Turtle, Screen
# Construct a new object from the turtle class
# timmy is the new object and Turtle() is the class
timmy = Turtle()

print(timmy)
timmy.shape("turtle")
timmy.color("teal")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()