# Write a function that takes the current game state as a parameter,
# prompts the user for a move,
# validates the specified move (reprompt if not valid)
# and returns the update game state.
# It should use the function written by team member 1.

import Constants
import BoardGenerator as bg

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


def getColumnSign(column_index):
    if column_index % 2 == 1:
        return 1
    else:
        return -1

def getRowSign(row_index):
    if row_index <= 2:
        return 1
    else:
        return -1

def getIdentifier(corner_index, order_index):
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
        return getIdentifier(corner_index, 2) + getIdentifier(corner_index, 1)

def piecesByCorner(game_state, corner_index, column, row):
    pieces = []
    order_index = 0
    column_sign = getColumnSign(corner_index)
    row_sign = getRowSign(corner_index)
    for i in range(2):
        for j in range(2):
            if order_index > 0:
                identifier = getIdentifier(corner_index, order_index)
            else:
                identifier = "C"
            pieces.append(getPieceAt(chr(ord(column) + (j * column_sign)), row + (i * row_sign), game_state) + ":" + identifier)
            order_index += 1
    return pieces

def countFilledSpaces(pieces):
    count = 0
    for i in pieces:
        piece = i[:1]
        if piece == Constants.PIECE_BLACK or piece == Constants.PIECE_WHITE:
            count += 1
    return count

def getColumn(column):
    if column == Constants.COLUMN_LETTERS[0]:
        return 1
    else:
        return 2

def getColumnIdentifier(column_index, order_index):
    if column_index == 1:
        order = ["T", "TR", "", "R", "B", "BR"]
        return order[order_index]
    else:
        order = ["T", "TL", "", "L", "B", "BL"]
        return order[order_index]

def piecesByColumn(game_state, column_index, column, row):
    pieces = []
    order_index = 0
    column_sign = getColumnSign(column_index)
    for i in range(3):
        for j in range(2):
            if order_index == 2:
                identifier = "C"
            else:
                identifier = getColumnIdentifier(column_index, order_index)
            pieces.append(getPieceAt(chr(ord(column) + (j * column_sign)), row + (i - 1), game_state) + ":" + identifier)
            order_index += 1
    return pieces

def getRow(row):
    if row == Constants.ROW_NUMBERS[0]:
        return 1
    else:
        return 2

def getRowIdentifier(row_index, order_index):
    if row_index == 1:
        order = ["L", "", "R", "BL", "B", "BR"]
        return order[order_index]
    else:
        order = ["L", "", "R", "TL", "T", "TR"]
        return order[order_index]

def piecesByRow(game_state, row_index, column, row):
    pieces = []
    order_index = 0
    row_sign = getColumnSign(row_index)
    for i in range(2):
        for j in range(3):
            if order_index == 1:
                identifier = "C"
            else:
                identifier = getRowIdentifier(row_index, order_index)
            pieces.append(getPieceAt(chr(ord(column) + (j - 1)), row + (i * row_sign), game_state) + ":" + identifier)
            order_index += 1
    return pieces

def getPointIdentifier(order_index):
    order = ["TL", "T", "TR", "L", "C", "R", "BL", "B", "BR"]
    return order[order_index]

def piecesByPoint(game_state, column, row):
    pieces = []
    order_index = 0
    for i in range(3):
        for j in range(3):
            identifier = getPointIdentifier(order_index)
            pieces.append(getPieceAt(chr(ord(column) + (j - 1)), row + (i - 1), game_state) + ":" + identifier)
            order_index += 1
    return pieces

def isValidMove(move, game_state):
    #Test code
    if move == "f":
        return True

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
            return filled_spaces > 1
    else:
        #Piece not on board
        return False

def validate(game_state):
    move = input("Enter a move: ")
    while not isValidMove(move, game_state):
        print("Not valid!")
        move = input("Enter a move: ")

if __name__ == "__main__":
    board = bg.generate(False, False)
    for i in range(1, len(board) + 1):
        print(board[i - 1], end = "")
        if i % 8 == 0:
            print()
    print()
    validate(board)
