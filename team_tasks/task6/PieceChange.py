import Constants

#############################################################################
#This function will change the string so that the opponents pieces, in a valid move, will be changed on the string.
#This function will change the pieces in the west direction.
#Three parameters: The game state string, the Index of the move on the string, and the current turn colour.
#returns: Updated string with new pieces.
def CheckWest(game_state, stringID, turn_colour):


	NofChanges = 0 #Counts the number of pieces to change.
	other_colour = OtherColour(turn_colour) #Determines the other colour.
	new_state = "" #Calls the variable for the new_string.
	MoveID = stringID #Makes a copy of the index of the move.

	#While the next token to check is the other colour.
	#WEST = -1
	while game_state[stringID + (Constants.WEST)] == other_colour:

		#Possible statements for catching valid moves.
		"""
		if NofChanges > (MoveID % 8) - 1:
			print ("out of bounds")
			return game_state

		if game_state[stringID + Constants.WEST] != other_colour or game_state[stringID + Constants.WEST] != turn_colour:
			print ("!= turn colour or other")
			return game_state
		"""

		#Testing
		print (NofChanges, "NofChanges Number of other colours")
		print (stringID + (Constants.WEST), "index of other_colour")

		#Move on to the Next Token
		stringID = stringID + (Constants.WEST)

		#If the next token to check is N, return the original game_state
		if game_state[stringID] == "N":
			print("None in that direction.")
			return game_state

		#Add one to the number of tokens that need to be changed.
		NofChanges = NofChanges + 1

		#If the next token that is checked is the current turn's player, create the new game state string.
		if game_state[stringID + (Constants.WEST)] == turn_colour:
			new_state = game_state[:stringID] + (turn_colour * NofChanges) + game_state[stringID + (Constants.WEST) + NofChanges + 1:]
			print (game_state)
			print(new_state)
			print (NofChanges, "How many times we have to print the turn_colour's letter.")

	#Returns the string that is the new game state.
	return new_state


#############################################################################
#This function will change the string so that the opponents pieces, in a valid move, will be changed on the string.
#This function will change the pieces in the east direction.
#Three parameters: The game state string, the Index of the move on the string, and the current turn colour.
#returns: Updated string with new pieces.
def CheckEast(game_state, stringID, turn_colour):

	NofChanges = 0 #Counts the number of pieces to change.
	other_colour = OtherColour(turn_colour) #Determines the other colour.
	new_state = "" #Calls the variable for the new_string.
	MoveID = stringID #Makes a copy of the index of the move.


	#While the next token to check is the other colour.
	#EAST = 1
	while game_state[stringID + (Constants.EAST)] == other_colour:

		if NofChanges > (8 - (MoveID % 8)) - 1:
			print("Out of bounds.")
			return game_state

		if game_state[stringID + Constants.EAST] != other_colour or game_state[stringID + Constants.EAST] != turn_colour:
			print("!= any colour")
			return game_state

		print (NofChanges, "NofChanges Number of other colours")
		print (stringID + (Constants.EAST), "index of other_colour")
		stringID = stringID + (Constants.EAST)

		if game_state[stringID] == "N":
			print("None in that direction.")
			return game_state

		NofChanges = NofChanges + 1



		if game_state[stringID + (Constants.EAST)] == turn_colour:
			new_state = game_state[:stringID - NofChanges + 1] + (turn_colour * NofChanges) + game_state[stringID + 1:]
			print (game_state)
			print(new_state)
			print (NofChanges, "How many times we have to print the turn_colour's letter.")

	return new_state

