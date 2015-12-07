#Contains methods for interpreting input and placing pieces
import string
import constants
import reversiGrid
import listUpdater

#Holds all valid moves that have been displayed
SHOWN_MOVES = []

#Redraws a single square back to default
#Params: move, The position of the square to reset
#Returns: None
def resetSquare(move):
	#Get column and row from move
	column = move[0]
	row = int(move[1])

	#Get the turtle
	turtle = constants.TURTLE

	#Go to the position
	turtle.up()
	turtle.goto(getPosition(column, row))
	turtle.down()

	#Set the color
	turtle.fillcolor("dark green")

	#Draw the square
	turtle.begin_fill()
	for i in range(4):
		turtle.forward(constants.CELL_WIDTH / 2)
		turtle.left(90)
		turtle.forward(constants.CELL_WIDTH / 2)
	turtle.end_fill()

def getMoveIndices(move):#TODO Comment this method
    x = constants.COLUMN_LETTERS.index(move[0])
    y = constants.ROW_NUMBERS.index(int(move[1]))

    return (x, y)

#Draw all valid moves to the board
#Params: valid_moves, The moves to draw
#Returns: None
def displayValidMoves(valid_moves, state):#TODO Comment this method
	global SHOWN_MOVES

	for i in range(len(state)):
		for j in range(len(state[i])):
			if state[j][i] == constants.PIECE_NONE:
				column = constants.COLUMN_LETTERS[i]
				row = constants.ROW_NUMBERS[j]

				resetSquare(column + str(row))

	for move in valid_moves:
		converted_move = listUpdater.convertMove(move)

		y, x = getMoveIndices(move)

		if state[x][y] == constants.PIECE_NONE:
			placePiece(move[0], int(move[1]), "#34DDDD")
			SHOWN_MOVES.append(move)

# Gets the position in pixesl at the coordinate
# Params: column, The column letter of the coordinate
#		  row, The row number of teh coordinate
# Returns: The position of the coordinates, in a tuple (x, y)
# Example: ("a", 1) returns (200, 475)
def getPosition(column, row):
	#Get the x coordinate which is
	#the offset plus the cell width * the cell letter as a number
	x = constants.X_OFFSET + (constants.COLUMN_LETTERS.index(column) * constants.CELL_WIDTH)

	#Get the y coordinate which is
	#the offset minus the cell height * the cell number
	y = constants.Y_OFFSET - (constants.ROW_NUMBERS.index(row) * constants.CELL_HEIGHT)

	#Return coordinates in tuple
	return (x, y)

# Places a piece at a column and row with specified color
# Params: column, The column letter of the position
#		  row, The row number of the position
#		  color, A string specifying piece color; None does not draw
# Returns: None
# Example, ("A", 2, "white") places a white piece at (A, 2)
def placePiece(column, row, color):
	#Upper case letter
	column = column.upper()

	#Get the turtle from the grid
	turtle = constants.TURTLE

	#Get the screen from the grid
	wn = constants.WINDOW

	#Go to the position
	turtle.up()
	turtle.goto(getPosition(column, row))
	turtle.down()

	#Set turtle properties
	turtle.fillcolor(color)
	turtle.pensize(1)

	#Draw a filled circle
	turtle.begin_fill()
	turtle.circle(constants.CELL_WIDTH / 2)
	turtle.end_fill()

	#Update what is drawn
	wn.update()
