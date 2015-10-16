#Write a function that takes a current game state as a parameter and returns true if the game is over.
#It must detect if the board is full or if there are no further moves possible.
import Constants
import ConfigGenerator as cfg

#Checks if the game is over
#Params: game_state, A string representation of the board
#Returns: True if the board is full and False otherwise
#Author: Inderpreet Dhillon
def is_game_over(game_state):
	limit = Constants.NUM_OF_CELLS
	count = 0
	#Iterate through the game state
	for s in game_state:
		if s == Constants.PIECE_BLACK or s == Constants.PIECE_WHITE:
			count += 1
	return count == limit

if __name__ == "__main__":
	#Asks the user for input if not q then run tests
	while (input("Press q to quit: ") != 'q'):
		#Make sure the user wants this
		if input("Enter 'PROCEED' to continue: ") == "PROCEED":
			game_over = False
			count = 0
			#Tests can take between 1 and infinity generations, 1s+
			while not game_over:
				if count % 100 == 0:
					print("TEST #%d" % count)
				count += 1
				game_state = cfg.generate()
				game_over = is_game_over(game_state)
			#Finally print a test that passed, all others failed
			print(game_state + "\n\nHas resulted in a game over after %d generations!" % count)
		else:
			print("You saved a lot of time, congratulations!")
