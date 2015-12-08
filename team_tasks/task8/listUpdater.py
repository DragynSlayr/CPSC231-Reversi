#This file handles all the flipping of the pieces after they are placed,
#also heavily needed for move validation
import turtleMove
import constants
import converter

#Converts a location to it's indexes
#Params: location, The location to convert
#Returs: X and Y index of the location as [X, Y]
#Author: David Keizer
#Editor: Inderpreet Dhillon
def convertMove(location):
	#Separate column from row
	column = location[0]
	row = int(location[1])

	#Get indices
	x = constants.COLUMN_LETTERS.index(column) + 1
	y = constants.ROW_NUMBERS.index(row) + 1

	#Return indices
	return [x, y]

#Inverse of convertMove, converts X and Y to a move
#Params: x, The x of the location
#		 y, The y of the location
#Returns: A move of form "A1"
def convertMoveType(x, y):
	#Convert x
	x = constants.COLUMN_LETTERS[x]

	#Return x and y
	return [x, y]

#Takes a the turn letter and returns the opposite turn letter
#Params: char, The char to inverse
#Returns: The opposite letter to char
#Author: David Keizer
#Editor: None
def inverseTurnChar(char):
	if char == constants.PIECE_BLACK:
		return constants.PIECE_WHITE
	elif char == constants.PIECE_WHITE:
		return constants.PIECE_BLACK
	else:
		return 'Error Invalid Param'

#Places a piece at x, y of color determined by temp_piece
#Params: x, The x coordinate to place at
#		 y, The y coordinate to place at
#		 temp_piece, The letter of the piece to be placed
#Returns: None
#Author: David Keizer
#Editor: Inderpreet Dhillon
def charToPiece(x, y, temp_piece):
	#Convert x and y
	conv_move = convertMoveType(x, y)
	temp_x = conv_move[0]

	#Add 1 in order to start counting at 1
	temp_y = conv_move[1] + 1

	#Only draw in not a blank space
	if temp_piece != constants.PIECE_NONE:
		#Get the colour of the piece
		if temp_piece == constants.PIECE_BLACK:
			color = constants.PIECE_COLOR_BLACK
		else:
			color = constants.PIECE_COLOR_WHITE

		#Place the piece on the board in the appropriate spot
		turtleMove.placePiece(temp_x, temp_y, color)

#IMPORTANT FUNCTION: - Any Logic Errors in the will be pervasive
#<<<<< FUNCTION ASSUMES ALL PASSED PARAMETERS ARE ALREADY VALIDATED
#Takes row as a list of the chars to works with, the location of the char in the string, and the letter that was placed.
#row = 			['N', 'W', 'B', 'W', 'N', 'W', 'N']
#Say we insert a 'B' here 			  ^ at the the relative location of 5
#Would return 	['N', 'W', 'B', 'B', 'B', 'W', 'N']
#Function takes a specific row or list, the location that a piece has been placed, and the turn letter as parameters
#Function then updates the row as if it was horizontal
#Works for 'rows' of all sizes
#returns the updated row
#Author: David Keizer
#Editor: None
def updateRow(row, relative_location, turn_letter):
	row_left = row[:relative_location]
	row_left.reverse()
	row_right = row[relative_location + 1:]

	row_left = updateCore(row_left, turn_letter)
	row_left.reverse()
	row_right = updateCore(row_right, turn_letter)

	new_row = row_left
	new_row.append(turn_letter)
	new_row = new_row + row_right

	return new_row

#Function is the core of the list updating
#Takes a portion of a list in the form of a row
#Also takes the turn_letter
#Function returns the row updated assuming it is the right half of a list to be upadated
#Author: David Keizer
#Editor: None
def updateCore(row, turn_letter):
	#Declare Necessary Variables
	start_que = True
	que = []
	end_found = False

	#Main loop adds letters to the que until the end is found
	for letter in row:
		if start_que == True:
			if letter == inverseTurnChar(turn_letter):
				#add the letter to the que
				que.append(letter)

			#check if the end was found and if so end the que additions
			if letter == turn_letter:
				start_que = False
				end_found = True

			#Check if the end is empty, and then empty the que as it is no longer valid
			if letter == constants.PIECE_NONE:
				end_found = False
				start_que = False
				que = []

	#Update the row based on the letters in the que
	index = 0
	if end_found == True and len(que) > 0:
		for letter in que:
			row[index] = turn_letter
			index = index+1

	return row

