import turtle
import random
import math
import time

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.penup()
t.speed(0)

# Particle class
class Particle:
    def __init__(self):
        self.x = 0
        self.y = 0
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(2, 6)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        self.life = random.randint(30, 60)
        self.color = random.choice(["red", "orange", "yellow", "cyan", "magenta"])

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy -= 0.1   # gravity
        self.life -= 1

    def draw(self):
        t.goto(self.x, self.y)
        t.dot(4, self.color)

# Create burst
particles = []

def explode():
    for _ in range(120):
        particles.append(Particle())

explode()

# Animation loop
while True:
    t.clear()

    for p in particles[:]:
        p.update()
        p.draw()
        if p.life <= 0:
            particles.remove(p)

    if len(particles) == 0:
        explode()   # new explosion

    screen.update()
    time.sleep(0.02)
