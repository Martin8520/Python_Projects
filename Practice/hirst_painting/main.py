# import colorgram
# rgb_colors = []
# colors = colorgram.extract("hirstbs.jpg", 10)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import random
from turtle import *

color_list = [(229, 222, 210), (223, 159, 80), (39, 107, 149), (118, 164, 192), (150, 63, 88), (207, 134, 157), (180, 160, 35), (28, 133, 96), (213, 86, 59), (120, 181, 152)]

tim = Turtle()
tim.shape("turtle")
tim.color("red")
tim.pensize(10)
tim.speed(0)
colormode(255)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = Screen()
screen.exitonclick()
