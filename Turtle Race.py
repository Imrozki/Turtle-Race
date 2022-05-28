import random
from turtle import Turtle, Screen


screen = Screen()
is_race_on = False
# screen.setup helps to set up the width and height of the screen
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color:")

y_positions = [-150, -100, -50, 0, 50, 100]
colors = ["red", "yellow", "blue", "green", "orange", "purple"]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

# This if statement makes the compiler to wait until user bets and prevent the code starting prematurely
if user_bet:
    is_race_on = True

while is_race_on == True:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
              print(f"You won! The {winning_color} turtle is the winning one!")
            else:
              print("You lost!")


        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

    




screen.exitonclick()
