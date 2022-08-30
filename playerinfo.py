# script responsible for all player variables and player customisation

import gui as g
import inventory as inv
import items
import text
import time  # imports necessary modules

classList = ["Rogue", "Knight", "Paladin"]
classNumber = 0
playerClass = ""
classInput = ""  # variables used to assign the player a class


class Player:  # player class. Includes all player stats such as health, armour, experience, etc.
    def __init__(self, name, health, maxHealth, wDamage, defence, inventory, weaponSlot, armourSlot, level, exp, gold, battle):
        self.name = name
        self.health = health
        self.maxHealth = maxHealth
        self.wDamage = wDamage
        self.defence = defence
        self.inventory = inventory
        self.weaponSlot = weaponSlot
        self.armourSlot = armourSlot
        self.level = level
        self.exp = exp
        self.gold = gold
        self.battle = battle

    def GetPlayerStats(self):  # calculates player stats
        self.wDamage = self.weaponSlot.item.damage
        self.defence = self.armourSlot.item.defence
        g.StatPrint(self.health, self.maxHealth, self.weaponSlot.name, self.wDamage,
                    self.armourSlot.name,
                    self.defence, self.level, self.exp, self.gold, self.inventory)
        if self.exp >= 200 + self.level * 100:  # if player can level up
            self.exp -= (200 + self.level * 100)
            self.level += 1
            self.health += 30
            self.maxHealth += 30
            g.Print(f"You have levelled up to level {self.level}!")

    def PrintInventory(self):  # prints player's inventory
        for i in self.inventory:
            g.Print(str(self.inventory.index(i) + 1) + ".", i.name)


def PlayerName():  # function to ask player for their name
    g.Print("What is your name?")
    name = g.input()
    g.Print(f"{name}? What a lovely name!")
    return name


def PlayerClass():  # function to determine the player's class
    global playerClass
    global classNumber
    global classInput
    g.Print("Classes:")
    for i in classList:  # prints classes
        g.Print(str(classList.index(i) + 1) + ". " + i)
    g.Print("Pick your class(type the class number eg. \"2\" for Knight):")
    classInput = g.input()
    if classInput.isdigit() and int(classInput) < len(classList) + 1:  # if input is valid
        playerClass = classList[int(classInput) - 1]
    else:  # if input is invalid
        g.Print("Please type a valid response")
        classInput = ""
        PlayerClass()
    g.Print("You have chosen " + playerClass)
    playerClass = playerClass.lower()
    classNumber = int(classInput) - 1


def MakePlayer(pInventory, weaponSlot, armourSlot):  # function to make the player according to class
    pName = PlayerName()
    PlayerClass()
    rogue = Player(pName, 150, 150, 0, 0, pInventory, weaponSlot, armourSlot, 1, 0, 0, False)
    knight = Player(pName, 200, 200, 0, 0, pInventory, weaponSlot, armourSlot, 1, 0, 0, False)
    paladin = Player(pName, 250, 250, 0, 0, pInventory, weaponSlot, armourSlot, 1, 0, 0, False)
    pList = [rogue, knight, paladin]
    return pList[classNumber]


def ClassItems(player):  # function to give the player their classes' items
    if player.maxHealth == 150:
        inv.AddItem(items.blade, player)
        inv.AddItem(items.clothArmour, player)
        inv.Use(1, player)
        inv.Use(1, player)
    elif player.maxHealth == 200:
        inv.AddItem(items.longSword, player)
        inv.AddItem(items.leatherArmour, player)
        inv.Use(1, player)
        inv.Use(1, player)
    else:
        inv.AddItem(items.hammer, player)
        inv.AddItem(items.metalArmour, player)
        inv.Use(1, player)
        inv.Use(1, player)

g.BoxPrint()
text.Language()
time.sleep(1)
text.Intro()
time.sleep(1)
pNothing = inv.Object(inv.Weapon("Nothing", 0, 0), "Nothing")
aNothing = inv.Object(inv.Armour("Nothing", 0, 0), "Nothing")
weaponSlot = pNothing
armourSlot = aNothing
inventory = []
health = 20
maxHealth = 20
wDamage = None
defence = 0
player = MakePlayer(inventory, weaponSlot, armourSlot)
time.sleep(1)
