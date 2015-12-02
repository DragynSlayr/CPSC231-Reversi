#This file holds the functions to start the game
import mainMenu
import reversiGrid
import listInterpret
import constants
import boardClick
import random

def start():
	#Draw the board
	reversiGrid.main()

	#Get the starting board config
	game_state = constants.GAME_STATE_START

	#Place the pieces from the starting board
	listInterpret.listToPiece(game_state)

	#The number of moves made so far
	move_num = 0

	#Determine who goes first
	player_move = random.randint(0, 1) == 0

	#Start listening for clicks on a board,
	#BoardClick takes over the logic from here
	boardClick.run(game_state, move_num, player_move)

if __name__ == "__main__":
	mainMenu.main()
