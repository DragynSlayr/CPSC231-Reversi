#This program contains methods for updating the state once a move has been made
import constants
import converter
import stringInterpret

#Author: Kyle Hinton
#This function will change the string so that the opponents pieces, in a valid move, will be changed on the string.
#This function will change the pieces in the north direction.
#Three parameters: The game state string, the Index of the move on the string, and the current turn colour and an optional parameter for testing
#returns: Updated string with new pieces.
def CheckNorth(game_state, stringID, turn_colour, isTesting = False):
	NofChanges = 0								#Counts the number of pieces to change.
	PlaceHolder = "" 							#This will be a section of the new string.
	slice_new_state = "" 						#This will be a bigger section of the new game state string.
	new_state = "" 								#This going to be the new game stat.
	MoveID = 0									#This will make a copy of the index of the players move.
	MoveXID = 0 								#This will be a marker for where the players piece is accross from their move.
	other_colour = OtherColour(turn_colour) 	#This Determines the colour of the other player's piece.
	MoveID = stringID 							#This will make a copy of the index of the players move.


	if stringID + constants.NORTH > len(game_state) or stringID + constants.NORTH < 0:
		return game_state
	#While the next token to check is the other colour.
	#NORTH = -8
	while game_state[stringID + constants.NORTH] == other_colour:

		#Return game state if the move is not valid
		if NofChanges > (MoveID // 8) - 1:
			print("Out of bounds")
			return game_state
		if game_state[stringID + constants.NORTH] != other_colour and game_state[stringID + constants.NORTH] != turn_colour:
			print("!= any colour")
			return game_state

		#Move to check the next piece.
		stringID = stringID + constants.NORTH

		#Counts one more for the number of pieces to change.
		NofChanges = NofChanges + 1

	#If the next piece is the turn player's colour....
	if game_state[stringID + constants.NORTH] == turn_colour:

		#Mark token across is the ID of the last piece to change plus NORTH.
		MoveXID = stringID + constants.NORTH

		#While there is still a number of pieces left to change.
		while NofChanges != 0:

			#Create a block of string with the character changed at the beginning.
			PlaceHolder = turn_colour + game_state[stringID + 1:stringID - constants.NORTH]

			#Create another block of string that was assembled from the blocks of Placeholder.
			slice_new_state = slice_new_state + PlaceHolder

			#Moving backwards through the index of the pieces that need to be changed.
			stringID = stringID - constants.NORTH

			#One less piece to change.
			NofChanges = NofChanges - 1

			#testing
			if isTesting:
				print (PlaceHolder, "PlaceHolder")
				print (slice_new_state, "slice_new_state")
				print (stringID, "Index of Change")
				print (NofChanges, "Number of Changes left")

		#If there are no pieces left to change, assemble the new string.
		if NofChanges == 0:
			new_state = game_state[:MoveXID - constants.NORTH] + slice_new_state + game_state[MoveID:]

			#testing
			if isTesting:
				print ("01234567890123456789012345678901234567890")
				print (game_state)
				print (new_state)

	#Returns the new string.
	return new_state

#Author: Kyle Hinton
#This function will change the string so that the opponents pieces, in a valid move, will be changed on the string.
#This function will change the pieces in the north east direction.
#Three parameters: The game state string, the Index of the move on the string, and the current turn colour and an optional one for testing
#returns: Updated string with new pieces.
def CheckNorthEast(game_state, stringID, turn_colour, isTesting = False):
	NofChanges = 0								#Counts the number of pieces to change.
	PlaceHolder = "" 							#This will be a section of the new string.
	slice_new_state = "" 						#This will be a bigger section of the new game state string.
	new_state = "" 								#This going to be the new game stat.
	MoveID = 0									#This will make a copy of the index of the players move.
	MoveXID = 0 								#This will be a marker for where the players piece is accross from their move.
	other_colour = OtherColour(turn_colour) 	#This Determines the colour of the other player's piece.
	MoveID = stringID 							#This will make a copy of the index of the players move.

	if stringID + constants.NORTHEAST > len(game_state) or stringID + constants.NORTHEAST < 0:
		return game_state

	#While the next token to check is the other colour.
	#NORTHEAST = -7
	while game_state[stringID + constants.NORTHEAST] == other_colour:

		#Check if move is valid
		if NofChanges > (MoveID // 8) - 1:
			print("Out of bounds!")
			return game_state
		if game_state[stringID + constants.NORTHEAST] != other_colour and game_state[stringID + constants.NORTHEAST] != turn_colour:
			print(game_state[stringID + constants.NORTHEAST] != other_colour)
			print(game_state[stringID + constants.NORTHEAST] != turn_colour)
			print("!= any color")
			return game_state

		#Move to the next piece.
		stringID = stringID + constants.NORTHEAST

		#Counts one more for the number of pieces to change.
		NofChanges = NofChanges + 1

	#If the next piece is the turn player's colour....
	if game_state[stringID + constants.NORTHEAST] == turn_colour:

		#The token across is the ID of the last piece to change plus NORTHEAST.
		MoveXID = stringID + constants.NORTHEAST

		#While there is still a number of pieces left to change.
		while NofChanges != 0:

			#Create a block of string with the character changed at the beginning
			PlaceHolder = turn_colour + game_state[stringID + 1:stringID - constants.NORTHEAST]

			#Create another block of string that was assembled from the blocks of Placeholder.
			slice_new_state = slice_new_state + PlaceHolder

			#Moving backwards through the index of the pieces that need to be changed.
			stringID = stringID - constants.NORTHEAST

			#One less piece to change.
			NofChanges = NofChanges - 1

			#Testing
			if isTesting:
				print (PlaceHolder, "PlaceHolder")
				print (slice_new_state, "slice_new_state")
				print (stringID, "Index of Change")
				print (NofChanges, "Number of Changes left")

		#If there are no pieces left to change, assemble the new string.
		if NofChanges == 0:
			new_state = game_state[:MoveXID - constants.NORTHEAST] + slice_new_state + game_state[MoveID:]

			#Testing
			if isTesting:
				print ("01234567890123456789012345678901234567890")
				print (game_state)
				print (new_state)

	return new_state

#Author: Kyle Hinton
#This function will change the string so that the opponents pieces, in a valid move, will be changed on the string.
#This function will change the pieces in the east direction.
#Three parameters: The game state string, the Index of the move on the string, and the current turn colour and an optional parameter for testing
#returns: Updated string with new pieces.
def CheckEast(game_state, stringID, turn_colour, isTesting = False):
	NofChanges = 0								#Counts the number of pieces to change.
	MoveID = 0									#This will make a copy of the index of the players move.
	other_colour = OtherColour(turn_colour) 	#This Determines the colour of the other player's piece.
	MoveID = stringID 							#This will make a copy of the index of the players move.


	if stringID + constants.EAST> len(game_state) - 1 or stringID + constants.EAST < 0:
		return game_state
	#While the next token to check is the other colour.
	#EAST = 1
	while game_state[stringID + constants.EAST] == other_colour:
		#Possible statements for catching invalid moves.
		if NofChanges > ((8 - (MoveID % 8)) - 1):
			print("Out of bounds.")
			return game_state
		if game_state[stringID + constants.EAST] != other_colour and game_state[stringID + constants.EAST] != turn_colour:
			print("!= any colour")
			return game_state

		#Testing.
		if isTesting:
			print (NofChanges, "NofChanges Number of other colours")
			print (stringID + (constants.EAST), "index of other_colour")

		#Move on to the Next Token
		stringID = stringID + constants.EAST

		#Add one to the number of tokens that need to be changed.
		NofChanges = NofChanges + 1

	return game_state[:MoveID + 1] + (turn_colour * NofChanges) + game_state[MoveID + NofChanges + 1:]

#Author: Kyle Hinton
#This function will change the string so that the opponents pieces, in a valid move, will be changed on the string.
#This function will change the pieces in the south-east direction.
#Three parameters: The game state string, the Index of the move on the string, and the current turn colour and an optional one for testing
#returns: Updated string with new pieces.
def CheckSouthEast(game_state, stringID, turn_colour, isTesting = False):
	NofChanges = 0								#Counts the number of pieces to change.
	PlaceHolder = "" 							#This will be a section of the new string.
	slice_new_state = "" 						#This will be a bigger section of the new game state string.
	new_state = "" 								#This going to be the new game stat.
	MoveID = 0									#This will make a copy of the index of the players move.
	MoveXID = 0 								#This will be a marker for where the players piece is accross from their move.
	other_colour = OtherColour(turn_colour) 	#This Determines the colour of the other player's piece.
	MoveID = stringID 							#This will make a copy of the index of the players move.


	if stringID + constants.SOUTHEAST > len(game_state) or stringID + constants.SOUTHEAST < 0:
		return game_state
	#While the next token to check is the other colour.
	#SouthEast = 9
	while game_state[stringID + constants.SOUTHEAST] == other_colour:

		#Check if move is invalid
		if NofChanges > (8 - (MoveID // 8)) - 1:
			print("Out of bounds!")
			return game_state
		if game_state[stringID + constants.SOUTHEAST] != other_colour and game_state[stringID + constants.SOUTHEAST] != turn_colour:
			print("!= any color")
			return game_state

		#Move to the next piece.
		stringID = stringID + constants.SOUTHEAST

		#Counts one more for the number of pieces to change.
		NofChanges = NofChanges + 1

	#If the next piece is the turn player's colour....
	if game_state[stringID + constants.SOUTHEAST] == turn_colour:

		#The token across is the ID of the last piece to change plus SOUTHEAST.
		MoveXID = stringID + constants.SOUTHEAST

		#While there is still a number of pieces left to change.
		while NofChanges != 0:

			#Create a block of string with the character changed at the beginning.
			PlaceHolder = turn_colour + game_state[stringID + 1:stringID + constants.SOUTHEAST]

			#Create another block of string that was assembled from the blocks of Placeholder.
			slice_new_state = PlaceHolder + slice_new_state

			#Moving backwards through the index of the pieces that need to be changed.
			stringID = stringID - constants.SOUTHEAST

			#One less piece to change.
			NofChanges = NofChanges - 1

			#Testing
			if isTesting:
				print (PlaceHolder, "PlaceHolder")
				print (slice_new_state, "slice_new_state")
				print (stringID, "Index of Change")
				print (NofChanges, "Number of Changes left")

		#If there are no pieces left to change, assemble the new string.
		if NofChanges == 0:
			new_state = game_state[:MoveID + constants.SOUTHEAST] + slice_new_state + game_state[MoveXID:]

			#Testing
			if isTesting:
				print ("01234567890123456789012345678901234567890")
				print (game_state)
				print (new_state)

	#Return the new string.
	return new_state

#Author: Kyle Hinton
#This function will change the string so that the opponents pieces, in a valid move, will be changed on the string.
#This function will change the pieces in the south direction.
#Three parameters: The game state string, the Index of the move on the string, and the current turn colour and an optional one for testing
#returns: Updated string with new pieces.
def CheckSouth(game_state, stringID, turn_colour, isTesting = False):
	NofChanges = 0								#Counts the number of pieces to change.
	PlaceHolder = "" 							#This will be a section of the new string.
	slice_new_state = "" 						#This will be a bigger section of the new game state string.
	new_state = "" 								#This going to be the new game stat.
	MoveID = 0									#This will make a copy of the index of the players move.
	MoveXID = 0 								#This will be a marker for where the players piece is accross from their move.
	other_colour = OtherColour(turn_colour) 	#This Determines the colour of the other player's piece.
	MoveID = stringID 							#This will make a copy of the index of the players move.


	if stringID + constants.SOUTH > len(game_state) or stringID + constants.SOUTH < 0:
		return game_state
	#While the next token to check is the other colour.
	#SOUTH = 8
	while game_state[stringID + constants.SOUTH] == other_colour:

		#Check if move is invalid
		if NofChanges > (8 - (MoveID // 8)) - 1:
			print("Out of bounds")
			return game_state
		if game_state[stringID + constants.SOUTHEAST] != other_colour and game_state[stringID + constants.SOUTHEAST] != turn_colour:
			print("!= any color")
			return game_state

		#Move to the next piece.
		stringID = stringID + constants.SOUTH

		#Counts one more for the number of pieces to change.
		NofChanges = NofChanges + 1

	#If the next piece is the turn player's colour....
	if game_state[stringID + constants.SOUTH] == turn_colour:

		#The token across is the ID of the last piece to change plus SOUTH.
		MoveXID = stringID + constants.SOUTH

		#While there is still a number of pieces left to change.
		while NofChanges != 0:

			#Create a block of string with the character changed at the beginning.
			PlaceHolder = turn_colour + game_state[stringID + 1:stringID + constants.SOUTH]

			#Create another block of string that was assembled from the blocks of Placeholder.
			slice_new_state = PlaceHolder + slice_new_state

			#Moving backwards through the index of the pieces that need to be changed.
			stringID = stringID - constants.SOUTH

			#One less piece to change.
			NofChanges = NofChanges - 1

			#Testing
			if isTesting:
				print (PlaceHolder, "PlaceHolder")
				print (slice_new_state, "slice_new_state")
				print (stringID, "Index of Change")
				print (NofChanges, "Number of Changes left")

		#If there are no pieces left to change, assemble the new string.
		if NofChanges == 0:
			new_state = game_state[:MoveID + constants.SOUTH] + slice_new_state + game_state[MoveXID:]

			#Testing.
			if isTesting:
				print (MoveID + constants.SOUTH, " MoveID")
				print (MoveXID, " MoveXID")
				print ("012345678901234567890123456789012345678901234567890123")
				print (game_state)
				print (new_state)

	#Return the new string with all the pieces changed in the corresponding direction.
	return new_state

#Author: Kyle Hinton
#This function will change the string so that the opponents pieces, in a valid move, will be changed on the string.
#This function will change the pieces in the south-west direction.
#Three parameters: The game state string, the Index of the move on the string, and the current turn colour and an optional one for testing
#returns: Updated string with new pieces.
def CheckSouthWest(game_state, stringID, turn_colour, isTesting = False):
	NofChanges = 0								#Counts the number of pieces to change.
	PlaceHolder = "" 							#This will be a section of the new string.
	slice_new_state = "" 						#This will be a bigger section of the new game state string.
	new_state = "" 								#This going to be the new game stat.
	MoveID = 0									#This will make a copy of the index of the players move.
	MoveXID = 0 								#This will be a marker for where the players piece is accross from their move.
	other_colour = OtherColour(turn_colour) 	#This Determines the colour of the other player's piece.
	MoveID = stringID 							#This will make a copy of the index of the players move.


	if stringID + constants.SOUTHWEST > len(game_state) or stringID + constants.SOUTHWEST < 0:
		return game_state

	while game_state[stringID + constants.SOUTHWEST] == other_colour:
		#Check if move is invalid
		if NofChanges > (8-(MoveID // 8)) - 1:
			print("Out of bounds!")
			return game_state
		if game_state[stringID + constants.SOUTHWEST] != other_colour and game_state[stringID + constants.SOUTHWEST] != turn_colour:
			print("!= any color")
			return game_state

		#Move to the next piece in South West.
		stringID = stringID + constants.SOUTHWEST

		#Counts one more for the number of pieces to change.
		NofChanges = NofChanges + 1

	#If the next piece is the turn player's colour....
	if game_state[stringID + constants.SOUTHWEST] == turn_colour:

		#The token across is the ID of the last piece to change plus SOUTHWEST.
		MoveXID = stringID + constants.SOUTHWEST

		#While there is still a number of pieces left to change.
		while NofChanges != 0:

			#Create a block of string with the character changed at the beginning.
			PlaceHolder = turn_colour + game_state[stringID + 1:stringID + constants.SOUTHWEST]

			#Create another block of string that was assembled from the blocks of Placeholder.
			slice_new_state = PlaceHolder + slice_new_state

			#Moving backwards through the index of the pieces that need to be changed.
			stringID = stringID - constants.SOUTHWEST

			#One less piece to change.
			NofChanges = NofChanges - 1

			#Testing
			if isTesting:
				print (PlaceHolder, "PlaceHolder")
				print (slice_new_state, "slice_new_state")
				print (stringID, "Index of Change")
				print (NofChanges, "Number of Changes left")

		#If there are no pieces left to change, assemble the new string.
		if NofChanges == 0:
			new_state = game_state[:MoveID + constants.SOUTHWEST] + slice_new_state + game_state[MoveXID:]

			#testing
			if isTesting:
				print ("01234567890123456789012345678901234567890")
				print (game_state)
				print (new_state)

	#Return the new string with all the pieces changed in the corresponding direction.
	return new_state

#Author: Kyle Hinton
#This function will change the string so that the opponents pieces, in a valid move, will be changed on the string.
#This function will change the pieces in the west direction.
#Three parameters: The game state string, the Index of the move on the string, and the current turn colour and an optional one for testing
#Returns: Updated string with new pieces.
def CheckWest(game_state, stringID, turn_colour, isTesting = False):
	NofChanges = 0								#Counts the number of pieces to change.
	PlaceHolder = "" 							#This will be a section of the new string.
	slice_new_state = "" 						#This will be a bigger section of the new game state string.
	new_state = "" 								#This going to be the new game stat.
	MoveID = 0									#This will make a copy of the index of the players move.
	MoveXID = 0 								#This will be a marker for where the players piece is accross from their move.
	other_colour = OtherColour(turn_colour) 	#This Determines the colour of the other player's piece.
	MoveID = stringID 							#This will make a copy of the index of the players move.

	if stringID + constants.WEST > len(game_state) or stringID + constants.WEST < 0:
		return game_state

	#While the next token to check is the other colour.
	#WEST = -1
	while game_state[stringID + constants.WEST] == other_colour:
		#Possible statements for catching invalid moves.
		if NofChanges > (MoveID % 8) - 1:
			print ("out of bounds")
			return game_state
		if game_state[stringID + constants.WEST] != other_colour and game_state[stringID + constants.WEST] != turn_colour:
			print ("!= turn colour or other")
			return game_state

		#Testing
		if isTesting:
			print(NofChanges, "NofChanges Number of other colours")
			print(stringID + (constants.WEST), "index of other_colour")

		#Move on to the Next Token
		stringID = stringID + constants.WEST

		#Add one to the number of tokens that need to be changed.
		NofChanges = NofChanges + 1

	return game_state[:(MoveID - NofChanges)] + (turn_colour * NofChanges) + game_state[MoveID:]

#Author: Kyle Hinton
#This function will change the string so that the opponents pieces, in a valid move, will be changed on the string.
#This function will change the pieces in the north-west direction.
#Three parameters: The game state string, the Index of the move on the string, and the current turn colour and an optional parameter for testing
#returns: Updated string with new pieces.
def CheckNorthWest(game_state, stringID, turn_colour, isTesting = False):
	NofChanges = 0 						#Counts the number of pieces to change.
	PlaceHolder = "" 					#This will be sections of string.
	slice_new_state = "" 				#This will make a bigger section of the game state string from PlaceHolders.
	new_state = "" 						#This is going to be the new string for the games state.
	MoveXID = 0 						#This is going to be where the token across from
	other_colour = OtherColour(turn_colour) #Determines the other colour.
	MoveID = stringID 					#Makes a copy of the index of the current player's move.

	if stringID + constants.NORTHWEST > len(game_state) or stringID + constants.NORTHWEST < 0:
		return game_state

	#While the next token to check is the other colour.
	#NORTHWEST = -9
	while game_state[stringID + constants.NORTHWEST] == other_colour:

		#Catch invalid moves
		if NofChanges > (MoveID // 8) - 1:
			print("Out of bounds!")
			return game_state

		if game_state[stringID + constants.NORTHWEST] != other_colour and game_state[stringID + constants.NORTHWEST] != turn_colour:
			print("!= any colour")
			return game_state

		#Move to the next piece.
		stringID = stringID + constants.NORTHWEST

		#Counts one more for the number of pieces to change.
		NofChanges = NofChanges + 1

	#If the next piece is the turn player's colour....
	if game_state[stringID + constants.NORTHWEST] == turn_colour:

		#The token across is the ID of the last piece to change plus NORTHWEST
		MoveXID = stringID + constants.NORTHWEST

		#While there is still a number of pieces left to change.
		while NofChanges != 0:

			#Create a block of string with the character changed at the beginning
			PlaceHolder = turn_colour + game_state[stringID + 1:stringID - constants.NORTHWEST]

			#Create another block of string that was assembled from the blocks of Placeholder.
			slice_new_state = slice_new_state + PlaceHolder

			#Moveing backwards through the index of the pieces that need to be changed.
			stringID = stringID - constants.NORTHWEST

			#One less piece to change.
			NofChanges = NofChanges - 1

			#Testing
			if isTesting:
				print (PlaceHolder, "PlaceHolder")
				print (slice_new_state, "slice_new_state")
				print (stringID, "Index of Change")
				print (NofChanges, "Number of Changes left")

		#If there are no pieces left to change, assemble the new string.
		if NofChanges == 0:
			new_state = game_state[:MoveXID - constants.NORTHWEST] + slice_new_state + game_state[MoveID:]

			#Testing
			if isTesting:
				print ("01234567890123456789012345678901234567890")
				print (game_state)
				print (new_state)

	#Return the new string with all the pieces changed in the corresponding direction.
	return new_state

#This function will determine the colour of the other player's token, based on the player's turn colour.
#This function takes the current turn colour as the parameter.
#returns: the character for the other colour.
def OtherColour(turn_colour):
	if turn_colour == "W":
		return "B"
	elif turn_colour == "B":
		return "W"
	else:
		return turn_colour

#DOES NOT WORK YET.
#This function will change the string so that the opponents pieces, in a valid move, will be changed on the string.
#This function will change the pieces in all the directions.
#Three parameters: The game state string, the Index of the move on the string, and the current turn colour and an optional one for testing
#returns: Updated string with new pieces.
def ChangePieces(game_state, stringID, turn_colour, isTesting = False):
	#Check every direction
	game_state = CheckNorth(game_state, stringID, turn_colour, isTesting)
	game_state = CheckNorthEast(game_state, stringID, turn_colour, isTesting)
	game_state = CheckEast(game_state, stringID, turn_colour, isTesting)
	game_state = CheckSouthEast(game_state, stringID, turn_colour, isTesting)
	game_state = CheckSouth(game_state, stringID, turn_colour, isTesting)
	game_state = CheckSouthWest(game_state, stringID, turn_colour, isTesting)
	game_state = CheckWest(game_state, stringID, turn_colour, isTesting)
	game_state = CheckNorthWest(game_state, stringID, turn_colour, isTesting)

	#Return updated string
	return game_state[:stringID] + turn_colour + game_state[stringID + 1:]

#Tests a function
#Params: function, The function to test
#		 param_one, The first parameter of the function to test
#		 param_two, The second parameter of the function to test
#		 param_three, The third parameter of the function to test
# 		 param_four, The fourth parameter of the function to test, defaults to False
#Returns: None
#Notes: Refer to the function for what it's parameters are
def testFunction(function, param_one, param_two, param_three, param_four = False):
	result = function(param_one, param_two, param_three, param_four)
	formatted_start = converter.asBoardRepresentation(param_one)
	formatted_end = converter.asBoardRepresentation(result)
	print("At:", stringInterpret.pieceToString(param_two))
	print("Input".center(8))
	print(formatted_start)
	print("Output".center(8))
	print(formatted_end)

#A function to test the check functions
def testProgram():
	input("Beginning testing, press Enter to continue")

	print("NORTH NORTH NORTH".center(27))
	print("___________________________")
	print("TEST 1 TEST 1 TEST 1 TEST 1\n")
	testFunction(CheckNorth, "WWWWWWWWBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBW", 63, "W")

	input()

	print("NORTHEAST NORTHEAST NORTHEAST".center(27))
	print("___________________________")
	print("TEST 1 TEST 1 TEST 1 TEST 1\n")
	testFunction(CheckNorthEast, "WWWWWWWWBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBWBBBBBBB", 56, "W")

	input()

	print("EAST EAST EAST".center(27))
	print("___________________________")
	print("TEST 1 TEST 1 TEST 1 TEST 1\n")
	testFunction(CheckEast, "WBBBBBBWBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB", 0, "W")

	input()

	print("SOUTHEAST SOUTHEAST SOUTHEAST".center(27))
	print("___________________________")
	print("TEST 1 TEST 1 TEST 1 TEST 1\n")
	testFunction(CheckSouthEast, "WBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBW", 0, "W")

	input()

	print("SOUTH SOUTH SOUTH".center(27))
	print("___________________________")
	print("TEST 1 TEST 1 TEST 1 TEST 1\n")
	testFunction(CheckSouth, "WWWWWWWWBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBWWWWWWWW", 5, "W")

	input()

	print("SOUTHWEST SOUTHWEST SOUTHWEST".center(27))
	print("___________________________")
	print("TEST 1 TEST 1 TEST 1 TEST 1\n")
	testFunction(CheckSouthWest, "BBBBBBBWBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBWBBBBBBB", 7, "W")

	input()

	print("WEST WEST WEST".center(27))
	print("___________________________")
	print("TEST 1 TEST 1 TEST 1 TEST 1\n")
	testFunction(CheckWest, "WBBBBBBWBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB", 7, "W")

	input()

	print("NORTHWEST NORTHWEST NORTHWEST".center(27))
	print("___________________________")
	print("TEST 1 TEST 1 TEST 1 TEST 1\n")
	testFunction(CheckNorthWest, "WBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBW", 63, "W")



	input()
	print("CHECK ALL CHECK ALL CHECK ALL".center(27))
	print("___________________________")
	print("TEST TEST TEST TEST\n".center(27))
	testFunction(ChangePieces, ("W" * 8) + ("B" * 48) + ("W" * 8), 33, "W")
	testFunction(ChangePieces, "WBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBW", 63, "W")
	testFunction(ChangePieces, "WWWWWWWWBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBWWWWWWWW", 5, "W")

if __name__ == "__main__":
	testProgram()
	#testFunction(ChangePieces, ("W" * 8) + ("B" * 48) + ("W" * 8), 33, "W")
