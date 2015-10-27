import MainMenu
import ReversiGrid
import StringMove
import VictoryStatus
import PlayerVictory
import StringInterpret
import Constants
import BoardGenerator

def main():
	#Set up the other classes
	MainMenu.main()
	ReversiGrid.main()

	#Generate a random board
	token = BoardGenerator.generate(False, False)

	#Place the pieces from the random board
	StringInterpret.stringToPiece(token, 0)

	#Place starting config
	token = StringInterpret.stringInterpret(token, "D4", 0)
	token = StringInterpret.stringInterpret(token, "E4", 1)
	token = StringInterpret.stringInterpret(token, "E5", 2)
	token = StringInterpret.stringInterpret(token, "D5", 3)

	#Keeps track of how many moves have been made
	move_num = 4

	#Loop until board is full
	while VictoryStatus.endGameStatus(token) == False:
		#Get validated player move
		move = StringMove.getMove(token, "Please enter a move:")

		#If the player didn't hit cancel
		if move != "invalid":
			hame_state = StringInterpret.stringInterpret(token, move, move_num)
			move_num += 1

	#Print who won
	print(PlayerVictory.playerWon(token))

	#Wait for user
	Constants.WINDOW.exitonclick()

if __name__ == "__main__":
	main()
