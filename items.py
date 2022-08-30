# script responsible for initialising all items

import inventory as inv
import actions as act
import npc  # imports necessary modules

longSword = inv.Weapon("Longsword", 50, 400)
blade = inv.Weapon("Blade", 70, 500)
hammer = inv.Weapon("Hammer", 30, 300)
taser = inv.Weapon("Taser", 90, 700)
waterGun = inv.Weapon("Weapon Gun", 130, 900)
swissArmyKnife = inv.Weapon("Sws. Army Knife", 200, 1500)  # weapon items

clothArmour = inv.Armour("Cloth Armour", 7, 300)
leatherArmour = inv.Armour("Leather Armour", 10, 400)
metalArmour = inv.Armour("Metal Armour", 13, 500)
germanArmour = inv.Armour("German Armour", 20, 700)
enchantedArmour = inv.Armour("Enchanted Armour", 30, 900)
militaryArmour = inv.Armour("Military Armour", 50, 1500)  # armour items

apple = inv.Consumable("Apple", 20, 20)
banana = inv.Consumable("Banana", 30, 30)
orange = inv.Consumable("Orange", 40, 40)
starfruit = inv.Consumable("Starfruit", 60, 60)
healthPotion = inv.Consumable("Health Potion", 100, 100)  # consumable items

level2Key = inv.Key("Level 2 Key", "2", 45)
level3Key = inv.Key("Level 3 Key", "3", 150)
level4Key = inv.Key("Level 4 Key", "4", 400)
exitKey = inv.Key("Exit Key", "5", 1000)  # key items

ratHair = inv.Consumable("Rat Hair", -5, 5)
goblinDust = inv.Consumable("Goblin Dust", 30, 30)
brain = inv.Consumable("Half A Brain", 60, 60)
taxReturns = inv.Consumable("Tax Returns", 0, 200)
meseeksBox = inv.Consumable("Meseeks Box", 150, 150)
weirdJuice = inv.Consumable("Weird Juice", 200, 200)  # enemy dropped consumable items

giantRat = act.Enemy("Giant Rat", 15, 30, 2, ratHair, 100, 5, False)
goblin = act.Enemy("Goblin", 25, 50, 2, goblinDust, 250, 20, False)
airhead = act.Enemy("Airhead", 50, 140, 4, brain, 300, 35, False)
taxCollector = act.Enemy("Tax Collector", 60, 170, 5, taxReturns, 350, 50, False)
meseeks = act.Enemy("Mr. Meeseks", 70, 160, 7, meseeksBox, 500, 150, False)
dungeonGuardian = act.Enemy("Dungeon Guardian", 85, 250, 12, weirdJuice, 1000, 300, False)  # enemies

level1 = npc.npc("Cheapo Charlie", [apple, orange, banana, level2Key], 250, False)
level2 = npc.npc("Low-Life Larry", [taser, germanArmour, level3Key], 600, False)
level3 = npc.npc("Black Market Bob", [waterGun, enchantedArmour, level4Key], 1500, False)
level4 = npc.npc("Scotty From Marketing", [swissArmyKnife, militaryArmour, exitKey], 5000, False)  # npcs
