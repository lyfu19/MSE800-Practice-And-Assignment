from turtle import Turtle, Screen
import random

my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.pensize(10)
my_turtle.speed("fast") 

colors = ["red","orange","yellow","green","cyan","blue","purple","black","grey","brown","pink"]

def random_walk(steps):
    for _ in range(steps):
        my_turtle.color(random.choice(colors))
        my_turtle.forward(50)
        my_turtle.setheading(random.choice([0, 90, 180, 270]))

random_walk(50)

screen = Screen()
screen.exitonclick()