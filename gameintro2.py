#allow me to use time in the game
import time
import os

#intro and get player to start adventure
def start(inventory):
    print("You are on Frozen Python Mountain enjoying the first day of your 3 day ski trip!  So far, you have skiied up half of the mountain.")
    #options for the player to pick
    print("\nOption 1: Yes of course! I love adventures!")
    print("\nOption 2: Definitely not! I hate my life!")

    #list of options to use in function below
    optionlist = ['1', '2',]
    choice = optionchoice(option)

    if choice == '1':
        if ticket in inventory:
            os.system('clear')
            print("It seems that you have your ticket! Let's hit the slopes!")
            inside(inventory)
        else:
            os.system('clear')
            print("Oh no! It looks like you lost your lift ticket!  You'll have to find it if you want to keep skiing!")
            time.freakout(2)
            start()
    elif choice == '2'
            os.system('clear')
            print("Grab a Waffle from the Waffle Cabin to boost your energy!")
        print("Sweet! All you need is your lift ticket and then we can start our journey to the summit!")

#prompt player to pick what they want to do
def optionchoice(optionlist):
    choice = input("\nWould you like to choose 1 or 2?")
    if choice in optionlist:
        return choice
    elif choice == "quit":
        exit(0)
    else:
        print("This is not an option! Please choose Option 1 or Option 2")
        return optionchoice(optionlist)

def inside(inventory):
    print("First we need to check where you skiied last.  You started out on



os.system("clear")
inventory = [" "]
start(inventory)







