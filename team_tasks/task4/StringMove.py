import TurtleMove
import string
import Constants
import ReversiGrid
import StringInterpret

#Function returns a string that represents the initial grid state
#Takes no parameters
def initialize_grid_string_start():
	l_gridState = 'NNNNNNNNNNNNNNNNNNNNNNNNNNNBWNNNNNNWBNNNNNNNNNNNNNNNNNNNNNNNNNNN'
	return l_gridState


#Function takes a string and a location and returns the char at the loction
def get_Char(P_string, P_location):
	#print(P_location, "in", P_string)
	l_location = P_string[P_location-1]
	return l_location

#Converts a column letter to an index number
#Takes a column letter as a parameter
def convert_column_number(column):
	columnAll = 'ABCDEFGH'
	loopcount = 0
	for letter in columnAll:
		if column.upper() == letter:
			return loopcount +1
		loopcount = loopcount +1

	#print (column)
	return 'invalid_range'

#Function checks if a location is on the board
#Function takes the current grid string and an unstripped location string
#Returns Boolean whether or not it is on the grid.
def validate_move_location(P_gridString, P_location):
	L_xy = TurtleMove.get_column_and_row(P_location)
	L_x =  convert_column_number(L_xy[0]) #NOTE!!: This will be assigned 'invalid_range' if it is outside of range. This is done by the convert function
	L_y = L_xy[1]

	#Check if the location is on the board,
	if L_x == 'invalid_range':
		return False

	if 0<= L_y > 8:
		return False

	#Checks if the location is occupied already
	if 'N' != get_Char(P_gridString, L_x + (8*(L_y -1))):
		#All of that math simply takes the number of x + a certain number of rows
		return False
	else:
		#If the location is on the board return True.
		return True

#Displays a window that asks the user for input
#Takes a message as input
#Returns the user's input
def MenuInput(text):
	wn = Constants.WINDOW
	userinput = wn.textinput("User Input", text)
	return userinput

#Function asks the user for a move and then validates it
#Takes the current string state and a message to prompt the user
#Function returns the move if valid
def get_move(P_StringState, message):
	L_userMove = MenuInput(message)
	if L_userMove == None:
		return "invalid"
	else:
		validMove = False
		while not validMove:
			#Check if the move is not blank
			if L_userMove != "":
				validMove = validate_move_location(P_StringState, L_userMove)
			else:
				validMove = False
			#Ask the user for the move again if it is not valid
			if not validMove:
				L_userMove = MenuInput("Invalid Location: Re-Enter")
		return L_userMove

#Function updates the string to include the move
#Takes previous grid state and the location change, and colour
#Function returns updated grid state
#Example: update_string_state(initialize_grid_string_start(), 'H8', 'B')
def update_string_state(P_gridString, P_location, colour):
	#Get column and row from location
	L_xy = TurtleMove.get_column_and_row(P_location)

	#Extract column and row from above
	L_x =  convert_column_number(L_xy[0]) #NOTE!!: This will be assigned 'invalid_range' if it is outside of range. This is done by the convert function
	L_y = L_xy[1] - 1 #This needs to start at 0 in order to match the for loop

	#Convert column and row to an index
	L_updateLocation = (8*L_y + L_x)
	F_LetterTracker = 0
	L_updatedString = ''

	#Iterate through gamesate and accumulate an updated board
	for letter in P_gridString:
		F_LetterTracker = F_LetterTracker +1
		if F_LetterTracker == L_updateLocation:
			L_updatedString = L_updatedString + colour
		else:
			L_updatedString = L_updatedString + letter

	return L_updatedString
