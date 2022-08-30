# script responsible for drawing map and all player interactions with the map

import turtle, os
from turtle import *
import text
import time
import gui as g
import inventory as inv
import playerinfo as ps
import items
import actions as act
import npc  # imports necessary modules

mapList = []
objList = []
enemyList = []
npcList = []
doorList = []
droppedObjListTurtle = []
droppedObjList = []  # puts map objects into their lists
activeEnemy = None
activeTurt = None
activeNPC = None
lastMove = None  # variables for determining state of the player

pTurtle = turtle.Turtle()
pScreen = pTurtle.screen  # player turtle


class Rectangle():  # rectangle class. Every object on the map is this class
    def __init__(self, minX, maxX, minY, maxY, type, obj):
        self.minX = minX
        self.minY = minY
        self.maxX = maxX
        self.maxY = maxY
        self.type = type
        self.obj = obj

        if self.type == "player":  # if object is type player
            self.turt = pTurtle
            pTurtle.penup()
            pTurtle.setheading(90)
            pTurtle.color("DodgerBlue2")
            pScreen.tracer(0, 0)
        else:
            self.turt = turtle.Turtle()
        if self.type == "map":  # if object is type map
            mapList.append(self)
            self.turt.screen.tracer(0, 0)
            self.turt.speed(0)
            self.turt.color("#FEF3E2")
        elif self.type == "obj":  # if object is type object for inventory
            objList.append(self)
            self.turt.screen.tracer(0, 0)
            self.turt.speed(0)
            self.turt.color("#29B330")
        elif self.type == "enemy":  # if object is type enemy
            enemyList.append(self)
            self.turt.screen.tracer(0, 0)
            self.turt.speed(0)
            self.turt.color("red")
        elif self.type == "npc":  # if object is type npc
            npcList.append(self)
            self.turt.screen.tracer(0, 0)
            self.turt.speed(0)
            self.turt.color("HotPink1")
        elif self.type == "door":  # if object is type door
            doorList.append(self)
            self.turt.screen.tracer(0, 0)
            self.turt.speed(0)
            self.turt.color("brown")
        self.MakeRect()
        self.turt.hideturtle()

    def MakeRect(self):  # function to make rectangle with turtle
        if self.maxX < 90 and self.maxY < 50:
            self.turt.penup()
            self.turt.setposition(self.minX, self.minY)
            self.turt.pendown()
            self.turt.begin_fill()
            self.turt.pendown()
            self.turt.setposition(self.minX, self.maxY)
            self.turt.setposition(self.maxX, self.maxY)
            self.turt.setposition(self.maxX, self.minY)
            self.turt.end_fill()
            # mRoomTurtle.reset()
            self.turt.penup()

    def CheckIntersect(self, other):  # function to check if object is colliding with other rectangle
        if self.minX > other.maxX or self.maxX < other.minX:
            return False
        if self.minY > other.maxY or self.maxY < other.minY:
            return False
        return True

    def CheckEnemyIntersect(self, other):  # function to check if object is near enemy
        if self.minX > other.maxX + 10 or self.maxX < other.minX - 10:
            return False
        if self.minY > other.maxY + 10 or self.maxY < other.minY - 10:
            return False
        return True



pTurt = Rectangle(-200, -195, -200, -195, "player", None)
pTurt.MakeRect()  # draws player turtle


def KeepInMap():  # keeps player in map if trying to leave. Also calls other functions to check for any type of collision
    CheckEnemyCollision()
    CheckItemCollision()
    CheckNPCCollision()
    CheckDoorCollision()
    if CheckMapCollision() == False:
        DoLastMove()


def CheckMapCollision():  # checks if player is still in map
    for i in mapList:
        if i.CheckIntersect(pTurt):
            return True
    return False


def CheckItemCollision():  # checks if player has walked on top of an item
    addedItem = False
    for i in objList:
        if i.CheckIntersect(pTurt):  # if player is intersecting item
            i.turt.reset()
            i.minX = 10000
            i.maxX = 10000
            i.minY = 10000
            i.maxY = 10000
            if addedItem is False:  # add item to inventory
                inv.AddItem(i.obj, ps.player)
                ps.player.GetPlayerStats()
                objList.remove(i)
                addedItem = True


def CheckEnemyCollision():  # checks if player is near an enemy
    global activeTurt
    for i in enemyList:
        if i.CheckEnemyIntersect(pTurt):  # if enemy is near player start battle
            activeTurt = i
            i.obj.battle = True
            g.BattleBox()
            StartBattle(i.obj)


def CheckNPCCollision():  # checks if player has walked over an npc
    global activeNPC
    for i in npcList:
        if i.CheckIntersect(pTurt) and i.obj.active is False:  # if colliding with npc start dialogue
            ps.player.GetPlayerStats()
            activeNPC = i
            ps.player.battle = True
            print("collided with npc")
            i.obj.active = True
            npc.NPCDialogue(i.obj)


