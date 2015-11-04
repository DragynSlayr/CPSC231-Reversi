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
	token = Constants.PIECE_NONE * Constants.NUM_OF_CELLS

	#Place the pieces from the random board
	StringInterpret.stringToPiece(token, 0)

	#Place starting config
	token = StringInterpret.stringInterpret(token, "D4", 0)
	token = StringInterpret.stringInterpret(token, "E4", 1)
	token = StringInterpret.stringInterpret(token, "E5", 2)
	token = StringInterpret.stringInterpret(token, "D5", 3)
	move_num = 4

	#Determine who goes first
	rand_num = random.randint(0, 1)
	isPlayerMove = rand_num == 0

	#Start listening for clicks on a board,
	#BoardClick takes over the logic from here
	BoardClick.run(token, move_num, isPlayerMove)

if __name__ == "__main__":
	main()
