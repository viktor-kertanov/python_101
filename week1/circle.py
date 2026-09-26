import math
import turtle

screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor("#315F9C")
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.color("#C44743")

angle = 3 * math.pi / 2
radius = 100
print(angle)

sine = round(math.sin(angle),4) #0
cosine = round(math.cos(angle),4) #-1

num_pieces = 12
angle_delta = 2 * math.pi / num_pieces

cur_angle = 0
for my_dot in range(num_pieces):
    dot_y = round(math.sin(cur_angle),4) * radius
    dot_x = round(math.cos(cur_angle),4) * radius
    t.penup()
    t.goto(dot_x, dot_y)
    # t.pendown()
    t.dot(10, 'red')
    cur_angle += angle_delta
    screen.update()




# screen.update()

print("Hello world!")
