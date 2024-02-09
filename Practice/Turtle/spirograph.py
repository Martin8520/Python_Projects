from turtle import *
from random import *

tim = Turtle()
tim.shape("turtle")
tim.color("red")
tim.pensize(1)
angles = [0, 90, 180, 270]
tim.speed(0)


def get_random_color():
    return tuple(randint(0, 255) for _ in range(3))


def random_angle():
    return tim.left(choice(angles))


colormode(255)

for _ in range(144):
    tim.right(5)
    tim.circle(100)
    tim.pencolor(*get_random_color())

screen = Screen()
screen.exitonclick()
