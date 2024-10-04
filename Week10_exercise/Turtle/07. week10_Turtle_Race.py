from turtle import Turtle, Screen
import random

# Create screen object and set its size
screen = Screen()
screen.setup(width=500, height=400)

# Ask the user for their bet
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# List of colors and starting positions for the turtles
colors = ["red","orange","yellow","green","cyan","blue","purple"]
y_positions = [-100, -60, -20, 20, 60, 100]

# Create AI-controlled turtles and place them at the starting position
turtles = []
for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[i])
    turtles.append(new_turtle)

# Create a user-controlled turtle and set its initial position
user_turtle = Turtle(shape="turtle")
user_turtle.color("black")
user_turtle.penup()
user_turtle.goto(x=-230, y=-150)

# Flag to start the race
is_race_on = False

# Function to move the user-controlled turtle
def move_user_turtle_forward():
    user_turtle.forward(10)

def move_user_turtle_backward():
    user_turtle.backward(10)

def turn_user_turtle_left():
    user_turtle.left(15)

def turn_user_turtle_right():
    user_turtle.right(15)

# Set up key bindings to control the user-controlled turtle
screen.listen()
screen.onkey(move_user_turtle_forward, "w")
screen.onkey(move_user_turtle_backward, "s")
screen.onkey(turn_user_turtle_left, "a")
screen.onkey(turn_user_turtle_right, "d")

if user_bet:
    is_race_on = True

# Start the race
while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            break
        # Move the AI turtles forward by a random distance
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
    
    # Check if the user-controlled turtle has crossed the finish line
    if user_turtle.xcor() > 230:
        is_race_on = False
        print("Congratulations! You've won the race with your turtle!")
        break

# Exit the screen on click
screen.exitonclick()