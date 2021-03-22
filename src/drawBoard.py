#!/usr/bin/env python3.7
from tkinter import *
import option

skinDir = "classic/"
spritesFile = []
spritesX = []
spritesY = []
tileX = -1
tileY = -1
selected = 0
tileNowX = -1
tileNowY = -1
playerToPlay = "WHITE"
isCheckBlack = False
isCheckWhite = False
pieceBackUpBlack = "D"
pieceBackUpWhite = "d"


# Change the global variable
def changeSkinDir(dir):
    global skinDir

    skinDir = dir


# Change the skin
def changeSkin(mainWindow):
    listbox = Toplevel(mainWindow)
    photo = PhotoImage(file="../sprites/classic/pb.png")
    photo1 = PhotoImage(file="../sprites/3D/pb.png")
    photo2 = PhotoImage(file="../sprites/minimalist/pb.png")
    photo3 = PhotoImage(file="../sprites/old/pb.png")
    photo4 = PhotoImage(file="../sprites/colors-classic/pb.png")
    photo5 = PhotoImage(file="../sprites/colors-blue/pb.png")
    photo6 = PhotoImage(file="../sprites/colors-grey/pb.png")
    photo7 = PhotoImage(file="../sprites/colors-green/pb.png")
    photo8 = PhotoImage(file="../sprites/colors-red/pb.png")
    photo9 = PhotoImage(file="../sprites/colors-yellow/pb.png")

    button = Button(listbox, image=photo, command=lambda:changeSkinDir("classic/"))
    button.pack()
    button.place(x=50, y=20)
    button1 = Button(listbox, image=photo1, command=lambda:changeSkinDir("3D/"))
    button1.pack()
    button1.place(x=150, y=20)
    button2 = Button(listbox, image=photo2, command=lambda:changeSkinDir("minimalist/"))
    button2.pack()
    button2.place(x=250, y=20)
    button3 = Button(listbox, image=photo3, command=lambda:changeSkinDir("old/"))
    button3.pack()
    button3.place(x=350, y=20)
    button4 = Button(listbox, image=photo4, command=lambda:changeSkinDir("colors-classic/"))
    button4.pack()
    button4.place(x=450, y=20)
    button5 = Button(listbox, image=photo5, command=lambda:changeSkinDir("colors-blue/"))
    button5.pack()
    button5.place(x=50, y=100)
    button6 = Button(listbox, image=photo6, command=lambda:changeSkinDir("colors-grey/"))
    button6.pack()
    button6.place(x=150, y=100)
    button7 = Button(listbox, image=photo7, command=lambda:changeSkinDir("colors-green/"))
    button7.pack()
    button7.place(x=250, y=100)
    button8 = Button(listbox, image=photo8, command=lambda:changeSkinDir("colors-red/"))
    button8.pack()
    button8.place(x=350, y=100)
    button9 = Button(listbox, image=photo9, command=lambda:changeSkinDir("colors-yellow/"))
    button9.pack()
    button9.place(x=450, y=100)
    button10 = Button(listbox, text="Ok", command=lambda: listbox.destroy())
    button10.pack()
    button10.place(x=260, y=200)

    listbox.geometry("{}x{}+{}+{}".format(575, 250, 70, 306))

    if option.quit == 1:
        listbox.destroy()
    listbox.mainloop()


