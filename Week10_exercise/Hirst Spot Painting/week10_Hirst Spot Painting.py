import turtle as t
import random

t.colormode(255)
my_turtle = t.Turtle()
my_turtle.speed("fastest")
my_turtle.penup()
my_turtle.hideturtle()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_hirst_painting(dot_count, dot_size, dot_spacing):
    radius = dot_count * dot_spacing / 2
    for y in range(-dot_count // 2, dot_count // 2):
        for x in range(-dot_count // 2, dot_count // 2):
            if (x * dot_spacing)**2 + (y * dot_spacing)**2 <= radius**2:
                my_turtle.goto(x * dot_spacing, y * dot_spacing)
                my_turtle.dot(dot_size, random_color())

draw_hirst_painting(dot_count=20, dot_size=20, dot_spacing=40)

screen = t.Screen()
screen.exitonclick()