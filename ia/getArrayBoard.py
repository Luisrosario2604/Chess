#!/usr/bin/env python3.7


def getArrayLetter(letter):
    if letter == "A":
        return 0
    elif letter == "B":
        return 1
    elif letter == "C":
        return 2
    elif letter == "D":
        return 3
    elif letter == "E":
        return 4
    elif letter == "F":
        return 5
    elif letter == "G":
        return 6
    elif letter == "H":
        return 7
    return 8


def getArrayNumber(nb):
    if nb == 1:
        return 8
    elif nb == 2:
        return 7
    elif nb == 3:
        return 6
    elif nb == 4:
        return 5
    elif nb == 5:
        return 4
    elif nb == 6:
        return 3
    elif nb == 7:
        return 2
    elif nb == 8:
        return 1
    return 9


def arrayToSquare(x, y):
    if x == 1:
        letter = "A"
    elif x == 2:
        letter = "B"
    elif x == 3:
        letter = "C"
    elif x == 4:
        letter = "D"
    elif x == 5:
        letter = "E"
    elif x == 6:
        letter = "F"
    elif x == 7:
        letter = "G"
    elif x == 8:
        letter = "H"
    elif x == 9:
        letter = "I"
    else:
        return 0
    return letter + str(y)


def squareToArray(x, y):
    if x == "A":
        letter = 0
    elif x == "B":
        letter = 1
    elif x == "C":
        letter = 2
    elif x == "D":
        letter = 3
    elif x == "E":
        letter = 4
    elif x == "F":
        letter = 5
    elif x == "G":
        letter = 6
    elif x == "H":
        letter = 7
    elif x == "I":
        letter = 8
    else:
        return 9

    if y == 8:
        number = 0
    elif y == 7:
        number = 1
    elif y == 6:
        number = 2
    elif y == 5:
        number = 3
    elif y == 4:
        number = 4
    elif y == 3:
        number = 5
    elif y == 2:
        number = 6
    elif y == 1:
        number = 7
    else:
        number = 8
    return str(letter) + str(number)


def selectToSquare(x, y):
    if x == 0:
        x = "A"
    elif x == 1:
        x = "B"
    elif x == 2:
        x = "C"
    elif x == 3:
        x = "D"
    elif x == 4:
        x = "E"
    elif x == 5:
        x = "F"
    elif x == 6:
        x = "G"
    else:
        x = "H"

    if y == 0:
        y = 8
    elif y == 1:
        y = 7
    elif y == 2:
        y = 6
    elif y == 3:
        y = 5
    elif y == 4:
        y = 4
    elif y == 5:
        y = 3
    elif y == 6:
        y = 2
    elif y == 7:
        y = 1
    elif y == 8:
        y = 0

    return str(x) + str(y)


def squareToSelect(x, y):
    if x == "A":
        x = 0
    elif x == "B":
        x = 1
    elif x == "C":
        x = 2
    elif x == "D":
        x = 3
    elif x == "E":
        x = 4
    elif x == "F":
        x = 5
    elif x == "G":
        x = 6
    else:
        x = 7

    if y == "8":
        y = 0
    elif y == "7":
        y = 1
    elif y == "6":
        y = 2
    elif y == "5":
        y = 3
    elif y == "4":
        y = 4
    elif y == "3":
        y = 5
    elif y == "2":
        y = 6
    elif y == "1":
        y = 7
    elif y == "0":
        y = 8

    return str(x) + str(y)

