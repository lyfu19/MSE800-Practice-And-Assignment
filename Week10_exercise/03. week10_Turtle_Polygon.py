from turtle import Turtle, Screen
import random

my_turtle = Turtle()
my_turtle.shape("turtle")

colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple", "black", "grey", "brown", "pink"]

def draw_polygon(sides):
    angle = 360 / sides
    my_turtle.color(random.choice(colors))
    for _ in range(sides):
        my_turtle.forward(100)
        my_turtle.right(angle)

for sides in range(3, 11):
    draw_polygon(sides)

screen = Screen()
screen.exitonclick()
