import turtle
import math
import time

t = turtle.Turtle()
turtle.bgcolor("black")
t.hideturtle()
t.speed(0)
t.penup()

colors = ["#ff0033", "#ff3366", "#ff6699"]

def heart(k, scale):
    x = scale * 16 * math.sin(k) ** 3
    y = scale * (
        13 * math.cos(k)
        - 5 * math.cos(2 * k)
        - 2 * math.cos(3 * k)
        - math.cos(4 * k)
    )
    return x, y

for glow in range(3):
    t.color(colors[glow])
    for i in range(0, 628):
        k = i / 100
        x, y = heart(k, 10 + glow)
        t.goto(x, y)
        t.dot(4 - glow)
    time.sleep(0.3)

turtle.done()
