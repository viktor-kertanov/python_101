import turtle

#Настраиваем экран
screen = turtle.Screen()
screen.setup(600,600)
screen.title("Прыгающий мяч")
screen.tracer(0)


ball = turtle.Turtle()
ball.shape("circle")
ball.shapesize(2)
ball.color("blue")
ball.penup()


LIMIT = 260
velocity = [4, 3]

def central_university():
    x, y = ball.position()
    x = x + velocity[0]
    y = y + velocity[1]

    if x > LIMIT or x < -LIMIT:
        velocity[0] = -velocity[0]
    if y > LIMIT or y < -LIMIT:
        velocity[1] = -velocity[1]

    ball.goto(x, y)
    screen.update()
    screen.ontimer(central_university, 1000)


central_university()
screen.mainloop()






