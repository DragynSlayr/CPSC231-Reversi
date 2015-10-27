import TurtleMove
import string
import Constants
import ReversiGrid
import StringInterpret

#Function returns a string that represents the initial grid state
#Takes no parameters
def initializeGridStringStart():
	token = 'NNNNNNNNNNNNNNNNNNNNNNNNNNNBWNNNNNNWBNNNNNNNNNNNNNNNNNNNNNNNNNNN'
	return token


#Function takes a string and a location and returns the char at the loction
def getChar(token, location):
	#print(location, "in", token)
	character = token[location-1]
	return character

#Converts a column letter to an index number
#Takes a column letter as a parameter
def convertColumnNumber(column):
	column_All = 'ABCDEFGH'
	loopcount = 0
	for letter in column_All:
		if column.upper() == letter:
			return loopcount +1
		loopcount = loopcount +1

	#print (column)
	return 'invalid_range'

#Function checks if a location is on the board
#Function takes the current grid string and an unstripped location string
#Returns Boolean whether or not it is on the grid.
def validateMoveLocation(token, location):
	
	xy = TurtleMove.getColumnAndRow(location)
	x =  convertColumnNumber(xy[0]) #NOTE!!: This will be assigned 'invalid_range' if it is outside of range. This is done by the convert function
	y = xy[1]
	
	#Check if the location is on the board,
	if x == 'invalid_range':
		
		return False

	if 0<= y > 8:
		
		return False

	#Checks if the location is occupied already
	if 'N' != getChar(token, x + (8*(y -1))):
		#All of that math simply takes the number of x + a certain number of rows
		return False
	else:
		#If the location is on the board return True.
		return True

#Displays a window that asks the user for input
#Takes a message as input
#Returns the user's input
def menuInput(text):
	wn = Constants.WINDOW
	user_input = wn.textinput("User Input", text)
	return user_input

#Function asks the user for a move and then validates it
#Takes the current string state and a message to prompt the user
#Function returns the move if valid
def getMove(token, message):
	user_move = menuInput(message)
	if user_move == None:
		return "invalid"
	else:
		valid_move = False
		while not valid_move:
			#Check if the move is at least length 2
			if len(user_move) == 2:
				
				valid_move = validateMoveLocation(token, user_move)
			else:
				
				valid_move = False
			#Ask the user for the move again if it is not valid
			if not valid_move:
				user_move = menuInput("Invalid Location: Re-Enter")
		return user_move

#Function updates the string to include the move
#Takes previous grid state and the location change, and colour
#Function returns updated grid state
#Example: updateStringState(initializeGridStringStart(), 'H8', 'B')
def updateStringState(token, location, colour):
	#Get column and row from location
	xy = TurtleMove.get_column_and_row(location)

	#Extract column and row from above
	x =  convertColumnNumber(xy[0]) #NOTE!!: This will be assigned 'invalid_range' if it is outside of range. This is done by the convert function
	y = xy[1] - 1 #This needs to start at 0 in order to match the for loop

	#Convert column and row to an index
	update_location = (8*y + x)
	letter_tracker = 0
	new_token = ''

	#Iterate through gamesate and accumulate an updated board
	for letter in token:
		letter_tracker = letter_tracker +1
		if letter_tracker == update_location:
			new_token = new_token + colour
		else:
			new_token = new_token + letter

	return new_token
