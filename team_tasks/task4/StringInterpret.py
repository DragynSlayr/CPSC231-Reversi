#Running this file in the terminal will let you play the board with input from the command prompt.
#It will setup the board and place the correct piece colour based on the turn number.
#It will prompt the user for moves in the terminal and will only take a valid move so a Capital and a number.
#It will update the board and the token string based on the move.


import Constants
import TurtleMove
import ReversiGrid


#This function will take a token and update the gamestate on the game board.
#It's parameters are for the token, which is the 64 character string;i, which is the index number on that string.
#It's output will update the board by placing pieces based on the token-string it receives.
#Author: Kyle Hinton
def StringToPiece(token, i):
	for y in range(len(Constants.ROW_NUMBERS)):
		for x in range(len(Constants.COLUMN_LETTERS)):
			x_coord = Constants.COLUMN_LETTERS[x]
			y_coord = Constants.ROW_NUMBERS[y]
			if token[i] == "N": #if index i on the string equals N place a green piece which is a non-piece.
				TurtleMove.place_piece(x_coord, y_coord, "Green")
			elif token[i] == "B":
				TurtleMove.place_piece(x_coord, y_coord, "Black")
			elif token[i] == "W":
				TurtleMove.place_piece(x_coord,y_coord, "White")
			i = i + 1




#This function will decide on the colour of the next piece based on whose turn number it is.
#The takes a counter for the turns as a parameter.
#It returns a B or a W depending on whose turn it is.
def WhoseTurn(counter):
	Piece = ""
	if counter % 2 == 0:
		Piece = "B"
	else:
		Piece = "W"
	return Piece



#This function will convert a move coordinate into a string.
#It receives the parameters are a token, a move coordinate, and the turn number.
#It returns the updated string as NewToken.
#For testing, you can get the index number of the changed character with MoveToString
#Author: Kyle Hinton
def StringInterpret(token, NewMove, turn):
		column = NewMove[0].upper() 
		row = int(NewMove[1])

		ColumnIDX = (Constants.COLUMN_LETTERS.index(column))
		RowIDX = (Constants.ROW_NUMBERS.index(row))

		MoveToString = ((RowIDX * Constants.NUM_OF_ROWS) + ColumnIDX) #Equation for converting a move coordinate to the index number to be changed


		TurnColour = WhoseTurn(turn)

		NewToken = token[:MoveToString] + TurnColour + token[MoveToString + 1:]

		StringToPiece(NewToken, 0)



		#TESTING TESTING TESTING
		##########################
		print(" ")
		print("turn ", turn)
		print(ColumnIDX, "Columnidx") # Column index number from letters
		print(RowIDX, "Rowidx")	#Row index number from numbers
		print(column, "Column")	#Prints the Column Letter
		print(row, "Row") #Prints the Row Number
		print(token[MoveToString], ": Character at the move's index number.") #Prints the character at the index [MoveToString]
		print(MoveToString, "Index number of new move") #Takes the move and converts it to the index number for the string
		print(NewToken)	#Prints the NewToken with the character at index.MoveToString in place
		print(" ")
		##########################


		return NewToken	#returns the NewToken, The updated move.


#Sets up the board using the pieces and reading through the string.
#

def Setup2():
	NewToken = StringInterpret(("NNNNNNNN" * 8), "D4", -2)
	NewToken = StringInterpret((NewToken), "E4", -1)
	NewToken = StringInterpret((NewToken), "D5", -1)
	NewToken = StringInterpret((NewToken), "E5", -2)
	for turn in range(64):
		NewToken = StringInterpret((NewToken), input("Move?"), turn + 1)






if __name__ == "__main__":
		TurtleMove.setup()
		Setup2()

		Constants.WINDOW.exitonclick()
