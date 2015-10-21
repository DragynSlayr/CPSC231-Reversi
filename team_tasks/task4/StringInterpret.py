import Constants
import TurtleMove
import ReversiGrid

def StringToPiece(token, i):
        for y in range(len(Constants.COLUMN_LETTERS)):
                for x in range(len(Constants.ROW_NUMBERS)):
                        x_coord = Constants.COLUMN_LETTERS[x]
                        y_coord = Constants.ROW_NUMBERS[y]
                        if token[i] == "N":
                                TurtleMove.place_piece(x_coord, y_coord, "Blue")
                        elif token[i] == "B":
                                TurtleMove.place_piece(x_coord, y_coord, "Black")
                        elif token[i] == "W":
                                TurtleMove.place_piece(x_coord,y_coord, "White")
                        i = i + 1

def StringInterpret(token, NewMove):
        column = NewMove[0]
        row = int(NewMove[1])

        ColumnIDX = (Constants.COLUMN_LETTERS.index(column))
        RowIDX = (Constants.ROW_NUMBERS.index(row))
        
        StringGrab = ((RowIDX * Constants.NUM_OF_ROWS) + ColumnIDX)
        
        NewToken = token[:StringGrab] + "B" + token[StringGrab + 1:]
        
        StringToPiece(NewToken, 0)

        print(token[StringGrab])
        print(ColumnIDX, "Columnidx")
        print(RowIDX, "Rowidx")
        print(column, "Column")
        print(row, "Row")
        print(StringGrab)
        print(NewToken)


if __name__ == "__main__":
        TurtleMove.setup()
        StringToPiece(("NWWBBWBB" * 8), 0)
        StringInterpret(("NWWBBWBB" * 8), "C7")
        Constants.WINDOW.exitonclick()

        
