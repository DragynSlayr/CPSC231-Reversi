#Running this file in the terminal will let you play the board with input from the command prompt.
#It will setup the board and place the correct piece colour based on the turn number.
#It will prompt the user for moves in the terminal and will only take a valid move so a Capital and a number.
#It will update the board and the game state string based on the move.
import constants
import turtleMove
import listUpdater

#This function will take a game state and update the gamestate on the game board.
#It takes the game state, which is a 64 character string
#It returns nothing
#Author: Kyle Hinton
def stringToPiece(game_state):
	for y in range(len(game_state)):
		for x in range(len(game_state[y])):
			column = constants.COLUMN_LETTERS[y]
			row = constants.ROW_NUMBERS[x]
			piece = game_state[x][y]

			if piece == constants.PIECE_BLACK:
				turtleMove.placePiece(column, row, "Black")
			elif piece == constants.PIECE_WHITE:
				turtleMove.placePiece(column, row, "White")
			else:
				turtleMove.resetSquare(column + str(row))

#Converts an index to a move
#Params: index, The index to convert
#Returns: A string representing the Index
#Example: pieceToString(10) returns "C2"
def pieceToString(index):
	column = constants.COLUMN_LETTERS[index % 8]
	row = constants.ROW_NUMBERS[index // 8]
	return str(column) + str(row)

#This function will decide on the colour of the next piece based on whose turn number it is.
#The takes a counter for the turns as a parameter.
#It returns a B or a W depending on whose turn it is.
def whoseTurn(counter):
	if counter % 2 == 0:
		return constants.PIECE_WHITE
	else:
		return constants.PIECE_BLACK

#This function will convert a move coordinate into a string.
#It receives the parameters are a game state, a move coordinate, and the turn number.
#It returns the updated string as new_state.
#For testing, you can get the index number of the changed character with move_to_string
#Author: Kyle Hinton
def stringInterpret(game_state, NewMove, turn):
		column = NewMove[0].upper()
		row = int(NewMove[1])

		column_IDX = (constants.COLUMN_LETTERS.index(column))
		row_IDX = (constants.ROW_NUMBERS.index(row))

		turn_colour = whoseTurn(turn)

		new_state = game_state[:]

		new_state = listUpdater.updateGameState(new_state, NewMove, turn_colour )

		if whoseTurn(turn) == constants.PIECE_WHITE:
			color = "White"
		else:
			color = "Black"

		turtleMove.placePiece(column, row, color)

		return new_state	#Return the updated game state
