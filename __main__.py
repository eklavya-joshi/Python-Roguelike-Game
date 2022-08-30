#  main script for game

import titlescreen
import time
time.sleep(1)
import gui as g
import inventory as inv
import playerinfo as ps
import items as items
import text
import map as m
import actions as act
import mapturts  # imports necessary modules

frame = 1
invNum = 0
ps.ClassItems(ps.player)  # gives player class items

def InvDescribe():  # shows inventory in gui
    if len(ps.player.inventory) > 0:
        g.InvDescription(ps.player, invNum)


def InvNumUp():  # goes up in inventory
    global invNum
    if invNum <= len(ps.player.inventory) - 2:
        invNum += 1
        InvDescribe()
    else:  # if player has reached the end of their inventory
        g.Print("You have reached the end of your inventory!")
        InvDescribe()


def InvNumDown():  # goes down in inventory
    global invNum
    if invNum > 0:
        invNum -= 1
        InvDescribe()
    else:  # if player has reached the start of their inventory
        g.Print("Can't go any further back in your inventory!")
        InvDescribe()


def PlayerUse():  # once called the selected item in the inventory will be used
    global invNum
    inv.Use(invNum + 1, ps.player)
    g.StatBox()
    g.StatPrint(ps.player.health, ps.player.maxHealth, ps.player.weaponSlot.name, ps.player.wDamage, ps.player.armourSlot.name,
                ps.player.defence, ps.player.level, ps.player.exp, ps.player.gold, ps.player.inventory)
    invNum = len(ps.player.inventory) - 1
    InvDescribe()
    if ps.player.battle is True:  # if player is in battle and uses an item, takes up player's turn
        g.Print(f"{ps.player.name} uses an item, taking up their turn!")
        act.TakeTurns(act.currentEnemy, ps.player, act.currentEnemy)


def PlayerDrop():  # once called the selected item in the inventory will be dropped
    global invNum
    print(invNum)
    m.DroppedObjTurtle(ps.player.inventory[invNum].item, m.pTurt)
    inv.Drop(invNum + 1, ps.player)
    g.StatBox()
    g.StatPrint(ps.player.health, ps.player.maxHealth, ps.player.weaponSlot.name, ps.player.wDamage, ps.player.armourSlot.name,
                ps.player.defence, ps.player.level, ps.player.exp, ps.player.gold, ps.player.inventory)
    invNum = 0
    InvDescribe()


def StartInput():  # called to start sensing for input related to inventory
    g.statScreen.listen()
    g.statScreen.onkey(fun=InvNumDown, key="Up")
    g.statScreen.onkey(fun=InvNumUp, key="Down")
    g.statScreen.onkey(fun=PlayerUse, key="o")
    g.statScreen.onkey(fun=PlayerDrop, key="p")
    g.statScreen.onkey(fun=text.InfoPrint, key="y")
    m.AttackInput()


m.pScreen.listen()  # input for moving around map
m.pScreen.onkeypress(m.MoveUp, "w")
m.pScreen.onkeypress(m.MoveDown, "s")
m.pScreen.onkeypress(m.MoveLeft, "a")
m.pScreen.onkeypress(m.MoveRight, "d")
StartInput()
ps.player.GetPlayerStats()
text.InfoPrint()
inv.AddItem(items.apple, ps.player)
inv.AddItem(items.banana, ps.player)  # adds some consumables to the player's inventory

while True:  # main loop. Runs for duration of game
    ps.player.GetPlayerStats()
    g.statScreen.update()
    g.printTurtle.screen.update()
    InvDescribe()
    m.MoveUp()
    m.pScreen.mainloop()
    g.statScreen.mainloop()