#Updates the board game_state vertically
#Takes the game_state as a 2D list, the relative location, and the turn letter
#Returns the updated list
#Author: David Keizer
#Editor: None
def updateColumn(game_state, x, y, turn_letter, draw_move = True):
	#Create a temporary row of all of ther vertical letters for easy updating
	temp_row = []
	for row in game_state:
		temp_row.append(row[x])

	#Update the row
	temp_row = updateRow(temp_row, y, turn_letter)

	#Using the updated row, change the game_state
	new_game_state = game_state [:]
	index = 0

	#index is what tracks where we are in the updated row
	for row in new_game_state:
		if index < len(temp_row):
			#Update the piece in the location in the game_state
			temp_piece = temp_row[index]
			row[x] = temp_piece

			#update board
			if draw_move:
				charToPiece(x, index, temp_piece)

		index = index + 1

	return new_game_state

#Function returns a diagonal based on the direction that it is given
#Functions takes the game state, x and y coordinates of the move
#deltaX and deltaY represent the change in direction in the 2d list.
#returns the diagonal that was found in said direction
#Author: David Keizer
#Editor: None
def getDiagonal(game_state, x, y, deltaX, deltaY):
	#Declare all necessary variables
	edge_found = False
	yTracker = y + deltaY	#We change the x and y coord so that it skips the coordinate given
	xTracker = x + deltaX
	diag_row = []

	#Until we hit an edge: (when we index a list out of range)
	#We can still incriment the trackers and find more pieces
	while edge_found == False:
		if 0<= yTracker <=7:
			#Find the y coord
			temp_row = game_state[yTracker]
			if 0 <= xTracker <= 7:
				#Find the x coord
				temp_piece = temp_row[xTracker]
				diag_row.append(temp_piece)
			else:
				edge_found = True
		else:
			edge_found = True

		#Incriment in the direction desired
		xTracker = xTracker + deltaX
		yTracker = yTracker + deltaY

	return diag_row

#Function updates the game state for diagonals based on the change desired, then places them on the board
#Takes many parameters because this has to be a very versatile function
#game_state is the 2d list representing the board
#diag_row is the row that represents the diagonal to insert
#x is the coord, and likewise y is the y coord (number based on a 0 index)
#relative is the relative location in the diag_row that the piece was placed
#deltaX is the change in x, used for handling directions.
#deltaY is the change in y, used to handling directions
#deltaIteration handles if the function moves forward or backward in the string
#Author: David Keizer
#Editor: None
def diagCore(game_state, diag_row, x, y, relative, deltaX, deltaY, deltaIteration, draw_move = True):
	#Declare necessary variables
	xTracker = x
	yTracker = y
	iteration = relative-1

	#main loop
	for letter in diag_row:
		if 0<= yTracker <=7:
			#find row that we are need
			temp_row = game_state[yTracker]
			if 0 <= xTracker <= 7:
				#find piece that is needed
				if 0<= iteration <= len(diag_row)-1:
					#find piece that is needed
					#and then update it using the updated row
					piece = diag_row[iteration]
					temp_row[xTracker] = piece
					game_state[yTracker] = temp_row

					if draw_move:
						#update board
						charToPiece(xTracker, yTracker, piece)

		xTracker = xTracker + deltaX
		yTracker = yTracker + deltaY
		iteration = iteration + deltaIteration

#Function updates the board's Up to Down diagonals based on a game_state, move and turn_letter
#Up to down is styled like this:
		#
			#
				#
					#
