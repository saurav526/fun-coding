import turtle
import math

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
t.color("red")
t.width(2)

for i in range(360):
    x = 16 * math.sin(math.radians(i)) ** 3
    y = (
        13 * math.cos(math.radians(i))
        - 5 * math.cos(2 * math.radians(i))
        - 2 * math.cos(3 * math.radians(i))
        - math.cos(4 * math.radians(i))
    )
    t.goto(x * 10, y * 10)

t.hideturtle()
turtle.done()
