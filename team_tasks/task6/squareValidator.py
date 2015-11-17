import BoardGenerator as bg
import Constants

#==================================================================================================================================
#==================================================================================================================================
#=================================================================DOCUMENTATION====================================================
#==================================================================================================================================
#==================================================================================================================================

#Author: Anton Lysov

#The Idea: We create a list that consists of squares of the board and assume that all squares are valid moves.
#After a series of validation tests we get a list of squares that only consists of valid steps (the state of the square is not valid to "Invalid").
#So, the computer can randomly choose one of them and the player won't be able to click invalid squares.


#1ST STEP:
#The program gets a game state as a string and converts it into a list using gameStateFromStringToList function

#2nd STEP:
#1ST VALIDATION: A piece cannot be placed on a square with another piece on it.
               # The program will go over the whole grid and check whether there is aready a piece on a square or not
               # using isAlreadyAPiece funciton. If not, then the state of the square will be changed to "Invalid"

#2ND VALIDATION: A piece cannot be placed on a square that is not surrounded by at least one piece
               # The program will go over the whole grid and check whether there is at least one piece of opposite color around the square that is checked.


#The function checks whether the coordiantes of the square are valid or not.
#The function returns True if the coordiantes of a testing square are valid.
def onTheBoard(testingSquare):

    if (testingSquare[0] >= 1 and
        testingSquare[0] <= 8 and
        testingSquare[1] >= 1 and
        testingSquare[1] <= 8):

        return True

#The function gets a game state string and converts it into a list validMoves.
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


#The function checks whether there's already a piece on a testing square or not. and returns True if conditions are met.
#The funciton returns True if there's already a piece on a testing square.
def isAlreadyAPiece(testingSquare):
    if testingSquare[2] == "B" or testingSquare[2] == "W":
        return True

#The function checks whether there's already a piece on a testing square or not. and returns True if conditions are met.
#The funciton changes the state of the square if there's already a piece on a testing square .
def firstValidation(validMoves):

    for square in range(len(validMoves)):
        if isAlreadyAPiece(validMoves[square]) == True:
            validMoves[square][2] = "is" + validMoves[square][2]

    return validMoves


#==============================================================================================================================
#==============================================================================================================================
#======================================================THE 2ND VALIDATION======================================================
#==============================================================================================================================
#==============================================================================================================================


#The funciton gets the piece color that has to be placed on the board.
#If the color is opposite to the color of the testing piece, the function returns True
#If the color is the same to the color of the testing piece, the function returns False
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

#The function checks whether whether there's a piece of opposite color in the NW from the testing square.
#The funciton return True if there's a piece.
def testColorNW(testingSquare, validMoves, color):

    testColorNW = [0,0,'']
    testColorNW[0] = testingSquare[0] - 1
    testColorNW[1] = testingSquare[1] - 1

    #looking for the state of the square with the same coordinates and checks if it's on the board and checks if it's empty
    if onTheBoard(testColorNW) == True:

        for square in range(len(validMoves)):

            if (validMoves[square][0] == testColorNW[0] and
                validMoves[square][1] == testColorNW[1]):

                if oppositeColor(color, validMoves[square][2]):
                    return True
                else:
                    return False

#The function checks whether whether there's a piece of opposite color in the N from the testing square.
#The funciton return True if there's a piece.
def testColorN(testingSquare, validMoves, color):

    testColorN = [0,0,'']
    testColorN[0] = testingSquare[0]
    testColorN[1] = testingSquare[1] - 1

    #looking for the state of the square with the same coordinates and checks if it's on the board and checks if it's empty
    if onTheBoard(testColorN) == True:

        for square in range(len(validMoves)):

            if (validMoves[square][0] == testColorN[0] and
                validMoves[square][1] == testColorN[1]):

                if oppositeColor(color, validMoves[square][2]):
                    return True

#The function checks whether whether there's a piece of opposite color in the NE from the testing square.
#The funciton return True if there's a piece.
def testColorNE(testingSquare, validMoves, color):

    testColorNE = [0,0,'']
    testColorNE[0] = testingSquare[0] + 1
    testColorNE[1] = testingSquare[1] - 1

    #looking for the state of the square with the same coordinates and checks if it's on the board and checks if it's empty
    if onTheBoard(testColorNE) == True:

        for square in range(len(validMoves)):

            if (validMoves[square][0] == testColorNE[0] and
                validMoves[square][1] == testColorNE[1]):

                if oppositeColor(color, validMoves[square][2]):
                    return True

