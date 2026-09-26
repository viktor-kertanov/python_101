import turtle
from random import random, randint, choice

CANVAS_W = 1000
CANVAS_H = 1000

screen = turtle.Screen()
screen.setup(CANVAS_W, CANVAS_H)
# screen.bgcolor("#315F9C")
screen.tracer(0)

t = turtle.Turtle()
t.shape('turtle')
t.hideturtle()
t.speed(0)

num_rows = 4
num_cols = 5
start_x = -CANVAS_W / 2
start_y = CANVAS_H / 2




screen.update()
screen.exitonclick()