# Write a function that takes the current game state as a parameter,
# prompts the user for a move,
# validates the specified move (reprompt if not valid)
# and returns the update game state.
# It should use the function written by team member 1.

import Constants
import Converter
import StringInterpret as si

#Checks if a column is near the edges of the board
#Params: column, The column to check
#Returns: True if the column is an edge one, False otherwise
def isEdgeColumn(column):
    return (column == Constants.COLUMN_LETTERS[0] or column == Constants.COLUMN_LETTERS[len(Constants.COLUMN_LETTERS) - 1])

#Checks if a row is near the edges of the board
#Params: row, The row to check
#Returns: True if the row is an edge one, False otherwise
def isEdgeRow(row):
    return (row == Constants.ROW_NUMBERS[0] or row == Constants.ROW_NUMBERS[len(Constants.ROW_NUMBERS) - 1])

#Checks if a point is a corner
#Params: column, The column of the point
#        row, The row of the point
#Returns: True if the point is a corner, False otherwise
def isCorner(column, row):
    return isEdgeColumn(column) and isEdgeRow(row)

#Get the index of the corner represented by a point
#Params: column, The column of the point
#        row, The row of the point
#Returns: The index of the corner represented by:
# |1|~|~|~|~|~|~|2|
# |~|~|~|~|~|~|~|~|
# |~|~|~|~|~|~|~|~|
# |~|~|~|~|~|~|~|~|
# |~|~|~|~|~|~|~|~|
# |~|~|~|~|~|~|~|~|
# |~|~|~|~|~|~|~|~|
# |3|~|~|~|~|~|~|4|
def getCorner(column, row):
    if column == Constants.COLUMN_LETTERS[0]:#Column A
        if row == Constants.ROW_NUMBERS[0]:#Row 1
            return 1
        else:
            return 3
    else:#Column H
        if row == Constants.ROW_NUMBERS[0]:#Row 1
            return 2
        else:
            return 4

#Converts a 2D point to a 1D index
#Params: column, The column of the point
#        row, The row of the point
#Returns: Index of a point
#Example: calculateIndex("C", 5) returns 34
def calculateIndex(column, row):
    return Constants.COLUMN_LETTERS.index(column) + (Constants.ROW_NUMBERS.index(row) * 8)

#Gets a letter from a game state using a point
#Params: column, The column of the point
#        row, The row of the point
#        game_state, The state of the game
#Returns: The letter at the point
def getPieceAt(column, row, game_state):
    index = calculateIndex(column, row)
    return game_state[index]

#Gets whether the column's modifier is negative or positive
#Params: column_index, The index of the column
#Returns: 1 if the column_index is odd, -1 otherwise
def getColumnModifier(column_index):
    if column_index % 2 == 1:
        return 1
    else:
        return -1

#Get whether the row's modifier is positive or negative
#Params: row_index, The index of the row
#Returns: 1 if the row_index is odd, -1 otherwise
def getRowModifier(row_index):
    if row_index % 2 == 1:
        return 1
    else:
        return -1

#Get whether the row's modifier is positive or negative
#Params: corner_index, The index of the corner
#Returns: 1 if the corner_index is 1 or 2, -1 otherwise
def getRowSignOfCorner(corner_index):
    if corner_index <= 2:
        return 1
    else:
        return -1

#Gets the identifier of an index in a corner relative to the user's move
#Params: corner_index, The index of the corner
#        order_index, The index of the position relative to the corner
#Returns a string that represents the order_index's position relative to the corner
def getIdentifierOfCorner(corner_index, order_index):
    if order_index == 1:
        if corner_index % 2 == 1:
            return "R"
        else:
            return "L"
    elif order_index == 2:
        if corner_index <= 2:
            return "B"
        else:
            return "T"
    else:
        #Return a combination of T or B and R or L
        return getIdentifierOfCorner(corner_index, 2) + getIdentifierOfCorner(corner_index, 1)

#Gets all the pieces surrounding a corner
#Params: game_state, The current state of the game
#        corner_index, The index of the corner
#        column, The current column, either 'A' or 'H'
#        row, The current row, either 1 or 8
#Returns: A list containing 4 objects that represent a position and it's realation to the corner
#Notes: Corner indices are as follows, top corner are 1 and 2 bottom are 3 and 4
def piecesByCorner(game_state, corner_index, column, row):
    pieces = []
    order_index = 0
    column_sign = getColumnModifier(corner_index)
    row_sign = getRowSignOfCorner(corner_index)
    for i in range(2):
        for j in range(2):
            if order_index > 0:
                identifier = getIdentifierOfCorner(corner_index, order_index)
            else:
                identifier = "C"
            pieces.append(getPieceAt(chr(ord(column) + (j * column_sign)), row + (i * row_sign), game_state) + ":" + identifier)
            order_index += 1
    return pieces

#Counts how many places in a list are occupied by "B" or "W":
#Params: pieces, The list to check
#Returns: A count of the number of indexs in the list that start with "B" or "W"
def countFilledSpaces(pieces):
    count = 0
    for i in pieces:
        piece = i[:1]
        if piece == Constants.PIECE_BLACK or piece == Constants.PIECE_WHITE:
            count += 1
    return count

#Gets the index of a column
#Params: column, The column to get the index for
#Returns: 1 if left-most column, 2 otherwise
def getColumn(column):
    if column == Constants.COLUMN_LETTERS[0]:
        return 1
    else:
        return 2

