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
               # The program will go over the whole grid and check whether there is at least one piece around the square that is checked or not.
               # using isSurrounded function. If not, then the state of the square will be changed to "Invalid"

#3RD VALIDATION: Based on a piece color that has to be placed on the board, the program will find valid squares to move the piece next to squares with pieces of opposite color on them.

#4RTH VALIDATION:


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

#==============================================================================================================================
#==============================================================================================================================
#======================================================THE 1ST VALIDATION======================================================
#==============================================================================================================================
#==============================================================================================================================


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

#The function checks whether whether there's piece in the NW from the testing square.
#The funciton return True if there's a piece.
def testNW(testingSquare, validMoves):

    squareNW = [0,0,'']
    squareNW[0] = testingSquare[0] - 1
    squareNW[1] = testingSquare[1] - 1

    #looking for the state of the square with the same coordinates and checks if it's on the board and checks if it's empty
    if onTheBoard(squareNW) == True:

        for square in range(len(validMoves)):

            if (validMoves[square][0] == squareNW[0] and
                validMoves[square][1] == squareNW[1]):

                if validMoves[square][2] != 'N' and validMoves[square][2] != "Invalid":
                    return True

#The function checks whether whether there's piece in the N from the testing square.
#The funciton return True if there's a piece.
def testN(testingSquare, validMoves):

    squareN = [0,0,'']
    squareN[0] = testingSquare[0]
    squareN[1] = testingSquare[1] - 1

    #looking for the state of the square with the same coordinates and checks if it's on the board and checks if it's empty
    if onTheBoard(squareN) == True:

        for square in range(len(validMoves)):

            if (validMoves[square][0] == squareN[0] and
                validMoves[square][1] == squareN[1]):

                if validMoves[square][2] != 'N' and validMoves[square][2] != "Invalid":
                    return True

#The function checks whether whether there's piece in the NE from the testing square.
#The funciton return True if there's a piece.
def testNE(testingSquare, validMoves):

    squareNE = [0,0,'']
    squareNE[0] = testingSquare[0] + 1
    squareNE[1] = testingSquare[1] - 1

    #looking for the state of the square with the same coordinates and checks if it's on the board and checks if it's empty
    if onTheBoard(squareNE) == True:

        for square in range(len(validMoves)):

            if (validMoves[square][0] == squareNE[0] and
                validMoves[square][1] == squareNE[1]):

                if validMoves[square][2] != 'N' and validMoves[square][2] != "Invalid":
                    return True

#The function checks whether whether there's piece in the W from the testing square.
#The funciton return True if there's a piece.
def testW(testingSquare, validMoves):

    squareW = [0,0,'']
    squareW[0] = testingSquare[0] - 1
    squareW[1] = testingSquare[1]

    #looking for the state of the square with the same coordinates and checks if it's on the board and checks if it's empty
    if onTheBoard(squareW) == True:

        for square in range(len(validMoves)):

            if (validMoves[square][0] == squareW[0] and
                validMoves[square][1] == squareW[1]):

                if validMoves[square][2] != 'N' and validMoves[square][2] != "Invalid":
                    return True

#The function checks whether whether there's piece in the E from the testing square.
#The funciton return True if there's a piece.
def testE(testingSquare, validMoves):

    squareE = [0,0,'']
    squareE[0] = testingSquare[0] + 1
    squareE[1] = testingSquare[1]

    #looking for the state of the square with the same coordinates and checks if it's on the board and checks if it's empty
    if onTheBoard(squareE) == True:

        for square in range(len(validMoves)):

            if (validMoves[square][0] == squareE[0] and
                validMoves[square][1] == squareE[1]):

                if validMoves[square][2] != 'N' and validMoves[square][2] != "Invalid":
                    return True

#The function checks whether whether there's piece in the SW from the testing square.
#The funciton return True if there's a piece.
def testSW(testingSquare, validMoves):

    squareSW = [0,0,'']
    squareSW[0] = testingSquare[0] - 1
    squareSW[1] = testingSquare[1] + 1

    #looking for the state of the square with the same coordinates and checks if it's on the board and checks if it's empty
    if onTheBoard(squareSW) == True:

        for square in range(len(validMoves)):

            if (validMoves[square][0] == squareSW[0] and
                validMoves[square][1] == squareSW[1]):

                if validMoves[square][2] != 'N' and validMoves[square][2] != "Invalid":
                    return True

