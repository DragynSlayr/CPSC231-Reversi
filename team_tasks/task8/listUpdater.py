import screenState
import stringInterpret
import reversiGrid
import converter
import turtleMove
import constants

#Converts the location into a list of ints that represent the x y coordinates
#Only parameter is the location as a string, ex 'A7' or 'H8'
#Returns a list of ints: ex [1, 7] or [8, 8]
def convertMove(location):
	letter = location[0]
	number = int(location[1])

	column = constants.COLUMN_LETTERS.index(letter) + 1
	row = constants.ROW_NUMBERS.index(number) + 1

	return [column, row]

#This does the opposite of the previous function: It takes an x and a y coordinate ex(1, 2)
#And then converts it into the form that turtleMove.placePiece can use.
#Returns: a char and a integer
#Ex ['A', 2]
def convertMoveType(x, y):
	x = constants.COLUMN_LETTERS[x]

	return [x, y]

#Takes a the turn letter and returns the opposite turn letter
#Ex 'W' returns 'B'
# and 'B' returns 'W'
def inverseTurnChar(char):
	if char == constants.PIECE_BLACK:
		return constants.PIECE_WHITE
	elif char == constants.PIECE_WHITE:
		return constants.PIECE_BLACK
	else:
		return 'Error Invalid Param'

		
#Takes list based coordinates and a colour and placed the piece in the location
#Takes x and y coordinates as well as the piece type from a list. 
#ex charToPiece(0, 0, 'B') would place a black piece at A1.
def charToPiece(x, y, temp_piece):
	conv_move = convertMoveType(x, y)
	temp_x = conv_move[0]
	temp_y = conv_move[1] + 1 #Add 1 in order to start counting at 1

	#Get the colour of the piece
	if temp_piece != constants.PIECE_NONE:
		if temp_piece == constants.PIECE_BLACK:
			color = "Black"
		else:
			color = "White"
		#Place the piece on the board in the appropriate spot
		turtleMove.placePiece(temp_x, temp_y, color)

#IMPORTANT FUNCTION: - Any Logic Errors in the will be persvasive
#<<<<< FUNCTION ASSUMES ALL PASSED PARAMETERS ARE ALREADY VALIDATED
#Takes row as a list of the chars to works with, the location of the char in the string, and the letter that was placed.
#row = 			['N', 'W', 'B', 'W', 'N', 'W', 'N']
#Say we insert a 'B' here   ^ at the the relative location of 5
#Would return 	['N', 'W', 'B', 'B', 'B', 'W', 'N']

#Function takes a specific row or list, the location that a piece has been placed, and the turn letter as parameters
#Function then updates the row as if it was horizontal
#Works for "rows" of all sizes
#returns the updated row

def updateRow(row, relative_location, turn_letter):	
	row_left = row[:relative_location]
	row_left.reverse()
	row_right = row[relative_location+1:] 
	
	row_left = updateCore(row_left, turn_letter)
	row_left.reverse()
	row_right = updateCore(row_right, turn_letter)
			
	new_row = row_left 
	new_row.append(turn_letter) 
	new_row = new_row + row_right
	
	return new_row

	
	
#Function is the core of the list updation.
#Takes a portion of a list in the form of a row
#Also takes the turn_letter
#Function returns the row updated assuming it is the right half of a list to be upadated	
	
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
			if letter == 'N':
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

def updateColumn(game_state, x, y, turn_letter):
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
			charToPiece(x, index, temp_piece)

		index = index + 1

	return new_game_state

	
#Function returns a diagnal based on the direction that it is given
#Functions takes the game state, x and y coordinates of the move
#deltaX and deltaY represent the change in direction in the 2d list.
#returns the diagnal that was found in said direction	
	
def getDiagnal(game_state, x, y, deltaX, deltaY):
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



#Function updates the game state for diagnals based on the change desired, then places them on the board
#Takes many parameters because this has to be a very versatile function
#game_state is the 2d list representing the board
#diag_row is the row that represents the diagnal to insert
#x is the coord, and likewise y is the y coord (number based on a 0 index)
#relative is the relative location in the diag_row that the piece was placed
#deltaX is the change in x, used for handling directions.
#deltaY is the change in y, used to handling directions
#deltaIteration handles if the function moves forward or backward in the string

def diagCore(game_state, diag_row, x, y, relative, deltaX, deltaY, deltaIteration):
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
					
					
					#update board
					charToPiece(xTracker, yTracker, piece)

		xTracker = xTracker + deltaX
		yTracker = yTracker + deltaY
		iteration = iteration + deltaIteration