# Draw letters of the board
def drawLettersNumbers(canvas):
    canvas.create_text(132.5, 662, fill="black", font="Fixedsys 50 bold", text="A")
    canvas.create_text(132.5 + 64 * 1, 662, fill="black", font="Fixedsys 50 bold", text="B")
    canvas.create_text(132.5 + 64 * 2, 662, fill="black", font="Fixedsys 50 bold", text="C")
    canvas.create_text(132.5 + 64 * 3, 662, fill="black", font="Fixedsys 50 bold", text="D")
    canvas.create_text(132.5 + 64 * 4, 662, fill="black", font="Fixedsys 50 bold", text="E")
    canvas.create_text(132.5 + 64 * 5, 662, fill="black", font="Fixedsys 50 bold", text="F")
    canvas.create_text(132.5 + 64 * 6, 662, fill="black", font="Fixedsys 50 bold", text="G")
    canvas.create_text(132.5 + 64 * 7, 662, fill="black", font="Fixedsys 50 bold", text="H")

    canvas.create_text(132.5 - 64 - 15, 75, fill="black", font="Fixedsys 10 bold", text="Blanc")
    canvas.create_text(132.5, 50, fill="black", font="Fixedsys 50 bold", text="A")
    canvas.create_text(132.5 + 64 * 1, 50, fill="black", font="Fixedsys 50 bold", text="B")
    canvas.create_text(132.5 + 64 * 2, 50, fill="black", font="Fixedsys 50 bold", text="C")
    canvas.create_text(132.5 + 64 * 3, 50, fill="black", font="Fixedsys 50 bold", text="D")
    canvas.create_text(132.5 + 64 * 4, 50, fill="black", font="Fixedsys 50 bold", text="E")
    canvas.create_text(132.5 + 64 * 5, 50, fill="black", font="Fixedsys 50 bold", text="F")
    canvas.create_text(132.5 + 64 * 6, 50, fill="black", font="Fixedsys 50 bold", text="G")
    canvas.create_text(132.5 + 64 * 7, 50, fill="black", font="Fixedsys 50 bold", text="H")
    canvas.create_text(132.5 + 64 * 8 + 15, 75, fill="black", font="Fixedsys 10 bold", text="Noir")

    canvas.create_text(50, 132.5, fill="black", font="Fixedsys 50 bold", text="8")
    canvas.create_text(50, 132.5 + 64 * 1, fill="black", font="Fixedsys 50 bold", text="7")
    canvas.create_text(50, 132.5 + 64 * 2, fill="black", font="Fixedsys 50 bold", text="6")
    canvas.create_text(50, 132.5 + 64 * 3, fill="black", font="Fixedsys 50 bold", text="5")
    canvas.create_text(50, 132.5 + 64 * 4, fill="black", font="Fixedsys 50 bold", text="4")
    canvas.create_text(50, 132.5 + 64 * 5, fill="black", font="Fixedsys 50 bold", text="3")
    canvas.create_text(50, 132.5 + 64 * 6, fill="black", font="Fixedsys 50 bold", text="2")
    canvas.create_text(50, 132.5 + 64 * 7, fill="black", font="Fixedsys 50 bold", text="1")

    canvas.create_text(662, 132.5, fill="black", font="Fixedsys 50 bold", text="8")
    canvas.create_text(662, 132.5 + 64 * 1, fill="black", font="Fixedsys 50 bold", text="7")
    canvas.create_text(662, 132.5 + 64 * 2, fill="black", font="Fixedsys 50 bold", text="6")
    canvas.create_text(662, 132.5 + 64 * 3, fill="black", font="Fixedsys 50 bold", text="5")
    canvas.create_text(662, 132.5 + 64 * 4, fill="black", font="Fixedsys 50 bold", text="4")
    canvas.create_text(662, 132.5 + 64 * 5, fill="black", font="Fixedsys 50 bold", text="3")
    canvas.create_text(662, 132.5 + 64 * 6, fill="black", font="Fixedsys 50 bold", text="2")
    canvas.create_text(662, 132.5 + 64 * 7, fill="black", font="Fixedsys 50 bold", text="1")

    if option.players == 0:
        canvas.create_rectangle(30, 15, 30 + 45, 15 + 45, fill="#E8CB2E")
        canvas.create_rectangle(640, 15, 640 + 45, 15 + 45, fill="#E8CB2E")
    elif option.players == 1:
        canvas.create_rectangle(30, 15, 30 + 45, 15 + 45, fill="#FF4452")
        canvas.create_rectangle(640, 15, 640 + 45, 15 + 45, fill="#E8CB2E")
    else:
        if playerToPlay == "WHITE":
            canvas.create_rectangle(30, 15, 30 + 45, 15 + 45, fill="#69FF8E")
            canvas.create_rectangle(640, 15, 640 + 45, 15 + 45, fill="#FF4452")
        else:
            canvas.create_rectangle(30, 15, 30 + 45, 15 + 45, fill="#FF4452")
            canvas.create_rectangle(640, 15, 640 + 45, 15 + 45, fill="#69FF8E")
    if isCheckWhite:
        canvas.create_rectangle(30 + 10, 15 + 10, 30 + 45 - 10, 15 + 45 - 10, fill="#353839")
    if isCheckBlack:
        canvas.create_rectangle(640 + 10, 15 + 10, 640 + 45 - 10, 15 + 45 - 10, fill="#353839")
    # vert : #69FF8E
    # rouge : #FF4452
    # jaune : #E8CB2E
    # noir : #353839