#The function checks whether whether there's piece in the S from the testing square.
#The funciton return True if there's a piece.
def testS(testingSquare, validMoves):

    squareS = [0,0,'']
    squareS[0] = testingSquare[0]
    squareS[1] = testingSquare[1] + 1

    #looking for the state of the square with the same coordinates and checks if it's on the board and checks if it's empty
    if onTheBoard(squareS) == True:

        for square in range(len(validMoves)):

            if (validMoves[square][0] == squareS[0] and
                validMoves[square][1] == squareS[1]):

                if validMoves[square][2] != 'N' and validMoves[square][2] != "Invalid":
                    return True

#The function checks whether whether there's piece in the NW from the testing square.
#The funciton return True if there's a piece.
def testSE(testingSquare, validMoves):

    squareSE = [0,0,'']
    squareSE[0] = testingSquare[0] + 1
    squareSE[1] = testingSquare[1] + 1

    #looking for the state of the square with the same coordinates and checks if it's on the board and checks if it's empty
    if onTheBoard(squareSE) == True:

        for square in range(len(validMoves)):

            if (validMoves[square][0] == squareSE[0] and
                validMoves[square][1] == squareSE[1]):

                if validMoves[square][2] != 'N' and validMoves[square][2] != "Invalid":
                    return True

#The function checks whether there is at least one piece around the square.
#The function changes the state of the square if the square does not have pieces around it.
def secondValidation(validMoves):

    for square in range(len(validMoves)):
        if (testNW(validMoves[square], validMoves) != True and
            testN(validMoves[square], validMoves)  != True and
            testNE(validMoves[square], validMoves) != True and
            testW(validMoves[square], validMoves)  != True and
            testE(validMoves[square], validMoves)  != True and
            testSW(validMoves[square], validMoves) != True and
            testS(validMoves[square], validMoves)  != True and
            testSE(validMoves[square], validMoves) != True):

            validMoves[square][2] = "Invalid"

    return validMoves


#==============================================================================================================================
#==============================================================================================================================
#======================================================THE 3RD VALIDATION======================================================
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
#The function returns squares where that piece can be placed
def thirdValidation(pieceColor, validMoves):
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

    return validMoves



#==============================================================================================================================
#==============================================================================================================================
#======================================================THE 4TH VALIDATION======================================================
#==============================================================================================================================
#==============================================================================================================================



#The funciton gets the piece color that has to be placed on the board.
#If the color is Black, the color is changed to white.
#If the color is white, the color is changed to black.
def changeToOppositeColor(pieceColor):
    if pieceColor == "Black":
        pieceColor = "White"
        return pieceColor
    elif pieceColor == "White":
        pieceColor = "Black"
        return pieceColor
    elif pieceColor == "isW":
        pieceColor = "isB"
        return pieceColor
    elif pieceColor == "isB":
        pieceColor = "isW"
        return pieceColor

#the function checks if all pieces of the input list have the same color
def checkColorList(list):

    if len(list) == 3:
        return True

    if len(list) == 4:
        colorToShare = list[1] #assign a color that all pieces must share
        count = 0 #if the list is valid the counter has to have have value: len(list) - 1
        list.pop(0)
        list.pop(-1)

        if oppositeColor(list[0], list[1]) == False:
            return True
        else:
            return False

    if len(list) > 3:

        colorToShare = list[1] #assign a color that all pieces must share
        count = 0 #if the list is valid the counter has to have have value: len(list) - 1
        list.pop(0)
        list.pop(-1)

        for square in range(len(list)):
            if square != len(list) - 1:
                if oppositeColor(list[square], list[square+1]) == False:
                    count += 1
                elif oppositeColor(list[square], list[square-1]) == False:
                    count += 1

                if count == len(list):
                    return True
                else:
                    return False
    else:
        return False


#returns a color of the square that is located in the NW from the testing square
def returnColorNW(testingSquare, validMoves, pieceColor):

    retColorNW = [0,0,'']
    retColorNW[0] = testingSquare[0] - 1
    retColorNW[1] = testingSquare[1] - 1

    #looking for the state of the square with the same coordinates and checks if it's on the board and checks if it's empty
    if onTheBoard(retColorNW) == True:

        for square in range(len(validMoves)):

            if (validMoves[square][0] == retColorNW[0] and
                validMoves[square][1] == retColorNW[1]):
                retColorNW[2] = validMoves[square][2]

                return retColorNW

