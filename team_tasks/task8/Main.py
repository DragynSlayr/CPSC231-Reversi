#This file holds the functions to start the game
import MainMenu
import ReversiGrid
import ListInterpret
import Constants
import BoardClick
import random

def main():
	#Set up the other classes
	ReversiGrid.main()

	#Get the starting board config
	game_state = Constants.GAME_STATE_START

	#Place the pieces from the starting board
	ListInterpret.stringToPiece(game_state)

	#The number of moves made so far
	move_num = 0

	#Determine who goes first
	isPlayerMove = random.randint(0, 1) == 0

	#Start listening for clicks on a board,
	#BoardClick takes over the logic from here
	BoardClick.run(game_state, move_num, isPlayerMove)

if __name__ == "__main__":
	MainMenu.main()
