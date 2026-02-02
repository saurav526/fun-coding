import turtle

t = turtle.Turtle()
turtle.bgcolor("black")
t.color("red")
t.speed(0)

for i in range(100):
    t.circle(100)
    t.left(20)

t.hideturtle()
turtle.done()
