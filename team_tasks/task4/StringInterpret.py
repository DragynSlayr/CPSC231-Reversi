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


#This function takes the current game state as a token and the next move and updates the gamestate token based on the move.
#
def StringInterpret(token, NewMove):
        column = NewMove[0]
        row = int(NewMove[1])

        ColumnIDX = (Constants.COLUMN_LETTERS.index(column))
        RowIDX = (Constants.ROW_NUMBERS.index(row))
        
        StringGrab = ((RowIDX * Constants.NUM_OF_ROWS) + ColumnIDX)
        
        NewToken = token[:StringGrab] + "B" + token[StringGrab + 1:]
        
        StringToPiece(NewToken, 0)

        print(token[StringGrab]) #Prints the character at the index [StringGrab]
        print(ColumnIDX, "Columnidx") # Column index number from letters
        print(RowIDX, "Rowidx")	#Row index number from numbers
        print(column, "Column")	#Prints the Column Letter
        print(row, "Row") #Prints the Row Number
        print(StringGrab, "Index number of new move") #Takes the move and converts it to the index number for the string 
        print(NewToken)	#Prints the NewToken with the character at index.StringGrab in place
        return NewToken	#returns the NewToken, The updated move.


if __name__ == "__main__":
        TurtleMove.setup()
 #       StringToPiece(("NWWBBWBB" * 8), 0)
        NewToken = StringInterpret(("NNNNNNNN" * 8), input("Move?"))
        NewToken = StringInterpret((NewToken), input("Move"))
        NewToken = StringInterpret((NewToken), input("Move?"))
        """
        NewToken = StringInterpret((NewToken), "B3")
        NewToken = StringInterpret((NewToken), "B4")
        NewToken = StringInterpret((NewToken), "C2")
        NewToken = StringInterpret((NewToken), "C4")
        NewToken = StringInterpret((NewToken), "D2")
        NewToken = StringInterpret((NewToken), "D3")
        NewToken = StringInterpret((NewToken), "D4")
        """
        Constants.WINDOW.exitonclick()

        
