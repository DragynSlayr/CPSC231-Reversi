#Checks each square in the grid and returns a list of valid of moves based on the current game state

#Author: Anton Lysov


import BoardGenerator as bg
import Constants

#Checks whether the coordiantes of the square are valid
#Params: testedSquare: the square's coordianates
#Returns: True
def onTheBoard(testedSquare):

    if (testedSquare[0] >= 1 and
        testedSquare[0] <= 8 and
        testedSquare[1] >= 1 and
        testedSquare[1] <= 8):

        return True

#Gets a game state string and converts it into a list validMoves
#Params: gameStateString: the current game state stored in a string
#Returns: validMoves: the current list of valid moves
def gameStateFromStringToList(gameStateString):

    #Creates initial list of possible valid steps
    validMoves = []
    for y in range(1,9):
        for x in range(1,9):
            validMoves.append([x,y])

    #Assign the state (N or B or W) sign from the game state string to each member of a list
    count = 0
    for state in gameStateString:
        validMoves[count].append(state)
        count += 1

    return validMoves

#Checks whether there's already a piece on the tested square
#Params: testedSquare: the square's coordianates
#Returns: True
def isAlreadyPieceOnSquare(testedSquare):
    if testedSquare[2] == "B" or testedSquare[2] == "W":
        return True

#Checks the whole grid and makes the squares that already have a piece invalid
#Params: validMoves: the current list of valid moves
#Returns: validMoves: updated list of valid moves
def testPieceOnSquares(validMoves):

    for square in range(len(validMoves)):
        if isAlreadyPieceOnSquare(validMoves[square]) == True:
            validMoves[square][2] = "is" + validMoves[square][2]

    return validMoves

#Checks whether color of the input pieces are opposite
#Params:        color: the color of the first piece
#        colorToMatch: the color of the second piece
#Returns: True
#        False
def oppositeColor(color, colorToMatch):
    if (color == "Black" and colorToMatch == "isW" or
        color == "White" and colorToMatch == "isB" or
        color == "isW" and colorToMatch == "Black" or
        color == "isB" and colorToMatch == "White"):
        return True
    elif (color == "Black" and colorToMatch == "isB" or
          color == "White" and colorToMatch == "isW" or
          color == "isB" and colorToMatch == "Black" or
          color == "Black" and colorToMatch == "White"):
          return False


#Checks whether there's a piece of opposite color in the NW from the tested square
#Params: testedSquare: the square's coordianates
#                color: the color of the piece
#           validMoves: the current list of valid moves
#Returns: True
def testColorNW(testedSquare, validMoves, color):

    testColorNW = [0,0,'']
    testColorNW[0] = testedSquare[0] - 1
    testColorNW[1] = testedSquare[1] - 1

    #looking for the state of the square with the same coordinates and checks whether it's on the board and empty
    if onTheBoard(testColorNW) == True:

        for square in range(len(validMoves)):

            if (validMoves[square][0] == testColorNW[0] and
                validMoves[square][1] == testColorNW[1]):

                if oppositeColor(color, validMoves[square][2]):
                    return True
                else:
                    return False

#Checks whether there's a piece of opposite color in the N from the tested square
#Params: testedSquare: the square's coordianates
#                color: the color of the piece
#           validMoves: the current list of valid moves
#Returns: True
def testColorN(testedSquare, validMoves, color):

    testColorN = [0,0,'']
    testColorN[0] = testedSquare[0]
    testColorN[1] = testedSquare[1] - 1

    #looking for the state of the square with the same coordinates and checks whether it's on the board and empty
    if onTheBoard(testColorN) == True:

        for square in range(len(validMoves)):

            if (validMoves[square][0] == testColorN[0] and
                validMoves[square][1] == testColorN[1]):

                if oppositeColor(color, validMoves[square][2]):
                    return True

#Checks whether there's a piece of opposite color in the NE from the tested square
#Params: testedSquare: the square's coordianates
#                color: the color of the piece
#           validMoves: the current list of valid moves
#Returns: True
def testColorNE(testedSquare, validMoves, color):

    testColorNE = [0,0,'']
    testColorNE[0] = testedSquare[0] + 1
    testColorNE[1] = testedSquare[1] - 1

    #looking for the state of the square with the same coordinates and checks whether it's on the board and empty
    if onTheBoard(testColorNE) == True:

        for square in range(len(validMoves)):

            if (validMoves[square][0] == testColorNE[0] and
                validMoves[square][1] == testColorNE[1]):

                if oppositeColor(color, validMoves[square][2]):
                    return True

#Checks whether there's a piece of opposite color in the W from the tested square
#Params: testedSquare: the square's coordianates
#                color: the color of the piece
#           validMoves: the current list of valid moves
#Returns: True
def testColorW(testedSquare, validMoves, color):

    testColorW = [0,0,'']
    testColorW[0] = testedSquare[0] - 1
    testColorW[1] = testedSquare[1]

    #looking for the state of the square with the same coordinates and checks whether it's on the board and empty
    if onTheBoard(testColorW) == True:

        for square in range(len(validMoves)):

            if (validMoves[square][0] == testColorW[0] and
                validMoves[square][1] == testColorW[1]):

                if oppositeColor(color, validMoves[square][2]):
                    return True

