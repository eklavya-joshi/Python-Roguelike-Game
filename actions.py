# script responsible for all player interactions with the enemy

import random
import gui as g
import playerinfo as ps
import time  # imports necessary modules

currentEnemy = None
pDamage = 0  # variables for enemy

class Enemy:  # enemy class
    def __init__(self, name, damage, health, level, dropItem, exp, gold, battle):
        self.name = name
        self.damage = damage
        self.health = health
        self.level = level
        self.dropItem = dropItem
        self.exp = exp
        self.gold = gold
        self.battle = battle


def Fight(enemy, player):  # function called when starting a fight
    if enemy.battle is True:
        g.Print(f"You have entered a battle with {enemy.name}!")
        g.Print("Determining first move...........................")
        enemy.battle = False
        time.sleep(0.5)
        TakeTurns(enemy, player, FirstMove(enemy, player))


def FirstMove(enemy, player):  # calculates first move
    players = [enemy, player]
    highestLevel = 0
    highestChar = None
    randNum = random.randint(1, 2)

    g.BoxPrint()
    for i in players:
        if i.level > highestLevel:  # gives first move to the person with the highest level
            highestLevel = i.level
            highestChar = i
        elif i.level == highestLevel:  # if both enemy and player are the same level randomly select first move
            if randNum == 1:
                highestChar = ps.player
            else:
                highestChar = currentEnemy
    print(randNum)
    g.Print(f"{highestChar.name} goes first.")
    return highestChar


def TakeTurns(enemy, player, firstPlayer):  # alternates between enemy and player turns in battle
    players = [enemy, player]
    currentPlayer = None
    if firstPlayer == player:  # assigns currentPlayer variable
        currentPlayer = player
    else:
        currentPlayer = enemy

    if enemy.health > 0 or player.health > 0:  # if both enemy and player have more than 0 health
        if currentPlayer == enemy:
            g.Print(f"{enemy.name}'s turn!")
            time.sleep(0.5)
            EnemyTurn(enemy, player)
        else:
            g.Print(f"{player.name}'s turn!")
            time.sleep(0.5)
            PlayerTurn(enemy, player)
    else:  # if someone has 0 health or less
        if enemy.health <= 0:
            g.Print(f"{player.name} has blown up the {enemy.name}!")
            time.sleep(0.5)
        else:
            g.Print("You blew up.")
            g.Print("--GAME OVER--")


def EnemyTurn(enemy, player):  # called when enemy's turn
    pHealthLost = int((enemy.damage * random.randint(8, 12) / 10) - (player.defence*0.5))
    if enemy.health > 0 or player.health > 0:
        if random.randint(0, 100) < (player.level / player.level) * 10:  # player can dodge attacks
            g.Print(f"{player.name} dodged the attack!")
        else:  # if player doesnt dodge attack deplete health
            player.health -= pHealthLost
            g.Print(f"The {currentEnemy.name} hit {player.name} and did {pHealthLost} damage.")
            g.StatBox()
            g.StatPrint(ps.player.health, ps.player.maxHealth, ps.player.weaponSlot.name, ps.player.wDamage,
                        ps.player.armourSlot.name,
                        ps.player.defence, ps.player.level, ps.player.exp, ps.player.gold, ps.player.inventory)
            g.BattleBox()
            if player.health <= 0:
                g.Print("You blew up.")
                g.Print("--GAME OVER--")
                time.sleep(1000)
        time.sleep(0.5)
        TakeTurns(enemy, player, player)


def PlayerTurn(enemy, player):  # called when player's turn
    #g.Print(f"{player.name}'s turn")
    return True


def Attack():  # called when player presses attack command on keyboard
    global currentEnemy
    global pDamage
    if ps.player.battle is True and currentEnemy is not None and PlayerTurn(currentEnemy, ps.player) is True:
        g.Print(f"{ps.player.name} attacks!")
        healthLost = int((ps.player.wDamage * random.randint(8, 12) / 10))
        if random.randint(0, 100) < (currentEnemy.level / currentEnemy.level) * 10:  # enemy can dodge attack
            g.Print(f"{currentEnemy.name} dodges the attack!")
            TakeTurns(currentEnemy, ps.player, currentEnemy)
        else:  # if enemy doesnt dodge attack deplete health
            currentEnemy.health -= healthLost
            pDamage = healthLost
            if currentEnemy.health <= 0:  # if enemy health is greater than 0
                g.Print(f"{currentEnemy.name} lost {healthLost} health! Now at 0.")
                g.Print(f"{currentEnemy.name} has blown up. {ps.player.name} wins the fight!")
            else:  # if enemy health is less than or equal to 0
                g.Print(f"{currentEnemy.name} lost {healthLost} health! Now at {currentEnemy.health}.")
                time.sleep(0.5)
                TakeTurns(currentEnemy, ps.player, currentEnemy)
