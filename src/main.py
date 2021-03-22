#!/usr/bin/env python3.7
from tkinter import *
import sys
import drawBoard
import option
import getArrayBoard as gab
import possibleMooves
import getArrayBoard
import os

kingMooveBlack = False
kingMooveWhite = False
fileName = "../plays.txt"
blackPlayer = 0
whitePlayer = 0
lastMoove = ""
moovesEnd = 0
moovesTotal = []
playerPossibleMooves = []
debug = 0

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


def createFile():
    file = open(fileName, "w")
    file.close()
    option.board = gameBoard
    option.moovesTotal = []
    option.getBoardInformation()
    option.getTotalMovesInformation()


def readFile():
    file = open(fileName, 'r')
    read = file.readlines()
    file.close()
    if read:
        read = read[len(read) - 1]
        if read != "\n":
            return read
    return ""


def writeFile(text):
    if text != "":
        file = open(fileName, 'a')
        text = "\n" + text
        file.write(text)
        file.close()


def modifyGameBoard(x1, y1, x2, y2, player, comeBack=None):
    global gameBoard
    # global piecesLeft
    global moovesEnd
    global kingMooveBlack
    global kingMooveWhite

    pieceTaken = gameBoard[x2][y2]

    #Petit roque noir
    if kingMooveBlack == False and gameBoard[x1][y1] == "R" and x1 == 0 and y1 == 4 and gameBoard[x2][y2] == "."\
            and x2 == 0 and y2 == 2:
        gameBoard[x2][y2] = "R"
        gameBoard[x1][y1] = "."
        gameBoard[0][3] = "T"
        gameBoard[0][0] = "."
    # Grand roque noir
    elif kingMooveBlack == False and gameBoard[x1][y1] == "R" and x1 == 0 and y1 == 4 and gameBoard[x2][y2] == "." \
            and x2 == 0 and y2 == 6:
        gameBoard[x2][y2] = "R"
        gameBoard[x1][y1] = "."
        gameBoard[0][5] = "T"
        gameBoard[0][7] = "."
    # Petit roque blanc
    elif kingMooveWhite == False and gameBoard[x1][y1] == "r" and x1 == 7 and y1 == 4 and gameBoard[x2][y2] == "." \
             and x2 == 7 and y2 == 2:
        gameBoard[x2][y2] = "r"
        gameBoard[x1][y1] = "."
        gameBoard[7][3] = "t"
        gameBoard[7][0] = "."
        # Grand roque blanc
    elif kingMooveWhite == False and gameBoard[x1][y1] == "r" and x1 == 7 and y1 == 4 and gameBoard[x2][y2] == "." \
             and x2 == 7 and y2 == 6:
        gameBoard[x2][y2] = "r"
        gameBoard[x1][y1] = "."
        gameBoard[7][5] = "t"
        gameBoard[7][7] = "."
    elif gameBoard[x2][y2] != ".":
        if pieceTaken == "T":
            if x2 == 0 and y2 == 0:
                possibleMooves.didBlackTower1Moove = True
            if x2 == 0 and y2 == 7:
                possibleMooves.didBlackTower2Moove = True
        elif pieceTaken == "t":
            if x2 == 7 and y2 == 0:
                possibleMooves.didWhiteTower1Moove = True
            if x2 == 7 and y2 == 7:
                possibleMooves.didWhiteTower2Moove = True
        if gameBoard[x2][y2] == "r":
            writeFile("[END] BLACK")
            return True
        elif gameBoard[x2][y2] == "R":
            writeFile("[END] WHITE")
            return True
        # piecesLeft.append(gameBoard[x2][y2])
        moovesEnd = -1
        gameBoard[x2][y2] = gameBoard[x1][y1]
        gameBoard[x1][y1] = "."
    else:
        gameBoard[x2][y2] = gameBoard[x1][y1]
        gameBoard[x1][y1] = "."

    if gameBoard[x2][y2] == "R":
        kingMooveBlack = True
        possibleMooves.didBlackKingMoove = True
    elif gameBoard[x2][y2] == "r":
        kingMooveWhite = True
        possibleMooves.didWhiteKingMoove = True

    if gameBoard[x2][y2] == "T":
        if x1 == 0 and y1 == 0:
            possibleMooves.didBlackTower1Moove = True
        if x1 == 0 and y1 == 7:
            possibleMooves.didBlackTower2Moove = True
    elif gameBoard[x2][y2] == "t":
        if x1 == 7 and y1 == 0:
            possibleMooves.didWhiteTower1Moove = True
        if x1 == 7 and y1 == 7:
            possibleMooves.didWhiteTower2Moove = True

    if comeBack is not None:
        moovesEnd = -1
        if player == "WHITE":
            gameBoard[x2][y2] = comeBack.lower()
        elif player == "BLACK":
            gameBoard[x2][y2] = comeBack.upper()
    moovesEnd += 1
    return False


