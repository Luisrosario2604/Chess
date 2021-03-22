#!/usr/bin/env python3.7
import sys
import signal
import os
import ast

fileName = "../plays.txt"
isRead = 0

tmpMoove = 0


# MAJ = NOIR
# PAS MAJ = BLANC
# . = VOID
gameBoard = [["T", "C", "F", "D", "R", "F", "C", "T"],
             ["P", "P", "P", "P", "P", "P", "P", "P"],
             [".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", "."],
             ["p", "p", "p", "p", "p", "p", "p", "p"],
             ["t", "c", "f", "d", "r", "f", "c", "t"]]


def signal_handler(sig, frame):
    print('Exit !')
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)


def readFile():
    global isRead

    file = open(fileName, 'r')
    read = file.readlines()
    file.close()
    if read:
        read = read[len(read) - 1]
        # print(read)
        return read
    return ""


def writeFile(text):
    global isRead
    isRead = 0
    file = open(fileName, 'a')
    text = "\n" + text
    file.write(text)
    file.close()


def getBoardInformation():
    board = ""
    while board == "":
        file = open("../boardInformation.txt", 'r')
        read = file.readlines()
        file.close()
        for i in read:
            board = ast.literal_eval(i)
    return board


def getTotalMovesInformation():
    moves = ""
    while moves == "":
        file = open("../totalMovesInformation.txt", 'r')
        read = file.readlines()
        file.close()
        for i in read:
            moves = ast.literal_eval(i)
    return moves


def yourTurn(player, read):
    #print(read)
    #print(getTotalMovesInformation())
    #print(getBoardInformation())
    #writeFile("[PLAY] " + player + " B1 C3")
    return


def checkWhereLaunch():
    if not os.path.isfile("../sprites/chess.png"):
        print("[ERROR] Run ./main.py in the src directory")
        sys.exit(84)


def main():
    checkWhereLaunch()
    writeFile("START")
    player = ""
    while 1:
        read = readFile()
        # print(read)
        if read.find("[NEW] WHITE") != -1 and player == "":
            player = "WHITE"
            print(player)
        elif read.find("[NEW] BLACK") != -1 and player == "":
            player = "BLACK"
            print(player)
        turn = "[TURN] " + player
        if read.find(turn) != -1:
            yourTurn(player, read)


if __name__ == "__main__":
    main()
