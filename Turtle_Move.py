import string

def get_stripped_line(location):
	"""
	Removes unneeded characters from a string.
	Unneeded characters include blank space and punctuation.
	Returns a string on only numbers and letters, ex: A8
	"""
	
	#Get all characters that can't be used
	not_needed_chars = string.punctuation + string.whitespace + " "

	#Store location
	stripped_line = location

	#Remove every character that is not need
	for i in not_needed_chars:
		stripped_line = stripped_line.replace(i, "")

	#Return the stripped line
	return stripped_line

def get_column_and_row(location):
	"""
	Takes a string in the form letterNumber, ex: B6 and separates number from letter.
	Returns an array of [letter, number]; ex: ['A', 2]
	"""
	
	#Get the stripped line ex: A8
	column_and_row = get_stripped_line(location)

	#Get the column
	column = column_and_row[:1]

	#Get the row
	row = int(column_and_row[1:])

	#Return column and row
	return [column, row]

def check_validity(column, row):
	"""
		Checks if the coordinate lies within the board.
		Takes the column and row of the coordinate.
		Returns True if on the board and False otherwise.
	"""
	#columns = {"A" : 1, "B" : 2, "C" :  3, "D" : 4, "E" : 5, "F" : 6, "G" :  7, "H" : 8}
	#return (columns[column] >= 1 and columns[column] <= 8) and (row >= 1 and row <= 8)
		
	#Valid columns
	columns = "ABCDEFGH"
	
	#Change entered column to uppercase
	column = column.upper()
	
	#Check if column is in the valid columns and is in the rows
	return (column in columns) and (row >= 1 and row <= 8)

def place_piece(column, row):
	"""
	Places a piece at a column and row
	Takes a column, ex: 'A'	and a row, ex: 8
	"""
	
	#Upper case letter
	column = column.upper()
	
	
	print(column, row)

def prompt_move():
	"""Prompts the user for a move until it is valid. 
	Then places a piece on the board if the move is valid."""
	
	valid_move = False

	#Only run when move is not valid
	while not valid_move:
		#Prompt the user for a location
		location = input("Enter a location: ").strip()

		#Splits location into column and row
		column_and_row = get_column_and_row(location)

		#Extract column and row
		column = column_and_row[0]
		row = column_and_row[1]

		print(column + str(row))

		#Check if the move is valid
		valid_move = check_validity(column, row)
		
		#Alert the user
		if not valid_move:
			print("That is not a valid position!")

	#Place a piece at the position
	place_piece(column, row)

#Only run this file if it is the main file
if __name__ == "__main__":
	prompt_move()
