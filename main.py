import random
import turtle


def set_direction(direction, step):
    if direction == "North":
        turtle.setheading(90)
    elif direction == "East":
        turtle.setheading(0)
    elif direction == "South":
        turtle.setheading(270)
    elif direction == "West":
        turtle.setheading(180)
    turtle.forward(1 * step)


def move(rounds, steps):
    nesw = ["North", "East", "South", "West"]
    for i in range(0, rounds):
        set_direction(random.choice(nesw), steps)


def reset_pos():
    turtle.penup()
    turtle.setposition(0, 0)
    turtle.pendown()


# variables
paRounds = 10
paSteps = 10
maRounds = 50
maSteps = 5

# pa
move(paRounds, paSteps)

# ma
reset_pos()  # reset position
turtle.color("red")
move(maRounds, maSteps)

# pause
wait = input("PRESS ENTER TO CONTINUE.")