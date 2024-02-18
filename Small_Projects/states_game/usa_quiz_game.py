import os
import turtle
import pandas

script_dir = os.path.dirname(__file__)

csv_filename = "50_states.csv"
csv_path_temp = os.path.join(os.getcwd(), csv_filename)
csv_path_script = os.path.join(script_dir, csv_filename)
print("Temporary CSV path:", csv_path_temp)
print("Script CSV path:", csv_path_script)

screen = turtle.Screen()
screen.title("U.S. States Game")
image_path = os.path.join(script_dir, "blank_states_img.gif")
print("Image path:", image_path)
screen.addshape(image_path)
turtle.shape(image_path)

data_path = os.path.join(script_dir, "50_states.csv")
data = pandas.read_csv(data_path)
all_states = data.state.to_list()
guessed_states = []

if os.path.exists(csv_path_temp):
    data_path = csv_path_temp
else:
    data_path = csv_path_script
print("Chosen CSV path:", data_path)
print("States to learn path:", script_dir)
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What is the state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data_path = os.path.join(script_dir, "states_to_learn.csv")
        new_data.to_csv(new_data_path, index=False)
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
