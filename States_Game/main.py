import turtle
import pandas as pd

BG_IMAGE = "blank_states_img.gif"

my_turtle = turtle.Turtle()
my_turtle.hideturtle()
my_turtle.teleport(-280, 250)
my_turtle.color("gray")
my_turtle.write("Type 'Exit' to exit the game", align="center", font=("Arial", 13, "normal"))
my_turtle.color("black")

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(BG_IMAGE)
screen.setup(width=750, height=550)
turtle.shape(BG_IMAGE)

data = pd.read_csv("50_states.csv")
states_list = data.state.to_list()

nbr_correct_answers = 0
nbr_of_states = len(data)

while nbr_correct_answers < nbr_of_states:
    user_answer = screen.textinput(title=f"{nbr_correct_answers}/{nbr_of_states} correct answers", prompt="Give a name of a state...")
    if user_answer is None or user_answer.strip().lower() == "exit":
        break

    user_answer = user_answer.strip().lower().title()

    if user_answer in states_list:
        x_cord = data[data.state == user_answer].x.item()
        y_cord = data[data.state == user_answer].y.item()
        my_turtle.teleport(x_cord,y_cord)
        my_turtle.write(user_answer, align="center", font=("Arial", 13, "normal"))
        nbr_correct_answers += 1



# def get_mouse_click_coords(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coords)
# turtle.mainloop()