# modify a global of drawboard to know if someone is check and then display black square
def modifyGlobalCheckForBlackSquare(player, check):
    global isCheckBlack
    global isCheckWhite

    if player == "BLACK":
        drawBoard.isCheckBlack = check
    else:
        drawBoard.isCheckWhite = check


# 0 == No / 1 == Nul / 2 == Mat / 3 == echec
def checkEnd(player):
    tmp = possibleMooves.isEnd(gameBoard, player)
    if moovesEnd >= 50:
        writeFile("[END] Nul")
        modifyGlobalCheckForBlackSquare(player, False)
        return True
    elif tmp == 0:
        modifyGlobalCheckForBlackSquare(player, False)
        return False
    elif tmp == 1:
        modifyGlobalCheckForBlackSquare(player, False)
        writeFile("[END] Pat")
        return True
    elif tmp == 2 and player == "WHITE":
        writeFile("[END] BLACK")
        modifyGlobalCheckForBlackSquare(player, True)
        return True
    elif tmp == 2 and player == "BLACK":
        writeFile("[END] WHITE")
        modifyGlobalCheckForBlackSquare(player, True)
        return True
    else:
        modifyGlobalCheckForBlackSquare(player, True)
        return False


def popUpEnd(read, mainWindow):
    if read.find("[END] Nul") != -1:
        drawBoard.resultPopUp(mainWindow, "Égalité !")
    elif read.find("[END] Pat") != -1:
        drawBoard.resultPopUp(mainWindow, "Pat ! (Égalité)")
    elif read.find("[END] BLACK") != -1:
        drawBoard.resultPopUp(mainWindow, "Le joueur noir à gagné, échec et mat !")
        return True
    elif read.find("[END] WHITE") != -1:
        drawBoard.resultPopUp(mainWindow, "Le joueur blanc à gagné, échec et mat !")
    return False


def addMoovesTotalToOptionFile(moove):
    option.moovesTotal.append(moove)
    option.getBoardInformation()
    option.getTotalMovesInformation()


# print in file witch player as to play
# end == si le roi est mangé
def turnManager(pieceComeBack, end, read, lastMoove):
    if read.find("[PLAY] WHITE") != -1 and end == False:
        if not checkEnd("BLACK"):
            checkEnd("WHITE")
            if pieceComeBack == "":
                addMoovesTotalToOptionFile(lastMoove)
                writeFile("[TURN] BLACK " + lastMoove)
            else:
                addMoovesTotalToOptionFile(lastMoove + pieceComeBack)
                writeFile("[TURN] BLACK " + lastMoove + pieceComeBack)
            drawBoard.playerToPlay = "BLACK"
    elif read.find("[PLAY] BLACK") != -1 and end == False:
        if not checkEnd("WHITE"):
            checkEnd("BLACK")
            if pieceComeBack == "":
                addMoovesTotalToOptionFile(lastMoove)
                writeFile("[TURN] WHITE " + lastMoove)
            else:
                addMoovesTotalToOptionFile(lastMoove + pieceComeBack)
                writeFile("[TURN] WHITE " + lastMoove + pieceComeBack)
            drawBoard.playerToPlay = "WHITE"


# import time
def readingFileLoop(mainWindow):
    # time.sleep(1)
    global blackPlayer
    global whitePlayer
    global moovesTotal

    pieceComeBack = ""
    read = readFile()
    player = ""

    if read.find("[END]") != -1:
        popUpEnd(read, mainWindow)
        return
    if blackPlayer == 2:
        blackPlayer = 3
        writeFile("[TURN] WHITE")
        drawBoard.playerToPlay = "WHITE"
    elif read == "START":
        option.players += 1
        if whitePlayer == 0:
            writeFile("[NEW] WHITE")
            whitePlayer = 1
        elif blackPlayer == 0:
            writeFile("[NEW] BLACK")
            blackPlayer = 2
    elif read.find("[PLAY]") != -1:
        if debug == 1:
            input("Press key")
        if read.find("[PLAY] WHITE") != -1:
            player = "WHITE"
        elif read.find("[PLAY] BLACK") != -1:
            player = "BLACK"
        read2 = read.split()
        lastMoove = read2[2][0] + read2[2][1] + read2[2][2] + read2[2][3]

        if len(read2[2]) > 4:
            end = modifyGameBoard(gab.getArrayNumber(int(read2[2][1])) - 1, gab.getArrayLetter(read2[2][0]),
                            gab.getArrayNumber(int(read2[2][3])) - 1, gab.getArrayLetter(read2[2][2]), player, read2[2][4])
            pieceComeBack = read2[2][4]
        else:
            end = modifyGameBoard(gab.getArrayNumber(int(read2[2][1])) - 1, gab.getArrayLetter(read2[2][0]),
                            gab.getArrayNumber(int(read2[2][3])) - 1, gab.getArrayLetter(read2[2][2]), player)
        option.board = gameBoard
        turnManager(pieceComeBack, end, read, lastMoove)