#The function checks whether whether there's a piece of opposite color in the NW from the testing square.
#The funciton return True if there's a piece.
def finalcheckNW(testingSquare, validMoves, pieceColor):

    listOfColors = []
    listOfColors.append(pieceColor) #the first piece color

    squareColor = returnColorNW(testingSquare, validMoves, pieceColor) #will assign the first N square

    while (squareColor[2] != "Invalid" and squareColor[2] != "N"):
           if squareColor[2] != "Invalid" and squareColor[2] != "N":
               listOfColors.append(squareColor[2])
           squareColor = returnColorNW(squareColor, validMoves, pieceColor)



    if listOfColors != []:
        return listOfColors


#returns a color of the square that is located in the N from the testing square
def returnColorN(testingSquare, validMoves, pieceColor):

    retColorN = [0,0,'']
    retColorN[0] = testingSquare[0]
    retColorN[1] = testingSquare[1] - 1

    #looking for the state of the square with the same coordinates and checks if it's on the board and checks if it's empty
    if onTheBoard(retColorN) == True:

        for square in range(len(validMoves)):

            if (validMoves[square][0] == retColorN[0] and
                validMoves[square][1] == retColorN[1]):

                retColorN[2] = validMoves[square][2]

                return retColorN

#The function checks whether whether there's a piece of opposite color in the NW from the testing square.
#The funciton return True if there's a piece.
def finalcheckN(testingSquare, validMoves, pieceColor):

    listOfColors = []
    listOfColors.append(pieceColor) #the first piece color

    squareColor = returnColorN(testingSquare, validMoves, pieceColor) #will assign the first N square

    while (squareColor[2] != "Invalid" and squareColor[2] != "N"):
           if squareColor[2] != "Invalid" and squareColor[2] != "N":
               listOfColors.append(squareColor[2])
           squareColor = returnColorN(squareColor, validMoves, pieceColor)



    if listOfColors != []:
        return listOfColors


#returns a color of the square that is located in the N from the testing square
def returnColorNE(testingSquare, validMoves, pieceColor):

    retColorNE = [0,0,'']
    retColorNE[0] = testingSquare[0] + 1
    retColorNE[1] = testingSquare[1] - 1

    #looking for the state of the square with the same coordinates and checks if it's on the board and checks if it's empty
    if onTheBoard(retColorNE) == True:

        for square in range(len(validMoves)):

            if (validMoves[square][0] == retColorNE[0] and
                validMoves[square][1] == retColorNE[1]):
                retColorNE[2] = validMoves[square][2]

                return retColorNE

#The function checks whether whether there's a piece of opposite color in the NW from the testing square.
#The funciton return True if there's a piece.
def finalcheckNE(testingSquare, validMoves, pieceColor):

    listOfColors = []
    listOfColors.append(pieceColor) #the first piece color

    squareColor = returnColorNE(testingSquare, validMoves, pieceColor) #will assign the first N square

    while (squareColor[2] != "Invalid" and squareColor[2] != "N"):
           if squareColor[2] != "Invalid" and squareColor[2] != "N":
               listOfColors.append(squareColor[2])
           squareColor = returnColorNE(squareColor, validMoves, pieceColor)



    if listOfColors != []:
        return listOfColors


#returns a color of the square that is located in the W from the testing square
def returnColorW(testingSquare, validMoves, pieceColor):

    retColorW = [0,0,'']
    retColorW[0] = testingSquare[0] - 1
    retColorW[1] = testingSquare[1]

    #looking for the state of the square with the same coordinates and checks if it's on the board and checks if it's empty
    if onTheBoard(retColorW) == True:

        for square in range(len(validMoves)):

            if (validMoves[square][0] == retColorW[0] and
                validMoves[square][1] == retColorW[1]):
                retColorW[2] = validMoves[square][2]

                return retColorW

#The function checks whether whether there's a piece of opposite color in the NW from the testing square.
#The funciton return True if there's a piece.
def finalcheckW(testingSquare, validMoves, pieceColor):

    listOfColors = []
    listOfColors.append(pieceColor) #the first piece color

    squareColor = returnColorW(testingSquare, validMoves, pieceColor) #will assign the first N square

    while (squareColor[2] != "Invalid" and squareColor[2] != "N"):
           if squareColor[2] != "Invalid" and squareColor[2] != "N":
               listOfColors.append(squareColor[2])
           squareColor = returnColorW(squareColor, validMoves, pieceColor)



    if listOfColors != []:
        return listOfColors