#############################################################################
#This function will change the string so that the opponents pieces, in a valid move, will be changed on the string.
#This function will change the pieces in the north-west direction.
#Three parameters: The game state string, the Index of the move on the string, and the current turn colour.
#returns: Updated string with new pieces.
def CheckNorthWest(game_state, stringID, turn_colour):


	NofChanges = 0 #Counts the number of pieces to change.
	PlaceHolder = "" #This will be sections of string.
	slice_new_state = "" #This will make a bigger section of the game state string from PlaceHolders.
	new_state = "" #This is going to be the new string for the games state.
	MoveXID = 0 #This is going to be where the token across from
	other_colour = OtherColour(turn_colour) #Determines the other colour.
	MoveID = stringID #Makes a copy of the index of the current player's move.

	#While the next token to check is the other colour.
	#NORTHWEST = -9
	while game_state[stringID + Constants.NORTHWEST] == other_colour:
		"""
		if NofChanges > (MoveID // 8) - 1:
			return game_state

		if game_state[stringID + Constants.NORTHWEST] != other_colour or game_state[stringID + Constants.NORTHWEST] != turn_colour:
			return game_state
		"""

		#Move to the next piece.
		stringID = stringID + Constants.NORTHWEST

		#Counts one more for the number of pieces to change.
		NofChanges = NofChanges + 1


	#If the next piece is the turn player's colour....
	if game_state[stringID + Constants.NORTHWEST] == turn_colour:

		#The token across is the ID of the last piece to change plus NORTHWEST
		MoveXID = stringID + Constants.NORTHWEST

		#While there is still a number of pieces left to change.
		while NofChanges != 0:

			#Create a block of string with the character changed at the beginning
			PlaceHolder = turn_colour + game_state[stringID + 1:stringID - Constants.NORTHWEST]

			#Create another block of string that was assembled from the blocks of Placeholder.
			slice_new_state = slice_new_state + PlaceHolder

			#Moveing backwards through the index of the pieces that need to be changed.
			stringID = stringID - Constants.NORTHWEST

			#One less piece to change.
			NofChanges = NofChanges - 1

			#Testing
			print (PlaceHolder, "PlaceHolder")
			print (slice_new_state, "slice_new_state")
			print (stringID, "Index of Change")
			print (NofChanges, "Number of Changes left")

			#If there are no pieces left to change, assemble the new string.
		if NofChanges == 0:
			new_state = game_state[:MoveXID - Constants.NORTHWEST] + slice_new_state + game_state[MoveID:]
			print ("01234567890123456789012345678901234567890")
			print (game_state)
			print (new_state)

	return new_state


#############################################################################
#This function will change the string so that the opponents pieces, in a valid move, will be changed on the string.
#This function will change the pieces in the north direction.
#Three parameters: The game state string, the Index of the move on the string, and the current turn colour.
#returns: Updated string with new pieces.
def CheckNorth(game_state, stringID, turn_colour):


	NofChanges = 0

	PlaceHolder = ""
	slice_new_state = ""
	new_state = ""
	MoveID = 0
	MoveXID = 0
	other_colour = OtherColour(turn_colour)
	MoveID = stringID

	while game_state[stringID + Constants.NORTH] == other_colour:

		"""
		if NofChanges > (MoveID // 8) - 1:
			return game_state


		if game_state[stringID + Constants.NORTH] != other_colour or game_state[stringID + Constants.NORTH] != turn_colour:
			return game_state
		"""

		stringID = stringID + Constants.NORTH
		NofChanges = NofChanges + 1



	if game_state[stringID + Constants.NORTH] == turn_colour:
		MoveXID = stringID + Constants.NORTH

		while NofChanges != 0:
			PlaceHolder = turn_colour + game_state[stringID + 1:stringID - Constants.NORTH]
			slice_new_state = slice_new_state + PlaceHolder
			stringID = stringID - Constants.NORTH
			NofChanges = NofChanges - 1
			print (PlaceHolder, "PlaceHolder")
			print (slice_new_state, "slice_new_state")
			print (stringID, "Index of Change")
			print (NofChanges, "Number of Changes left")

		if NofChanges == 0:
			new_state = game_state[:MoveXID - Constants.NORTH] + slice_new_state + game_state[MoveID:]
			print ("01234567890123456789012345678901234567890")
			print (game_state)
			print (new_state)

	return new_state


