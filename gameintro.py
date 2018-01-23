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

#makes sure desired result is received
required = ("\nOnly use 1, 2, or 3 to answer most questions \n")


#start with introduction section of game
def intro():
    #will set the scene
    print ("""You're on Frozen Python Mountain! After a gnarley morning
    on the slopes, you find yourself about half way up the mountain.
    You've always wanted to take the high-speed lift to the top of the
    mountain.  All you need is your lift ticket! Double check that you
    have it, and then we'll be ready to go!""")
    #delay to give time to read
    time.sleep(7)
    print("...checking for ticket...")
    time.sleep(3)

#check for lift ticket
def check():
    if ticket == 0:
        print("""OH NO!!!! It seems that your lift ticket isn't on your
        jacket.  Without your ticket, you won't be able to ride any ski
        lifts on the mountain.  What are you going to do next???""")
        time.sleep(7)
        #options for what to do about missing lift ticket
        print("""
        1. Try to slide past the lift attendant
        2. Sit down in the snow and cry
        3. Ski across to Cobra's Pursuit, the trail that you just came from""")
        #first choice
        choice = input(">>> ")
        if choice in answer_1:
            #goes to sneak function
            option_sneak()
        #second choice
        elif choice in answer_2:
            #dies
            print ("""\nWomp womp womp. The cold is not for the weak-hearted
            \n\nYou died!""")
        #third choice
        elif choice in answer_3:
            #goes to search function
            option_search1()
        else:
            #remind player of possible inputs and return to beginning
            print (required)
            check()
    else:
        #if the player already has a ticket in the inventory
        print("Rad! You're on your way to the top of the mountain")
        option_top()

#to search on previous trail
def option_search1():
    time.sleep(5)
    print ("""\nYou ski slightly uphill over to Cobra's Pursuit.  You ski down
    the trail, but you can't seem to find your ticket.  Would you
    like to...""")
    time.sleep(4)
    print ("""
    1. Give up and resort to sneaking past the lift attendant
    2. Do another sweep over Cobra's Pursuit
    3. Search the Bunny Hill, where you warmed up this morning""")
    choice = input(">>> ")
    #first choice
    if choice in answer_1:
        #goes to sneak option
        option_sneak()
    #second choice
    elif choice in answer_2:
        #dies
        print ("""\nYou decided to ski over Cobra's Trail again, but
        while searching you got a bit too close to the edge and fell
        300 feet!  \n\nYou died!""")
    #third choice
    elif choice in answer_3:
        #will search bunny hill
        option_search2()
    else:
        #prompt to pick correct response and restart the function
        print (required)
        option_search1()

#to sneak past lift attendant
def option_sneak():
    print("""You get into the crowded line of eager skiiers waiting to board the
    high speed lift to the top. The left attendant is checking the tickets of
    each skiier.  You try to keep your head down and slide by, but the attendant
    notices that you don't have your ticket clipped to your jacket.
    What do you do next?""")
    #time to read
    time.sleep(8)
    #options
    print("""
    1. Obey the rules and respectfully step out of line
    2. Throw up a peace sign and hop on the lift anyway
    3. Get trampled by the lift attendant""")
    choice = input(">>> ")
    #first choice
    if choice in answer_1:
        #dies
        print("Following the rules will get you no where.\n\nYou died!")
    #second choice
    elif choice in answer_2:
        #reward by going to the top of the mountain
        print("""Risky move, but I like your style! Congrats, you're on your
        way to the top.""")
        #function to take player to the top
        option_top()
    #thrid choice
    elif choice in answer_3:
        #dies
        print("""Your stupidity will get you killed.  You've been trampled by
        the Yeti. \n\n You died!""")
    else:
        #prompt to pick a valid response
        print(required)
        #restart function
        option_sneak()

