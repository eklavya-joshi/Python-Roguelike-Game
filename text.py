# script responsible for handling large chunks of text

import gui as g
import playerinfo as ps


def Language():  # asks the player for their language
    g.Print("Welcome to \"Blower-Upper\"")
    g.Print("Select your language(Answer in numbers eg. \"1\" for Arabic):")
    g.Print("1. Pig Latin")
    g.Print("2. English")
    langInput = g.input()
    if langInput == "1":
        g.Print("Unfortunately, we did not have the budget for a pig latin translator :(. Consider donating to us by")
        g.Print("sending us your credit card details.")
    elif langInput == "2":
        g.Print("You have chosen English.")
    else:
        g.Print("Input not recognised. Try again")
        Language()


def Intro():  # prints the text for the introduction to the game
    g.Print("")
    g.Print("Intro:")
    g.Print("")
    g.Print(f"You are a mercenary in the kingdom of Fatwa'lah, and you have been living there for years.")
    g.Print(
        "In this world, you have found that it is possible to achieve great things without having to work hard at them.")
    g.Print("You don't really need to be a hero; all you really need is a sword and some skill with it.")
    g.Print(
        "You just have to go out into the world and blow up people. The more people you blow up, the better off you will be!")
    g.Print("You never had any real ambitions or desires other than blowing up as many people as possible.")
    g.Print("You became a blower upper, and now you feel like an empty shell inside.")
    g.Print(
        "To try to redeem yourself, you go to the Fatwa'lah forest in search of a dragon that has been terrorising the village.")
    g.Print(
        "You reach the forest and in the middle, you find a castle. \"He must be up there.\" You think to yourself.")
    g.Print("You make your way up the castle, but to get to the dragon you will have to blow up some monsters first.")
    g.Print("")
    g.Print("")
    g.Print("")
    g.Print("")
    g.Print("")
    g.Print("")


def InfoPrint():  # prints the information on controls and the gui. Can be called again if the player presses "Y"
    g.Print("")
    g.Print("Controls:")
    g.Print("")
    g.Print(
        "On the bottom left is your map. There you can see yourself(blue), items you could pick up(green), enemies(red),")
    g.Print(
        "traders(pink), doors(brown), and the castle(white). You can only open doors with a chamber key.")
    g.Print(" You can only move inside the dungeon and can walk over items to interact with them.")
    g.Print(" If you get too close to an enemy, it will attack. To move around the map, press w, s, a, and d.")
    g.Print("To open a door, walk up to it. To interact with an npc or pick up an item, walk over it.")
    g.Print("When in a fight, you can attack by pressing \"k\" or use an item by pressing \"o\".")
    g.Print("")
    g.Print(
        "On the bottom right are your stats. This includes your health, armour, and damage. It also includes the items you have")
    g.Print(
        "equipped, and the items in your inventory and their descriptions. To navigate through the items in your inventory, press")
    g.Print("The up and down arrow keys. To use an item, press \"O\", and to drop an item, press \"P\". If you drop an item, you")
    g.Print("can pick it up again in the map. Once you use an object, it is removed from your inventory.")
    g.Print("")
    g.Print("Over here at the top is the dialogue box. It prints any dialogue you will have to see in the video game.")
    g.Print("Sometimes, a window will pop up with a box for a response. You can type something into this window and the")
    g.Print("game will respond to it. The dialogue box clears after a certain amount of lines have been printed.")
    g.Print("If you would like to read the instructions again at any time, press \"Y\"")