#############################################################################
#This function will change the string so that the opponents pieces, in a valid move, will be changed on the string.
#This function will change the pieces in the north east direction.
#Three parameters: The game state string, the Index of the move on the string, and the current turn colour.
#returns: Updated string with new pieces.
def CheckNorthEast(game_state, stringID, turn_colour):

	turn_colour = "W"
	other_colour = "B"
	NofChanges = 0

	PlaceHolder = ""
	slice_new_state = ""
	new_state = ""
	MoveID = 0
	MoveXID = 0
	other_colour = OtherColour(turn_colour)
	MoveID = stringID



	while game_state[stringID + Constants.NORTHEAST] == other_colour:

		"""
		if NofChanges > (MoveID // 8) - 1:
			return game_state

		if game_state[stringID + Constants.NORTHEAST] != other_colour or game_state[stringID + Constants.NORTHEAST] != turn_colour:
			return game_state
		"""

		stringID = stringID + Constants.NORTHEAST
		NofChanges = NofChanges + 1



	if game_state[stringID + Constants.NORTHEAST] == turn_colour:
		MoveXID = stringID + Constants.NORTHEAST				#!!!!!!to slice must be [stringID+Constants.NORTHEAST+9]

		while NofChanges != 0:
			PlaceHolder = turn_colour + game_state[stringID + 1:stringID - Constants.NORTHEAST]
			slice_new_state = slice_new_state + PlaceHolder
			stringID = stringID - Constants.NORTHEAST
			NofChanges = NofChanges - 1
			print (PlaceHolder, "PlaceHolder")
			print (slice_new_state, "slice_new_state")
			print (stringID, "Index of Change")
			print (NofChanges, "Number of Changes left")

		if NofChanges == 0:
			new_state = game_state[:MoveXID - Constants.NORTHEAST] + slice_new_state + game_state[MoveID:]

			print ("01234567890123456789012345678901234567890")
			print (game_state)
			print (new_state)

	return new_state



#############################################################################
#This function will change the string so that the opponents pieces, in a valid move, will be changed on the string.
#This function will change the pieces in the south-west direction.
#Three parameters: The game state string, the Index of the move on the string, and the current turn colour.
#returns: Updated string with new pieces.
def CheckSouthWest(game_state, stringID, turn_colour):


	NofChanges = 0
	PlaceHolder = ""
	slice_new_state = ""
	new_state = ""
	MoveID = 0
	MoveXID = 0
	other_colour = OtherColour(turn_colour)
	MoveID = stringID


	while game_state[stringID + Constants.SOUTHWEST] == other_colour:

		"""
		if NofChanges > (8-(MoveID // 8)) - 1:
			return game_state

		if game_state[stringID + Constants.SOUTHWEST] != other_colour or game_state[stringID + Constants.SOUTHWEST] != turn_colour:
			return game_state
		"""

		stringID = stringID + Constants.SOUTHWEST
		NofChanges = NofChanges + 1

	if game_state[stringID + Constants.SOUTHWEST] == turn_colour:
		MoveXID = stringID + Constants.SOUTHWEST				#!!!!!!to slice must be [stringID+Constants.SOUTHWEST+9]


		while NofChanges != 0:
			PlaceHolder = turn_colour + game_state[stringID + 1:stringID + Constants.SOUTHWEST]
			slice_new_state = PlaceHolder + slice_new_state
			stringID = stringID - Constants.SOUTHWEST
			NofChanges = NofChanges - 1
			print (PlaceHolder, "PlaceHolder")
			print (slice_new_state, "slice_new_state")
			print (stringID, "Index of Change")
			print (NofChanges, "Number of Changes left")


		if NofChanges == 0:
			new_state = game_state[:MoveID + Constants.SOUTHWEST] + slice_new_state + game_state[MoveXID:]

			print ("01234567890123456789012345678901234567890")
			print (game_state)
			print (new_state)
	return new_state


