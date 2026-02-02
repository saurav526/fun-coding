import turtle
import time

t = turtle.Turtle()
turtle.bgcolor("black")
t.color("red")
t.hideturtle()
t.speed(0)

for _ in range(6):
    t.clear()
    t.begin_fill()
    t.circle(80)
    t.end_fill()
    time.sleep(0.4)

    t.clear()
    t.begin_fill()
    t.circle(95)
    t.end_fill()
    time.sleep(0.4)

turtle.done()
