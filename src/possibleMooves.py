#!/usr/bin/env python3.7

import getArrayBoard


didWhiteKingMoove = False
didBlackKingMoove = False
didWhiteTower1Moove = False
didWhiteTower2Moove = False
didBlackTower1Moove = False
didBlackTower2Moove = False

mooves = []
moovesCheck = []
gameBoard = [[".", ".", ".", ".", ".", ".", ".", "."], #x=1 ; y=8  0 0
             [".", ".", ".", ".", ".", ".", ".", "."], #x=1 ; y=7
             [".", ".", ".", ".", ".", "R", ".", "."], #x=1 ; y=6
             [".", ".", ".", ".", ".", ".", ".", "."], #Tour Cavalier Fou Roi Dame Pion
             [".", ".", ".", ".", ".", "T", "T", "T"],
             [".", ".", ".", "f", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", "p", "p", "p"],
             [".", ".", ".", ".", ".", "T", "r", "."]]


def isPossibleMoove(x, y):
    if 8 >= x >= 1 and 8 >= y >= 1:
        return True
    return False


def appendMoove(board, player, x1, y1, x2, y2):
    global mooves

    piece = getPiece(board, x2, y2)

    if piece.islower() and player == "WHITE":
        return
    if piece.isupper() and player == "BLACK":
        return

    if piece != ".":
        tmpStr = getArrayBoard.arrayToSquare(x1, y1) + " " + getArrayBoard.arrayToSquare(x2, y2) + " " + piece
    else:
        tmpStr = getArrayBoard.arrayToSquare(x1, y1) + " " + getArrayBoard.arrayToSquare(x2, y2)
    mooves.append(tmpStr)


def getPiece(board, x, y):
    return board[getArrayBoard.getArrayNumber(y) - 1][x - 1]


def pawnMoove(board, player, x, y):
    if player == "BLACK":
        if y == 7 and getPiece(board, x, y - 1) == "." and getPiece(board, x, y - 2) == ".":
            appendMoove(board, player, x, y, x, y - 2)
        if isPossibleMoove(x, y - 1) and getPiece(board, x, y - 1) == ".":
            appendMoove(board, player, x, y, x, y - 1)
        if isPossibleMoove(x + 1, y - 1) and (getPiece(board, x + 1, y - 1) != "."):
            appendMoove(board, player, x, y, x + 1, y - 1)
        if isPossibleMoove(x - 1, y - 1) and (getPiece(board, x - 1, y - 1) != "."):
            appendMoove(board, player, x, y, x - 1, y - 1)

    elif player == "WHITE":
        if y == 2 and getPiece(board, x, y + 1) == "." and getPiece(board, x, y + 2) == ".":
            appendMoove(board, player, x, y, x, y + 2)
        if isPossibleMoove(x, y + 1) and getPiece(board, x, y + 1) == ".":
            appendMoove(board, player, x, y, x, y + 1)
        if isPossibleMoove(x + 1, y + 1) and (getPiece(board, x + 1, y + 1) != "."):
            appendMoove(board, player, x, y, x + 1, y + 1)
        if isPossibleMoove(x - 1, y + 1) and (getPiece(board, x - 1, y + 1) != "."):
            appendMoove(board, player, x, y, x - 1, y + 1)


def addRock(board, player, x, y, enemyMooves):
    pathIsFree1 = True
    pathIsFree2 = True
    pathIsFree3 = True
    pathIsFree4 = True

    for i in enemyMooves:
        if (i[3] == "E" and i[4] == "1") or (i[3] == "D" and i[4] == "1") or (i[3] == "C" and i[4] == "1"):
            pathIsFree1 = False
        if (i[3] == "E" and i[4] == "1") or (i[3] == "F" and i[4] == "1") or (i[3] == "G" and i[4] == "1"):
            pathIsFree2 = False
        if (i[3] == "E" and i[4] == "8") or (i[3] == "D" and i[4] == "8") or (i[3] == "C" and i[4] == "8"):
            pathIsFree3 = False
        if (i[3] == "E" and i[4] == "8") or (i[3] == "F" and i[4] == "8") or (i[3] == "G" and i[4] == "8"):
            pathIsFree4 = False

    if not didWhiteKingMoove and not didWhiteTower1Moove and pathIsFree1\
            and board[7][1] == "." and board[7][2] == "." and board[7][3] == ".":
        # king -> 5 8 / tower1 -> 1 8 / passage -> 4 8 / arrive -> 3 8
        #         E1              A1               D1              C1
        appendMoove(board, player, x, y, x - 2, y)
    if not didWhiteKingMoove and not didWhiteTower2Moove and pathIsFree2 \
            and board[7][5] == "." and board[7][6] == ".":
        # king -> 5 8 / tower1 -> 8 8 / passage -> 6 8 / arrive -> 7 8
        #         E1              H1               F1              G1
        appendMoove(board, player, x, y, x + 2, y)
    if not didBlackKingMoove and not didBlackTower1Moove and pathIsFree3\
            and board[0][1] == "." and board[0][2] == "." and board[0][3] == ".":
        # king -> 5 1 / tower1 -> 1 1 / passage -> 4 1 / arrive -> 3 1
        #         E8              A8               D8              C8
        appendMoove(board, player, x, y, x - 2, y)
    if not didBlackKingMoove and not didBlackTower2Moove and pathIsFree4\
            and board[0][5] == "." and board[0][6] == ".":
        # king -> 5 1 / tower1 -> 8 1 / passage -> 6 1 / arrive -> 7 1
        #         E8              H8               F8              G8
        appendMoove(board, player, x, y, x + 2, y)


def kingMoove(board, player, x, y, enemyMooves, comingFromFunctionEnd=False):
    if isPossibleMoove(x, y - 1):
        appendMoove(board, player, x, y, x, y - 1)
    if isPossibleMoove(x, y + 1):
        appendMoove(board, player, x, y, x, y + 1)
    if isPossibleMoove(x + 1, y):
        appendMoove(board, player, x, y, x + 1, y)
    if isPossibleMoove(x - 1, y):
        appendMoove(board, player, x, y, x - 1, y)
    if isPossibleMoove(x + 1, y - 1):
        appendMoove(board, player, x, y, x + 1, y - 1)
    if isPossibleMoove(x + 1, y + 1):
        appendMoove(board, player, x, y, x + 1, y + 1)
    if isPossibleMoove(x - 1, y - 1):
        appendMoove(board, player, x, y, x - 1, y - 1)
    if isPossibleMoove(x - 1, y + 1):
        appendMoove(board, player, x, y, x - 1, y + 1)
    if not comingFromFunctionEnd:
        addRock(board, player, x, y, enemyMooves)


def knightMoove(board, player, x, y):
    if isPossibleMoove(x + 2, y - 1):
        appendMoove(board, player, x, y, x + 2, y - 1)
    if isPossibleMoove(x + 2, y + 1):
        appendMoove(board, player, x, y, x + 2, y + 1)
    if isPossibleMoove(x + 1, y - 2):
        appendMoove(board, player, x, y, x + 1, y - 2)
    if isPossibleMoove(x - 1, y - 2):
        appendMoove(board, player, x, y, x - 1, y - 2)
    if isPossibleMoove(x - 2, y - 1):
        appendMoove(board, player, x, y, x - 2, y - 1)
    if isPossibleMoove(x - 2, y + 1):
        appendMoove(board, player, x, y, x - 2, y + 1)
    if isPossibleMoove(x + 1, y + 2):
        appendMoove(board, player, x, y, x + 1, y + 2)
    if isPossibleMoove(x - 1, y + 2):
        appendMoove(board, player, x, y, x - 1, y + 2)


def towerMoove(board, player, x, y):
    tmp = 1
    while tmp != 0:
        if isPossibleMoove(x, y - tmp):
            appendMoove(board, player, x, y, x, y - tmp)
            if getPiece(board, x, y - tmp) != ".":
                tmp = -1
        else:
            tmp = -1
        tmp += 1
    tmp = 1
    while tmp != 0:
        if isPossibleMoove(x, y + tmp):
            appendMoove(board, player, x, y, x, y + tmp)
            if getPiece(board, x, y + tmp) != ".":
                tmp = -1
        else:
            tmp = -1
        tmp += 1
    tmp = 1
    while tmp != 0:
        if isPossibleMoove(x + tmp, y):
            appendMoove(board, player, x, y, x + tmp, y)
            if getPiece(board, x + tmp, y) != ".":
                tmp = -1
        else:
            tmp = -1
        tmp += 1
    tmp = 1
    while tmp != 0:
        if isPossibleMoove(x - tmp, y):
            appendMoove(board, player, x, y, x - tmp, y)
            if getPiece(board, x - tmp, y) != ".":
                tmp = -1
        else:
            tmp = -1
        tmp += 1


def bishopMoove(board, player, x, y):
    tmp = 1
    while tmp != 0:
        if isPossibleMoove(x - tmp, y - tmp):
            appendMoove(board, player, x, y, x - tmp, y - tmp)
            if getPiece(board, x - tmp, y - tmp) != ".":
                tmp = -1
        else:
            tmp = -1
        tmp += 1
    tmp = 1
    while tmp != 0:
        if isPossibleMoove(x + tmp, y + tmp):
            appendMoove(board, player, x, y, x + tmp, y + tmp)
            if getPiece(board, x + tmp, y + tmp) != ".":
                tmp = -1
        else:
            tmp = -1
        tmp += 1
    tmp = 1
    while tmp != 0:
        if isPossibleMoove(x + tmp, y - tmp):
            appendMoove(board, player, x, y, x + tmp, y - tmp)
            if getPiece(board, x + tmp, y - tmp) != ".":
                tmp = -1
        else:
            tmp = -1
        tmp += 1
    tmp = 1
    while tmp != 0:
        if isPossibleMoove(x - tmp, y + tmp):
            appendMoove(board, player, x, y, x - tmp, y + tmp)
            if getPiece(board, x - tmp, y + tmp) != ".":
                tmp = -1
        else:
            tmp = -1
        tmp += 1


# get the path of one piece with 2 coords
def getPathOfPiece(i, board):
    piece = board[getArrayBoard.getArrayNumber(int(i[1])) - 1][getArrayBoard.getArrayLetter(i[0])]
    if piece == "c" or piece == "C" or piece == "r" or piece == "R":
        return []
    letterCounter = 0
    numberCounter = 0
    arrayPath = []
    if i[0] < i[3]:
        letterCounter = 1
    elif i[0] > i[3]:
        letterCounter = -1

    if int(i[1]) < int(i[4]):
        numberCounter = 1
    elif int(i[1]) > int(i[4]):
        numberCounter = -1
    end = i[3] + i[4]
    path = i[0] + i[1]
    while path != end:
        tmp = path
        path = chr(ord(tmp[0]) + letterCounter)
        path += str(int(tmp[1]) + numberCounter)
        arrayPath.append(path)
    arrayPath.pop()
    return arrayPath


def whereIsKing(board, player):
    king = ""
    y = 9

    for row in board:
        y -= 1
        x = 0
        for piece in row:
            x += 1
            if piece == "r" and player == "WHITE":
                king = getArrayBoard.arrayToSquare(x, y)
            if piece == "R" and player == "BLACK":
                king = getArrayBoard.arrayToSquare(x, y)
    return king


def resultIsEnd(echec, isFinish, board, player, king):
    if echec == 0 and isFinish == 0:
        # print("Nothing")#TODO DEL
        return 0
    if echec == 1 and isFinish == 0:
        # print("Echec")#TODO DEL
        return 3
    if echec == 1 and isFinish == 1:
        # print("Mat")#TODO DEL
        return 2
    moovesTmp = possibleMooves(board, player, True)
    for i in moovesTmp:
        if i[0] != king[0] and i[1] != king[1]:
            # print("Nothing")  # TODO DEL
            return 0
    # print("Egal Pat")#TODO DEL
    return 1


# 0 == No / 1 == Nul / 2 == Mat / 3 == echec
def isEnd(board, player):
    global mooves, moovesCheck

    myMooves = possibleMooves(board, player, True)
    kingsMooves, mooves = [], []
    isFinish = 1
    chessAggressiv, eatChessAggressiv, echec = 0, 0, 0

    if player == "WHITE":
        enemyMooves = possibleMooves(board, "BLACK", True)
    else:
        enemyMooves = possibleMooves(board, "WHITE", True)

    king = whereIsKing(board, player)
    for i in myMooves:
        if len(king) != 0 and i[0] == king[0] and i[1] == king[1]:
            kingsMooves.append(i)
    # mooves of black
    for i in enemyMooves:
        # if adversaire is sur le roi
        if len(king) != 0 and i[3] == king[0] and i[4] == king[1]:
            echec = 1
            chessAggressiv += 1
            # pathOfAggressiv is the path that take the piece who can eat the king
            pathOfAggressiv = getPathOfPiece(i, board)
            for j in myMooves:
                # check if path can be cut by mypiece and check if the piece is not the king
                for k in pathOfAggressiv:
                    if j[3] == k[0] and j[4] == k[1] and (j[0] != king[0] or j[1] != king[1]):
                        eatChessAggressiv = 1
                        moovesCheck.append(j)
                # check if enemy piece can not be eat by one of my piece
                if i[0] == j[3] and i[1] == j[4] and (j[0] != king[0] or j[1] != king[1]):
                    eatChessAggressiv = 1
                    moovesCheck.append(j)

    isFinish = kingCanMooveIfCheck(board, isFinish, kingsMooves, player)

    # if chessAggressiv (piece qui font echec) = si une seule piece fait echec
    # eatChessAggressiv == si la piece qui fait echec peut se faire manger
    if chessAggressiv == 1 and eatChessAggressiv == 1:
        # print("Echec !")  # TODO DEL
        return 3

    if len(kingsMooves) == 0:
        isFinish = 0

    return resultIsEnd(echec, isFinish, board, player, king)


def kingCanMooveIfCheck(board, isFinish, kingsMooves, player):
    global moovesCheck

    for i in kingsMooves:
        array = getArrayBoard.squareToArray(i[0], int(i[1]))
        array2 = getArrayBoard.squareToArray(i[3], int(i[4]))
        pieceTmp = board[int(array2[1])][int(array2[0])]
        if player == "WHITE":
            board[int(array2[1])][int(array2[0])] = "r"
        else:
            board[int(array2[1])][int(array2[0])] = "R"
        board[int(array[1])][int(array[0])] = "."
        if player == "WHITE":
            enemyMooves = possibleMooves(board, "BLACK", True)
        else:
            enemyMooves = possibleMooves(board, "WHITE", True)
        tmp = 0
        for j in enemyMooves:
            if j[3] == i[3] and j[4] == i[4]:
                tmp = 1
        if tmp == 0:
            isFinish = 0
            moovesCheck.append(i)
        board[int(array2[1])][int(array2[0])] = pieceTmp
        if player == "WHITE":
            board[int(array[1])][int(array[0])] = "r"
        else:
            board[int(array[1])][int(array[0])] = "R"
    return isFinish


def removeImpossibleMoves(myMooves, board, player):
    index = 0
    myMoovesFilter = []
    for i in myMooves:
        array = getArrayBoard.squareToArray(i[0], int(i[1]))
        array2 = getArrayBoard.squareToArray(i[3], int(i[4]))
        myPiece = board[int(array[1])][int(array[0])]
        enemyPiece = board[int(array2[1])][int(array2[0])]

        board[int(array[1])][int(array[0])] = "."
        board[int(array2[1])][int(array2[0])] = myPiece
        end = isEnd(board, player)
        if end != 2 and end != 3:
            myMoovesFilter.append(i)
        board[int(array[1])][int(array[0])] = myPiece
        board[int(array2[1])][int(array2[0])] = enemyPiece
        index += 1
    return myMoovesFilter


def possibleMooves(board, player, comingFromFunctionEnd=False):
    global mooves
    global moovesCheck

    mooves = []
    y = 9

    enemyMooves = []
    if player == "WHITE" and not comingFromFunctionEnd:
        enemyMooves = possibleMooves(board, "BLACK", True)
    elif not comingFromFunctionEnd:
        enemyMooves = possibleMooves(board, "WHITE", True)

    mooves = []

    for row in board:
        y -= 1
        x = 0
        for piece in row:
            x += 1
            if piece == "p" and player == "WHITE":
                pawnMoove(board, player, x, y)
            elif piece == "P" and player == "BLACK":
                pawnMoove(board, player, x, y)
            if piece == "r" and player == "WHITE":
                kingMoove(board, player, x, y, enemyMooves, comingFromFunctionEnd)
            if piece == "R" and player == "BLACK":
                kingMoove(board, player, x, y, enemyMooves, comingFromFunctionEnd)
            if piece == "t" and player == "WHITE":
                towerMoove(board, player, x, y)
            if piece == "T" and player == "BLACK":
                towerMoove(board, player, x, y)
            if piece == "f" and player == "WHITE":
                bishopMoove(board, player, x, y)
            if piece == "F" and player == "BLACK":
                bishopMoove(board, player, x, y)
            if piece == "d" and player == "WHITE":
                bishopMoove(board, player, x, y)
                towerMoove(board, player, x, y)
            if piece == "D" and player == "BLACK":
                bishopMoove(board, player, x, y)
                towerMoove(board, player, x, y)
            if piece == "c" and player == "WHITE":
                knightMoove(board, player, x, y)
            if piece == "C" and player == "BLACK":
                knightMoove(board, player, x, y)
    myMooves = mooves
    # avoid depth
    if not comingFromFunctionEnd:
        myMooves = removeImpossibleMoves(myMooves, board, player)
        moovesCheck = []
        end = isEnd(board, player)
        if end == 3:
            return moovesCheck

    return myMooves

#isEnd(gameBoard, "WHITE")
# print(possibleMooves(gameBoard, "WHITE"))