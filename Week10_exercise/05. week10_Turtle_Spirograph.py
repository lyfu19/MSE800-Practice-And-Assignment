from turtle import Turtle, Screen
import random

my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.speed("fastest")

colors = ["red","orange","yellow","green","cyan","blue","purple","black","grey","brown","pink"]

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        my_turtle.color(random.choice(colors))
        my_turtle.circle(100)
        my_turtle.setheading(my_turtle.heading() + size_of_gap)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()