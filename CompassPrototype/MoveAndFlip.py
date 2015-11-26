import StringInterpret
import PieceChange
import TurtleMove
import ReversiGrid
import Constants
import Converter

#def Move_and_Flip(game_state, MoveID, turn)
ReversiGrid.main()

new_state = "NNNNNNNNNNNNNNNNNNNNNNNNNNNBWNNNNNNWBNNNNNNNNNNNNNNNNNNNNNNNNNNN"
start_board = StringInterpret.stringToPiece(new_state)



for turn in range(64):
    print (new_state, "Game State")
    NewMove = input("Move?")
    new_state = StringInterpret.stringInterpret(new_state, NewMove, turn)
    print(new_state, "Move")
    new_state = PieceChange.CheckSouth(new_state, StringInterpret.moveToIndex(NewMove), StringInterpret.whoseTurn(turn))
    print (new_state, "South")
    new_state = PieceChange.CheckNorth(new_state, StringInterpret.moveToIndex(NewMove), StringInterpret.whoseTurn(turn))
    print (new_state, "North")
    new_state = PieceChange.CheckWest(new_state, StringInterpret.moveToIndex(NewMove), StringInterpret.whoseTurn(turn))
    print (new_state, "West")
    new_state = PieceChange.CheckEast(new_state, StringInterpret.moveToIndex(NewMove), StringInterpret.whoseTurn(turn))
    print (new_state, "East")
    new_state = PieceChange.CheckNorthWest(new_state, StringInterpret.moveToIndex(NewMove), StringInterpret.whoseTurn(turn))
    print (new_state, "NorthWest")
    new_state = PieceChange.CheckNorthEast(new_state, StringInterpret.moveToIndex(NewMove), StringInterpret.whoseTurn(turn))
    print (new_state, "NorthEast")
    new_state = PieceChange.CheckSouthWest(new_state, StringInterpret.moveToIndex(NewMove), StringInterpret.whoseTurn(turn))
    print (new_state, "SouthWest")
    new_state = PieceChange.CheckSouthEast(new_state, StringInterpret.moveToIndex(NewMove), StringInterpret.whoseTurn(turn))
    print (new_state, "SouthEast")

    print(turn)
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