# Detect all the possible mooves when a player as clicked on a piece of the board
def printPossibleMooves():
    global playerPossibleMooves
    playerPossibleMooves = []

    piece = gameBoard[drawBoard.tileY][drawBoard.tileX]
    square = getArrayBoard.selectToSquare(drawBoard.tileX, drawBoard.tileY)
    if piece.islower():
        mooves = possibleMooves.possibleMooves(gameBoard, "WHITE")
    else:
        mooves = possibleMooves.possibleMooves(gameBoard, "BLACK")
    for i in mooves:
        if i[0] == square[0] and i[1] == square[1]:
            possiblemoove = getArrayBoard.squareToSelect(i[3], i[4])
            drawBoard.appendCanvas("../sprites/" + drawBoard.skinDir + "c7.png", int(possiblemoove[0]), int(possiblemoove[1]))
            playerPossibleMooves.append([int(possiblemoove[0]), int(possiblemoove[1])])


# Detect if the player as choosen a moove to do and write it to the file
def detectMooveFromPlayer():
    pieceBackToTheGame = ""
    piece = gameBoard[drawBoard.tileY][drawBoard.tileX]
    if drawBoard.selected == 2:
        for i in playerPossibleMooves:
            if i[0] == drawBoard.tileNowX and i[1] == drawBoard.tileNowY:
                if piece == "p" and getArrayBoard.selectToSquare(drawBoard.tileNowX, drawBoard.tileNowY)[1] == "8":
                    pieceBackToTheGame = drawBoard.pieceBackUpWhite
                if piece == "P" and getArrayBoard.selectToSquare(drawBoard.tileNowX, drawBoard.tileNowY)[1] == "1":
                    pieceBackToTheGame = drawBoard.pieceBackUpBlack
                if piece.islower():
                    toPrint = "[PLAY] " + "WHITE " + getArrayBoard.selectToSquare(drawBoard.tileX, drawBoard.tileY) + getArrayBoard.selectToSquare(drawBoard.tileNowX, drawBoard.tileNowY) + pieceBackToTheGame.lower()
                else:
                    toPrint = "[PLAY] " + "BLACK " + getArrayBoard.selectToSquare(drawBoard.tileX, drawBoard.tileY) + getArrayBoard.selectToSquare(drawBoard.tileNowX, drawBoard.tileNowY) + pieceBackToTheGame.upper()
                writeFile(toPrint)
        drawBoard.selected = 0


def mainDisplay(mainWindow, canvas):
    canvas.delete('all')
    drawBoard.spritesFile.clear()
    drawBoard.spritesX.clear()
    drawBoard.spritesY.clear()
    drawBoard.drawBoardTiles()
    mainWindow.bind('<Motion>', drawBoard.mouseDetection)
    mainWindow.bind('<Button-1>', drawBoard.mouseClickDetection)
    detectMooveFromPlayer()
    if drawBoard.tileX != -1 and drawBoard.tileY != -1:
        if drawBoard.selected == 0:
            drawBoard.appendCanvas("../sprites/" + drawBoard.skinDir + "c7.png", drawBoard.tileX, drawBoard.tileY)
        else:
            printPossibleMooves()
            drawBoard.appendCanvas("../sprites/" + drawBoard.skinDir + "c6.png", drawBoard.tileX, drawBoard.tileY)
    drawBoard.drawBoardGame(gameBoard)

    i = 0
    while i < len(drawBoard.spritesFile):
        canvas.create_image(drawBoard.spritesX[i], drawBoard.spritesY[i], anchor=NW, image=drawBoard.spritesFile[i])
        i += 1
    drawBoard.drawLettersNumbers(canvas)

    if option.quit == 0:
        readingFileLoop(mainWindow)
        mainWindow.after(100, lambda: mainDisplay(mainWindow, canvas))


def checkArguments():
    global debug

    if not os.path.isfile("../sprites/chess.png"):
        print("[ERROR] Run ./main.py in the src directory")
        sys.exit(84)
    if len(sys.argv) == 2 and sys.argv[1] == "--help":
        print("./main.py [-d]")
        sys.exit(0)
    if len(sys.argv) != 1 and len(sys.argv) != 2:
        print("[ERROR] Bad argument")
        sys.exit(84)
    if len(sys.argv) == 2 and sys.argv[1] == "-d":
        debug = 1


def main():
    checkArguments()
    createFile()
    mainWindow = Tk()
    mainWindow.title('Jeu d\'echec')
    mainWindow.protocol("WM_DELETE_WINDOW", lambda: option.exitAll(mainWindow))
    canvas = Canvas(mainWindow, width=712, height=712)
    canvas.pack(side=TOP)
    option.topbarSetup(mainWindow)
    mainDisplay(mainWindow, canvas)
    mainWindow.mainloop()


if __name__ == "__main__":
    main()
