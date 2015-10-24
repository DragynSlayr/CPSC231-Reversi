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
	print("before loop")
	while VictoryStatus.is_game_over(Gamestate) == False:
		move = StringMove.get_move(Gamestate)
		#print(type(move))
		Gamestate = StringInterpret.StringInterpret(Gamestate, move)
		print("in loop")
	if PlayerVictory.PlayerWon(Gamestate) == True:
		#Black Won!
		print("Black Won")
		
	else:
		print("White Won!")
		#White Won!
		
if __name__ == "__main__":
	Main()