import StringInterpret
import PieceChange
import TurtleMove
import ReversiGrid
import Constants
import Converter

#def Move_and_Flip(game_state, MoveID, turn)
ReversiGrid.main()

game_state = "NNNNNNNNNNNNNNNNNNNNNNNNNNNBWNNNNNNWBNNNNNNNNNNNNNNNNNNNNNNNNNNN"
start_board = StringInterpret.stringToPiece(game_state)

NewMove = input("Move?")
turn = 2

move_state = StringInterpret.stringInterpret(game_state, NewMove, turn)
new_state = PieceChange.CheckSouth(move_state, StringInterpret.moveToIndex(NewMove), StringInterpret.whoseTurn(turn))
new_state = PieceChange.CheckNorth(move_state, StringInterpret.moveToIndex(NewMove), StringInterpret.whoseTurn(turn))
#new_state3 = PieceChange.CheckWest(new_state2, StringInterpret.moveToIndex(NewMove), StringInterpret.whoseTurn(turn))
#new_state4 = PieceChange.CheckEast(new_state3, StringInterpret.moveToIndex(NewMove), StringInterpret.whoseTurn(turn))
#new_state5 = PieceChange.CheckNorthWest(new_state4, StringInterpret.moveToIndex(NewMove), StringInterpret.whoseTurn(turn))
#new_state6 = PieceChange.CheckNorthEast(new_state5, StringInterpret.moveToIndex(NewMove), StringInterpret.whoseTurn(turn))
#new_state7 = PieceChange.CheckSouthWest(new_state6, StringInterpret.moveToIndex(NewMove), StringInterpret.whoseTurn(turn))
#new_state8 = PieceChange.CheckSouthEast(new_state7, StringInterpret.moveToIndex(NewMove), StringInterpret.whoseTurn(turn))

print(game_state)
print(new_state, "HI YA")




"""
for turn in range(64):
    NewMove = input("Move?")
    move_state = StringInterpret.stringInterpret(game_state, NewMove, turn + 1)
    print(move_state, "Thing 1")
    new_state = PieceChange.ChangePieces(move_state, int(StringInterpret.moveToIndex(NewMove)), StringInterpret.whoseTurn(turn))
    print(new_state, "SAVANT!!!")
"""
Constants.WINDOW.exitonclick()
