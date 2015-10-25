import MainMenu
import ReversiGrid
import StringMove
import VictoryStatus
import PlayerVictory
import StringInterpret
import Constants

def Main():

	MainMenu.main()
	ReversiGrid.main()
	#Gamestate = StringMove.initialize_grid_string_start()
	Gamestate = "N" * 64
	Gamestate = StringInterpret.StringInterpret(Gamestate, "D4", 0)
	Gamestate = StringInterpret.StringInterpret(Gamestate, "E4", 1)
	Gamestate = StringInterpret.StringInterpret(Gamestate, "E5", 2)
	Gamestate = StringInterpret.StringInterpret(Gamestate, "D5", 3)
	move_num = 4
	while VictoryStatus.is_game_over(Gamestate) == False:
		move = StringMove.get_move(Gamestate, "Please enter a move:")
		if move != None:
			Gamestate = StringInterpret.StringInterpret(Gamestate, move, move_num)
			move_num += 1
	#Print who won
	print(PlayerVictory.PlayerWon(Gamestate))

	#Wait for user
	Constants.WINDOW.exitonclick()

if __name__ == "__main__":
	Main()
