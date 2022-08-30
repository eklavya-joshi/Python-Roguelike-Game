# script responsible for entire gui excluding map

import turtle
import tkinter as tk
import sys
import time
from tkinter import simpledialog  # imports necessary modules

printColumns = 0
printSpeed = 0.025
invNum = 0
isTyping = False
holdList = []  # variables relating to printing text

printTurtle = turtle.Turtle()
printTurtle.screen.bgcolor("black")

statsTurtle = turtle.Turtle()
statsTurtle.hideturtle()
statScreen = statsTurtle.screen
statScreen.tracer(0, 0)
statScreen.listen()  # turtle for printing player stats


def BoxPrint():  # function to print text box
    printTurtle.reset()
    printTurtle.hideturtle()
    printTurtle.speed(0)
    printTurtle.penup()
    printTurtle.setposition(-405, 305)
    printTurtle.color("#FEF3E2")
    printTurtle.pendown()
    printTurtle.begin_fill()
    printTurtle.forward(800)
    printTurtle._rotate(270)
    printTurtle.forward(250)
    printTurtle._rotate(270)
    printTurtle.forward(800)
    printTurtle._rotate(270)
    printTurtle.forward(250)
    printTurtle.end_fill()
    printTurtle.color("black")
    printTurtle.penup()
    printTurtle.setposition(-400, 290)


def StatBox():  # function to print stat box
    statsTurtle.speed(0)
    statsTurtle.color("#FEF3E2")
    statsTurtle.penup()
    statsTurtle.setposition(395, 30)
    statsTurtle.pendown()
    statsTurtle.begin_fill()
    for i in range(0, 4):  # turtle rotates four times
        statsTurtle._rotate(270)
        if i % 2 == 0:
            statsTurtle.forward(360)
        else:
            statsTurtle.forward(300)
    statsTurtle.end_fill()


def StatPrint(health, maxHealth, weapon, damage, armour, defence, level, exp, gold, inv): # function to print player stats
    # statsTurtle.clear()
    StatBox()
    statsTurtle.penup()
    statsTurtle.setposition(245, 0)
    statsTurtle.color("black")
    statsTurtle.write("Player Stats", False, font=("Courier", 16, "bold"), align="center")
    statsTurtle.setposition(120, -30)
    statsTurtle.write("Health:" + str(health) + "/" + str(maxHealth), False, font=("Courier", 11, "normal"),
                      align="left")
    statsTurtle.setposition(120, statsTurtle.ycor() - 15)
    statsTurtle.write("Weapon:" + weapon, False, font=("Courier", 11, "normal"), align="left")
    statsTurtle.setposition(120, statsTurtle.ycor() - 15)
    statsTurtle.write("Damage:" + str(damage), False, font=("Courier", 11, "normal"), align="left")
    statsTurtle.setposition(120, statsTurtle.ycor() - 15)
    statsTurtle.write("Armour:" + armour, False, font=("Courier", 11, "normal"), align="left")
    statsTurtle.setposition(120, statsTurtle.ycor() - 15)
    statsTurtle.write("Defence:" + str(defence), False, font=("Courier", 11, "normal"), align="left")
    statsTurtle.setposition(120, statsTurtle.ycor() - 15)
    statsTurtle.write("Level:" + str(level), False, font=("Courier", 11, "normal"), align="left")
    statsTurtle.setposition(120, statsTurtle.ycor() - 15)
    statsTurtle.write(f"Exp:{exp}/{200 + level * 100}", False, font=("Courier", 11, "normal"), align="left")
    statsTurtle.setposition(120, statsTurtle.ycor() - 15)
    statsTurtle.write("Gold:" + str(gold), False, font=("Courier", 11, "normal"), align="left")

    statsTurtle.setposition(120, -170)  # draws all player stats
    statsTurtle.write("Inventory:", font=("Courier", 12))
    statsTurtle.setposition(120, -190)
    for i in inv:  # draws player inventory
        statsTurtle.write(str(inv.index(i) + 1) + ". " + str(i.name), font=("Courier", 9, "normal"))
        statsTurtle.setposition(statsTurtle.xcor(), statsTurtle.ycor() - 15)