#Gets an identifier for a piece in a column
#Params: column_index, The index of the column
#        order_index, The index of the piece
#Returns: A unique identifier for the piece
def getColumnIdentifier(column_index, order_index):
    if column_index == 1:
        order = ["T", "TR", "", "R", "B", "BR"]
        return order[order_index]
    else:
        order = ["T", "TL", "", "L", "B", "BL"]
        return order[order_index]

#Gets a list of all pieces around a point near the edge of the board
#Params: game_state, The current state of the game
#        column_index, The index of the column, either 1 or 2
#        column, The column, either 'A' or 'H'
#        row, The row
#Returns: A list of pieces around the point (column, row)
def piecesByColumn(game_state, column_index, column, row):
    pieces = []
    order_index = 0
    column_sign = getColumnModifier(column_index)
    for i in range(3):
        for j in range(2):
            if order_index == 2:
                identifier = "C"
            else:
                identifier = getColumnIdentifier(column_index, order_index)
            pieces.append(getPieceAt(chr(ord(column) + (j * column_sign)), row + (i - 1), game_state) + ":" + identifier)
            order_index += 1
    return pieces

#Gets the index of the row near the top or bottom of the board
#Params: row, The row check
#Returns: 1 if row is 1, 2 otherwise
def getRow(row):
    if row == Constants.ROW_NUMBERS[0]:
        return 1
    else:
        return 2

#Get the identifier for a row
#Params: row_index, The index of the row, either 1 or 2
#        order_index, The piece number in relation to the point
#Returns: A unique identifier for the relation between a point and the order_index
def getRowIdentifier(row_index, order_index):
    if row_index == 1:
        order = ["L", "", "R", "BL", "B", "BR"]
        return order[order_index]
    else:
        order = ["L", "", "R", "TL", "T", "TR"]
        return order[order_index]

#Gets a list of all the pieces by a point near the top or bottom of the board
#Params: game_state, The current state of the game
#        row_index, The index of the row, either 1 or 2
#        column, The column
#        row, The row, either 1 or 2
def piecesByRow(game_state, row_index, column, row):
    pieces = []
    order_index = 0
    row_sign = getRowModifier(row_index)
    for i in range(2):
        for j in range(3):
            if order_index == 1:
                identifier = "C"
            else:
                identifier = getRowIdentifier(row_index, order_index)
            pieces.append(getPieceAt(chr(ord(column) + (j - 1)), row + (i * row_sign), game_state) + ":" + identifier)
            order_index += 1
    return pieces

#Get an identifer for a point in relation to another
#Params: order_index, The index of the position
#Returns: A unique identifer for the index
def getPointIdentifier(order_index):
    order = ["TL", "T", "TR", "L", "C", "R", "BL", "B", "BR"]
    return order[order_index]

#Gets a list of all pieces around a point
#Params: game_state, The current state of the game
#        column, The column of the point
#        row, The row of the point
#Returns: A list of all pieces around the point (column, row)
def piecesByPoint(game_state, column, row):
    pieces = []
    order_index = 0
    for i in range(3):
        for j in range(3):
            identifier = getPointIdentifier(order_index)
            pieces.append(getPieceAt(chr(ord(column) + (j - 1)), row + (i - 1), game_state) + ":" + identifier)
            order_index += 1
    return pieces

#Checks whether a move is close to another piece on the board
#Params: move, The move to check
#        game_state, The curent state of the game
#Returns: True if the move is adjacent to another piece, False otherwise
def isValidMove(move, game_state):
    #Extract row and column
    row = int(move[1:])
    column = move[:1].upper()

    #Check if the move is on the board at all
    if (column in Constants.COLUMN_LETTERS) and (row in Constants.ROW_NUMBERS):
        #Make sure that position is empty
        if getPieceAt(column, row, game_state) != "N":
            return False
        else:
            if isCorner(column, row):#Check if move is a corner
                #Identify the corner
                corner_index = getCorner(column, row)

                #Get pieces around corner
                surrounding_pieces = piecesByCorner(game_state, corner_index, column, row)
            elif isEdgeColumn(column):#Check for column near edges
                #Identify column
                column_index = getColumn(column)

                #Get pieces around move
                surrounding_pieces = piecesByColumn(game_state, column_index, column, row)
            elif isEdgeRow(row):#Check for row near edges
                #Identify row
                row_index = getRow(row)

                #Get pieces around move
                surrounding_pieces = piecesByRow(game_state, row_index, column, row)
            else:#Move must be near the middle
                #Get pieces around move
                surrounding_pieces = piecesByPoint(game_state, column, row)

            #Count number of pieces near the point
            filled_spaces = countFilledSpaces(surrounding_pieces)

            #Move is valid if at least 1 piece is near the move
            return filled_spaces >= 1
    else:
        #Piece not on board
        return False

#Test the validate method with user input
#Params: game_state, The state of the game
#Returns: None
def testWithInput(game_state):
    move = input("Enter a move: ")
    while not isValidMove(move, game_state):
        print("Not valid!")
        move = input("Enter a move: ")

#Gets all possible moves
#Params: game_state, The current game's state
#Returns: A list of possible moves
def getValidMoves(game_state):
    valid_moves = []
    for y in range(len(game_state)):
        for x in range(len(game_state[y])):
            column = Constants.COLUMN_LETTERS[y]
            row = Constants.ROW_NUMBERS[x]
            move = column + str(row)
            if isValidMove(move, Converter.toString(game_state)):
                valid_moves.append(move)
    return valid_moves
