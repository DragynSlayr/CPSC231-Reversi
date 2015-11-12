import Constants

#############################################################################
def CheckWest(game_state, stringID, turn_colour):


	NofChanges = 0
	other_colour = OtherColour(turn_colour)
	new_state = ""
	MoveID = stringID

	while game_state[stringID + (Constants.WEST)] == other_colour:
		"""
		if NofChanges > (MoveID % 8) - 2:
			print ("out of bounds")
			return game_state

		if game_state[stringID + Constants.WEST] != other_colour or game_state[stringID + Constants.WEST] != turn_colour:
			print ("!= turn colour or other")
			return game_state
		"""
		print (NofChanges, "NofChanges Number of other colours")
		print (stringID + (Constants.WEST), "index of other_colour")
		stringID = stringID + (Constants.WEST)

		if game_state[stringID] == "N":
			print("None in that direction.")
			return game_state
		NofChanges = NofChanges + 1



		if game_state[stringID + (Constants.WEST)] == turn_colour:
			new_state = game_state[:stringID] + (turn_colour * NofChanges) + game_state[stringID + (Constants.WEST) + NofChanges + 1:]
			print (game_state)
			print(new_state)
			print (NofChanges, "How many times we have to print the turn_colour's letter.")

	return new_state


#############################################################################
def CheckEast(game_state, stringID, turn_colour):
#	turn_colour = "W"
#	other_colour = "B"
	NofChanges = 0
	other_colour = OtherColour(turn_colour)
	new_state = ""
	MoveID = stringID


	while game_state[stringID + (Constants.EAST)] == other_colour:
		"""
		if NofChanges > (8 - (MoveID % 8)) - 2:
			print("Out of bounds.")
			return game_state

		if game_state[stringID + Constants.EAST] != other_colour or game_state[stringID + Constants.EAST] != turn_colour:
			print("!= any colour")
			return game_state
		"""
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
def CheckNorthWest(game_state, stringID, turn_colour):


	NofChanges = 0
	PlaceHolder = ""
	slice_new_state = ""
	new_state = game_state
	MoveXID = 0
	other_colour = OtherColour(turn_colour)
	MoveID = stringID

	while game_state[stringID + Constants.NORTHWEST] == other_colour:

		if NofChanges > (MoveID // 8) - 2:
			return game_state

		if game_state[stringID + Constants.NORTHWEST] != other_colour or game_state[stringID + Constants.NORTHWEST] != turn_colour:
			return game_state

		stringID = stringID + Constants.NORTHWEST
		NofChanges = NofChanges + 1



	if game_state[stringID + Constants.NORTHWEST] == turn_colour:
		MoveXID = stringID + Constants.NORTHWEST

		while NofChanges != 0:
			PlaceHolder = turn_colour + game_state[stringID + 1:stringID - Constants.NORTHWEST]
			slice_new_state = slice_new_state + PlaceHolder
			stringID = stringID - Constants.NORTHWEST
			NofChanges = NofChanges - 1
			print (PlaceHolder, "PlaceHolder")
			print (slice_new_state, "slice_new_state")
			print (stringID, "Index of Change")
			print (NofChanges, "Number of Changes left")

		if NofChanges == 0:
			new_state = game_state[:MoveXID - Constants.NORTHWEST] + slice_new_state + game_state[MoveID:]
			print ("01234567890123456789012345678901234567890")
			print (game_state)
			print (new_state)

	return new_state


#############################################################################
def CheckNorth(game_state, stringID, turn_colour):

#	turn_colour = "W"
#	other_colour = "B"
	NofChanges = 0

	PlaceHolder = ""
	slice_new_state = ""
	new_state = ""
	MoveID = 0
	MoveXID = 0
	other_colour = OtherColour(turn_colour)
	MoveID = stringID

	while game_state[stringID + Constants.NORTH] == other_colour:

#		if NofChanges > (MoveID // 8) - 2:
#			return game_state


#		if game_state[stringID + Constants.NORTH] != other_colour or game_state[stringID + Constants.NORTH] != turn_colour:
#			return game_state

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
def CheckNorthEast(game_state, stringID, turn_colour):

#	turn_colour = "W"
#	other_colour = "B"
	NofChanges = 0

	PlaceHolder = ""
	slice_new_state = ""
	new_state = ""
	MoveID = 0
	MoveXID = 0
	other_colour = OtherColour(turn_colour)
	MoveID = stringID



	while game_state[stringID + Constants.NORTHEAST] == other_colour:

		if NofChanges > (MoveID // 8) - 2:
			return game_state

		if game_state[stringID + Constants.NORTHEAST] != other_colour or game_state[stringID + Constants.NORTHEAST] != turn_colour:
			return game_state

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
def CheckSouthWest(game_state, stringID, turn_colour):

#	turn_colour = "W"
#	other_colour = "B"
	NofChanges = 0
	PlaceHolder = ""
	slice_new_state = ""
	new_state = ""
	MoveID = 0
	MoveXID = 0
	other_colour = OtherColour(turn_colour)
	MoveID = stringID


	while game_state[stringID + Constants.SOUTHWEST] == other_colour:

		if NofChanges > (8-(MoveID // 8)) - 2:
			return game_state

		if game_state[stringID + Constants.SOUTHWEST] != other_colour or game_state[stringID + Constants.SOUTHWEST] != turn_colour:
			return game_state

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
def CheckSouthEast(game_state, stringID, turn_colour):

#	turn_colour = "W"
#	other_colour = "B"
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

		if NofChanges > (8 - (MoveID // 8)) - 2:
			return game_state

		if game_state[stringID + Constants.SOUTHEAST] != other_colour or game_state[stringID + Constants.SOUTHEAST] != turn_colour:
			return game_state

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
def CheckSouth(game_state, stringID, turn_colour):

#	turn_colour = "W"
#	other_colour = "B"
	NofChanges = 0
	PlaceHolder = ""
	slice_new_state = ""
	new_state = ""
	MoveID = 0
	MoveXID = 0
	other_colour = OtherColour(turn_colour)

	MoveID = stringID
	while game_state[stringID + Constants.SOUTH] == other_colour:

#		if NofChanges > (8 - (MoveID // 8)) - 2:
#			return game_state

#		if game_state[stringID + Constants.SOUTHEAST] != other_colour or game_state[stringID + Constants.SOUTHEAST] != turn_colour:
#			return game_state

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
def OtherColour(turn_colour):
	if turn_colour == "W":
		other_colour = "B"
	if turn_colour == "B":
		other_colour = "W"
	return other_colour

#############################################################################
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
