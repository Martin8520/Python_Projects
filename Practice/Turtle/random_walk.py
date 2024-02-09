from turtle import *
from random import *

tim = Turtle()
tim.shape("turtle")
tim.color("red")
tim.pensize(10)
angles = [0, 90, 180, 270]
tim.speed(0.10)


def get_rand_color():
    return tuple(randint(0, 255) for _ in range(3))


def random_angle():
    return tim.left(choice(angles))


colormode(255)

for _ in range(250):
    tim.forward(25)
    tim.pencolor(*get_rand_color())
    random_angle()
screen = Screen()
screen.exitonclick()
