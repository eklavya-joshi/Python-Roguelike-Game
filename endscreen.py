# Script to show the end screen to the player

import turtle
import time  # imports necessary modules

boxTurtle = turtle.Turtle()
boxScreen = boxTurtle.screen
boxScreen.bgcolor("black")
boxTurtle.color("yellow")
boxScreen.tracer(0, 0)
boxTurtle.setposition(-300, 300)
boxTurtle.begin_fill()
for i in range(4):
    boxTurtle.forward(600)
    boxTurtle._rotate(270)
boxTurtle.end_fill()  # draws end screen box

def MakeBox(horiz, vert):  # makes box depending on arguments
    boxTurtle.pendown()
    boxTurtle.begin_fill()
    for i in range(4):
        if i % 2 == 0:
            boxTurtle.forward(horiz)
        else:
            boxTurtle.forward(vert)
        boxTurtle._rotate(270)
    boxTurtle.end_fill()

textTurtle = turtle.Turtle()
textTurtle.screen.tracer(0, 0)
textTurtle.penup()
textTurtle.setposition(0, 50)
textTurtle.write("Congratulations!", font=("Bahnschrift", 56, "bold"), align="center")
textTurtle.setposition(0, -60)
textTurtle.write("You Beat The Game", font=("Bahnschrift", 48, "bold"), align="center")
textTurtle.setposition(-200, -200)
textTurtle.hideturtle()  # initialises turtle for drawing text

time.sleep(2)
print(boxTurtle.xcor())
print(boxTurtle.ycor())
boxTurtle.penup()
boxTurtle.setposition(-310, 300)
boxTurtle.pendown()
boxScreen.tracer(1, 1)
boxTurtle.speed(10)
boxTurtle.pensize(30)
boxTurtle.color("black")  # spiral effect
spiral = 600
for i in range(80):
    boxTurtle.forward(spiral)
    boxTurtle._rotate(270)
    spiral -= 10
