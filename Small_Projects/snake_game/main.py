from turtle import Screen, Turtle
import time

from Small_Projects.snake_game.snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()




game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

















screen.exitonclick()