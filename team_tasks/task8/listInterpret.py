#This file contains methods to load and change lists
import constants
import turtleMove
import listUpdater

#Places pieces from a list to the board
#Params: game_state, The list to load
#Returns: None
#Author: Kyle Hinton
#Editor: Inderpreet Dhillon
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
				turtleMove.placePiece(column, row, constants.PIECE_COLOR_BLACK)
			elif piece == constants.PIECE_WHITE:
				turtleMove.placePiece(column, row, constants.PIECE_COLOR_WHITE)
			else:
				turtleMove.resetSquare(column + str(row))

#Gets the current turn piece based on the turn number
#Params: counter, The turn number
#Return: White's piece if even turn, Black's otherwise
#Author: Kyle Hinton
#Editor: None
def whoseTurn(counter):
	if counter % 2 == 0:
		return constants.PIECE_WHITE
	else:
		return constants.PIECE_BLACK

#Interpret's a move into the game state
#Params: game_state, The state of the game
#		 move, The move to interpret
#		 turn, The turn number
#Returns: The updated state
#Author: Kyle Hinton
#Editor: Inderpreet Dhillon, David Keizer
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
