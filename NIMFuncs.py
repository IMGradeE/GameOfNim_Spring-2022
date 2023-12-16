'''
Description: NIM functions
'''
from random import randint
from AnimalCrossingTextAudioRender import txtRndr


def isValidEntry(s, negS):
    if (3 >= negS >= 1) and (s >= negS):
        return True
    else:
        return False


def DrawStones(s):
    if s >= 3:
        return randint(1, 3)
    elif s == 2:
        return randint(1, 2)
    elif s == 1:
        return 1


def PlayerTurn(s):
    unknownStr = 'An unknown error occurred, please try again.'
    while True:
        try:
            negS = int(input(txtRndr("How many stones would you like to take?\n")).strip())
            if not isValidEntry(s, negS):
                raise Exception(txtRndr(
                    f"Invalid input\nThe number of stones you take must be an integer less than or equal to 3, and cannot exceed "
                    f"the remaining number of stones ({s}).\nPlease try again."))
            else:
                break
        except ValueError:
            txtRndr(f"That didn't work, The number of stones you take must be an integer.\nTry again.")
        except Exception as err:
            txtRndr(str(err))
        except:
            txtRndr(unknownStr)
    return negS


def Output(s, hu, negS):
    if hu == True:
        op = "You"
        notOp = "me"
        turn = "my"
    else:
        op = "I"
        notOp = "you"
        turn = "your"
    if (negS == 1) and (s > 1):
        txtRndr(f"\n{op} took {negS} stone.\n There are {s} stones remaining.\nIt's {turn} turn!")
        return False
    elif s >= 1:
        txtRndr(f"\n{op} took {negS} stones.\n There are {s} stones remaining.\nIt's {turn} turn!")
        return False
    else:
        txtRndr(f"{op} took the last stone! That makes {notOp} the winner!\nWould you like to play again?")
        return True


def LoopOrExit(a, b):
    ans = input(txtRndr(a)).lower().strip()
    while (ans != "y") and (ans != "n"):
        ans = input(txtRndr(b)).strip().lower()
    else:
        if ans == "y":
            return True
        else:
            return False