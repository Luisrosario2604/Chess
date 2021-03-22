#!/usr/bin/env python3.7
import sys
import signal
import os
import time
from subprocess import Popen, PIPE, STDOUT

debug = 0
fileName = "../plays.txt"
isRead = 0
mooves = "position startpos moves"


def signal_handler(sig, frame):
    print('Exit !')
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)


def getLetterPawnInverse(piece):
    piece = piece.lower()
    if piece == "r":
        piece = "k"
    elif piece == "d":
        piece = "q"
    elif piece == "t":
        piece = "r"
    elif piece == "f":
        piece = "b"
    elif piece == "c":
        piece = "n"
    return piece


def getLetterPawn(piece, player):
    piece.lower()
    if piece == "k":
        piece = "r"
    elif piece == "q":
        piece = "d"
    elif piece == "r":
        piece = "t"
    elif piece == "b":
        piece = "f"
    elif piece == "n":
        piece = "c"

    if player == "BLACK":
        piece = piece.upper()
    return piece


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


def yourTurn(player, comeBack):
    global mooves
    x = Popen(['./stockfish'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    mooves += getLetterPawnInverse(comeBack)
    # print(mooves)
    toSend = mooves + "\ngo\n"
    toSend = bytes(toSend, 'utf-8')
    while x.poll() is None:
        x.stdin.write(toSend)
        x.stdin.flush()
        child_output = x.stdout.readline()
        child_output = child_output.decode('utf8')
        while child_output.find("bestmove") == -1:
            child_output = x.stdout.readline()
            child_output = child_output.decode('utf8')
        break
    x.stdout.close()
    x.stdin.close()
    mooves += " " + child_output[9:13].lower()

    if debug == 1:
        time.sleep(1)
    # if je comeback un pion [13] = q (queen comeback)
    if len(child_output) > 13 and child_output[13] != " " and child_output[13] != "\n":
        letter = getLetterPawn(child_output[13], player)
        mooves += child_output[13].lower()
        writeFile("[PLAY] " + player + " " + child_output[9:13].upper() + letter)
    else:
        writeFile("[PLAY] " + player + " " + child_output[9:13].upper())


def checkWhereLaunch():
    if not os.path.isfile("../sprites/chess.png"):
        print("[ERROR] Run ./main.py in the src directory")
        sys.exit(84)


def main():
    global mooves
    global debug

    if len(sys.argv) == 2:
        debug = 1
    checkWhereLaunch()
    writeFile("START")
    player = ""
    while 1:
        comeBack = ""
        read = readFile()
        if read.find("[NEW] WHITE") != -1 and player == "":
            player = "WHITE"
            print(player)
        elif read.find("[NEW] BLACK") != -1 and player == "":
            player = "BLACK"
            print(player)
        turn = "[TURN] " + player
        if read.find(turn) != -1:
            if len(read) > 12:
                # print(read)
                mooves += " " + read[13:17].lower()
                if len(read) > 17:
                    comeBack = read[17].lower()
            yourTurn(player, comeBack)
    return


if __name__ == "__main__":
    main()
