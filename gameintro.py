import time
#can use time to create pauses

#possible player responses
answer_1 = "1"
answer_2 = "2"
answer_3 = "3"
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

#Grabbing objects
ice_pick = 0
flower = 0

required = ("\nOnly use 1, 2, or 3\n")
#makes sure desired result is received

#start with introduction section of game
def intro():
    print ("You're on Frozen Python Mountain! After a gnarley morning"
    "on the slopes, you find yourself about half way up the mountain."
    "You've always wanted to take the high-speed lift to the top of the"
    "mountain, but OH NO it seems that you have lost your lift ticket!"
    "You need it to continue your ski trip, so you decide to...")
    time.sleep(1)
    print("""  1. Try to slide past the lift attendant
    2. Sit down in the snow and cry
    3. Ski across to Cobra's Persuit, the trail that you just came from""")
    choice = input(">>> ") #Here is your first choice.
    if choice in answer_1:
        option_search1()
    elif choice in answer_2:
        print ("\nWomp womp womp. The cold is not for the weak-hearted"
        "\n\nYou died!")
    elif choice in answer_3:
        option_sneak()
    else:
        print (required)
        intro()





