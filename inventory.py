# script responsible for all inventory classes and interactions excluding gui functions and navigation

import gui as g  # imports necessary modules


class Object:  # class accepted into the player's inventory
    def __init__(self, item, name):
        self.item = item
        self.name = name


class Weapon:  # weapon object class for inventory
    def __init__(self, name, damage, gold):
        self.name = name
        self.damage = damage
        self.gold = gold


class Armour:  # armour object class for inventory
    def __init__(self, name, defence, gold):
        self.name = name
        self.defence = defence
        self.gold = gold


class Consumable:  # consumable object class for inventory. Provides health
    def __init__(self, name, health, gold):
        self.name = name
        self.health = health
        self.gold = gold


class Key:  # key object class for inventory. Opens doors
    def __init__(self, name, code, gold):
        self.name = name
        self.code = code
        self.gold = gold


def AddItem(itemName, p):  # function to add item into inventory
    if len(p.inventory) < 9:
        p.inventory.append(Object(itemName, itemName.name))
    else:  # if inventory is full
        g.Print(f"Inventory full! Can't add \"{itemName.name}\"")


def Use(itemNumber, p):  # uses/equips/consumes item
    itemEquip = p.inventory[itemNumber - 1]
    if isinstance(itemEquip.item, Weapon):  # if item is weapon
        if p.weaponSlot.item.damage <= 0:
            p.weaponSlot = itemEquip
            g.Print("Equipping " + itemEquip.item.name)
            p.GetPlayerStats()
            p.inventory.pop(itemNumber - 1)
        else:  # if there is already a weapon equipped swap it with item being equipped
            wUnequip = p.weaponSlot.item
            p.weaponSlot = itemEquip
            g.Print("Unequipping " + wUnequip.name + " and equipping " + itemEquip.item.name)
            p.GetPlayerStats()
            p.inventory.pop(itemNumber - 1)
            AddItem(wUnequip, p)

    if isinstance(itemEquip.item, Armour):  # if item is armour
        if p.armourSlot.item.defence <= 0:
            p.armourSlot = itemEquip
            g.Print("Wearing " + itemEquip.item.name)
            p.GetPlayerStats()
            p.inventory.pop(itemNumber - 1)
        else:  # if there is already armour equipped swap it with item being equipped
            aUnequip = p.armourSlot.item
            p.armourSlot = itemEquip
            g.Print("Taking off " + aUnequip.name + " and wearing " + itemEquip.item.name)
            p.GetPlayerStats()
            p.inventory.pop(itemNumber - 1)
            AddItem(aUnequip, p)

    if isinstance(itemEquip.item, Consumable):  # if item is consumable
        if p.health == p.maxHealth:  # if health already at max
            g.Print("Health already at max.")
        else:  # if health not at max
            if p.health + itemEquip.item.health > p.maxHealth:
                g.Print(f"Consuming {itemEquip.name}. Health now at max.")
                p.health = p.maxHealth
                p.GetPlayerStats()
                p.inventory.pop(itemNumber - 1)
            else:
                g.Print(f"Consuming {itemEquip.name}. Health now at " + str(p.health + itemEquip.item.health))
                p.health += itemEquip.item.health
                p.GetPlayerStats()
                p.inventory.pop(itemNumber - 1)


def Drop(itemNumber, p):  # drops item
    #g.Print(f"Dropping {p.inventory[itemNumber - 1].name}.")
    p.inventory.pop(itemNumber - 1)
