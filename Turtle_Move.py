def check_validity(column, row):
	#columns = {"A" : 1, "B" : 2, "C" :  3, "D" : 4, "E" : 5, "F" : 6, "G" :  7, "H" : 8}
	#return (columns[column] >= 1 and columns[column] <= 8) and (row >= 1 and row <= 8)
	columns = "ABCDEFGH"
	column = column.upper()
	return (column in columns) and (row >= 1 and row <= 8)
	
def place_piece(column, row):
	print(column, row)
		
def prompt_move():
	valid_move = False
	while not valid_move:
		#Prompt the user for a location
		column = input("Enter a column letter: ")
		row = int(input("Enter a row number: "))
		
		#Check if the move is valid
		valid_move = check_validity(column, row)
	place_piece(column, row)
	
prompt_move()