# Add the sprites to the global array for being draw after in mainDisplay function
def appendCanvas(filePath, x, y):
    global spritesFile
    global spritesX
    global spritesY

    image = PhotoImage(file=filePath)
    spritesFile.append(image)
    spritesX.append(x * 64 + 100)
    spritesY.append(y * 64 + 100)


def drawBoardGame(gameBoard):
    swap = 1
    for i in range(0, 8):
        swap *= -1
        for j in range(0, 8):
            if gameBoard[j][i] == "p":
                appendCanvas("../sprites/" + skinDir + "pb.png", i, j)
            elif gameBoard[j][i] == "t":
                appendCanvas("../sprites/" + skinDir + "tb.png", i, j)
            elif gameBoard[j][i] == "c":
                appendCanvas("../sprites/" + skinDir + "cb.png", i, j)
            elif gameBoard[j][i] == "f":
                appendCanvas("../sprites/" + skinDir + "fb.png", i, j)
            elif gameBoard[j][i] == "d":
                appendCanvas("../sprites/" + skinDir + "db.png", i, j)
            elif gameBoard[j][i] == "r":
                appendCanvas("../sprites/" + skinDir + "rb.png", i, j)
            elif gameBoard[j][i] == "P":
                appendCanvas("../sprites/" + skinDir + "pn.png", i, j)
            elif gameBoard[j][i] == "T":
                appendCanvas("../sprites/" + skinDir + "tn.png", i, j)
            elif gameBoard[j][i] == "C":
                appendCanvas("../sprites/" + skinDir + "cn.png", i, j)
            elif gameBoard[j][i] == "F":
                appendCanvas("../sprites/" + skinDir + "fn.png", i, j)
            elif gameBoard[j][i] == "R":
                appendCanvas("../sprites/" + skinDir + "rn.png", i, j)
            elif gameBoard[j][i] == "D":
                appendCanvas("../sprites/" + skinDir + "dn.png", i, j)
            swap *= -1
    if pieceBackUpBlack.upper() == "D":
        appendCanvas("../sprites/" + skinDir + "dn.png", 8.27, 8.3)
    elif pieceBackUpBlack.upper() == "F":
        appendCanvas("../sprites/" + skinDir + "fn.png", 8.27, 8.3)
    elif pieceBackUpBlack.upper() == "C":
        appendCanvas("../sprites/" + skinDir + "cn.png", 8.27, 8.3)
    elif pieceBackUpBlack.upper() == "T":
        appendCanvas("../sprites/" + skinDir + "tn.png", 8.27, 8.3)

    if pieceBackUpWhite.lower() == "d":
        appendCanvas("../sprites/" + skinDir + "db.png", -1.3, 8.27)
    elif pieceBackUpWhite.lower() == "f":
        appendCanvas("../sprites/" + skinDir + "fb.png", -1.3, 8.27)
    elif pieceBackUpWhite.lower() == "c":
        appendCanvas("../sprites/" + skinDir + "cb.png", -1.3, 8.27)
    elif pieceBackUpWhite.lower() == "t":
        appendCanvas("../sprites/" + skinDir + "tb.png", -1.3, 8.27)


# Add an over tile if the mouse is in one of them
def drawOverTile(x, y):
    global tileX
    global tileY
    global tileNowX
    global tileNowY

    if 100 <= x < 612 and 100 <= y < 612:
        x1 = int((x - 100) / 64)
        y1 = int((y - 100) / 64)
        tileNowX = x1
        tileNowY = y1
    else:
        tileNowX = -1
        tileNowY = -1

    if 100 <= x < 612 and 100 <= y < 612 and selected == 0:
        x = int((x - 100) / 64)
        y = int((y - 100) / 64)
        tileX = x
        tileY = y
    elif selected == 0:
        tileY = -1
        tileX = -1


