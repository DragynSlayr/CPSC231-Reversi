import MainMenu
import ReversiGrid
import StringMove
import VictoryStatus
import PlayerVictory
import StringInterpret

def Main():
	MainMenu.main()
	ReversiGrid.main()
	Gamestate = StringMove.initialize_grid_string_start()
	while VictoryStatus.is_game_over(Gamestate) == False:
		move = StringMove.get_move
		Gamestate = StringInterpret.StringInterpret(Gamestate, move)
		
	if PlayerVictory.PlayerWon(Gamestate) == True:
		#Black Won!
		print("Black Won")
		
	else:
		print("White Won!")
		#White Won!
		
	