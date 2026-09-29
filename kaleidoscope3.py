import turtle
import math

WIDTH = 900
HEIGHT = 900

TILE = 32
RINGS = 22
BLACK = "black"

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("white")
screen.title("Black Hypnotic Vortex")
screen.tracer(0, 0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()
t.fillcolor(BLACK)
t.pencolor(BLACK)
t.pensize(1)

variants = [
    [(-0.5, -0.5), (0.5, -0.5), (0.5, 0.5)],
    [(0.5, -0.5), (0.5, 0.5), (-0.5, 0.5)],
    [(0.5, 0.5), (-0.5, 0.5), (-0.5, -0.5)],
    [(-0.5, 0.5), (-0.5, -0.5), (0.5, -0.5)],
]

cells = []

for gx in range(-RINGS, RINGS + 1):
    for gy in range(-RINGS, RINGS + 1):
        r = math.sqrt(gx * gx + gy * gy)
        theta = math.atan2(gy, gx)

        if theta < 0:
            theta += math.tau

        cells.append((gx, gy, r, theta))

frame = 0


def draw_triangle(cx, cy, variant):
    points = variants[variant]

    t.begin_fill()

    t.goto(cx + points[0][0] * TILE, cy + points[0][1] * TILE)
    t.pendown()

    t.goto(cx + points[1][0] * TILE, cy + points[1][1] * TILE)

    t.goto(cx + points[2][0] * TILE, cy + points[2][1] * TILE)

    t.goto(cx + points[0][0] * TILE, cy + points[0][1] * TILE)

    t.penup()
    t.end_fill()


def animate():
    global frame

    t.clear()

    phase = frame * 0.055

    for gx, gy, r, theta in cells:

        x = gx * TILE
        y = gy * TILE

        value = theta * 2.4 + r * 0.58 - phase

        variant = int(value / (math.pi / 2)) % 4

        draw_triangle(x, y, variant)

    screen.update()

    frame += 1
    screen.ontimer(animate, 40)


animate()

screen.onkey(screen.bye, "Escape")
screen.listen()

turtle.done()
