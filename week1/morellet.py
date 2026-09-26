import turtle
from random import random, randint, choice

colors = [['red', 'orange', 'yellow'], 'green', 'blue', 'gold', 'black']

for index in range(10):
    # random_number = random() #генерация от 0 до 1
    random_number = randint(13, 379)
    random_paragraph = randint(1, 5)
    random_color = choice(colors)
    print(f"""
Генерация номер {index}.
Наше случайная страница: {random_number}. 
Абзац: {random_paragraph}.
Случайный цвет: {random_color}.
""")

print('---'*10)

# Настраиваем окно черепахи
screen = turtle.Screen()
screen.setup(1000, 1000)
screen.bgcolor("#315F9C")
screen.tracer(0)

# Настраиваем черепаху
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.color("#C44743")

size = 5

for row in range(200):
    for col in range(200):
        x = -500 + col * size
        y = 500 - row * size

        if random() < 0.7:
            t.penup()
            t.goto(x, y)
            t.pendown()

            t.begin_fill()

            for _ in range(4):
                t.forward(size)
                t.right(90)

            t.end_fill()

        # screen.update()

screen.update()
screen.exitonclick()


print("Hello world")

