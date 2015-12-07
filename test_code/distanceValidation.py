import screenState
import stringInterpret
import reversiGrid
import converter
import turtleMove
import constants
import listUpdater

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




#Function takes a specific row or list, the location that a piece has been placed, and the turn letter as parameters
#Function then returns if the row and move would result in the change
#Returns boolean
def checkRow(row, relative_location, turn_letter):	
	#Get the left and right side of the rows
	row_left = row[:relative_location]
	row_left.reverse()
	row_right = row[relative_location+1:] 
	
	#Check their boolean
	row_left = checkRowCore(row_left, turn_letter)
	row_right = checkRowCore(row_right, turn_letter)
		

	
	if row_right or row_left ==True:
		return True
	
	else:
		return False

		
#Function checks if partial row and turn_letter would result in a change being made
#If a change would be made then the move is valid
#Returns Boolean		
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
		if len(row)> 2:
			return True
	else:
		return False
	


#Function checks distance validation fo a column
#Returns Boolean

def checkColumn(game_state, x, y, turn_letter):
	#Create a temporary row of all of ther vertical letters for easy updating
	temp_row = []
	for row in game_state:
		temp_row.append(row[x])


	#check the row
	boolean = checkRow(temp_row, y, turn_letter)

	

	return boolean

#
	


#Function checks distance validation for the down - up diagnal
#Takes the game state, move coordinates and turn_letter
#returns boolean

def checkDiagnalDU(game_state, x, y, turn_letter):

	#Get the diagnals in both directions
	left_row = listUpdater.getDiagnal(game_state, x, y, -1, 1)
	left_row.reverse()
	right_row = listUpdater.getDiagnal(game_state, x, y, 1, -1 )

	#Form the the row that is to updated, and add in the turn_letter
	temp_row = left_row
	temp_row.append(turn_letter)
	temp_row = temp_row + right_row


	#find the location of the turn_letter relative to the diagnal, which is needed to update the row
	relative = len(left_row)


	#Check the row
	boolean = checkRow(temp_row, relative-1, turn_letter)

	return boolean


#Function checks the distance validation in the other diagnal Up - Down
#Returns boolean
#Function works the same as the other diagnal checker, just with a modified dirction addition
def checkDiagnalUD(game_state, x, y, turn_letter):
	#Get the diagnals in both directions
	left_row = listUpdater.getDiagnal(game_state, x, y, 1, 1)
	left_row.reverse()									#SE
	right_row = listUpdater.getDiagnal(game_state, x, y, -1, -1)		#NW


	#Form the the row that is to updated, and add in the turn_letter
	temp_row = left_row
	temp_row.append(turn_letter)
	temp_row = temp_row + right_row


	#find the location of the turn_letter relative to the diagnal, which is needed to update the row
	relative = len(left_row)

	#Check the row
	boolean = checkRow(temp_row, relative-1, turn_letter)


	return boolean
	#We now need to update the game_state to match the diag that was just updated

#Function checks the game_state based on a move, that is assumed to be on the board
#Takes the current game_state, the move, and the turn letter
#Returns boolean
def checkGameState(game_state, move, turn_letter):
	#Get the x and y coordinates in the move,
	#Subtract 1 so they can be used as list indexes
	xy = convertMove(move)
	x = xy[0]-1
	y = xy[1]-1

	temp_game_state = game_state[:]

	#Check the column
	column_boolean = checkColumn(game_state, x, y, turn_letter)

	row_boolean = checkRow(temp_game_state[y], x, turn_letter)
	
	
	#Check the diagnals in both directions
	diag_DU_boolean = checkDiagnalDU(temp_game_state, x, y, turn_letter)
	diag_UD_boolean = checkDiagnalUD(game_state, x, y, turn_letter)


	if column_boolean or row_boolean or diag_DU_boolean or diag_UD_boolean == True:
		return True
	else:
		return False