#############################################################################
#This function will change the string so that the opponents pieces, in a valid move, will be changed on the string.
#This function will change the pieces in the south-east direction.
#Three parameters: The game state string, the Index of the move on the string, and the current turn colour.
#returns: Updated string with new pieces.
def CheckSouthEast(game_state, stringID, turn_colour):


	NofChanges = 0

	PlaceHolder = ""
	slice_new_state = ""
	new_state = ""
	MoveID = 0
	MoveXID = 0
	other_colour = OtherColour(turn_colour)
	MoveID = stringID

	if game_state[stringID + Constants.SOUTHEAST] != other_colour or game_state[stringID + Constants.SOUTHEAST] != turn_colour:
		return game_state

	while game_state[stringID + Constants.SOUTHEAST] == other_colour:

		""""
		if NofChanges > (8 - (MoveID // 8)) - 1:
			return game_state

		if game_state[stringID + Constants.SOUTHEAST] != other_colour or game_state[stringID + Constants.SOUTHEAST] != turn_colour:
			return game_state
		"""

		stringID = stringID + Constants.SOUTHEAST
		NofChanges = NofChanges + 1



	if game_state[stringID + Constants.SOUTHEAST] == turn_colour:
		MoveXID = stringID + Constants.SOUTHEAST				#!!!!!!to slice must be [stringID+Constants.SOUTHEAST+9]
		while NofChanges != 0:
			PlaceHolder = turn_colour + game_state[stringID + 1:stringID + Constants.SOUTHEAST]
			slice_new_state = PlaceHolder + slice_new_state
			stringID = stringID - Constants.SOUTHEAST
			NofChanges = NofChanges - 1
			print (PlaceHolder, "PlaceHolder")
			print (slice_new_state, "slice_new_state")
			print (stringID, "Index of Change")
			print (NofChanges, "Number of Changes left")
		if NofChanges == 0:
			new_state = game_state[:MoveID + Constants.SOUTHEAST] + slice_new_state + game_state[MoveXID:]

			print ("01234567890123456789012345678901234567890")
			print (game_state)
			print (new_state)
	return new_state



#############################################################################
#This function will change the string so that the opponents pieces, in a valid move, will be changed on the string.
#This function will change the pieces in the south direction.
#Three parameters: The game state string, the Index of the move on the string, and the current turn colour.
#returns: Updated string with new pieces.
def CheckSouth(game_state, stringID, turn_colour):


	NofChanges = 0
	PlaceHolder = ""
	slice_new_state = ""
	new_state = ""
	MoveID = 0
	MoveXID = 0
	other_colour = OtherColour(turn_colour)

	MoveID = stringID
	while game_state[stringID + Constants.SOUTH] == other_colour:

		"""

		if NofChanges > (8 - (MoveID // 8)) - 1:
			return game_state

		if game_state[stringID + Constants.SOUTHEAST] != other_colour or game_state[stringID + Constants.SOUTHEAST] != turn_colour:
			return game_state
		"""

		stringID = stringID + Constants.SOUTH
		NofChanges = NofChanges + 1



	if game_state[stringID + Constants.SOUTH] == turn_colour:
		MoveXID = stringID + Constants.SOUTH				#!!!!!!to slice must be [stringID+Constants.SOUTH+9]

		while NofChanges != 0:
			PlaceHolder = turn_colour + game_state[stringID + 1:stringID + Constants.SOUTH]
			slice_new_state = PlaceHolder + slice_new_state
			stringID = stringID - Constants.SOUTH
			NofChanges = NofChanges - 1
			print (PlaceHolder, "PlaceHolder")
			print (slice_new_state, "slice_new_state")
			print (stringID, "Index of Change")
			print (NofChanges, "Number of Changes left")

		if NofChanges == 0:
			new_state = game_state[:MoveID + Constants.SOUTH] + slice_new_state + game_state[MoveXID:]
			print (MoveID + Constants.SOUTH, " MoveID")
			print (MoveXID, " MoveXID")
			print ("012345678901234567890123456789012345678901234567890123")
			print (game_state)
			print (new_state)

	return new_state

#############################################################################
#This function will determine the colour of the other player's token, based on the player's turn colour.
#This function takes the current turn colour as the parameter.
#returns: the character for the other colour.
def OtherColour(turn_colour):
	if turn_colour == "W":
		other_colour = "B"
	if turn_colour == "B":
		other_colour = "W"
	return other_colour

#############################################################################
#DOES NOT WORK YET.
#This function will change the string so that the opponents pieces, in a valid move, will be changed on the string.
#This function will change the pieces in all the directions.
#Three parameters: The game state string, the Index of the move on the string, and the current turn colour.
#returns: Updated string with new pieces.
def ChangePieces(game_state, stringID, turn_colour):

	game_state = CheckEast(game_state, stringID, turn_colour)
	print (game_state)
	print (stringID)
	game_state = CheckSouthEast(game_state, stringID, turn_colour)
	game_state = CheckSouth(game_state, stringID, turn_colour)
	game_state = CheckSouthWest(game_state, stringID, turn_colour)
	game_state = CheckWest(game_state, stringID, turn_colour)
	game_state = CheckNorthWest(game_state, stringID, turn_colour)
	game_state = CheckNorth(game_state, stringID, turn_colour)
	game_state = CheckNorthEast(game_state, stringID, turn_colour)

	return game_state