#Function returns the updates game_state
#Author: David Keizer
#Editor: None
def updatediagonalDU2(game_state, x, y, turn_letter, draw_move = True):
	#Get the diagonals in both directions
	left_row = getDiagonal(game_state, x, y, -1, 1)
	left_row.reverse()
	right_row = getDiagonal(game_state, x, y, 1, -1 )

	#Form the the row that is to updated, and add in the turn_letter
	temp_row = left_row
	temp_row.append(turn_letter)
	temp_row = temp_row + right_row

	#find the location of the turn_letter relative to the diagonal, which is needed to update the row
	relative = len(left_row)

	#Update the row
	diag_row = updateRow(temp_row, relative-1, turn_letter)

	#update in the NE direction
	diagCore(game_state, diag_row, x, y, relative, 1, -1, 1, draw_move)

	#update in the SE direction
	diagCore(game_state, diag_row, x, y, relative, -1, 1, -1, draw_move)

	return game_state

#Function updates the board's Up to Down diagonals based on a game_state, move and turn_letter
#Up to down is styled like this:
					#
				#
			#
		#
#Function returns the updates game_state
#Function works the same as the other diagonal updater, just with a modified dirction addition
#Author: David Keizer
#Editor: None
def update_diagonalUD2(game_state, x, y, turn_letter, draw_move = True):
	#Get the diagonals in both directions
	left_row = getDiagonal(game_state, x, y, 1, 1)
	left_row.reverse()									#SE
	right_row = getDiagonal(game_state, x, y, -1, -1)		#NW

	#Form the the row that is to updated, and add in the turn_letter
	temp_row = left_row
	temp_row.append(turn_letter)
	temp_row = temp_row + right_row

	#find the location of the turn_letter relative to the diagonal, which is needed to update the row
	relative = len(left_row)

	#Update the row
	diag_row = updateRow(temp_row, relative-1, turn_letter)

	#Apply the update to the old game_state
	#update in the NW direction
	diagCore(game_state, diag_row, x, y, relative, -1, -1, 1, draw_move)

	#update in the SE direction
	diagCore(game_state, diag_row, x, y, relative, 1, 1, -1, draw_move)

	return game_state

#Prints a game state
#Params: game_state, The state to print
#Returns: None
#Author: David Keizer
#Editor: Inderpreet Dhillon
def showCurrentGameState(game_state):
	print("<<<Current Game State >>>")
	print("        A    B    C    D    E    F    G    H")
	counter = 1
	for row in game_state:
		print(counter , " : " , row)
		counter = counter + 1

#Function updates the game_state based on a move, that is ASSUMED VALID
#Only updates horizontal and vertical, will update diagnol eventually
#Takes the current game_state, the move, and the turn letter and whether update to grid
#Returns the updated game_state
#Author: David Keizer
#Editor: None
def updateGameState(game_state, move, turn_letter, draw_move = True):
	#Get the x and y coordinates in the move,
	#Subtract 1 so they can be used as list indexes
	xy = convertMove(move)
	x = xy[0]-1
	y = xy[1]-1

	#Create a copy of the state
	temp_game_state = converter.toList(converter.toString(game_state))

	#Update the row
	temp_row = updateRow(temp_game_state[y], x, turn_letter)
	temp_game_state[y] = temp_row

	#Update the column
	temp_game_state = updateColumn(game_state, x, y, turn_letter, draw_move)

	#Update the diagonals in both directions
	temp_game_state = updatediagonalDU2(temp_game_state, x, y, turn_letter, draw_move)
	temp_game_state = update_diagonalUD2(game_state, x, y, turn_letter, draw_move)

	#Update the row
	temp_row = updateRow(temp_game_state[y], x, turn_letter)
	temp_game_state[y] = temp_row

	#Because updateRow does not draw the pieces on the board, unlike the other update functions, we must draw them here
	if draw_move == True:
		counter = 0
		for i in temp_row:
			conv_move = convertMoveType(counter, y+1)
			Tx = conv_move[0]
			Ty = conv_move[1]
			if i != constants.PIECE_NONE:
					if i == constants.PIECE_BLACK:
						temp_piece = constants.PIECE_COLOR_BLACK
					else:
						temp_piece = constants.PIECE_COLOR_WHITE
					if draw_move:
						turtleMove.placePiece(Tx, Ty , temp_piece)
			counter = counter + 1

	return temp_game_state

