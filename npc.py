# script responsible for all npc interactions excluding gui related interactions such as in the map

import inventory as inv
import gui as g
import playerinfo as ps
import map as m  # imports necessary modules


class npc:  # npc class. NPCs can trade with the player and are essential for progression between chambers
    def __init__(self, name, inventory, gold, active):
        self.name = name
        self.inventory = inventory
        self.gold = gold
        self.active = active


def NPCDialogue(npc):  # npc dialogue. Called when player walks over npc in the map
    if npc.active is True:
        g.Print(f"Hi! I'm {npc.name}! I'm selling some things you might want to buy:")
        x = 0
        for i in npc.inventory:  # print npc inventory
            g.Print(str(x + 1) + ". " + i.name + " for " + str(i.gold) + " gold.")
            x += 1
        buyQuestion = BuyQuestion()  # ask player if they want to buy something
        if buyQuestion:
            BuyInput(npc)
        else:
            g.Print("You have chosen not to buy anything.")
        sellQuestion = SellQuestion()  # ask player if they want to sell something
        if sellQuestion:
            SellInput(npc)
        else:
            g.Print("You have chosen not to sell anything.")
        Recheck(npc)
        m.ExitNPC()


def BuyInput(npc):  # function checks what the player wants to buy and gives it to them if they can accept it
    g.Print("If you want to buy anything, type its number in the box(eg. \"1.\" for sword):")
    g.Print("if you have chosen not to buy anything, type \"no\" in lowercase.")
    buyInput = g.input()
    if buyInput.isdigit() and int(buyInput) < len(npc.inventory) + 1:  # check if player response is valid
        buyItem = npc.inventory[int(buyInput) - 1]
        if ps.player.gold < buyItem.gold:  # if item is too expensive for player
            g.Print("That item is too expensive for you to buy.")
            BuyQuestion()
        elif len(ps.player.inventory) < 9:  # if player can buy
            g.Print(f"You bought {buyItem.name}!")
            npc.inventory.pop(int(buyInput) - 1)
            ps.player.gold -= buyItem.gold
            npc.gold += buyItem.gold
            inv.AddItem(buyItem, ps.player)
            ps.player.GetPlayerStats()
            g.StatPrint(ps.player.health, ps.player.maxHealth, ps.player.weaponSlot.name, ps.player.wDamage,
                        ps.player.armourSlot.name,
                        ps.player.defence, ps.player.level, ps.player.exp, ps.player.gold, ps.player.inventory)
        else:  # if player inventory is too big
            g.Print("You have too many items in your inventory. Drop some by exiting this dialogue and pressing \"o\".")
    elif buyInput == "no":  # check if player does not want to buy anything
        g.Print("You have chosen not to buy anything.")
    else:
        g.Print("Invalid input. Please type a valid response.")
        BuyInput(npc)


def BuyQuestion():  # function asks the player if they want to buy anything
    g.Print("If you want to buy something type \"yes\" in lowercase. If not, type \"no\" in lowercase.")
    qInput = g.input()
    if qInput == "yes":  # check player input
        return True
    elif qInput == "no":
        return False
    else:
        g.Print("Invalid input. Please type a valid response.")
        BuyQuestion()


def SellQuestion():  # function asks the player if they want to sell anything
    g.Print("Do you have anything that you would like me to buy?")
    g.Print("If you want to sell something type \"yes\" in lowercase. If not, type \"no\" in lowercase.")
    qInput = g.input()
    if qInput == "yes":  # check player input
        return True
    elif qInput == "no":
        return False
    else:
        SellQuestion()


def SellInput(npc):  # function asks the player what they want to sell if the npc can accept it
    g.Print("Type in the number in your inventory of the item that you would like to sell(e.g. \"3\" for Goblin Dust)")
    g.Print("If you have changed your mind, type \"no\" in lowercase.")
    sellInput = g.input()
    if sellInput.isdigit() and int(sellInput) < len(ps.player.inventory) + 1:  # check if player response is valid
        buyItem = ps.player.inventory[int(sellInput) - 1]
        if npc.gold < buyItem.item.gold:  # if npc does not have enough gold
            g.Print("That item is too expensive for me to buy.")
            SellQuestion()
        else:  # if npc can purchase item
            g.Print(f"You sold {buyItem.name}!")
            npc.inventory.append(buyItem.item)
            npc.gold -= buyItem.item.gold
            ps.player.gold += buyItem.item.gold
            inv.Drop(int(sellInput), ps.player)
            ps.player.GetPlayerStats()
            g.StatPrint(ps.player.health, ps.player.maxHealth, ps.player.weaponSlot.name, ps.player.wDamage,
                        ps.player.armourSlot.name,
                        ps.player.defence, ps.player.level, ps.player.exp, ps.player.gold, ps.player.inventory)

    elif sellInput == "no":
        g.Print("You have chosen not to sell anything.")
    else:
        g.Print("Invalid input. Please type a valid response.")
        SellInput(npc)

def Recheck(npc):  # checks if the player has any more business with the npc. If yes, calls NPCDialogue function again
    g.Print("Thanks for doing business with me! If you forgot to so something or have more business,")
    g.Print("type \"yes\". If you don't have any business left, type \"no\".")
    rInput = g.input()
    if rInput == "yes":  # if player wants to continue business
        NPCDialogue(npc)
    elif rInput == "no":  # if player does not want to continue business
        g.Print("Thanks for doing business with me!")
        return
    else:  # if response is invalid
        g.Print("Invalid input. Please type a valid response.")
        Recheck(npc)