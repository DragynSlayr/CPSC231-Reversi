import Constants

#############################################################################
def CheckWest(game_state, stringID):

	TurnColour = "W"
	OtherColour = "B"
	n = 1

	while game_state[stringID + (Constants.WEST)] == OtherColour:
		print (n, "n Number of other colours")
		print (stringID + (Constants.WEST), "index of OtherColour")
		stringID = stringID + (Constants.WEST)
		if game_state[stringID] == "N":
			print("None in that direction.")
		n = n + 1

		if game_state[stringID + (Constants.WEST)] == TurnColour:
			new_state = game_state[:stringID] + (TurnColour * n) + game_state[stringID + (Constants.WEST) + n + 1:]
			print (game_state)
			print(new_state)
			print (n, "How many times we have to print the TurnColour's letter.")
	return new_state


#############################################################################
def CheckEast(game_state, stringID):
	TurnColour = "W"
	OtherColour = "B"
	n = 1

	while game_state[stringID + (Constants.EAST)] == OtherColour:
		print (n, "n Number of other colours")
		print (stringID + (Constants.EAST), "index of OtherColour")
		stringID = stringID + (Constants.EAST)
		if game_state[stringID] == "N":
			print("None in that direction.")
		n = n + 1

		if game_state[stringID + (Constants.EAST)] == TurnColour:
			new_state = game_state[:stringID - n + 1] + (TurnColour * n) + game_state[stringID + 1:]
			print (game_state)
			print(new_state)
			print (n, "How many times we have to print the TurnColour's letter.")
	return new_state

#############################################################################
def CheckNorthWest(game_state, stringID):

	TurnColour = "W"
	OtherColour = "B"
	NofChanges = 0

	PlaceHolder = ""
	slice_new_state = ""
	new_state = ""
	MoveID = 0
	MoveXID = 0


	MoveID = stringID
	while game_state[stringID + Constants.NORTHWEST] == OtherColour:
		stringID = stringID + Constants.NORTHWEST
		NofChanges = NofChanges + 1
	if game_state[stringID + Constants.NORTHWEST] == TurnColour:
		MoveXID = stringID + Constants.NORTHWEST
		while NofChanges != 0:
			PlaceHolder = TurnColour + game_state[stringID + 1:stringID - Constants.NORTHWEST]
			slice_new_state = slice_new_state + PlaceHolder
			stringID = stringID - Constants.NORTHWEST
			NofChanges = NofChanges - 1
			print (PlaceHolder, "PlaceHolder")
			print (slice_new_state, "slice_new_state")
			print (stringID, "Index of Change")
			print (NofChanges, "Number of Changes left")
		if NofChanges == 0:
			new_state = game_state[:MoveXID - Constants.NORTHWEST] + slice_new_state + game_state[MoveID:]
			print ("         #        #        #       #")
			print ("01234567890123456789012345678901234567890")
			print (game_state)
			print (new_state)
	return new_state


#############################################################################
def CheckNorth(game_state, stringID):

	TurnColour = "W"
	OtherColour = "B"
	NofChanges = 0

	PlaceHolder = ""
	slice_new_state = ""
	new_state = ""
	MoveID = 0
	MoveXID = 0

	MoveID = stringID
	while game_state[stringID + Constants.NORTH] == OtherColour:
		stringID = stringID + Constants.NORTH
		NofChanges = NofChanges + 1
	if game_state[stringID + Constants.NORTH] == TurnColour:
		MoveXID = stringID + Constants.NORTH
		while NofChanges != 0:
			PlaceHolder = TurnColour + game_state[stringID + 1:stringID - Constants.NORTH]
			slice_new_state = slice_new_state + PlaceHolder
			stringID = stringID - Constants.NORTH
			NofChanges = NofChanges - 1
			print (PlaceHolder, "PlaceHolder")
			print (slice_new_state, "slice_new_state")
			print (stringID, "Index of Change")
			print (NofChanges, "Number of Changes left")
		if NofChanges == 0:
			new_state = game_state[:MoveXID - Constants.NORTH] + slice_new_state + game_state[MoveID:]
			print ("         #        #        #       #")
			print ("01234567890123456789012345678901234567890")
			print (game_state)
			print (new_state)
	return new_state