def BattleBox():  # function to print battle warning
    startPos = [statsTurtle.xcor(), statsTurtle.ycor()]
    statsTurtle.penup()
    statsTurtle.setposition(300, -330)
    statsTurtle.color("red")
    statsTurtle.write("!", font=("Courier", 76, "bold"), align="center")
    statsTurtle.setposition(300, -330)
    statsTurtle.write("In Battle", font=("Courier", 16, "bold"), align="center")
    statsTurtle.color("black")
    statsTurtle.setposition(startPos[0], startPos[1])


def Print(text):  # function to print any text required
    global printColumns
    global isTyping
    if isTyping is False:
        x = 0
        if len(holdList) > 0:  # if there is any waiting text print it instead
            print(holdList)
            if text != "a":
                holdList.append(text)
            print("printing held text" + str(x))
            x += 1
            text = holdList[0]
            holdList.pop(0)
        isTyping = True
        i = 0
        if printColumns >= 23:  # if text box has to be cleared
            for letter in "Clearing text......................":
                i += 6.5
                printTurtle.write(letter, False, font=("Courier", 8))
                printTurtle.setposition(-400 + i, printTurtle.ycor())
                time.sleep(0.04)
            printColumns = 1
            BoxPrint()
            i = 0
            for letter in text:
                i += 6.5
                printTurtle.write(letter, False, font=("Courier", 8))
                printTurtle.setposition(-400 + i, printTurtle.ycor())
                time.sleep(printSpeed)
            if len(holdList) > 0:
                Print("a")
        else:  # if text box does not have to be cleared print text on screen
            for letter in text:
                i += 6.5
                printTurtle.write(letter, False, font=("Courier", 8))
                printTurtle.setposition(-400 + i, printTurtle.ycor())
                time.sleep(printSpeed)
            if len(holdList) > 0:
                Print("a")

        printColumns += 1
        printTurtle.penup()
        printTurtle.setposition(-400, printTurtle.ycor() - 10)
        isTyping = False
        if len(holdList) > 0:
            Print("a")
    else:  # if there is excess text put it in waiting list
        holdList.append(text)
        print("held text")


def input():  # function to show input window where player can type a response
    inputWin = tk.Tk()

    inputWin.withdraw()
    uInput = simpledialog.askstring(title="Input Box",  # show window for input
                                    prompt="Type your response")
    inputWin.destroy()
    return uInput


def InvDescription(player, invNum):  # describes inventory
    invItem = player.inventory[invNum]
    statsTurtle.setposition(250, -155)
    statsTurtle.begin_fill()
    for i in range(0, 4):  # draws box to clear description of previous item
        statsTurtle.color("#FEF3E2")
        if i % 2 == 0:
            statsTurtle.forward(130)
        else:
            statsTurtle.forward(60)
        statsTurtle._rotate(270)
    statsTurtle.end_fill()
    statsTurtle.color("black")
    statsTurtle.setposition(260, -170)  # prints item name and stats next to inventory list
    statsTurtle.write(str(invNum + 1) + ". " + invItem.name + ":", font=("Courier", 9))
    statsTurtle.setposition(260, -190)
    if hasattr(invItem.item, "damage"):
        statsTurtle.write("Damage: " + str(invItem.item.damage), font=("Courier", 9))
    elif hasattr(invItem.item, "defence"):
        statsTurtle.write("Defence: " + str(invItem.item.defence), font=("Courier", 9))
    elif hasattr(invItem.item, "health"):
        statsTurtle.write("Health: " + str(invItem.item.health), font=("Courier", 9))
    statsTurtle.setposition(260, statsTurtle.ycor() - 15)
    statsTurtle.write("Value: " + str(invItem.item.gold) + " Gold", font=("Courier", 9))

StatBox()