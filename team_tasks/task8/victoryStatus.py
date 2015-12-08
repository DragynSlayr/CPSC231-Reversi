#This file constains functions to check if the game is over
import constants

#Counts the number of a specified character in a string
#Params: piece, The piece to count occurences of
#		 game_state, The string to check
#Returns: A count of the piece in the game_state
#Author: Inderpreet Dhillon
#Editor: None
def countPieces(piece, game_state):
	count = 0

	#Traverse the list
	for y in game_state:
		for x in y:
			#Add to the count if piece was found
			if x == piece:
				count += 1

	return count

#Checks if the game is over
#Params: game_state, A string representation of the board
#Returns: True if the board is full and False otherwise
#Author: Inderpreet Dhillon
#Editor: None
def endGameStatus(game_state):
	#Max possible spaces that could be filled
	limit = constants.NUM_OF_CELLS

	#Number of spaces that are unfilled
	empty_spaces = countPieces(constants.PIECE_NONE, game_state)

	#Check if the board is full
	board_full = (limit - empty_spaces) == limit

	return board_full
