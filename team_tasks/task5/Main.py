import MainMenu
import ReversiGrid
import StringMove
import VictoryStatus
import PlayerVictory
import StringInterpret
import Constants
import BoardGenerator
import BoardClick

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

	#Start listening for clicks on a board,
	#BoardClick takes over the logic from here
	BoardClick.run(token)

if __name__ == "__main__":
	main()