#returns a color of the square that is located in the E from the testing square
def returnColorE(testingSquare, validMoves, pieceColor):

    retColorE = [0,0,'']
    retColorE[0] = testingSquare[0] + 1
    retColorE[1] = testingSquare[1]

    #looking for the state of the square with the same coordinates and checks if it's on the board and checks if it's empty
    if onTheBoard(retColorE) == True:

        for square in range(len(validMoves)):

            if (validMoves[square][0] == retColorE[0] and
                validMoves[square][1] == retColorE[1]):
                retColorE[2] = validMoves[square][2]

                return retColorE

#The function checks whether whether there's a piece of opposite color in the NW from the testing square.
#The funciton return True if there's a piece.
def finalcheckE(testingSquare, validMoves, pieceColor):

    listOfColors = []
    listOfColors.append(pieceColor) #the first piece color

    squareColor = returnColorE(testingSquare, validMoves, pieceColor) #will assign the first N square

    while (squareColor[2] != "Invalid" and squareColor[2] != "N"):
           if squareColor[2] != "Invalid" and squareColor[2] != "N":
               listOfColors.append(squareColor[2])
           squareColor = returnColorE(squareColor, validMoves, pieceColor)



    if listOfColors != []:
        return listOfColors


#returns a color of the square that is located in the SE from the testing square
def returnColorSW(testingSquare, validMoves, pieceColor):

    retColorSW = [0,0,'']
    retColorSW[0] = testingSquare[0] - 1
    retColorSW[1] = testingSquare[1] + 1

    #looking for the state of the square with the same coordinates and checks if it's on the board and checks if it's empty
    if onTheBoard(retColorSW) == True:

        for square in range(len(validMoves)):

            if (validMoves[square][0] == retColorSW[0] and
                validMoves[square][1] == retColorSW[1]):
                retColorSW[2] = validMoves[square][2]

                return retColorSW

#The function checks whether whether there's a piece of opposite color in the NW from the testing square.
#The funciton return True if there's a piece.
def finalcheckSW(testingSquare, validMoves, pieceColor):

    listOfColors = []
    listOfColors.append(pieceColor) #the first piece color

    squareColor = returnColorSW(testingSquare, validMoves, pieceColor) #will assign the first N square

    while (squareColor[2] != "Invalid" and squareColor[2] != "N"):
           if squareColor[2] != "Invalid" and squareColor[2] != "N":
               listOfColors.append(squareColor[2])
           squareColor = returnColorSW(squareColor, validMoves, pieceColor)



    if listOfColors != []:
        return listOfColors


#returns a color of the square that is located in the SE from the testing square
def returnColorS(testingSquare, validMoves, pieceColor):

    retColorS = [0,0,'']
    retColorS[0] = testingSquare[0]
    retColorS[1] = testingSquare[1] + 1

    #looking for the state of the square with the same coordinates and checks if it's on the board and checks if it's empty
    if onTheBoard(retColorS) == True:

        for square in range(len(validMoves)):

            if (validMoves[square][0] == retColorS[0] and
                validMoves[square][1] == retColorS[1]):
                retColorS[2] = validMoves[square][2]

                return retColorS

#The function checks whether whether there's a piece of opposite color in the NW from the testing square.
#The funciton return True if there's a piece.
def finalcheckS(testingSquare, validMoves, pieceColor):

    listOfColors = []
    listOfColors.append(pieceColor) #the first piece color

    squareColor = returnColorS(testingSquare, validMoves, pieceColor) #will assign the first N square

    while (squareColor[2] != "Invalid" and squareColor[2] != "N"):
           if squareColor[2] != "Invalid" and squareColor[2] != "N":
               listOfColors.append(squareColor[2])
           squareColor = returnColorS(squareColor, validMoves, pieceColor)



    if listOfColors != []:
        return listOfColors


#returns a color of the square that is located in the SE from the testing square
def returnColorSE(testingSquare, validMoves, pieceColor):

    retColorSE = [0,0,'']
    retColorSE[0] = testingSquare[0] + 1
    retColorSE[1] = testingSquare[1] + 1

    #looking for the state of the square with the same coordinates and checks if it's on the board and checks if it's empty
    if onTheBoard(retColorSE) == True:

        for square in range(len(validMoves)):

            if (validMoves[square][0] == retColorSE[0] and
                validMoves[square][1] == retColorSE[1]):
                retColorSE[2] = validMoves[square][2]

                return retColorSE