#Generic test code
#Do not worry about this, it was just used for debugging
#Author: David Keizer
#Editor: None
def testCode():
	row = ['N', 'N', 'W', 'W', 'W', 'N', 'N', 'N']
	print(row)
	row = updateRow(row, 1, 'B')
	print(row)
	"""
	print("CHECK HORIZONTAL BASIC::>>>")
	print("  A    B    C    D    E    F    G    H")
	game_state =         [['W', 'B', 'B', 'B', 'B', 'B', 'B', 'W', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]

	for row in game_state:
		print(row)
	print("  ")
	print("  is now  >>>")
	print("  A    B    C    D    E    F    G    H")

	game_state = updategame_state(game_state, 'C1', 'W')
	for row in game_state:
		print(row)

	game_state = []
	print("CHECK VERTICAL BASIC::>>>")
	print(" A    B    C    D    E    F    G    H")
	game_state =         [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'W', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'W', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'B', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'B', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'B', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'B', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'W', ]]
	for row in game_state:
		print(row)
	print("  ")
	print("  is now  >>>")
	print(" A    B    C    D    E    F    G    H")

	game_state = updategame_state(game_state, 'H2', 'W')
	for row in game_state:
		print(row)

	"""

	game_state = []
	print("CHECK DU diagonal BASIC::>>>")
	print(                    "  A    B    C    D    E    F    G    H")
	game_state =         	  [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'W', 'B', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'W', 'W', 'W', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	for row in game_state:
		print(row)

	print("  ")
	print("  is now  >>>")
	print(" A    B    C    D    E    F    G    H")

	game_state = updateGameState(game_state, 'C4', 'B')
	for row in game_state:
		print(row)
	""""
	game_state = []
	print("CHECK UD diagonal BASIC BASIC::>>>")
	print(" A    B    C    D    E    F    G    H")
	game_state =         [['B', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'W', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'W', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'W', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'B', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'W', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'B', ]]
	for row in game_state:
		print(row)

	print("  ")
	print("  is now  >>>")
	print(" A    B    C    D    E    F    G    H")

	game_state = updategame_state(game_state, 'D4', 'B')
	for row in game_state:
		print(row)

	game_state = []
	print("CHECK UD diagonal BASIC BASIC::>>>")
	print("  A    B    C    D    E    F    G    H")
	game_state =         [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	for row in game_state:
		print(row)

	print("  ")
	print("  is now  >>>")
	print(" A    B    C    D    E    F    G    H")

	game_state = updategame_state(game_state, 'A1', 'B')
	for row in game_state:
		print(row)

	game_state = []
	print("CHECK CUSTOM BASIC BASIC::>>>")
	print("  A    B    C    D    E    F    G    H")

	game_state =         [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'W', 'B', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'B', 'W', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'W', 'N', ]]
	tempCount = 1
	for row in game_state:
		print(tempCount, " ", row)
		tempCount = tempCount +1

	tempCount = 1
	print("  ")
	print("  is now  >>>")

	game_state = updategame_state(game_state, 'H8', 'B')
	print("      A    B    C    D    E    F    G    H")
	for row in game_state:
		print(tempCount, " ", row)
		tempCount = tempCount +1

	['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N']
	" A     B   C    D    E    F    G    H"
	['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N']
	['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N']
	['N', 'N', 'N', 'W', 'B', 'N', 'N', 'N']
	['N', 'N', 'N', 'B', 'W', 'N', 'N', 'N']
	['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N']
	['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N']
	['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N']
	row = ['B', 'W', 'W', 'N', 'W', 'B', 'W', 'B']
	print(row)
	row = updateRow(row, 2, 'B')
	print(row)
	"""

if __name__=="__main__":
	testCode()
