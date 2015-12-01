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

def checkRow(row, relative_location, turn_letter):	
	row_left = row[:relative_location]
	row_left.reverse()
	row_right = row[relative_location+1:] 
	
	row_left = checkRowCore(row_left, turn_letter)
	
	row_right = checkRowCore(row_right, turn_letter)
			
	if row_right or row_left ==True:
		return True
	
	else:
		return False

def checkRowCore(row, turn_letter):
	start_que = True
	que = []
	end_found = False
	
	for letter in row:
		if start_que == True:
			if letter == turn_letter:
				start_que = False
				end_found = True
			
			if letter == 'N':
				end_found = False
				start_que = False
				
				
	
	if end_found == True:	
		if len(row)> 1:
			return True
	else:
		return False
	


#Updates the board game_state vertically
#Takes the game_state as a 2D list, the relative location, and the turn letter
#Returns the updated list

def checkColumn(game_state, x, y, turn_letter):
	#Create a temporary row of all of ther vertical letters for easy updating
	temp_row = []
	for row in game_state:
		temp_row.append(row[x])


	#Update the row
	temp_row = checkRow(temp_row, y, turn_letter)

	

	return temp_row

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

	xTracker = x
	yTracker = y
	iteration = relative-1
	for letter in diag_row:
		if 0<= yTracker <=7:
			temp_row = game_state[yTracker]
			if 0 <= xTracker <= 7:
				if 0<= iteration <= len(diag_row)-1:

					piece = diag_row[iteration]
					temp_row[xTracker] = piece
					game_state[yTracker] = temp_row

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
#The function looks long and painful, but it operates on a similar idea as updateRow and update_column
	#The function starts by getting all characters above the location that is in the diagnol and adds it the row that we can use updateRow on
	#We the then get all the characters below and add it to the row
	#After updating it, we can change the characters using the same way that we found the diagnals

def checkDiagnalDU(game_state, x, y, turn_letter):

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
	boolean = checkRow(temp_row, relative-1, turn_letter)

	return boolean




#Function updates the board's Up to Down diagnals based on a game_state, move and turn_letter
#Up to down is styled like this:
					#
				#
			#
		#
#Function returns the updates game_state
#The function looks long and painful, but it operates on a similar idea as updateRow and update_column
	#The function starts by getting all characters above the location that is in the diagnol and adds it the row that we can use updateRow on
	#We the then get all the characters below and add it to the row
	#After updating it, we can change the characters using the same way that we found the diagnals

#Function works the same as the other diagnal updater, just with a modified dirction addition
def checkDiagnalUD(game_state, x, y, turn_letter):
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
	boolean = checkRow(temp_row, relative-1, turn_letter)


	return boolean
	#We now need to update the game_state to match the diag that was just updated

#Function updates the game_state based on a move, that is assumed valid
#Only updates horizontal and vertical, will update diagnol eventually
#Takes the current game_state, the move, and the turn letter
#Returns the updated game_state
def checkGameState(game_state, move, turn_letter):
	#Get the x and y coordinates in the move,
	#Subtract 1 so they can be used as list indexes
	xy = convertMove(move)
	x = xy[0]-1
	y = xy[1]-1

	temp_game_state = game_state[:]

	#Update the column
	column_boolean = checkColumn(game_state, x, y, turn_letter)

	row_boolean = checkRow(temp_game_state[y], x, turn_letter)
	
	
	#Update the diagnals in both directions
	diag_DU_boolean = checkDiagnalDU(temp_game_state, x, y, turn_letter)
	diag_UD_boolean = checkDiagnalUD(game_state, x, y, turn_letter)


	if column_boolean or row_boolean or diag_DU_boolean or diag_UD_boolean == True:
		return True
	else:
		return False

	
if __name__=="__main__":
	testCode()
