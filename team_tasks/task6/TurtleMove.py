#Contains methods for interpreting input and placing pieces
import string
import Constants
import ReversiGrid

#Redraws a single square back to default
#Params: column, The column of the square
#		 row, The row of the square
#Returns: None
def resetSquare(column, row):
	#Get the turtle
	turtle = Constants.TURTLE

	#Go to the position
	turtle.up()
	turtle.goto(getPosition(column, row))
	turtle.down()

	#Set the color
	turtle.fillcolor("dark green")

	#Draw the square
	turtle.begin_fill()
	for i in range(4):
		turtle.forward(Constants.CELL_WIDTH / 2)
		turtle.left(90)
		turtle.forward(Constants.CELL_WIDTH / 2)
	turtle.end_fill()

#Draw all valid moves to the board
#Params: valid_moves, The moves to draw
#Returns: None
def displayValidMoves(valid_moves):
	for move in valid_moves:
		placePiece(move[0], int(move[1]), "#34DDDD")

# Removes spaces and punctuation from a string
# Params: location, the string to strip
# Returns: A string of only numbers and letters
# Example: "A-**=-8" returns "A8"
def getStrippedLine(location):
	#Get all characters that can't be used
	not_needed_chars = string.punctuation + string.whitespace + " "

	#Store location
	stripped_line = location

	#Remove every character that is not need
	for i in not_needed_chars:
		stripped_line = stripped_line.replace(i, "")

	#Return the stripped line
	return stripped_line

# Seperates a string into letter and number(s)
# Params: location, A string of form "letter..<junk>..number"
# Returns: An array of [letter, number]
# Example: "A-=-.,-2" returns ["A", 2]
def getColumnAndRow(location):
	#Get the stripped line ex: A8
	column_and_row = getStrippedLine(location)

	#Get the column
	column = column_and_row[:1]

	#Get the row
	row = int(column_and_row[1:])

	#Return column and row
	return [column, row]

# Checks if the coordinate lies within the board
# Params: column, The column letter of the coordinate
#		  row, The row number of the coordinate
# Returns: True if on the board, False otherwise
# Example: ("a", 4) returns True, while ("i", 4) returns False
def checkvalidity(column, row):
	#Change entered column to uppercase
	column = column.upper()

	#Check if column is in the valid columns and is in the rows
	return (column in Constants.COLUMN_LETTERS) and (row in Constants.ROW_NUMBERS)

# Gets the position in pixesl at the coordinate
# Params: column, The column letter of the coordinate
#		  row, The row number of teh coordinate
# Returns: The position of the coordinates, in a tuple (x, y)
# Example: ("a", 1) returns (200, 475)
def getPosition(column, row):
	#Get the x coordinate which is
	#the offset plus the cell width * the cell letter as a number
	x = Constants.X_OFFSET + (Constants.COLUMN_LETTERS.index(column) * Constants.CELL_WIDTH)

	#Get the y coordinate which is
	#the offset minus the cell height * the cell number
	y = Constants.Y_OFFSET - (Constants.ROW_NUMBERS.index(row) * Constants.CELL_HEIGHT)

	#Return coordinates in tuple
	return (x, y)

# Places a piece at a column and row with specified color
# Params: column, The column letter of the position
#		  row, The row number of the position
#		  color, A string specifying piece color; None does not draw
# Returns: None
# Example, ("A", 2, "white") places a white piece at (A, 2)
def placePiece(column, row, color):
	#Upper case letter
	column = column.upper()

	#Get the turtle from the grid
	turtle = Constants.TURTLE

	#Get the screen from the grid
	wn = Constants.WINDOW

	#Go to the position
	turtle.up()
	turtle.goto(getPosition(column, row))
	turtle.down()

	#Set turtle properties
	turtle.fillcolor(color)
	turtle.pensize(1)

	#Draw a filled circle
	turtle.begin_fill()
	turtle.circle(Constants.CELL_WIDTH / 2)
	turtle.end_fill()

	#Update what is drawn
	wn.update()

# Prompts the user for a valid move then executes that move
# Params: None
# Returns: None
def promptMove():
	#Initialize some local variables
	valid_move = False
	location = ""

	#Try and except allow the program to keep going after an error
	try:
		#Only run when move is not valid
		while not valid_move:
			#Get the window
			wn = Constants.WINDOW

			#Prompt the user for a location
			location = wn.textinput("Piece Location", "Enter a location ('q' to quit): ").strip()

			#Splits location into column and row
			column_and_row = getColumnAndRow(location)

			#Extract column and row
			column = column_and_row[0]
			row = column_and_row[1]

			#Check if the move is valid
			valid_move = checkvalidity(column, row)

			#Alert the user
			if not valid_move:
				print("That is not a valid position!")

		#Place a piece at the position
		placePiece(column, row, "white")
	except:
		#Message printed after an error
		print("Game over.")

	#Exit when the screen is clicked
	Constants.WINDOW.exitonclick()

# Draws the board and places starting pieces
# Params: None
# Returns: None
def setup():
	#Draws the board
	ReversiGrid.main()

	#Places starting pieces for Reversi
	placePiece("D", 4, "black")
	placePiece("E", 4, "white")
	placePiece("D", 5, "white")
	placePiece("E", 5, "black")

#Only run this file if it is the main file
if __name__ == "__main__":
	setup()
	promptMove()
