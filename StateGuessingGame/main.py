import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


game_is_on = False
count = 0
guessed_state = []

while not game_is_on:
    answer_state = screen.textinput(title=f"Guess the State {count}/50", prompt="What's another state's name?")
    data = pandas.read_csv("50_states.csv")
    state_name = data["state"].tolist()
    if answer_state == "exit":
        # missing_states = []
        # for state in state_name:
        #     if state not in guessed_state:
        #         missing_states.append(state)
        missing_states = [state for state in state_name if state not in guessed_state]
        data_to_csv = {
            "missing_state" : missing_states
        }
        created_file = pandas.DataFrame(data_to_csv)
        created_csv = created_file.to_csv("missing_state")
        print(created_csv)
    if answer_state in state_name:
        guessed_state.append(answer_state)
        count += 1
        state_turtle = turtle.Turtle()
        state_turtle.hideturtle()
        fetched_row_data = data[data["state"] == answer_state]
        x_cor = fetched_row_data["x"].values[0]
        y_cor = fetched_row_data["y"].values[0]
        # Another method for the above code is
        # x_cor = int(fetched_row_data.x)
        # y_cor = int(fetched_row_data.y)
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

# turtle.mainloop()

