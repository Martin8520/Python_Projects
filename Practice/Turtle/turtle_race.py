from turtle import *
from random import *

screen = Screen()
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)

tim = Turtle()
tim.shape("turtle")
tim.color("blue")
tim.penup()
tim.goto(-200, 200)

tom = Turtle()
tom.shape("turtle")
tom.color("green")
tom.penup()
tom.goto(-200, 180)

tam = Turtle()
tam.shape("turtle")
tam.color("purple")
tam.penup()
tam.goto(-200, 160)

jim = Turtle()
jim.shape("turtle")
jim.color("red")
jim.penup()
jim.goto(-200, 140)

jam = Turtle()
jam.shape("turtle")
jam.color("teal")
jam.penup()
jam.goto(-200, 120)

pam = Turtle()
pam.shape("turtle")
pam.color("pink")
pam.penup()
pam.goto(-200, 100)

screen.exitonclick()
