import turtle

# Setup screen
screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("black")

# Create turtle
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

# Draw filled circle with black outline
def draw_circle(radius, fill_color):
    pen.penup()
    pen.goto(0, -radius)
    pen.setheading(0)
    pen.pendown()
    pen.color("black", fill_color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

# Draw petal shape with black outline
def draw_petal(radius, angle, fill_color):
    pen.color("black", fill_color)
    pen.begin_fill()
    pen.circle(radius, angle)
    pen.left(180 - angle)
    pen.circle(radius, angle)
    pen.end_fill()
    pen.left(180 - angle)

# Draw flower with outlined petals
def draw_flower(petals, radius, angle, fill_color):
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(0)
    pen.pendown()
    for _ in range(petals):
        draw_petal(radius, angle, fill_color)
        pen.left(360 / petals)

# Draw radial dots with black outline
def draw_dot_ring(count, distance, size, colors):
    for i in range(count):
        pen.penup()
        pen.goto(0, 0)
        pen.setheading(i * (360 / count))
        pen.forward(distance)
        pen.pendown()
        pen.color("black", colors[i % len(colors)])
        pen.begin_fill()
        pen.circle(size)
        pen.end_fill()

# Draw diamonds with black outline
def draw_diamond_ring(count, distance, size, fill_color):
    for i in range(count):
        pen.penup()
        pen.goto(0, 0)
        pen.setheading(i * (360 / count))
        pen.forward(distance)
        pen.setheading(i * (360 / count))
        pen.pendown()
        pen.color("black", fill_color)
        pen.begin_fill()
        for _ in range(4):
            pen.forward(size)
            pen.left(90)
        pen.end_fill()

# Main Pookalam
def draw_pookalam():
    draw_circle(300, "#4B0082")
    draw_circle(280, "#8B4513")
    draw_circle(260, "#FFD700")
    draw_circle(240, "#8B0000")

    draw_flower(12, 280, 60, "#FF4500")
    draw_flower(12, 240, 60, "#FFFF00")

    draw_circle(200, "#006400")
    draw_circle(180, "#FF564F")

    draw_diamond_ring(12, 180, 20, "#9F6347")

    draw_flower(8, 180, 60, "#1F6700")
    draw_flower(8, 120, 60, "#6FD700")

    draw_dot_ring(36, 120, 10, ["yellow", "orange"])

    draw_circle(30, "#4B0082")
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.dot(20, "gold")

draw_pookalam()
turtle.done()