#Function updates the board's Up to Down diagnals based on a game_state, move and turn_letter
#Up to down is styled like this:
		#
			#
				#
					#
#Function returns the updates game_state	

def updateDiagnalDU2(game_state, x, y, turn_letter):

	#Get the diagnals in both directions
	left_row = getDiagnal(game_state, x, y, -1, 1)
	left_row.reverse()
	right_row = getDiagnal(game_state, x, y, 1, -1 )

	#Form the the row that is to updated, and add in the turn_letter
	temp_row = left_row
	temp_row.append(turn_letter)
	temp_row = temp_row + right_row


	#find the location of the turn_letter relative to the diagnal, which is needed to update the row
	relative = len(left_row)


	#Update the row
	diag_row = updateRow(temp_row, relative-1, turn_letter)



	#update in the NE direction
	diagCore(game_state, diag_row, x, y, relative, 1, -1, 1)

	#update in the SE direction
	diagCore(game_state, diag_row, x, y, relative, -1, 1, -1)


	return game_state



#Function updates the board's Up to Down diagnals based on a game_state, move and turn_letter
#Up to down is styled like this:
					#
				#
			#
		#
#Function returns the updates game_state

#Function works the same as the other diagnal updater, just with a modified dirction addition
def update_diagnalUD2(game_state, x, y, turn_letter):
	#Get the diagnals in both directions
	left_row = getDiagnal(game_state, x, y, 1, 1)
	left_row.reverse()									#SE
	right_row = getDiagnal(game_state, x, y, -1, -1)		#NW


	#Form the the row that is to updated, and add in the turn_letter
	temp_row = left_row
	temp_row.append(turn_letter)
	temp_row = temp_row + right_row


	#find the location of the turn_letter relative to the diagnal, which is needed to update the row
	relative = len(left_row)

	#Update the row
	diag_row = updateRow(temp_row, relative-1, turn_letter)

	#Apply the update to the old game_state

	#update in the NW direction
	diagCore(game_state, diag_row, x, y, relative, -1, -1, 1)

	#update in the SE direction
	diagCore(game_state, diag_row, x, y, relative, 1, 1, -1)



	return game_state
	

#Function updates the game_state based on a move, that is ASSUMED VALID
#Only updates horizontal and vertical, will update diagnol eventually
#Takes the current game_state, the move, and the turn letter
#Returns the updated game_state
def updateGameState(game_state, move, turn_letter):
	#Get the x and y coordinates in the move,
	#Subtract 1 so they can be used as list indexes
	xy = convertMove(move)
	x = xy[0]-1
	y = xy[1]-1

	temp_game_state = game_state[:]

	#Update the column
	temp_game_state = updateColumn(game_state, x, y, turn_letter)

	#Update the row
	temp_row = updateRow(temp_game_state[y], x, turn_letter)
	temp_game_state[y] = temp_row
	

	#Because updateRow does not draw the pieces on the board, unlike the other update functions, we must draw them here
	counter = 0
	for i in temp_row:

		conv_move = convertMoveType(counter, y+1)
		Tx = conv_move[0]
		Ty = conv_move[1]
		if i != constants.PIECE_NONE:
				if i == constants.PIECE_BLACK:
					temp_piece = "Black"
				else:
					temp_piece = "White"
				turtleMove.placePiece(Tx, Ty , temp_piece)
		counter = counter +1



	#Update the diagnals in both directions
	temp_game_state = updateDiagnalDU2(temp_game_state, x, y, turn_letter)
	temp_game_state = update_diagnalUD2(game_state, x, y, turn_letter)


	#Ensure that the move is updated in the token
	final_row = temp_game_state[y]
	final_row[x] = turn_letter
	temp_game_state[y] = final_row


	return temp_game_state

#Generic test code
#Do not worry about this, it was just used for debugging
def testCode():

	#row = ['N', 'N', 'N', 'W', 'B', 'N', 'N', 'N']
	#print(row)
	#row = updateRow(row, 2, 'B')
	#print(row)
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
	print("CHECK DU DIAGNAL BASIC::>>>")
	print(                    "  A    B    C    D    E    F    G    H")
	game_state =         	  [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'W', 'B', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'B', 'W', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'W', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	for row in game_state:
		print(row)

	print("  ")
	print("  is now  >>>")
	print(" A    B    C    D    E    F    G    H")

	game_state = updateGameState(game_state, 'F3', 'W')
	for row in game_state:
		print(row)
	""""
	game_state = []
	print("CHECK UD DIAGNAL BASIC BASIC::>>>")
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
	print("CHECK UD DIAGNAL BASIC BASIC::>>>")
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

	"""
	""""
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
