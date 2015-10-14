#Gets the positive representation of a number
#Params: num, The number to get the absolute value of
#Returns: The absolute value of the num
def absolute(num):
	if num < 0:
		return -num
	else:
		return num

#Checks if the piece is on the board
#Params: row, The row of the piece
#		 column, The colum of the piece
#Returns: True if the column and row are valid
def isOnBoard(row, column):
	return (row >= 1 and row <= 8) and (column >= 1 and column <= 8)

#Checks if a knight's move is valid on a chess board
#Params: start_row, The row to start in
#		 start_column, The column to start in
#		 end_row, The row to end in
#		 end_column, The column to end in
#Returns: True if the move is valid, False otherwise
def isValidMove(start_row, start_column, end_row, end_column):
	#Check if the move is on the board
	if isOnBoard(start_row, start_column) and isOnBoard(end_row, end_column):
		#Check if the move can be made
		if absolute(start_column - end_column) == 2 and absolute(start_row - end_row) == 1:
			return True
		elif absolute(start_column - end_column) == 1 and absolute(start_row - end_row) == 2:
			return True
		else:
			return False
	else:
		return False

if __name__ == "__main__":
	#Valid cases
	print("\n+~~~~~~~~~~+")
	print("|True Cases|")
	print("+~~~~~~~~~~+")
	print("|  ", isValidMove(4, 3, 2, 4), "  |")
	print("|  ", isValidMove(4, 3, 3, 5), "  |")
	print("|  ", isValidMove(4, 3, 2, 2), "  |")
	print("|  ", isValidMove(4, 3, 3, 1), "  |")
	print("|  ", isValidMove(4, 3, 5, 5), "  |")
	print("|  ", isValidMove(4, 3, 6, 4), "  |")
	print("|  ", isValidMove(4, 3, 6, 2), "  |")
	print("|  ", isValidMove(4, 3, 5, 1), "  |")
	print("+~~~~~~~~~~+\n")
	
	#Invalid cases
	print("\n+~~~~~~~~~~~+")
	print("|False Cases|")
	print("+~~~~~~~~~~~+")
	print("|  ", isValidMove(5, 3, 2, 4), "  |")
	print("|  ", isValidMove(9, 9, 0, 0), "  |")
	print("|  ", isValidMove(5, 3, 2, 4), "  |")
	print("|  ", isValidMove(0, 0, -1, 6), "  |")
	print("+~~~~~~~~~~~+\n")
	
