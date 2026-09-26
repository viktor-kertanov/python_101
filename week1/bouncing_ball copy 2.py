"""
10. Прыгающий мяч — первая анимация (
- анимация = один и тот же кадр много раз подряд: сдвинуть, показать, подождать;
- скорость — это два числа, «сколько прибавлять к x и к y за кадр»;
  храним их в списке velocity = [4, 3];
- if x > LIMIT or x < -LIMIT: скорость по x меняет знак — это и есть отскок;
- and: мяч краснеет, когда он И справа от центра, И выше центра.
"""
import turtle

screen = turtle.Screen()
screen.setup(600, 600)
screen.title("10: прыгающий мяч")
screen.tracer(0)   # кадры показываем сами, через screen.update()

ball = turtle.Turtle()
ball.shape("circle")
ball.shapesize(2)   # стандартный кружок 20 px -> 40 px
ball.color("dodgerblue")
ball.penup()

LIMIT = 260   # где стенки
velocity = [4, 3]   # скорость по x и по y, пикселей за кадр


def frame():
    x, y = ball.position()
    x = x + velocity[0]
    y = y + velocity[1]

    if x > LIMIT or x < -LIMIT:  # ударились о левую или правую стенку
        velocity[0] = -velocity[0]
    if y > LIMIT or y < -LIMIT:  # о верх или низ
        velocity[1] = -velocity[1]

    if x > 0 and y > 0:   # правая верхняя четверть — особая зона
        ball.color("tomato")
    else:
        ball.color("dodgerblue")

    ball.goto(x, y)
    screen.update()   # показать кадр
    screen.ontimer(frame, 16)   # через 16 мс — следующий кадр (~60 кадров/с)


frame()
# Попробуй: velocity = [7, 2];
# ball.pendown() перед frame() — мяч оставит след.
screen.mainloop()