#############################################################################
def CheckNorthEast(game_state, stringID):

	TurnColour = "W"
	OtherColour = "B"
	NofChanges = 0

	PlaceHolder = ""
	slice_new_state = ""
	new_state = ""
	MoveID = 0
	MoveXID = 0


	MoveID = stringID
	while game_state[stringID + Constants.NORTHEAST] == OtherColour:
		stringID = stringID + Constants.NORTHEAST
		NofChanges = NofChanges + 1
	if game_state[stringID + Constants.NORTHEAST] == TurnColour:
		MoveXID = stringID + Constants.NORTHEAST				#!!!!!!to slice must be [stringID+Constants.NORTHEAST+9]
		while NofChanges != 0:
			PlaceHolder = TurnColour + game_state[stringID + 1:stringID - Constants.NORTHEAST]
			slice_new_state = slice_new_state + PlaceHolder
			stringID = stringID - Constants.NORTHEAST
			NofChanges = NofChanges - 1
			print (PlaceHolder, "PlaceHolder")
			print (slice_new_state, "slice_new_state")
			print (stringID, "Index of Change")
			print (NofChanges, "Number of Changes left")
		if NofChanges == 0:
			new_state = game_state[:MoveXID - Constants.NORTHEAST] + slice_new_state + game_state[MoveID:]
			print ("         #        #        #       #")
			print ("01234567890123456789012345678901234567890")
			print (game_state)
			print (new_state)
	return new_state


#############################################################################
def CheckSouthWest(game_state, stringID):

	TurnColour = "W"
	OtherColour = "B"
	NofChanges = 0
	PlaceHolder = ""
	slice_new_state = ""
	new_state = ""
	MoveID = 0
	MoveXID = 0


	MoveID = stringID
	while game_state[stringID + Constants.SOUTHWEST] == OtherColour:
		stringID = stringID + Constants.SOUTHWEST
		NofChanges = NofChanges + 1
	if game_state[stringID + Constants.SOUTHWEST] == TurnColour:
		MoveXID = stringID + Constants.SOUTHWEST				#!!!!!!to slice must be [stringID+Constants.SOUTHWEST+9]
		while NofChanges != 0:
			PlaceHolder = TurnColour + game_state[stringID + 1:stringID + Constants.SOUTHWEST]
			slice_new_state = PlaceHolder + slice_new_state
			stringID = stringID - Constants.SOUTHWEST
			NofChanges = NofChanges - 1
			print (PlaceHolder, "PlaceHolder")
			print (slice_new_state, "slice_new_state")
			print (stringID, "Index of Change")
			print (NofChanges, "Number of Changes left")
		if NofChanges == 0:
			new_state = game_state[:MoveID + Constants.SOUTHWEST] + slice_new_state + game_state[MoveXID:]
			print ("         #        #        #       #")
			print ("01234567890123456789012345678901234567890")
			print (game_state)
			print (new_state)
	return new_state


#############################################################################
def CheckSouthEast(game_state, stringID):

	TurnColour = "W"
	OtherColour = "B"
	NofChanges = 0

	PlaceHolder = ""
	slice_new_state = ""
	new_state = ""
	MoveID = 0
	MoveXID = 0

	MoveID = stringID
	while game_state[stringID + Constants.SOUTHEAST] == OtherColour:
		stringID = stringID + Constants.SOUTHEAST
		NofChanges = NofChanges + 1
	if game_state[stringID + Constants.SOUTHEAST] == TurnColour:
		MoveXID = stringID + Constants.SOUTHEAST				#!!!!!!to slice must be [stringID+Constants.SOUTHEAST+9]
		while NofChanges != 0:
			PlaceHolder = TurnColour + game_state[stringID + 1:stringID + Constants.SOUTHEAST]
			slice_new_state = PlaceHolder + slice_new_state
			stringID = stringID - Constants.SOUTHEAST
			NofChanges = NofChanges - 1
			print (PlaceHolder, "PlaceHolder")
			print (slice_new_state, "slice_new_state")
			print (stringID, "Index of Change")
			print (NofChanges, "Number of Changes left")
		if NofChanges == 0:
			new_state = game_state[:MoveID + Constants.SOUTHEAST] + slice_new_state + game_state[MoveXID:]
			print ("         #        #        #       #")
			print ("01234567890123456789012345678901234567890")
			print (game_state)
			print (new_state)
	return new_state



