#!/usr/bin/env python3.7
import sys
import signal
import os
import ast
import possibleMoves as pm
import getArrayBoard as gab

fileName = "../plays.txt"
isRead = 0
tmpMoove = 0
bestPoints = -1
bestMoves= ""

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


def movePieceAndGetNewBoard(tmpBoard, move):
    array = gab.squareToArray(move[0], int(move[1]))
    array2 = gab.squareToArray(move[3], int(move[4]))
    # pieceEat = board[int(array2[1])][int(array2[0])]

    tmpBoard[int(array2[1])][int(array2[0])] = tmpBoard[int(array[1])][int(array[0])]
    tmpBoard[int(array[1])][int(array[0])] = "."

    return tmpBoard


def getPoints(move):
    if len(move) > 5:
        if move[6].lower() == "p":
            return 10
        if move[6].lower() == "t":
            return 50
        if move[6].lower() == "f":
            return 30
        if move[6].lower() == "c":
            return 30
        if move[6].lower() == "r":
            return 900
        if move[6].lower() == "d":
            return 90
    return 0


maxDepth = 3 #IMPAIR !!!!!!!


def getBestMove(board, player, depth=0, points=0, originalMove="", debug=""):
    global bestPoints
    global bestMoves

    if depth == maxDepth:
        return
    # if depth % 2 == 0:
    possibleMoves = pm.possibleMooves(board, player)
    # else:
    #     if player == "WHITE":
    #         possibleMoves = pm.possibleMooves(board, "BLACK")
    #     else:
    #         possibleMoves = pm.possibleMooves(board, "WHITE")
    tmpBoard = [x[:] for x in board]

    for move in possibleMoves:
        if originalMove == "":
            originalMove = move

        # if depth % 2 == 0:
        tmpPoints = getPoints(move) * (maxDepth - depth)
        # else:
        #     tmpPoints = - getPoints(move) * (maxDepth - depth)
        tmpBoard = movePieceAndGetNewBoard(tmpBoard, move)

        if tmpPoints + points > bestPoints:
            bestPoints = tmpPoints + points
            bestMove = originalMove
            print("Best Points : ", bestPoints)
            print("Original Move : ", bestMove)
            print("Best Move : ", move)
            print("Depth :", depth)
            print("All path: ", debug)
            print()
        getBestMove(tmpBoard, player, depth+1, points + tmpPoints, originalMove, debug + " / " + move)

        if depth == 0:
            originalMove = move
            debug = ""
            points = 0
    return bestMove


def yourTurn(player, read):
    global bestPoints
    global bestMoves

    bestPoints = -1
    bestMove = ""
    # board = getBoardInformation()
    board = [["T", "C", "F", "D", "R", "F", "C", "T"],
             ["P", "P", "P", "P", "P", "P", "P", "P"],
             [".", ".", ".", "t", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", "."],
             ["p", "p", "p", ".", "p", "p", "p", "p"],
             ["t", "c", "f", "d", "r", "f", "c", "t"]]

    print("BEST MOOVE :", getBestMove(board, player))
    sys.exit(0)

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
    yourTurn("BLACK", "")
    main()
