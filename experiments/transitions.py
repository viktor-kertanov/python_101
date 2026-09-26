import turtle
from random import random, randint, choice

CANVAS_W = 1000
CANVAS_H = 1000
NUM_STRIPS = 10
ONE_STRIP_WIDTH = CANVAS_W / NUM_STRIPS

screen = turtle.Screen()
screen.setup(CANVAS_W, CANVAS_H)
# screen.bgcolor("#315F9C")
screen.tracer(0)

t = turtle.Turtle()
t.shape('turtle')
t.hideturtle()
t.speed(0)

x_start = - CANVAS_W / 2
y_start = CANVAS_H / 2

# ХОЧУ нарисовать прямоугольник шириной 100 высотой в весь холст
for strip_index in range(NUM_STRIPS):
    # if strip_index % 2 != 0:
    #     continue

    t.penup()
    t.goto(x_start + strip_index * ONE_STRIP_WIDTH, y_start)
    t.pendown()

    color_delta = strip_index / NUM_STRIPS
    t.color(color_delta, color_delta, color_delta)

    t.begin_fill()
    for _ in range(2):
        t.forward(ONE_STRIP_WIDTH)
        t.right(90)
        t.forward(CANVAS_H)
        t.right(90)
    t.end_fill()


screen.update()
screen.exitonclick()