#The function checks whether whether there's a piece of opposite color in the W from the testing square.
#The funciton return True if there's a piece.
def testColorW(testingSquare, validMoves, color):

    testColorW = [0,0,'']
    testColorW[0] = testingSquare[0] - 1
    testColorW[1] = testingSquare[1]

    #looking for the state of the square with the same coordinates and checks if it's on the board and checks if it's empty
    if onTheBoard(testColorW) == True:

        for square in range(len(validMoves)):

            if (validMoves[square][0] == testColorW[0] and
                validMoves[square][1] == testColorW[1]):

                if oppositeColor(color, validMoves[square][2]):
                    return True

#The function checks whether whether there's a piece of opposite color in the E from the testing square.
#The funciton return True if there's a piece.
def testColorE(testingSquare, validMoves, color):

    testColorE = [0,0,'']
    testColorE[0] = testingSquare[0] + 1
    testColorE[1] = testingSquare[1]

    #looking for the state of the square with the same coordinates and checks if it's on the board and checks if it's empty
    if onTheBoard(testColorE) == True:

        for square in range(len(validMoves)):

            if (validMoves[square][0] == testColorE[0] and
                validMoves[square][1] == testColorE[1]):

                if oppositeColor(color, validMoves[square][2]):
                    return True

#The function checks whether whether there's a piece of opposite color in the SW from the testing square.
#The funciton return True if there's a piece.
def testColorSW(testingSquare, validMoves, color):

    testColorSW = [0,0,'']
    testColorSW[0] = testingSquare[0] - 1
    testColorSW[1] = testingSquare[1] + 1

    #looking for the state of the square with the same coordinates and checks if it's on the board and checks if it's empty
    if onTheBoard(testColorSW) == True:

        for square in range(len(validMoves)):

            if (validMoves[square][0] == testColorSW[0] and
                validMoves[square][1] == testColorSW[1]):

                if oppositeColor(color, validMoves[square][2]):
                    return True

#The function checks whether whether there's a piece of opposite color in the S from the testing square.
#The funciton return True if there's a piece.
def testColorS(testingSquare, validMoves, color):

    testColorS = [0,0,'']
    testColorS[0] = testingSquare[0]
    testColorS[1] = testingSquare[1] + 1

    #looking for the state of the square with the same coordinates and checks if it's on the board and checks if it's empty
    if onTheBoard(testColorS) == True:

        for square in range(len(validMoves)):

            if (validMoves[square][0] == testColorS[0] and
                validMoves[square][1] == testColorS[1]):

                if oppositeColor(color, validMoves[square][2]):
                    return True

#The function checks whether whether there's a piece of opposite color in the SE from the testing square.
#The funciton return True if there's a piece.
def testColorSE(testingSquare, validMoves, color):

    testColorSE = [0,0,'']
    testColorSE[0] = testingSquare[0] + 1
    testColorSE[1] = testingSquare[1] + 1

    #looking for the state of the square with the same coordinates and checks if it's on the board and checks if it's empty
    if onTheBoard(testColorSE) == True:

        for square in range(len(validMoves)):

            if (validMoves[square][0] == testColorSE[0] and
                validMoves[square][1] == testColorSE[1]):

                if oppositeColor(color, validMoves[square][2]):
                    return True


#The function gets the color of a piece and is looking for squares with an opposite piece color on it
#The function returns a list of squares where that piece can be placed
def secondValidation(validMoves, pieceColor):
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


#==============================================================================================================================
#==============================================================================================================================
#======================================================THE MAIN FUNCTION=======================================================
#==============================================================================================================================
#==============================================================================================================================


#the main function
def mainSquareValidator(game_state, pieceColor):

    #The program gets a game state as a string and converts it into a validMoves list
    validMoves = gameStateFromStringToList(game_state)

    #The program will go over the whole grid and check whether there is aready a piece on a square or not
    validMoves = firstValidation(validMoves)

    if pieceColor == Constants.PIECE_WHITE:
        pieceColor = "White"
    else:
        pieceColor = "Black"

    #The program will go over the whole grid and check whether there is at least one piece of opposite color around the square that is checked.
    listOfValidMoves = secondValidation(validMoves, pieceColor)

    movesList = []
    
    for location in listOfValidMoves:
        x, y, piece = location
        letter = Constants.COLUMN_LETTERS[x - 1]
        number = Constants.ROW_NUMBERS[y - 1]
        movesList.append(letter + str(number))

    return movesList

if __name__ == "__main__":

    #TEST
    sampleGameState = bg.generate(False, False)
    print(sampleGameState)

    print(mainSquareValidator(sampleGameState, "Black"))
