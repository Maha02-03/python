import turtle
import math

# Setup
timmy = turtle.Turtle()
timmy.speed(0)

# === Shape Drawing Functions ===

def draw_polygon(sides, length):
    angle = 360 / sides
    for _ in range(sides):
        timmy.forward(length)
        timmy.right(angle)

def draw_square():
    draw_polygon(4, 80)

def draw_triangle():
    draw_polygon(3, 100)

def draw_pentagon():
    draw_polygon(5, 80)

def draw_hexagon():
    draw_polygon(6, 70)

def draw_pentagram():
    for _ in range(5):
        timmy.forward(100)
        timmy.right(144)

def draw_cross():
    for _ in range(4):
        timmy.forward(40)
        timmy.backward(40)
        timmy.right(90)
    timmy.forward(40)
    timmy.backward(80)
    timmy.forward(40)
    timmy.left(90)
    timmy.forward(40)
    timmy.backward(80)

def draw_fan():
    for _ in range(18):
        timmy.forward(80)
        timmy.backward(80)
        timmy.right(20)

def draw_nested_squares():
    for size in range(20, 120, 20):
        draw_polygon(4, size)
        timmy.right(10)

def sierpinski(length, depth):
    if depth == 0:
        for _ in range(3):
            timmy.forward(length)
            timmy.left(120)
    else:
        sierpinski(length / 2, depth - 1)
        timmy.forward(length / 2)
        sierpinski(length / 2, depth - 1)
        timmy.backward(length / 2)
        timmy.left(60)
        timmy.forward(length / 2)
        timmy.right(60)
        sierpinski(length / 2, depth - 1)
        timmy.left(60)
        timmy.backward(length / 2)
        timmy.right(60)

def draw_sierpinski():
    sierpinski(150, 3)

def draw_hexagon_small():
    for _ in range(6):
        timmy.forward(30)
        timmy.right(60)

def draw_honeycomb():
    radius = 35
    positions = [
        (0, 0),
        (radius, 0),
        (-radius, 0),
        (radius / 2, radius * math.sqrt(3) / 2),
        (-radius / 2, radius * math.sqrt(3) / 2),
        (radius / 2, -radius * math.sqrt(3) / 2),
        (-radius / 2, -radius * math.sqrt(3) / 2),
    ]
    for x, y in positions:
        timmy.penup()
        timmy.goto(timmy.xcor() + x, timmy.ycor() + y)
        timmy.pendown()
        draw_hexagon_small()
        timmy.penup()
        timmy.goto(timmy.xcor() - x, timmy.ycor() - y)

# === Drawing Shapes One by One ===

def move(x, y):
    timmy.penup()
    timmy.goto(x, y)
    timmy.setheading(0)
    timmy.pendown()

move(-300, 250)
draw_square()

move(-150, 250)
draw_triangle()

move(0, 250)
draw_pentagon()

move(150, 250)
draw_hexagon()

move(300, 250)
draw_pentagram()

move(-300, 50)
draw_cross()

move(-100, 50)
draw_nested_squares()

move(150, 50)
draw_fan()

move(300, 50)
draw_sierpinski()

move(0, -150)
draw_honeycomb()

# Finish
timmy.hideturtle()
turtle.done()

