#!/usr/bin/env python3.7
from tkinter import *
from tkinter import messagebox
import signal
import main
import drawBoard

board = [[".", ".", ".", ".", ".", ".", ".", "."], #x=1 ; y=8  0 0
         [".", ".", ".", ".", ".", ".", ".", "."], #x=1 ; y=7
         [".", ".", ".", ".", ".", "R", ".", "."], #x=1 ; y=6
         [".", ".", ".", ".", ".", ".", ".", "."], #Tour Cavalier Fou Roi Dame Pion
         [".", ".", ".", ".", ".", "T", "T", "T"],
         [".", ".", ".", "f", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "p", "p", "p"],
         [".", ".", ".", ".", ".", "T", "r", "."]]
moovesTotal = []

players = 0
quit = 0


def signal_handler(sig, frame):
    global quit

    print('Exit !')
    quit = 1
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)


# Called when you click quit or the cross in the topbar
def exitAll(mainWindow):
    global quit

    if messagebox.askokcancel("Quitter", "Voulez-vous vraiment quitter ?"):
        mainWindow.destroy()
        quit = 1


def addPlayer():
    if players >= 2:
        return
    main.writeFile("START")
    drawBoard.addPlayerPopUp()


def debug():
    print("GameBoard :",  board)
    print()
    print("Mooves :", moovesTotal)


def getBoardInformation():
    file = open("../boardInformation.txt", 'w')
    text = str(board)
    file.write(text)
    file.close()


def getTotalMovesInformation():
    file = open("../totalMovesInformation.txt", 'w')
    text = str(moovesTotal)
    file.write(text)
    file.close()


# Setting the topbar (menu, exit ...)
def topbarSetup(mainWindow):
    menubar = Menu(mainWindow)

    menu = Menu(menubar, tearoff=0)
    menu2 = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Menu", menu=menu)
    menubar.add_cascade(label="Pièce de retour", menu=menu2)

    menu.add_command(label="Ajouter un joueur", command=lambda: addPlayer())
    menu.add_command(label="Changer de skin", command=lambda: drawBoard.changeSkin(mainWindow))
    menu.add_command(label="Debug", command=lambda: debug())
    menu.add_command(label="Quit", command=lambda: exitAll(mainWindow))

    menu2.add_command(label="Changer pièce blanche", command=lambda: drawBoard.pickUpPieceBack(mainWindow, "WHITE"))
    menu2.add_command(label="Changer pièce noire", command=lambda: drawBoard.pickUpPieceBack(mainWindow, "BLACK"))

    mainWindow.config(menu=menubar)
    return mainWindow