# detect click
def mouseClickDetection(event):
    global selected

    if selected == 0:
        selected = 1
    elif selected == 1:
        selected = 2
    else:
        selected = 0


# detect if mouse is in one tile and highlight it
def mouseDetection(event):
    global tileX
    global tileY

    #print('mouseDetection : {}, {}'.format(tileX, tileY))
    drawOverTile(event.x, event.y)


# Draw the tiles of the board
def drawBoardTiles():

    swap = 1
    for i in range(8):
        swap *= -1
        for j in range(8):
            if swap == 1:
                appendCanvas("../sprites/" + skinDir + "c4.png", i, j)
            else:
                appendCanvas("../sprites/" + skinDir + "c1.png", i, j)
            swap *= -1


def changePickUpPiece(letter, player):
    global pieceBackUpBlack
    global pieceBackUpWhite

    if player == "WHITE":
        pieceBackUpWhite = letter.lower()
    else:
        pieceBackUpBlack = letter.upper()


# Pop up when a pawn reach the end and pick up the piece that you want
def pickUpPieceBack(mainWindow, player):
    # mainWindow.withdraw()
    # mainWindow.deiconify()
    global pieceCanClose

    listbox = Toplevel(mainWindow)

    if player == "BLACK":
        photo = PhotoImage(file="../sprites/" + skinDir + "tn.png")
        photo1 = PhotoImage(file="../sprites/" + skinDir + "fn.png")
        photo2 = PhotoImage(file="../sprites/" + skinDir + "cn.png")
        photo3 = PhotoImage(file="../sprites/" + skinDir + "dn.png")
    else:
        photo = PhotoImage(file="../sprites/" + skinDir + "tb.png")
        photo1 = PhotoImage(file="../sprites/" + skinDir + "fb.png")
        photo2 = PhotoImage(file="../sprites/" + skinDir + "cb.png")
        photo3 = PhotoImage(file="../sprites/" + skinDir + "db.png")

    button = Button(listbox, image=photo, command=lambda: [changePickUpPiece("t", player), listbox.destroy()])
    button.pack()
    button.place(x=50, y=20)
    button1 = Button(listbox, image=photo1, command=lambda: [changePickUpPiece("f", player), listbox.destroy()])
    button1.pack()
    button1.place(x=150, y=20)
    button2 = Button(listbox, image=photo2, command=lambda: [changePickUpPiece("c", player), listbox.destroy()])
    button2.pack()
    button2.place(x=250, y=20)
    button3 = Button(listbox, image=photo3, command=lambda: [changePickUpPiece("d", player), listbox.destroy()])
    button3.pack()
    button3.place(x=350, y=20)

    listbox.geometry("{}x{}+{}+{}".format(460, 100, 70, 306))

    if option.quit == 1:
        listbox.destroy()
    listbox.mainloop()


def quitAll(mainWindow):
    option.quit = 1
    mainWindow.destroy()


def addPlayerPopUp():
    listbox = Toplevel()

    label = Label(listbox, text="Un joueur à été ajouté !")
    label.pack()
    if option.players == 0:
        label2 = Label(listbox, text="Vous êtes le joueur blanc")
    else:
        label2 = Label(listbox, text="Vous êtes le joueur noir")
    label2.pack()
    button = Button(listbox, text="Ok", command=lambda: listbox.destroy())
    button.pack()

    listbox.geometry("{}x{}+{}+{}".format(300, 75, 200, 306))
    if option.quit == 1:
        listbox.destroy()
    listbox.mainloop()


def resultPopUp(mainWindow, text):
    listbox = Toplevel(mainWindow)

    print("RESULT : ", text)
    # text = Text(listbox, text=text)
    label = Label(listbox, text=text)
    label.pack(side="top", fill="x", pady=10)
    button = Button(listbox, text="Quit", command=lambda: quitAll(mainWindow))
    button.pack()
    # text.pack()

    listbox.geometry("{}x{}+{}+{}".format(300, 75, 200, 306))
    if option.quit == 1:
        listbox.destroy()
    listbox.mainloop()
