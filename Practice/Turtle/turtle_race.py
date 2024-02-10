
from turtle import *
from random import randint

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
y_pos = [-70, -40, -10, 20, 50, 80]
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for turtle_i in range(0, 6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colors[turtle_i])
    new_turtle.penup()
    new_turtle.goto(-230, y=y_pos[turtle_i])
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on = Turtle

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
        speed = randint(0, 10)
        turtle.forward(speed)

screen.exitonclick()
