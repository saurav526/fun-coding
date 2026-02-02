# Romantic glowing heart animation 💖

import math
from turtle import *

# Heart equations
def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return (
        12 * math.cos(k)
        - 5 * math.cos(2 * k)
        - 2 * math.cos(3 * k)
        - math.cos(4 * k)
    )

# Screen setup
setup(width=800, height=800)
bgcolor("black")
title("For You ❤️")

speed(0)
hideturtle()
penup()

# Glowing heart effect
colors = ["#ff4d6d", "#ff1c4d", "#ff5c8a"]

for glow in range(3):
    pencolor(colors[glow])
    for i in range(0, 628, 2):   # smoother curve
        k = i / 100
        x = hearta(k) * 20
        y = heartb(k) * 20
        goto(x, y)
        dot(4 - glow)           # glow layers
    time.sleep(0.5)

# Heart fill animation (slow & romantic)
pencolor("red")
for i in range(0, 628):
    k = i / 100
    x = hearta(k) * 20
    y = heartb(k) * 20
    goto(x, y)
    dot(3)
    time.sleep(0.01)

# Text inside heart
goto(0, -20)
color("white")
write("I love you ❤️", align="center", font=("Comic Sans MS", 24, "bold"))

done()
