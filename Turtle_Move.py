import string

def get_stripped_line(location):
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
	#Get the stripped line ex: A8
	colum_and_row = get_stripped_line(location)

	#Get the column
	column = colum_and_row[:1]

	#Get the row
	row = int(colum_and_row[1:])

	#Return column and row
	return [column, row]

def check_validity(column, row):
	#columns = {"A" : 1, "B" : 2, "C" :  3, "D" : 4, "E" : 5, "F" : 6, "G" :  7, "H" : 8}
	#return (columns[column] >= 1 and columns[column] <= 8) and (row >= 1 and row <= 8)
	columns = "ABCDEFGH"
	column = column.upper()
	return (column in columns) and (row >= 1 and row <= 8)

def place_piece(column, row):
	column = column.upper()
	print(column, row)

def prompt_move():
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

	#Place a piece at the position
	place_piece(column, row)

prompt_move()
