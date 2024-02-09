from turtle import *
from random import *

tim = Turtle()
tim.shape("turtle")
tim.color("red")


# for _ in range(10):
#     tim.forward(25)
#     tim.penup()
#     tim.forward(25)
#     tim.pendown()
def get_rand_color():
    return tuple(randint(0, 255) for _ in range(3))


colormode(255)


tim.pencolor(*get_rand_color())
for _ in range(3):
    tim.forward(50)
    tim.right(120)
tim.pencolor(*get_rand_color())
for _ in range(4):
    tim.forward(50)
    tim.right(90)
tim.pencolor(*get_rand_color())
for _ in range(5):
    tim.forward(50)
    tim.right(72)
tim.pencolor(*get_rand_color())
for _ in range(6):
    tim.forward(50)
    tim.right(60)
tim.pencolor(*get_rand_color())
for _ in range(7):
    tim.forward(50)
    tim.right(51)

screen = Screen()
screen.exitonclick()