#############################################################################
def CheckSouth(game_state, stringID):

	TurnColour = "W"
	OtherColour = "B"
	NofChanges = 0

	PlaceHolder = ""
	slice_new_state = ""
	new_state = ""
	MoveID = 0
	MoveXID = 0

	MoveID = stringID
	while game_state[stringID + Constants.SOUTH] == OtherColour:
		stringID = stringID + Constants.SOUTH
		NofChanges = NofChanges + 1
	if game_state[stringID + Constants.SOUTH] == TurnColour:
		MoveXID = stringID + Constants.SOUTH				#!!!!!!to slice must be [stringID+Constants.SOUTH+9]
		while NofChanges != 0:
			PlaceHolder = TurnColour + game_state[stringID + 1:stringID + Constants.SOUTH]
			slice_new_state = PlaceHolder + slice_new_state
			stringID = stringID - Constants.SOUTH
			NofChanges = NofChanges - 1
			print (PlaceHolder, "PlaceHolder")
			print (slice_new_state, "slice_new_state")
			print (stringID, "Index of Change")
			print (NofChanges, "Number of Changes left")
#		if NofChanges == 0:
		new_state = game_state[:MoveID + Constants.SOUTH] + slice_new_state + game_state[MoveXID:]
		print (MoveID + Constants.SOUTH, " MoveID")
		print (MoveXID, " MoveXID")
		print ("012345678901234567890123456789012345678901234567890123")
		print (game_state)
		print (new_state)
	return new_state

#def ChangePieces(game_state, turn_colour)


print ("___________________________")
print ("TEST 1 TEST 1 TEST 1 TEST 1")
print (" ")
CheckNorthWest("WWWWWWWWWBBBBBBBBBBBBWBBNBBBBBBWNNBWWWNNNBNNNBNNBNNNNNBNNNNNNNNW", 35)
print ("___________________________")
print ("TEST 2 TEST 2 TEST 2 TEST 2")
print (" ")
CheckNorthWest("WWWWWWWWWBBBBBBBBBBBBWBBNBBBBBBWNNBWWWNNNBNNNBNNBNNNNNBNNNNNNNNW", 36)

print("_____________________________")
print("TEST3 TEST3 TEST3".center(50))
CheckNorthWest("WWWWWWWWWBBBBBBBBBBBBWBBNBBBBBBWNNBWWWNNNBNNNBNNBNNNNNBNNNNNNNNW", 37)



print("_________________________________")
print("CHECK NORTH CHECK NORTH CHECK NORTH".center(50))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("TEST1TEST1TEST1".center(50))
print("_________________________________")
CheckNorth("WWWWWWWWWBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBWBBBBBBBBBBBB", 51)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("<('o'<)".center(50))
print("_________________________________")
print("CHECK NORTHEAST CHECK NORTHEAST CHECK NORTH".center(50))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("TEST1TEST1TEST1".center(50))
print("_________________________________")
CheckNorthEast("WWWWWWWWWBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBWBBBBBBBBBBBBBBBBBBBBBNN", 40)

print("_________________________________")
print("<('o'<)".center(50))
print("_________________________________")
print("CHECK SOUTHWEST CHECK SOUTHWEST CHECK SOUTHWEST".center(50))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("TEST1 TEST1 TEST1 ".center(50))
print("_________________________________")
print(" ")
CheckSouthWest("WWWWWBBBBBBBBBBBBBBBBBBBBBBBBBBWWBBBBBBWBBBBBBBBBBBBBBBBBBBBBBBB", 4)
print ("___________________________")
print ("TEST 2 TEST 2 TEST 2 TEST 2")
print (" ")
CheckSouthWest("WWWWBBBBBBBBBBBBBBBBBBBBBBBBBBBWWBBBBBBWBBBBBBBBBBBBBBBBBBBBBBBB", 3)
print("_________________________________")
print("<('o'<)".center(50))
print("_________________________________")
print("CHECK SOUTH CHECK SOUTH CHECK SOUTH".center(50))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("TEST1 TEST1 TEST1 ".center(50))
print("_________________________________")
print(" ")
CheckSouth("WWWWWWWWBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBWWWWWWWW", 3)
print("_________________________________")
print("<('o'<)".center(50))
print("_________________________________")
print("CHECK SOUTH CHECK SOUTH CHECK SOUTH".center(50))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("TEST2 TEST2 TEST2 ".center(50))
print("_________________________________")
print(" ")
CheckSouth("WWWWWWWWBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBWWWWWWWW", 5)
Hilda = CheckSouth("WWWWWWWWBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBWWWWWWWW", 5)
print(Hilda, "Hilda")
