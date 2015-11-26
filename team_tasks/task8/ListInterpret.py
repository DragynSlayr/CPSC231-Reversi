#Running this file in the terminal will let you play the board with input from the command prompt.
#It will setup the board and place the correct piece colour based on the turn number.
#It will prompt the user for moves in the terminal and will only take a valid move so a Capital and a number.
#It will update the board and the game state string based on the move.
import Constants
import TurtleMove
import ListUpdater

#This function will take a game state and update the gamestate on the game board.
#It takes the game state, which is a 64 character string
#It returns nothing
#Author: Kyle Hinton
def stringToPiece(game_state):
	for y in range(len(game_state)):
		for x in range(len(game_state[y])):
			column = Constants.COLUMN_LETTERS[y]
			row = Constants.ROW_NUMBERS[x]
			piece = game_state[x][y]

			if piece == Constants.PIECE_BLACK:
				TurtleMove.placePiece(column, row, "Black")
			elif piece == Constants.PIECE_WHITE:
				TurtleMove.placePiece(column, row, "White")
			else:
				TurtleMove.resetSquare(column, row)

#Converts an index to a move
#Params: index, The index to convert
#Returns: A string representing the Index
#Example: pieceToString(10) returns "C2"
def pieceToString(index):
	column = Constants.COLUMN_LETTERS[index % 8]
	row = Constants.ROW_NUMBERS[index // 8]
	return str(column) + str(row)

#This function will decide on the colour of the next piece based on whose turn number it is.
#The takes a counter for the turns as a parameter.
#It returns a B or a W depending on whose turn it is.
def whoseTurn(counter):
	if counter % 2 == 0:
		return Constants.PIECE_WHITE
	else:
		return Constants.PIECE_BLACK

#This function will convert a move coordinate into a string.
#It receives the parameters are a game state, a move coordinate, and the turn number.
#It returns the updated string as new_state.
#For testing, you can get the index number of the changed character with move_to_string
#Author: Kyle Hinton
def stringInterpret(game_state, NewMove, turn):
		column = NewMove[0].upper()
		row = int(NewMove[1])

		column_IDX = (Constants.COLUMN_LETTERS.index(column))
		row_IDX = (Constants.ROW_NUMBERS.index(row))

		turn_colour = whoseTurn(turn)

		new_state = game_state[:]

		new_state = ListUpdater.updateGameState(new_state, NewMove, turn_colour )

		if whoseTurn(turn) == Constants.PIECE_WHITE:
			color = "White"
		else:
			color = "Black"

		TurtleMove.placePiece(column, row, color)

		return new_state	#Return the updated game state