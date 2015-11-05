#This file constains a function that takes a current game state as a parameter and returns true if the game is over.
import Constants
import BoardGenerator as cfg

#Checks if the game is over
#Params: game_state, A string representation of the board
#Returns: True if the board is full and False otherwise
#Author: Inderpreet Dhillon
def endGameStatus(game_state):
	limit = Constants.NUM_OF_CELLS
	count = 0
	#Iterate through the game state
	for s in game_state:
		#Count non blank pieces
		if s == Constants.PIECE_BLACK or s == Constants.PIECE_WHITE:
			count += 1
	return count == limit

if __name__ == "__main__":
	board = cfg.generate(True, True)
	print(board, "\n%s" % checkEndGameStatus(board))

	board = cfg.generate(True, False)
	print(board, "\n%s" % checkEndGameStatus(board))

	board = cfg.generate(False, True)
	print(board, "\n%s" % checkEndGameStatus(board))

	board = cfg.generate(False, False)
	print(board, "\n%s" % checkEndGameStatus(board))
