import turtle
import time

t = turtle.Turtle()
turtle.bgcolor("black")
t.color("white")
t.hideturtle()
t.penup()

for y in range(-100, 100, 5):
    t.clear()
    t.goto(0, y)
    t.write("I love coding ❤️",
            align="center",
            font=("Arial", 20, "bold"))
    time.sleep(0.05)

turtle.done()
