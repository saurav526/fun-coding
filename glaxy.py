import turtle
import colorsys

t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)
t.width(2)

h = 0
for i in range(300):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    h += 0.01
    t.color(c)
    t.forward(i * 0.5)
    t.right(59)

t.hideturtle()
turtle.done()
