#This file contains methods that help with overall move validation
import TurtleMove
import string
import Constants
import ReversiGrid
import StringInterpret

#Function returns a string that represents the initial grid state
#Takes no parameters
def initializeGridStringStart():
	game_state = 'NNNNNNNNNNNNNNNNNNNNNNNNNNNBWNNNNNNWBNNNNNNNNNNNNNNNNNNNNNNNNNNN'
	return game_state

#Function takes a string and a location and returns the char at the loction
def getChar(game_state, location):
	#print(location, "in", game_state)
	character = game_state[location-1]
	return character

#Converts a column letter to an index number
#Takes a column letter as a parameter
def convertColumnNumber(column):
	loopcount = 0
	column = column.upper()
	for i in range(len(Constants.COLUMN_LETTERS)):
		if column == Constants.COLUMN_LETTERS[i]:
			return i + 1

	#print (column)
	return 'invalid_range'

#Function checks if a location is on the board
#Function takes the current grid string and an unstripped location string
#Returns Boolean whether or not it is on the grid.
def validateMoveLocation(game_state, location):
	xy = TurtleMove.getColumnAndRow(location)
	x =  convertColumnNumber(xy[0]) #NOTE!!: This will be assigned 'invalid_range' if it is outside of range. This is done by the convert function
	y = xy[1]

	#Check if the location is on the board,
	if x == 'invalid_range':
		return False
	if 0 <= y > 8:
		return False

	#print("Move:", y, x)

	#Checks if the location is occupied already
	#return getChar(game_state, x + (8*(y -1))) == Constants.PIECE_NONE
	return game_state[y - 1][x - 1] == Constants.PIECE_NONE
	#All of that math simply takes the number of x + a certain number of rows

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
def getMove(game_state, message):
	user_move = menuInput(message)
	if user_move == None:
		return "invalid"
	else:
		valid_move = False
		while not valid_move:
			#Check if the move is at least length 2
			if len(user_move) == 2:
				valid_move = validateMoveLocation(game_state, user_move)
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
def updateStringState(game_state, location, colour):
	#Get column and row from location
	xy = TurtleMove.get_column_and_row(location)

	#Extract column and row from above
	x =  convertColumnNumber(xy[0]) #NOTE!!: This will be assigned 'invalid_range' if it is outside of range. This is done by the convert function
	y = xy[1] - 1 #This needs to start at 0 in order to match the for loop

	#Convert column and row to an index
	update_location = (8*y + x)
	letter_tracker = 0
	new_state = ''

	#Iterate through gamesate and accumulate an updated board
	for letter in game_state:
		letter_tracker = letter_tracker +1
		if letter_tracker == update_location:
			new_state = new_state + colour
		else:
			new_state = new_state + letter

	return new_state
