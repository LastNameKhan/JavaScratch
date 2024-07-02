import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


game_is_on = False
count = 0
while not game_is_on:
    answer_state = screen.textinput(title=f"Guess the State {count}/50", prompt="What's another state's name?")
    data = pandas.read_csv("50_states.csv")
    state_name = data["state"].tolist()
    if answer_state in state_name:
        count += 1
        state_turtle = turtle.Turtle()
        state_turtle.hideturtle()
        fetched_row_data = data[data["state"] == answer_state]
        x_cor = fetched_row_data["x"].values[0]
        y_cor = fetched_row_data["y"].values[0]
        state_turtle.penup()
        state_turtle.goto(x_cor, y_cor)
        state_turtle.pendown()
        state_turtle.write(answer_state, align="center", font=("Arial", 12, "normal"))
    else:
        error_turtle = turtle.Turtle()
        error_turtle.hideturtle()
        error_turtle.write("Oops Game Lost!!!!", align="center", font=("Arial", 16, "normal"))
        game_is_on = True


# Below function was used to get the coordinaltion of the mouse click event x and y coordinates
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()