#search the bunny hill
def option_search2():
    print ("""\nYou ski down to the bunny hill, but you ear a loud grumble
    coming from behind you.  It's a Yeti!!!!!!  Luckily, you notice an ice
    pick on the ground. Do you pick it up. Y/N?""")
    #prompt to respond to whether or not player wants to pick up ice pick
    choice = input(">>> ")
    #the player has the ice pick
    if choice in yes:
        ice_pick = 1
    #the player doesn't have the ice pick
    else:
        ice_pick = 0
    #ask about how to solve Yeti problem
    print ("\nWhat do you do next?")
    #time to read
    time.sleep(4)
    #options for what to do
    print ("""
    1. Hide behind a snowbank like the coward you are
    2. Fight the Yeti
    3. Run""")
    choice = input(">>> ")
    #first choice
    if choice in answer_1:
        #dies
        print ("""\nReally? You're going to hide behind a measley pile of snow?
        Did you know that Yetis have a keen sense of smell?  WELP...
        They do, so...He was able to track you down in a matter of seconds.
        \n\nYou died!""")
    #second choice
    elif choice in answer_2:
        if ice_pick > 0:
        #player has the ice pick and is about to fight the Yeti
            print ("""\nYou took shelter behind the nearby snowbank. The
            shimmering ice pick attracted the Yeti, who was certain that you
            would be his dinner. He crept closer and closer, and your palms
            became sweaty in your gloves. The Yeti tried to reach out to grab
            your ice pick, but you were too quick for him! You stabbed his furry
            chest as he stumbled into the snow.""")
            #time to read
            time.sleep(11)
            print("""You survived the Yeti!!!!!""")
            print("""Would you like to...
            #options for what to do after survive the Yeti
            1. Ski over to the lodge
            2. Try to sneak onto the high speed lift
            3. Take a nap in the snow""")
            #first choice after stabbing Yeti
            if choice in answer_1:
                #goes to explore lodge area
                option_lodge()
            #second choice after stabbing Yeti
            elif choice in answer_2:
                #tries to sneak past attendant at lift
                option_sneak()
            else:
                #taking a nap leads to player's death
                print("""Sleeping in the snow is a dangerous choice! \n\nYOU DIED""")
        else:
            #If the player doesn't have the pick
            #dies
            print ("""\nNot picking up the ice pick was a terrible move.
            You now have no way to fight off the vicious Yeti.\n\nYou died!""")
    elif choice in answer_3:
        #player runs away instead of fighting the Yeti
        print ("""While the Yeti is distracted by other prey on the Bunny Hill,
        you slip away into the brush. You're several feet into the woods, but
        the Yeti turns around and sees you running.""")
        #time to read
        time.sleep(7)
        #run away from the Yeti again
        option_run()
    else:
        #prompts player to choose valid response and returns to start of the function
        print (required)
        option_search2()

#running from the Yeti
def option_run():
    print ("""\nYou kick off your skis and run as fast as you can
    You're unable to run in your ski boots, and the Yeti is
    gaining speed. You decide to...""")
    #time to read
    time.sleep(5)
    #options for what to do next
    print ("""
    1. Hide behind boulder
    2. Fight the Yeti
    3. Run towards the lodge and hope you make it there safe""")
    choice = input(">>> ")
    #first choice)
    if choice in answer_1:
        #dies
        print ("""The Yeti was able to spot you easily.
        \n\nYou died!""")
    #second choice
    elif choice in answer_2:
        #dies
        print ("""\nYou're no match for the massive Yeti.
        \n\nYou died!""")
    #third choice
    elif choice in answer_3:
        #goes to lodge
        option_lodge()
    else:
        #prompts player to choose valid input and restart
        print (required)
        option_run()

def option_lodge():
    print ("""\nWhile running, you notice a rusted
    ice pick in the snow. You try to pick it up while passing
    it, but you miss. You decide to hide behindthe main ski
    lodge building, knowing that the Yeti is not far behind.
    You spot a LIFT TICKET in the snow near your foot.
    Do you pick it up? Y/N""")
    choice = input(">>> ")
    #add lift ticket
    if choice in yes:
        #adds a ticket
        ticket = 1
    else:
        #still no ticket
        ticket = 0
    #Yeti still approaches
    print ("""You hear its heavy footsteps and you prepare yourself to be
    confronted by the massive Yeti""")
    #time to read
    time.sleep(4)
    if ticket > 0:
        #allows to ride lift
        print ("""\nNow that you have a valid ticket, you can ride the lift
        to the top of the mountain! You ski over to the lift as fast can,
        leaving the Yeti far behind.""")
        #time to read
        time.sleep(6)
        #goes to the top of the mountain
        option_top()
    else:
        #If player didn't take the ticket
        print ("""\nMaybe you should have picked up the ticket.
        You're defenseless against the ruthless Yeti, and you have no where to
        escape to.\n\nYou died!""")

def option_top():
    import os
    os.system('clear')
    print("""CONGRATULATIONS!!!!! YOU'VE MADE IT TO THE TOP! YOU MANAGED TO GET
    PAST THE YETI AND REACH THE SUMMIT OF FROZEN PYTHON MOUNTAIN!!!\n\nYOU WIN""")

intro()
check()


