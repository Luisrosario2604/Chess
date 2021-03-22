#!/usr/bin/env python3.7
import sys
import signal
import os
import ast
import possibleMoves as pm
import random
import time
import getArrayBoard as gab

fileName = "../plays.txt"
isRead = 0
tmpMoove = 0
debug = 0
bestPoints = -9999
bestMoves = []
maxDepth = 2

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


def getPoints(move, tmpBoard, player):
    if player == "WHITE":
        end = pm.isEnd(tmpBoard, "BLACK")
    else:
        end = pm.isEnd(tmpBoard, "WHITE")
    points = 0
    if end == 2:
        points += 20
    if end == 3:
        points += 900

    if len(move) > 5:
        if move[6].lower() == "p":
            points += 10
        if move[6].lower() == "t":
            points += 50
        if move[6].lower() == "f":
            points += 30
        if move[6].lower() == "c":
            points += 30
        if move[6].lower() == "r":
            points += 900
        if move[6].lower() == "d":
            points += 90
    return points


def movePieceAndGetNewBoard(tmpBoard, move):
    array = gab.squareToArray(move[0], int(move[1]))
    array2 = gab.squareToArray(move[3], int(move[4]))
    # pieceEat = board[int(array2[1])][int(array2[0])]

    tmpBoard[int(array2[1])][int(array2[0])] = tmpBoard[int(array[1])][int(array[0])]
    tmpBoard[int(array[1])][int(array[0])] = "."

    return tmpBoard


def getPlayer(depth, player):
    if player == "WHITE":
        enemy = "BLACK"
    else:
        enemy = "WHITE"
    if depth % 2 == 0:
        return player
    return enemy


def getBestMove(actualBoard, player, depth=0, points=0, originalMove="", totalMoves=[]):
    global bestMoves
    global bestPoints

    if depth == maxDepth:
        return
    turnTo = getPlayer(depth, player)
    possibleMoves = pm.possibleMooves(actualBoard, turnTo).copy()

    for move in possibleMoves:
        if depth == 0:
            originalMove = move

        tmpBoard = [x[:] for x in actualBoard]
        tmpBoard = movePieceAndGetNewBoard(tmpBoard, move)
        if player == turnTo:
            points += getPoints(move, tmpBoard, turnTo)
        else:
            points -= getPoints(move, tmpBoard, turnTo)

        if points > bestPoints:
            bestPoints = points
            bestMoves.clear()
            bestMoves.append(originalMove)
        if points == bestPoints:
            bestPoints = points
            bestMoves.append(originalMove)
        totalMoves.append(move)
        getBestMove(tmpBoard, player, depth + 1, points, originalMove, totalMoves.copy())
        totalMoves.pop()

    if depth != 0:
        return

    rdm = random.randint(0, len(bestMoves) - 1)
    bestMove = bestMoves[rdm][0] + bestMoves[rdm][1] + bestMoves[rdm][3] + bestMoves[rdm][4]
    return bestMove


def addComeback(move, player, actualBoard):
    array2 = gab.squareToArray(move[0], int(move[1]))

    piece = actualBoard[int(array2[1])][int(array2[0])]

    if move[1] == "7" and move[3] == "8" and player == "WHITE" and piece == "p":
        move += "d"
    if move[1] == "2" and move[3] == "1" and player == "BLACK" and piece == "P":
        move += "d"
    return move


def yourTurn(player):
    global bestMoves
    global bestPoints

    bestPoints = -9999
    bestMoves = []
    board = getBoardInformation()
    actualBoard = [x[:] for x in board]
    move = getBestMove(actualBoard, player)

    move = addComeback(move, player, actualBoard)
    if debug == 1:
        time.sleep(1)
    writeFile("[PLAY] " + player + " " + move)
    return


def checkWhereLaunch():
    if not os.path.isfile("../sprites/chess.png"):
        print("[ERROR] Run ./main.py in the src directory")
        sys.exit(84)


def main():
    global debug

    if len(sys.argv) == 2:
        debug = 1
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
            yourTurn(player)


if __name__ == "__main__":
    main()
