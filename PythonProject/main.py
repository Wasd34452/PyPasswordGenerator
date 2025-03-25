import random

passwordlist = []
password = ""

for _ in range(random.randint(5, 15)):
    randomletter1 = random.randint(1, 26)
    randomletter1cap = random.randint(1, 2)

    if randomletter1 == 1:
        if randomletter1cap == 2:
            randomletter = "a"
        else:
            randomletter = "A"
    elif randomletter1 == 2:
        if randomletter1cap == 2:
            randomletter = "b"
        else:
            randomletter = "B"
    elif randomletter1 == 3:
        if randomletter1cap == 2:
            randomletter = "c"
        else:
            randomletter = "C"
    elif randomletter1 == 4:
        if randomletter1cap == 2:
            randomletter = "d"
        else:
            randomletter = "D"
    elif randomletter1 == 5:
        if randomletter1cap == 2:
            randomletter = "e"
        else:
            randomletter = "E"
    elif randomletter1 == 6:
        if randomletter1cap == 2:
            randomletter = "f"
        else:
            randomletter = "F"
    elif randomletter1 == 7:
        if randomletter1cap == 2:
            randomletter = "g"
        else:
            randomletter = "G"
    elif randomletter1 == 8:
        if randomletter1cap == 2:
            randomletter = "h"
        else:
            randomletter = "H"
    elif randomletter1 == 9:
        if randomletter1cap == 2:
            randomletter = "i"
        else:
            randomletter = "I"
    elif randomletter1 == 10:
        if randomletter1cap == 2:
            randomletter = "j"
        else:
            randomletter = "J"
    elif randomletter1 == 11:
        if randomletter1cap == 2:
            randomletter = "k"
        else:
            randomletter = "K"
    elif randomletter1 == 12:
        if randomletter1cap == 2:
            randomletter = "l"
        else:
            randomletter = "L"
    elif randomletter1 == 13:
        if randomletter1cap == 2:
            randomletter = "m"
        else:
            randomletter = "M"
    elif randomletter1 == 14:
        if randomletter1cap == 2:
            randomletter = "n"
        else:
            randomletter = "N"
    elif randomletter1 == 15:
        if randomletter1cap == 2:
            randomletter = "o"
        else:
            randomletter = "O"
    elif randomletter1 == 16:
        if randomletter1cap == 2:
            randomletter = "p"
        else:
            randomletter = "P"
    elif randomletter1 == 17:
        if randomletter1cap == 2:
            randomletter = "q"
        else:
            randomletter = "Q"
    elif randomletter1 == 18:
        if randomletter1cap == 2:
            randomletter = "r"
        else:
            randomletter = "R"
    elif randomletter1 == 19:
        if randomletter1cap == 2:
            randomletter = "s"
        else:
            randomletter = "S"
    elif randomletter1 == 20:
        if randomletter1cap == 2:
            randomletter = "t"
        else:
            randomletter = "T"
    elif randomletter1 == 21:
        if randomletter1cap == 2:
            randomletter = "u"
        else:
            randomletter = "U"
    elif randomletter1 == 22:
        if randomletter1cap == 2:
            randomletter = "v"
        else:
            randomletter = "V"
    elif randomletter1 == 23:
        if randomletter1cap == 2:
            randomletter = "w"
        else:
            randomletter = "W"
    elif randomletter1 == 24:
        if randomletter1cap == 2:
            randomletter = "x"
        else:
            randomletter = "X"
    elif randomletter1 == 25:
        if randomletter1cap == 2:
            randomletter = "y"
        else:
            randomletter = "Y"
    elif randomletter1 == 26:
        if randomletter1cap == 2:
            randomletter = "z"
        else:
            randomletter = "Z"

    passwordlist.append(randomletter)

password = "".join(passwordlist)
print("Your password is...", password)