#Checks whether there's a piece of opposite color in the E from the tested square
#Params: testedSquare: the square's coordianates
#                color: the color of the piece
#           validMoves: the current list of valid moves
#Returns: True
def testColorE(testedSquare, validMoves, color):

    testColorE = [0,0,'']
    testColorE[0] = testedSquare[0] + 1
    testColorE[1] = testedSquare[1]

    #looking for the state of the square with the same coordinates and checks whether it's on the board and empty
    if onTheBoard(testColorE) == True:

        for square in range(len(validMoves)):

            if (validMoves[square][0] == testColorE[0] and
                validMoves[square][1] == testColorE[1]):

                if oppositeColor(color, validMoves[square][2]):
                    return True

#Checks whether there's a piece of opposite color in the SW from the tested square
#Params: testedSquare: the square's coordianates
#                color: the color of the piece
#           validMoves: the current list of valid moves
#Returns: True
def testColorSW(testedSquare, validMoves, color):

    testColorSW = [0,0,'']
    testColorSW[0] = testedSquare[0] - 1
    testColorSW[1] = testedSquare[1] + 1

    #looking for the state of the square with the same coordinates and checks whether it's on the board and empty
    if onTheBoard(testColorSW) == True:

        for square in range(len(validMoves)):

            if (validMoves[square][0] == testColorSW[0] and
                validMoves[square][1] == testColorSW[1]):

                if oppositeColor(color, validMoves[square][2]):
                    return True

#Checks whether there's a piece of opposite color in the S from the tested square
#Params: testedSquare: the square's coordianates
#                color: the color of the piece
#           validMoves: the current list of valid moves
#Returns: True
def testColorS(testedSquare, validMoves, color):

    testColorS = [0,0,'']
    testColorS[0] = testedSquare[0]
    testColorS[1] = testedSquare[1] + 1

    #looking for the state of the square with the same coordinates and checks whether it's on the board and empty
    if onTheBoard(testColorS) == True:

        for square in range(len(validMoves)):

            if (validMoves[square][0] == testColorS[0] and
                validMoves[square][1] == testColorS[1]):

                if oppositeColor(color, validMoves[square][2]):
                    return True

#Checks whether there's a piece of opposite color in the SE from the tested square
#Params: testedSquare: the square's coordianates
#                color: the color of the piece
#           validMoves: the current list of valid moves
#Returns: True
def testColorSE(testedSquare, validMoves, color):

    testColorSE = [0,0,'']
    testColorSE[0] = testedSquare[0] + 1
    testColorSE[1] = testedSquare[1] + 1

    #looking for the state of the square with the same coordinates and checks whether it's on the board and empty
    if onTheBoard(testColorSE) == True:

        for square in range(len(validMoves)):

            if (validMoves[square][0] == testColorSE[0] and
                validMoves[square][1] == testColorSE[1]):

                if oppositeColor(color, validMoves[square][2]):
                    return True

#Checks for the opposite color squares around the tested square
#Params: validMoves: the current list of valid moves
#        pieceColor: the color of the piece
#Returns: listOfValidMoves: updated list of valid moves
def testColorAroundSquare(validMoves, pieceColor):
    for square in range(len(validMoves)):
        if validMoves[square][2] == "N":
            if (testColorNW(validMoves[square], validMoves, pieceColor) != True and
                testColorN(validMoves[square], validMoves, pieceColor)  != True and
                testColorNE(validMoves[square], validMoves, pieceColor) != True and
                testColorW(validMoves[square], validMoves, pieceColor)  != True and
                testColorE(validMoves[square], validMoves, pieceColor)  != True and
                testColorSW(validMoves[square], validMoves, pieceColor) != True and
                testColorS(validMoves[square], validMoves, pieceColor)  != True and
                testColorSE(validMoves[square], validMoves, pieceColor) != True):

                validMoves[square][2] = "Invalid"

    listOfValidMoves = []

    for square in range(len(validMoves)):
        if validMoves[square][2] == "N":
            listOfValidMoves.append(validMoves[square])

    return listOfValidMoves

#The main function.
#Params: game_state: the current game state stored in a string
#        pieceColor: the color of the piece placed on the tested square
#Returns: movesList: list of valid moves
def mainSquareValidator(game_state, pieceColor):

    #Gets a game state string and converts it into a list validMoves
    validMoves = gameStateFromStringToList(game_state)

    #Checks the whole grid and makes the squares that already have a piece invalid
    validMoves = testPieceOnSquares(validMoves)

    if pieceColor == Constants.PIECE_WHITE:
        pieceColor = "White"
    else:
        pieceColor = "Black"

    #Checks the whole grid and makes the squares that already have a piece invalid
    listOfValidMoves = testColorAroundSquare(validMoves, pieceColor)

    movesList = []

    for location in listOfValidMoves:
        x, y, piece = location
        letter = Constants.COLUMN_LETTERS[x - 1]
        number = Constants.ROW_NUMBERS[y - 1]
        movesList.append(letter + str(number))

    return movesList

if __name__ == "__main__":

    #Test code
    sampleGameState = bg.generate(False, False)
    print(sampleGameState)

    print(mainSquareValidator(sampleGameState, "Black"))
