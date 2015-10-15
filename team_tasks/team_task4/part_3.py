#Write a function that takes a current game state as a parameter and returns true if the game is over. 
#It must detect if the board is full or if there are no further moves possible.
import Constants

#Checks if the game is over
#Params: game_state, A string representation of the board
#Returns: True if the board is full and False otherwise
def is_game_over(game_state):
	limit = Constants.NUM_OF_CELLS
	count = 0
	for s in game_state:
		if s == Constants.PIECE_BLACK or s == Constants.PIECE_WHITE:
			count += 1
	return count == limit

if __name__ == "__main__":
	print(is_game_over("BBWWNN"))
	print(is_game_over("BWNBWN"))
	print(is_game_over("BBBWWW"))