#The function checks whether whether there's a piece of opposite color in the NW from the testing square.
#The funciton returns a list if there's a piece.
def finalcheckSE(testingSquare, validMoves, pieceColor):

    listOfColors = []
    listOfColors.append(pieceColor) #the first piece color

    squareColor = returnColorSE(testingSquare, validMoves, pieceColor) #will assign the first N square

    while (squareColor[2] != "Invalid" and squareColor[2] != "N"):
           if squareColor[2] != "Invalid" and squareColor[2] != "N":
               listOfColors.append(squareColor[2])
           squareColor = returnColorSE(squareColor, validMoves, pieceColor)



    if listOfColors != []:
        return listOfColors


#The final function:
#The will check NW, N, NE, W, E, SW, S, SE  of each square for a valid possible combination of moves.
#The valid combination of moves is a row, starting with a piece of the opposite color, following by the number of pieces that is >= 1, following by a piece of the opposite color.
#The function returns squares where that piece can be placed.
def fourthValidation(pieceColor, validMoves):

    for square in range(len(validMoves)):
        if validMoves[square][2] == "N":
            if ((testColorNW(validMoves[square], validMoves, pieceColor) != True or
                oppositeColor(finalcheckNW(validMoves[square], validMoves, pieceColor)[0], finalcheckNW(validMoves[square], validMoves, pieceColor)[-1]) != False or
                checkColorList(finalcheckNW(validMoves[square], validMoves, pieceColor)) != True) and

                (testColorN(validMoves[square], validMoves, pieceColor) != True or
                oppositeColor(finalcheckN(validMoves[square], validMoves, pieceColor)[0], finalcheckN(validMoves[square], validMoves, pieceColor)[-1]) != False or
                checkColorList(finalcheckN(validMoves[square], validMoves, pieceColor)) != True) and

                (testColorNE(validMoves[square], validMoves, pieceColor) != True or
                oppositeColor(finalcheckNE(validMoves[square], validMoves, pieceColor)[0], finalcheckNE(validMoves[square], validMoves, pieceColor)[-1]) != False or
                checkColorList(finalcheckNE(validMoves[square], validMoves, pieceColor)) != True) and

                (testColorW(validMoves[square], validMoves, pieceColor) != True or
                oppositeColor(finalcheckW(validMoves[square], validMoves, pieceColor)[0], finalcheckW(validMoves[square], validMoves, pieceColor)[-1]) != False or
                checkColorList(finalcheckW(validMoves[square], validMoves, pieceColor)) != True) and

                (testColorE(validMoves[square], validMoves, pieceColor) != True or
                oppositeColor(finalcheckE(validMoves[square], validMoves, pieceColor)[0], finalcheckE(validMoves[square], validMoves, pieceColor)[-1]) != False or
                checkColorList(finalcheckE(validMoves[square], validMoves, pieceColor)) != True) and

                (testColorSW(validMoves[square], validMoves, pieceColor) != True or
                oppositeColor(finalcheckSW(validMoves[square], validMoves, pieceColor)[0], finalcheckSW(validMoves[square], validMoves, pieceColor)[-1]) != False or
                checkColorList(finalcheckSW(validMoves[square], validMoves, pieceColor)) != True) and

                (testColorS(validMoves[square], validMoves, pieceColor) != True or
                oppositeColor(finalcheckS(validMoves[square], validMoves, pieceColor)[0], finalcheckS(validMoves[square], validMoves, pieceColor)[-1]) != False or
                checkColorList(finalcheckS(validMoves[square], validMoves, pieceColor)) != True) and

                (testColorSE(validMoves[square], validMoves, pieceColor) != True or
                oppositeColor(finalcheckSE(validMoves[square], validMoves, pieceColor)[0], finalcheckSE(validMoves[square], validMoves, pieceColor)[-1]) != False or
                checkColorList(finalcheckSE(validMoves[square], validMoves, pieceColor)) != True)):

                validMoves[square][2] = "Invalid"

    return validMoves


#the main function
def main():

    sampleGameState = "NNNNNNNNNNNNNNNNNNNNNWNNNNNWBNNNNNNBWNNNNNNNNNNNNNNNNNNNNNNNNNNN"

    validMoves = gameStateFromStringToList(sampleGameState)

    firstValidation(validMoves)

    secondValidation(validMoves)

    #figure out where to get the color of the piece
    thirdValidation("White", validMoves)

    for i in range(len(validMoves)):
        if validMoves[i][2] == "N":
            print("{}:{}".format(i, validMoves[i]))
    print("")
    fourthValidation("White", validMoves)

    for i in range(len(validMoves)):
        if validMoves[i][2] == "N":
            print("{}:{}".format(i, validMoves[i]))



if __name__ == "__main__":
	main()
