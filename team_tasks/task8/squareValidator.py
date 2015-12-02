#Checks each square in the grid and returns a list of valid of moves based on the current game state

#Author: Anton Lysov

import constants

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
#Params:   pieceColor: the color of the first piece
#        colorToMatch: the color of the second piece
#Returns: True
#        False
def oppositeColor(pieceColor, colorToMatch):
    if (pieceColor == "Black" and colorToMatch == "isW" or
        pieceColor == "White" and colorToMatch == "isB" or
        pieceColor == "isW"   and colorToMatch == "Black" or
        pieceColor == "isB"   and colorToMatch == "White"):
        return True
    elif (pieceColor == "Black" and colorToMatch == "isB" or
          pieceColor == "White" and colorToMatch == "isW" or
          pieceColor == "isB"   and colorToMatch == "Black" or
          pieceColor == "Black" and colorToMatch == "White"):
          return False


#Checks whether there's a piece of opposite color in the position from the tested square
#Params: testedSquare: the square's coordianates
#          pieceColor: the color of the piece
#          validMoves: the current list of valid moves
#       horizontalPos: the horizontal coordinate of the tested square
#         verticalPos: the vertical coordinate of the tested square
#Returns: True
def testColor(testedSquare, validMoves, pieceColor, horizontalPos, verticalPos):

    testColorNW = [0,0,'']
    testColorNW[0] = testedSquare[0] + horizontalPos
    testColorNW[1] = testedSquare[1] + verticalPos

    #looking for the state of the square with the same coordinates and checks whether it's on the board and empty
    if onTheBoard(testColorNW) == True:

        for square in range(len(validMoves)):

            if (validMoves[square][0] == testColorNW[0] and
                validMoves[square][1] == testColorNW[1]):

                if oppositeColor(pieceColor, validMoves[square][2]):
                    return True
                else:
                    return False

#Checks for the opposite color squares around the tested square
#Params: validMoves: the current list of valid moves
#        pieceColor: the color of the piece
#Returns: listOfValidMoves: updated list of valid moves
def testColorAroundSquare(validMoves, pieceColor):
    for square in range(len(validMoves)):
        if validMoves[square][2] == "N":
            if (testColor(validMoves[square], validMoves, pieceColor, -1, -1) != True and  #tests the North-West
                testColor(validMoves[square], validMoves, pieceColor,  0, -1) != True and  #tests the North
                testColor(validMoves[square], validMoves, pieceColor,  1, -1) != True and  #tests the North-East
                testColor(validMoves[square], validMoves, pieceColor, -1,  0) != True and  #tests the West
                testColor(validMoves[square], validMoves, pieceColor,  1,  0) != True and  #tests the East
                testColor(validMoves[square], validMoves, pieceColor, -1,  1) != True and  #tests the South-West
                testColor(validMoves[square], validMoves, pieceColor,  0,  1) != True and  #tests the South
                testColor(validMoves[square], validMoves, pieceColor,  1,  1) != True):    #tests the South-East

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

    if pieceColor == constants.PIECE_WHITE:
        pieceColor = "White"
    else:
        pieceColor = "Black"

    #Checks the whole grid and makes the squares that already have a piece invalid
    listOfValidMoves = testColorAroundSquare(validMoves, pieceColor)

    movesList = []

    for location in listOfValidMoves:
        x, y, piece = location
        letter = constants.COLUMN_LETTERS[x - 1]
        number = constants.ROW_NUMBERS[y - 1]
        movesList.append(letter + str(number))

    return movesList
