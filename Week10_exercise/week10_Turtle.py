from turtle import Turtle, Screen
import random

my_turtle = Turtle()
my_turtle.shape("turtle")

colors = ["red","orange","yellow","green","cyan","blue","purple","black","grey","brown","pink"]

def draw_polygon(sides):
    angle = 360 / sides
    my_turtle.color(random.choice(colors))
    for _ in range(sides):
        my_turtle.forward(100)
        my_turtle.right(angle)

draw_polygon(3)
draw_polygon(4)
draw_polygon(5)
draw_polygon(6)
draw_polygon(7)
draw_polygon(8)
draw_polygon(9)
draw_polygon(10)

screen = Screen()
screen.exitonclick()