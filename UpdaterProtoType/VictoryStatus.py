#This file constains a function that takes a current game state as a parameter and returns true if the game is over.
import Constants
import BoardGenerator as cfg

#Counts the number of a specified character in a string
#Params: piece, The piece to count occurences of
#		 game_state, The string to check
#Returns: A count of the piece in the game_state
def countPieces(piece, game_state):
	count = 0
	for y in game_state:
		for x in y:
			if x == piece:
				count += 1
	return count

#Checks if the game is over
#Params: game_state, A string representation of the board
#Returns: True if the board is full and False otherwise
#Author: Inderpreet Dhillon
def endGameStatus(game_state):
	limit = Constants.NUM_OF_CELLS
	count = countPieces(Constants.PIECE_BLACK, game_state) + countPieces(Constants.PIECE_WHITE, game_state)
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