def CheckDoorCollision():  # checks if player has walked over a door
    unlocked = False
    for i in doorList:
        if i.CheckIntersect(pTurt):
            for x in ps.inventory:  # check if player has key to door
                if hasattr(x.item, "code") and x.item.name == i.obj.name:
                    inv.Drop(ps.player.inventory.index(x) + 1, ps.player)
                    unlocked = True
            if unlocked:  # if player has key open door
                g.printSpeed = 0
                if i.obj == items.exitKey:  # if door is final door show end screen
                    import endscreen
                i.turt.reset()
                doorList.remove(i)
                g.Print("You opened the door with the chamber key, using it up.")
                g.Print("Welcome to the next chamber!")
                g.printSpeed = 0.025
                ps.player.GetPlayerStats()
                g.StatPrint(ps.player.health, ps.player.maxHealth, ps.player.weaponSlot.name, ps.player.wDamage,
                            ps.player.armourSlot.name,
                            ps.player.defence, ps.player.level, ps.player.exp, ps.player.gold, ps.player.inventory)
                unlocked = False
            else:
                DoLastMove()


def DoLastMove():  # does opposite move to player. Used to keep the player in the map
    if lastMove == "up":
        MoveDown()
    elif lastMove == "down":
        MoveUp()
    elif lastMove == "left":
        MoveRight()
    elif lastMove == "right":
        MoveLeft()


def MoveMap(x, y):  # moves all objects in the map in the opposite direction of player. Gives effect of movement
    for i in mapList:
        i.minX += x
        i.maxX += x
        i.minY += y
        i.maxY += y
        i.turt.clear()
        i.MakeRect()  # moves map objects
    for i in objList:
        i.minX += x
        i.maxX += x
        i.minY += y
        i.maxY += y
        i.turt.clear()
        i.MakeRect()  # moves object objects
    for i in enemyList:
        i.minX += x
        i.maxX += x
        i.minY += y
        i.maxY += y
        i.turt.clear()
        i.MakeRect()  # moves enemy objects
    for i in npcList:
        i.minX += x
        i.maxX += x
        i.minY += y
        i.maxY += y
        i.turt.clear()
        i.MakeRect()  # moves npc objects
    for i in doorList:
        i.minX += x
        i.maxX += x
        i.minY += y
        i.maxY += y
        i.turt.clear()
        i.MakeRect()  # moves door objects


def MoveUp():  # moves player up in map
    if ps.player.battle is False:
        global lastMove
        MoveMap(0, -2)
        pTurtle.clear()
        pTurt.maxY += 0#.5
        pTurt.minY += 0#.5
        pTurt.MakeRect()
        lastMove = "up"
        KeepInMap()


def MoveDown():  # moves player down in map
    if ps.player.battle is False:
        global lastMove
        MoveMap(0, 2)
        pTurtle.clear()
        pTurt.maxY -= 0#.5
        pTurt.minY -= 0#.5
        pTurt.MakeRect()
        lastMove = "down"
        KeepInMap()


def MoveLeft():  # moves player left in map
    if ps.player.battle is False:
        global lastMove
        MoveMap(2, 0)
        pTurtle.clear()
        pTurt.maxX -= 0#.5
        pTurt.minX -= 0#.5
        pTurt.MakeRect()
        lastMove = "left"
        KeepInMap()


def MoveRight():  # moves player right in map
    if ps.player.battle is False:
        global lastMove
        MoveMap(-2, 0)
        pTurtle.clear()
        pTurt.maxX += 0#.5
        pTurt.minX += 0#.5
        pTurt.MakeRect()
        lastMove = "right"
        KeepInMap()


def DroppedObjTurtle(item, turt):  # places item in map if player drops it
    droppedObjListTurtle.append(turtle.Turtle())
    droppedObjList.append(Rectangle(turt.turt.xcor() + 2, turt.turt.xcor() + 7, turt.turt.ycor() + 2, turt.turt.ycor() + 7,
                                    "obj", item))

def StartBattle(enemy):  # starts battle with an enemy
    global activeEnemy
    print("in enemy vicinity")
    activeEnemy = enemy
    ps.player.battle = True
    act.currentEnemy = enemy
    act.Fight(enemy, ps.player)


def KillEnemy():  # destroys enemy if enemy health is 0
    global activeEnemy
    for i in enemyList:
        if act.currentEnemy.health <= 0 and act.currentEnemy is not None:
            g.Print(f"The {act.currentEnemy.name} dropped {act.currentEnemy.dropItem.name}!")
            DroppedObjTurtle(act.currentEnemy.dropItem, activeTurt)
            ps.player.battle = False
            ps.player.exp += act.currentEnemy.exp
            ps.player.gold += act.currentEnemy.gold
            activeTurt.turt.clear()
            activeTurt.turt.reset()
            enemyList.remove(activeTurt)
            ps.player.GetPlayerStats()
            g.StatBox()
            g.StatPrint(ps.player.health, ps.player.maxHealth, ps.player.weaponSlot.name, ps.player.wDamage,
                        ps.player.armourSlot.name,
                        ps.player.defence, ps.player.level, ps.player.exp, ps.player.gold, ps.player.inventory)
            activeEnemy = None
            act.currentEnemy = None

def ExitNPC():  # exits dialogue with npc
    global activeNPC
    activeNPC.obj.active = False
    ps.player.GetPlayerStats()
    pTurt.minX = activeNPC.minX - 7
    pTurt.maxX = activeNPC.maxX - 7
    pTurt.minY = activeNPC.minY - 7
    pTurt.maxY = activeNPC.maxY - 7
    activeNPC = None
    ps.player.battle = False
    pScreen.listen()
    g.statScreen.listen()


def AttackM():  # calls attack function
    act.Attack()
    KillEnemy()


def AttackInput():  # listens for player input to call attack function
    pTurtle.screen.listen()
    pTurtle.screen.onkeypress(AttackM, "k")
