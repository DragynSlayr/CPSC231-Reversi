#Running this file in the terminal will let you play the board with input from the command prompt.
#It will setup the board and place the correct piece colour based on the turn number.
#It will prompt the user for moves in the terminal and will only take a valid move so a Capital and a number.
#It will update the board and the game state string based on the move.
import constants
import pieceChange

#This function will take a game state and update the gamestate on the game board.
#It takes the game state, which is a 64 character string
#It returns nothing
#Author: Kyle Hinton
def stringToPiece(game_state):
	index = 0
	for y in range(len(constants.ROW_NUMBERS)):
		for x in range(len(constants.COLUMN_LETTERS)):
			#Get location
			x_coord = constants.COLUMN_LETTERS[x]
			y_coord = constants.ROW_NUMBERS[y]

			#Check each piece at the index in the game state
			piece = game_state[index]
			if piece == "B":
				TurtleMove.placePiece(x_coord, y_coord, "Black")
			elif piece == "W":
				TurtleMove.placePiece(x_coord, y_coord, "White")

			#Increment index
			index += 1

#Converts an index to a move
#Params: index, The index to convert
#Returns: A string representing the Index
#Example: pieceToString(10) returns "C2"
def pieceToString(index):
	column = constants.COLUMN_LETTERS[index % 8]
	row = constants.ROW_NUMBERS[index // 8]
	return str(column) + str(row)

#This function will decide on the colour of the next piece based on whose turn number it is.
#The takes a counter for the turns as a parameter.
#It returns a B or a W depending on whose turn it is.
def whoseTurn(counter):
	if counter % 2 == 0:
		return "W"
	else:
		return "B"

#This function takes the move entry and returns the string Index.
#Parameter: the move entry like "A7"
#Returns string index

def moveToIndex(NewMove):
	column = NewMove[0].upper()
	row = int(NewMove[1])

	column_IDX = (constants.COLUMN_LETTERS.index(column))
	row_IDX = (constants.ROW_NUMBERS.index(row))
 	#Equation for converting a move coordinate to the index number to be changed
	moveIDX = ((row_IDX * constants.NUM_OF_ROWS) + column_IDX)

	return moveIDX

#This function will convert a move coordinate into a string.
#It receives the parameters are a game state, a move coordinate, and the turn number.
#It returns the updated string as new_state.
#For testing, you can get the index number of the changed character with move_to_string
#Author: Kyle Hinton
def stringInterpret(game_state, NewMove, turn):
		column = NewMove[0].upper()
		row = int(NewMove[1])

		column_IDX = (constants.COLUMN_LETTERS.index(column))
		row_IDX = (constants.ROW_NUMBERS.index(row))

 		#Equation for converting a move coordinate to the index number to be changed
		move_to_string = ((row_IDX * constants.NUM_OF_ROWS) + column_IDX)

		turn_colour = whoseTurn(turn)

		new_state = pieceChange.ChangePieces(game_state, move_to_string, turn_colour)
		#new_state = game_state[:move_to_string] + turn_colour + game_state[move_to_string + 1:]

		if whoseTurn(turn) == "W":
			color = "White"
		else:
			color = "Black"

#		TurtleMove.placePiece(column, row, color)

		if __name__ == "__main__":
			#TESTING TESTING TESTING
			##########################
			print("Testing")
			print("turn ", turn)
			print(column_IDX, "column_IDX") # Column index number from letters
			print(row_IDX, "row_IDX")	#Row index number from numbers
			print(column, "Column")	#Prints the Column Letter
			print(row, "Row") #Prints the Row Number
			print(game_state[move_to_string], ": Character at the move's index number.") #Prints the character at the index [move_to_string]
			print(move_to_string, "Index number of new move") #Takes the move and converts it to the index number for the string
			print(new_state)	#Prints the new_state with the character at index.move_to_string in place
			print()
			##########################
		return new_state	#returns the new_state, The updated move.

#Sets up the board using the pieces and reading through the string.
def setup2():
	new_state = stringInterpret(("NNNNNNNN" * 8), "D4", -2)
	new_state = stringInterpret((new_state), "E4", -1)
	new_state = stringInterpret((new_state), "D5", -1)
	new_state = stringInterpret((new_state), "E5", -2)
	for turn in range(64):
		new_state = stringInterpret((new_state), input("Move?"), turn + 1)

if __name__ == "__main__":
		TurtleMove.setup()
		setup2()
		constants.WINDOW.exitonclick()
