import MainMenu
import ReversiGrid
import StringMove
import VictoryStatus
import PlayerVictory
import StringInterpret
import Constants
import BoardGenerator

def Main():
	#Set up the other classes
	MainMenu.main()
	ReversiGrid.main()

	#Generate a random board
	Gamestate = BoardGenerator.generate(False, False)

	#Place the pieces from the random board
	StringInterpret.StringToPiece(Gamestate, 0)

	#Place starting config
	Gamestate = StringInterpret.StringInterpret(Gamestate, "D4", 0)
	Gamestate = StringInterpret.StringInterpret(Gamestate, "E4", 1)
	Gamestate = StringInterpret.StringInterpret(Gamestate, "E5", 2)
	Gamestate = StringInterpret.StringInterpret(Gamestate, "D5", 3)

	#Keeps track of how many moves have been made
	move_num = 4

	#Loop until board is full
	while VictoryStatus.is_game_over(Gamestate) == False:
		#Get validated player move
		move = StringMove.get_move(Gamestate, "Please enter a move:")

		#If the player didn't hit cancel
		if move != None:
			Gamestate = StringInterpret.StringInterpret(Gamestate, move, move_num)
			move_num += 1
			
	#Print who won
	print(PlayerVictory.PlayerWon(Gamestate))

	#Wait for user
	Constants.WINDOW.exitonclick()

if __name__ == "__main__":
	Main()
