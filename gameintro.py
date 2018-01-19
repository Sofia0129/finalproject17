import time
#can use time to create pauses

#possible player responses
answer_1 = "1"
answer_2 = "2"
answer_3 = "3"
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

#objects to pick up along the way
ice_pick = 0
ticket = 0

required = ("\nOnly use 1, 2, or 3\n")
#makes sure desired result is received

#start with introduction section of game
def intro():
    #will set the scene
    print ("You're on Frozen Python Mountain! After a gnarley morning"
    "on the slopes, you find yourself about half way up the mountain."
    "You've always wanted to take the high-speed lift to the top of the"
    "mountain, but OH NO it seems that you have lost your lift ticket!"
    "You need it to continue your ski trip, so you decide to...")
    time.sleep(1)
    #options for what to do about missing lift ticket
    print("""  1. Try to slide past the lift attendant
    2. Sit down in the snow and cry
    3. Ski across to Cobra's Persuit, the trail that you just came from""")
    choice = input(">>> ") #Here is your first choice.
    if choice in answer_1:
        option_sneak()
    elif choice in answer_2:
        print ("\nWomp womp womp. The cold is not for the weak-hearted"
        "\n\nYou died!")
    elif choice in answer_3:
        option_search1()
    else:
        print (required)
        intro()

def option_search1():
    print ("\nYou ski slightly uphill over to Cobra's Persuit."
    "You ski down the trail, but you can't seem to find your ticket.  Would you"
    "like to...")
    time.sleep(1)
    print ("""  1. Give up and resort to sneaking past the lift attendant
    2. Do another sweep over Cobra's Persuit
    3. Search the Bunny Hill, where you warmed up this morning""")
    choice = input(">>> ")
    if choice in answer_1:
        option_sneak()
    elif choice in answer_2:
        print ("\nYou decided to ski over Cobra's Trail again, but"
        "while searching you got a bit too close to the edge and fell"
        "300 feet!  \n\nYou died!")
    elif choice in answer_3:
        option_search2()
    else:
        print (required)
        option_search1()

def option_sneak():
    print("You get into the crowded line of eager skiiers waiting to board the"
    "high speed lift to the top. The left attendant is checking the tickets of"
    "each skiier.  You try to keep your head down and slide by, but the attendant"
    "notices that you don't have your ticket clipped to your jacket."
    "What do you do next?"

    time.sleep(1)
    print(""" 1. Obey the rules and respectfully step out of line
    2. Throw up a peace sign and hop on the lift anyway
    3. Get trampled by the lift attendant """)
    if choice in answer_1:
        print("Following the rules will get you nowhere.\n\nYou died!")
    elif choice in answer_2:
        print("Risky move, but I like your style! Congrats, you're on your way"
        "to the top.")
        option_top()
    elif choice in answer_3:
        print("Your stupidity will get you killed.  You've been trampled by"
        "the Yeti. \n\n You died!")
    else:
        print(required)
        option_sneak()

def option_search2():
    print ("\nYou ski down to the bunny hill, but you ear a loud grumble"
    "coming from behind you.  It's a Yeti!!!!!!  Luckily, you notice an ice"
    "pick on the ground. Do you pick it up. Y/N?")
    choice = input(">>> ")
    if choice in yes:
        #the player has the ice pick
        ice_pick = 1
    else:
        ice_pick = 0
    print ("\nWhat do you do next?")
    time.sleep(1)
    print ("""  1. Hide behind a snowbank
    2. Fight Yeti
    3. Run""")
    choice = input(">>> ")
    if choice in answer_1:
        print ("\nReally? You're going to hide behind a measley pile of snow?"
        "Did you know that Yetis have a keen sense of smell?  WELP..."
        "They do, so...\n\nYou died!")
    elif choice in answer_2:
        if ice_pick > 0:
            print ("\nYou took shelter behind the nearby snowbank. The shimmering ice pick"
            "attracted the Yeti, who was certain that you would be his dinner."
            "He crept closer and closer, and your palms became sweaty in your gloves."
            "The Yeti tried to reach out to grab your ice pick, but you were too quick for him!"
            "You stabbed his furry chest as he stumbled into the snow.\n\nYou survived!")
        else:
            #If the player doesn't have the pick
            print ("\nNot picking up the ice pick was a terrible move."
            "You now have no way to fight off the vicious Yeti.\n\nYou died!")
    elif choice in answer_3:
        print ("While the Yeti is distracted by other prey on the Bunny Hill,"
        "you slip away into the brush. You're several feet into the woods, but the Yeti turns "
        "around and sees you running.")
        option_run()
    else:
        print (required)
        option_search2()

def option_run():
    print ("\nYou kick off your skis and run as fast as you can"
    "You're unable to run in your ski boots, and the Yeti is"
    "gaining speed. You decide to...")
    time.sleep(1)
    print ("""  1. Hide behind boulder
    2. Fight the Yeti
    3. Run towards the lodge and hope you make it there safe""")
    choice = input(">>> ")
    if choice in answer_1:
        print ("The Yeti was able to spot you easily. "
        "\n\nYou died!")
    elif choice in answer_2:
        print ("\nYou're no match for the massive Yeti. "
        "\n\nYou died!")
    elif choice in answer_3:
        option_lodge()
    else:
        print (required)
        option_run()

def option_town():
    print ("\nWhile running, you notice a rusted "
    "ice pick in the snow. You try to pick it up while passing"
    "it, but you miss. You decide to hide behind"
    "the main ski lodge building, knowing that the Yeti is not far behind."
    "You spot a LIFT TICKET in the snow near your foot."
    "Do you pick it up? Y/N")
    choice = input(">>> ")
    if choice in yes:
        ticket = 1 #adds a ticket
    else:
        ticket = 0
    print ("You hear its heavy footsteps and you prepare yourself to be"
    "confronted by the massive Yeti")
    time.sleep(1)
    if ticket > 0:
        print ("\nNow that you have a valid ticket, you can ride the lift"
        "to the top of the mountain! You ski over to the lift as fast can,"
        "leaving the Yeti far behind.")
        option_top()
    else: #If player didn't take the ice pick
        print ("\nMaybe you should have picked up the ice pick. "
        "You're defenseless against the ruthless Yeti.\n\nYou died!")

def option_top():
    print("CONGRATULATIONS!!!!! YOU'VE MADE IT TO THE TOP! YOU MANAGED TO GET"
    "PAST THE YETI AND REACH THE SUMMIT OF FROZEN PYTHON MOUNTAIN!!!\n\n YOU WIN")

intro()




