#This file holds the functions to start the game

import MainMenu
import ReversiGrid
import StringInterpret
import Constants
import BoardClick
import random

def main():
	#Set up the other classes
	MainMenu.main()
	ReversiGrid.main()

	#Use a blank starting board
	game_state = Constants.PIECE_NONE * Constants.NUM_OF_CELLS

	#Place the pieces from the random board
	StringInterpret.stringToPiece(game_state)

	#Place starting config
	game_state = StringInterpret.stringInterpret(game_state, "D4", 0)
	game_state = StringInterpret.stringInterpret(game_state, "E4", 1)
	game_state = StringInterpret.stringInterpret(game_state, "E5", 2)
	game_state = StringInterpret.stringInterpret(game_state, "D5", 3)
	move_num = 4

	#Determine who goes first
	rand_num = random.randint(0, 1)
	isPlayerMove = rand_num == 0

	#Start listening for clicks on a board,
	#BoardClick takes over the logic from here
	BoardClick.run(game_state, move_num, isPlayerMove)

if __name__ == "__main__":
	main()
