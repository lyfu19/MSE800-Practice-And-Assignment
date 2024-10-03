from turtle import Turtle, Screen

# Create turtle and screen objects
my_turtle = Turtle()
screen = Screen()

# Function for moving forward
def move_forward():
    my_turtle.forward(100)

# Function for moving backward
def move_backward():
    my_turtle.backward(100)

# Function for turning left
def turn_left():
    my_turtle.left(90)

# Function for turning right
def turn_right():
    my_turtle.right(90)

# Function for clearing the screen and resetting the turtle
def clear_screen():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()

# Listen for key presses
screen.listen()

# Map keys to functions
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "q")
screen.onkey(turn_right, "e")
screen.onkey(clear_screen, "c")

# Exit on click
screen.exitonclick()