from time import sleep
from random import randrange


def txtRndr(str,x = 1):
    for i in str:
        if i == " ":
            print(i, end='')
        else:
            sleep((randrange(300,400)/1000))
            print(i, end='')
    if x == 1:
        print('')
        sleep(.2)
    else:
        print(end="")
    sleep(.1)
    return ""

if __name__ == "__main__":
    str = "Hello! This program allows you to play a game of Nim against me, your computer! Have you heard of Nim before?"
    txtRndr(str)


