#This file holds the functions to start the game
import MainMenu
import ReversiGrid
import ListInterpret
import Constants
import BoardClick
import random
import Converter
import ListUpdater


def main():
	#Set up the other classes
	ReversiGrid.main()

	#Use a blank starting board
	game_state = Converter.toList("N" * 64)

	#Place the pieces from the random board
	ListInterpret.stringToPiece(game_state)

	#Place starting config
	game_state = ListInterpret.stringInterpret(game_state, "D4", 0)
	game_state = ListInterpret.stringInterpret(game_state, "E4", 1)
	game_state = ListInterpret.stringInterpret(game_state, "E5", 2)
	game_state = ListInterpret.stringInterpret(game_state, "D5", 3)
	
	game_state = Constants.GAME_STATE_START
	move_num = 0
	
	#Determine who goes first
	rand_num = random.randint(0, 1)
	isPlayerMove = rand_num == 0

	#Start listening for clicks on a board,
	#BoardClick takes over the logic from here
	BoardClick.run(game_state, move_num, isPlayerMove)


if __name__ == "__main__":
	MainMenu.main()
