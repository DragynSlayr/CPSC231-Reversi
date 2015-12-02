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
def listToPiece(game_state):
	#Iterate through game state list
	for y in range(len(game_state)):
		for x in range(len(game_state[y])):
			#Get column and row of position
			column = constants.COLUMN_LETTERS[y]
			row = constants.ROW_NUMBERS[x]

			#Get piece at position
			piece = game_state[x][y]

			#Place piece or reset square at position
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
	return column + str(row)

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
def listInterpret(game_state, move, turn):
	#Get letter and number from move
	letter = move[0].upper()
	number = int(move[1])

	#Get indices of the move
	column_index = constants.COLUMN_LETTERS.index(letter)
	row_index = constants.ROW_NUMBERS.index(number)

	#Get color of piece being placed
	turn_colour = whoseTurn(turn)

	#Update the game state
	new_state = listUpdater.updateGameState(game_state[:], move, turn_colour)

	#Return the updated game state
	return new_state
