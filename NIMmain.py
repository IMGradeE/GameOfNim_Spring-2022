"""
Name: Payton Wilkes
Date: Nov. 5th 2022
Description: Human vs. computer NIM Main file
"""
from random import randint
from random import randrange
from time import sleep

from AnimalCrossingTextAudioRender import txtRndr
from NIMFuncs import DrawStones
from NIMFuncs import LoopOrExit
from NIMFuncs import Output
from NIMFuncs import PlayerTurn


# Totally would like to class all of these strings so that I can render them  one character at a time like
# in animal crossing
def Greeting():
    greetStrings = ["\n(Please enter y to continue, or n for a tutorial.)",  # 0
                    "\n(That wasn't quite right. Please enter y to continue, or n for a tutorial.)",  # 1
                    "\nWell, since you already know how to play, all I need to know is whether you'd like to!" +
                    "\n(Please enter y to play, or n to exit.)",  # 2
                    "\n(That wasn't quite right. Please enter y to play, or n to exit.)",  # 3
                    "\nWould you like to play?\n(Please enter y to play, or n to exit.)"]  # 4

    tutorial = "Oh! First timer! Fantastic. I'll fill you in on the rules and stuff then, " \
               "that way you can decide if you'd like to play with me!" \
               "\nAll you need to play Nim is a friend, and some stones! \n(I can grab some, so no worries if you didn't" \
               " bring any.)\n" \
               "At the beginning of the game, an initial number of stones is set somewhere between 15 and 30.\n" \
               "Once this is done, we take turns removing stones from that pile. Whoever has to take the last stone wins!\n" \
               "The only rule is that you can't take 0 stones, and you can't take more than 3 stones per turn.\n" \
               "Oh and you can't take more stones than the available number, but I'm sure that's obvious."

    # tutorial = list(tutorial.split())

    txtRndr("Hello! This program allows you to play a game of Nim against me, your computer!\nHave you heard of Nim before?",0)
    if not LoopOrExit(greetStrings[0], greetStrings[1]):
        txtRndr(tutorial)
        if LoopOrExit(greetStrings[4], greetStrings[3]):
            MainNIM()
        else:
            EarlyEndVoid()
    else:
        if LoopOrExit(greetStrings[2], greetStrings[3]):
            MainNIM()
        else:
            EarlyEndVoid()

def MainNIM():
    rockNums = ["One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen",
                "Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen","Twenty","Twenty-one","Twenty-two",
                "Twenty-three","Twenty-four","Twenty-five","Twenty-six","Twenty-Seven","Twenty-Eight","Twenty-nine",
                "Thirty"]
    nimStrings = ["y to play again, n to quit.", "That didn't work, please input y to play again, or n to quit."]
    txtRndr("Okay, I'll get the stones! ")
    stones = randint(15, 30)
    for i in range(0, stones):
        chance = randint(1, 4)
        if i == 0:
            txtRndr(f"I found {rockNums[i]} stone...\n",0)
        elif chance == 1:
            txtRndr(f"...{rockNums[i]}...\n",0)
        else:
            txtRndr("...",0)

    sleep(1)
    txtRndr(f"\nI found {stones} stones, so that's how many we'll use! You get to make the first move! \nGood luck, and have fun!")
    winner = False
    while winner == False:
        stones, isPlayer, negateStones = GameLoop(stones)
        for i in range(negateStones):
            sleep((randrange(50, 90) / 200))
            txtRndr(f"...{rockNums[i]}...",0)
        winner = Output(stones, isPlayer, negateStones)
        if not winner:
            sleep((randint(1, 2)/5))
            stones, isPlayer, negateStones = GameLoop(stones, 2, False)
            for i in range(negateStones):
                sleep((randrange(50, 90) / 200))
                txtRndr(f"...{rockNums[i]}...",0)
            winner = Output(stones, isPlayer, negateStones)
    if LoopOrExit(nimStrings[0], nimStrings[1]):
        MainNIM()
    else:
        EndVoid()

def EndVoid():
    txtRndr("Thank you for playing NIM with me! I hope you had as much fun as I did. \nCome back soon!")

def EarlyEndVoid():
    txtRndr("No worries! If you ever change your mind, you know where to find me!\nHave a great day!")

def GameLoop(s, func=1, isP=True):
    if func == 1:
        nS = PlayerTurn(s)
        s -= nS
    else:
        nS = DrawStones(s)
        s -= nS
        isP = False
    return s, isP, nS

Greeting()