#############################################################################
def testProgram():
	input("Beginning testing, press Enter to continue")

	print("WEST WEST WEST".center(50))
	print("___________________________")
	print("TEST 1 TEST 1 TEST 1 TEST 1\n")
	CheckWest("WWWWWWWWWBBBBBBBBBBBBWBBNWBBBBBWNNBWWWNNNBNNNBNNBNNNNNBNNNNNNNNW", 31, "W")
	print("___________________________")
	print("TEST 2 TEST 2 TEST 2 TEST 2\n")
	CheckWest("WWWWWWWWWBBBBBBBBBBBBWBBNBBBBBBWNWBWWWNNNBNNNBNNBNNNNNBNNNNNNNNW", 35, "W")

	input()

	print("NORTHWEST NORTHWEST NORTHWEST".center(50))
	print("___________________________")
	print("TEST 1 TEST 1 TEST 1 TEST 1\n")
	CheckNorthWest("WWWWWWWWWBBBBBBBBBBBBWBBNBBBBBBWNNBWWWNNNBNNNBNNBNNNNNBNNNNNNNNW", 35, "W")
	print("___________________________")
	print("TEST 2 TEST 2 TEST 2 TEST 2\n")
	CheckNorthWest("WWWWWWWWWBBBBBBBBBBBBWBBNBBBBBBWNNBWWWNNNBNNNBNNBNNNNNBNNNNNNNNW", 36, "W")
	print("___________________________")
	print("TEST 3 TEST 3 TEST 3 TEST 3\n")
	CheckNorthWest("WWWWWWWWWBBBBBBBBBBBBWBBNBBBBBBWNNBWWWNNNBNNNBNNBNNNNNBNNNNNNNNW", 37, "W")

	input()

	print("NORTH NORTH NORTH".center(50))
	print("___________________________")
	print("TEST 1 TEST 1 TEST 1 TEST 1\n")
	CheckNorth("WWWWWWWWWBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBWBBBBBBBBBBBB", 51, "W")

	input()

	print("NORTHEAST NORTHEAST NORTHEAST".center(50))
	print("___________________________")
	print("TEST 1 TEST 1 TEST 1 TEST 1\n")
	CheckNorthEast("WWWWWWWWWBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBWBBBBBBBBBBBBBBBBBBBBBNN", 40, "W")

	input()

	print("SOUTHWEST SOUTHWEST SOUTHWEST".center(50))
	print("___________________________")
	print("TEST 1 TEST 1 TEST 1 TEST 1\n")
	CheckSouthWest("WWWWWBBBBBBBBBBBBBBBBBBBBBBBBBBWWBBBBBBWBBBBBBBBBBBBBBBBBBBBBBBB", 4, "W")
	print("___________________________")
	print("TEST 2 TEST 2 TEST 2 TEST 2\n")
	CheckSouthWest("WWWWBBBBBBBBBBBBBBBBBBBBBBBBBBBWWBBBBBBWBBBBBBBBBBBBBBBBBBBBBBBB", 3, "W")

	input()

	print("SOUTH SOUTH SOUTH".center(50))
	print("___________________________")
	print("TEST 1 TEST 1 TEST 1 TEST 1\n")
	CheckSouth("WWWWWWWWBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBWWWWWWWW", 3, "W")
	print("___________________________")
	print("TEST 2 TEST 2 TEST 2 TEST 2\n")
	Hilda = CheckSouth("WWWWWWWWBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBWWWWWWWW", 5, "W")
	print("Hilda: %s" % Hilda)

if __name__ == "__main__":
	testProgram()

#Change = ChangePieces("WWWWWWWWWBBBBBBBBBBBBWBBNBBBBBBWNNBWWWNNNBNNNBNNBNNNNNBNNNNNNNNW", 3, "W")
#print(Change)
