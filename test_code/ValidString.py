

#MoveToString = 27
                                    #
#token = "WWWWWWWWWBBBBBBBBBBBBWBBNBBBBBBWNNBWWWNNNBNNNBNNBNNNNNBNNNNNNNNW"
TurnColour = "W"
OtherColour = "B"
WEST = -1
NORTHEASTWEST = -9
n = 1

# if the piece next to the current move is the OtherColour:  (8 times one for each direction)
#while the index does not equal the OtherColour add that index to the turn's string. if the index finds the turn colour, turn all the colours up to that index into the TurnColour.
#if token[MoveToString - 1] == OtherColour or token[MoveToString - 9] == OtherColour or token[MoveToString - 8] == OtherColour or token[MoveToString - 7] == OtherColour or token[MoveToString + 1] == OtherColour
#or token[MoveToString + 9] == OtherColour or token[MoveToString + 8] == OtherColour or token[MoveToString + 7] == OtherColour:

n = 1

def CheckWest(token, MoveToString):

	TurnColour = "W"
	OtherColour = "B"
	WEST = -1
	NORTHWEST = -9
	n = 1

	while token[MoveToString + (WEST)] == OtherColour:
		print (n, "n Number of other colours")
		print (MoveToString + (WEST), "index of OtherColour")
		MoveToString = MoveToString + (WEST)
		if token[MoveToString] == "N":
			print("that move is invalid")
		n = n + 1

		if token[MoveToString + (WEST)] == TurnColour:
			NewToken = token[:MoveToString] + (TurnColour * n) + token[MoveToString + (WEST) + n + 1:]
			print (token)
			print(NewToken)
			print (n, "How many times we have to print the TurnColour's letter.")



def CheckEast(token, MoveToString):
	TurnColour = "W"
	OtherColour = "B"
	WEST = -1
	NORTHWEST = -9
	EAST = 1
	n = 1

	while token[MoveToString + (EAST)] == OtherColour:
		print (n, "n Number of other colours")
		print (MoveToString + (EAST), "index of OtherColour")
		MoveToString = MoveToString + (EAST)
		if token[MoveToString] == "N":
			print("that move is invalid")
		n = n + 1

		if token[MoveToString + (EAST)] == TurnColour:
			NewToken = token[:MoveToString - n + 1] + (TurnColour * n) + token[MoveToString + 1:]
			print (token)
			print(NewToken)
			print (n, "How many times we have to print the TurnColour's letter.")






def CheckNorthWest(token, MoveToString):
	#		#0123456789012345678901234567890123456789012345678901234567890123
	token = "WWWWWWWWWBBBBBBBBBBBBWBBNBBBBBBWNNBWWWNNNBNNNBNNBNNNNNBNNNNNNNNW"
	TurnColour = "W"
	OtherColour = "B"
	WEST = -1
	NORTHWEST = -9
	EAST = 1
	NofChanges = 0

	PlaceHolder = ""
	NextToken = ""
	NewToken = ""
	MoveID = 0
	MoveXID = 0

#	if token[MoveToString + NORTHWEST] == TurnColour or "N":
#		print("Not NorthWest")
#		return False
#	else:
	MoveID = MoveToString
	while token[MoveToString + NORTHWEST] == OtherColour:
		MoveToString = MoveToString + NORTHWEST
		NofChanges = NofChanges + 1
	if token[MoveToString + NORTHWEST] == TurnColour:
		MoveXID = MoveToString + NORTHWEST				#!!!!!!to slice must be [MoveToString+NORTHWEST+9]
		while NofChanges != 0:
			PlaceHolder = TurnColour + token[MoveToString + 1:MoveToString - NORTHWEST]
			NextToken = NextToken + PlaceHolder
			MoveToString = MoveToString - NORTHWEST
			NofChanges = NofChanges - 1
			print (PlaceHolder, "PlaceHolder")
			print (NextToken, "NextToken")
			print (MoveToString, "Index of Change")
			print (NofChanges, "Number of Changes left")
		if NofChanges == 0:
			NewToken = token[:MoveXID - NORTHWEST] + NextToken + token[MoveID:]
			print ("         #        #        #       #")
			print ("01234567890123456789012345678901234567890")
			print (token)
			print (NewToken)

def CheckNorth(token, MoveToString):
	#		#0123456789012345678901234567890123456789012345678901234567890123

	TurnColour = "W"
	OtherColour = "B"
	NORTH = -8
	NofChanges = 0

	PlaceHolder = ""
	NextToken = ""
	NewToken = ""
	MoveID = 0
	MoveXID = 0

#	if token[MoveToString + NORTH] == TurnColour or "N":
#		print("Not NORTH")
#		return False
#	else:
	MoveID = MoveToString
	while token[MoveToString + NORTH] == OtherColour:
		MoveToString = MoveToString + NORTH
		NofChanges = NofChanges + 1
	if token[MoveToString + NORTH] == TurnColour:
		MoveXID = MoveToString + NORTH				#!!!!!!to slice must be [MoveToString+NORTH+9]
		while NofChanges != 0:
			PlaceHolder = TurnColour + token[MoveToString + 1:MoveToString - NORTH]
			NextToken = NextToken + PlaceHolder
			MoveToString = MoveToString - NORTH
			NofChanges = NofChanges - 1
			print (PlaceHolder, "PlaceHolder")
			print (NextToken, "NextToken")
			print (MoveToString, "Index of Change")
			print (NofChanges, "Number of Changes left")
		if NofChanges == 0:
			NewToken = token[:MoveXID - NORTH] + NextToken + token[MoveID:]
			print ("         #        #        #       #")
			print ("01234567890123456789012345678901234567890")
			print (token)
			print (NewToken)

def CheckNorthEast(token, MoveToString):
	#		#0123456789012345678901234567890123456789012345678901234567890123

	TurnColour = "W"
	OtherColour = "B"
	NORTHEAST = -7
	NofChanges = 0

	PlaceHolder = ""
	NextToken = ""
	NewToken = ""
	MoveID = 0
	MoveXID = 0

#	if token[MoveToString + NORTH] == TurnColour or "N":
#		print("Not NORTHEASTEAST")
#		return False
#	else:
	MoveID = MoveToString
	while token[MoveToString + NORTHEAST] == OtherColour:
		MoveToString = MoveToString + NORTHEAST
		NofChanges = NofChanges + 1
	if token[MoveToString + NORTHEAST] == TurnColour:
		MoveXID = MoveToString + NORTHEAST				#!!!!!!to slice must be [MoveToString+NORTHEAST+9]
		while NofChanges != 0:
			PlaceHolder = TurnColour + token[MoveToString + 1:MoveToString - NORTHEAST]
			NextToken = NextToken + PlaceHolder
			MoveToString = MoveToString - NORTHEAST
			NofChanges = NofChanges - 1
			print (PlaceHolder, "PlaceHolder")
			print (NextToken, "NextToken")
			print (MoveToString, "Index of Change")
			print (NofChanges, "Number of Changes left")
		if NofChanges == 0:
			NewToken = token[:MoveXID - NORTHEAST] + NextToken + token[MoveID:]
			print ("         #        #        #       #")
			print ("01234567890123456789012345678901234567890")
			print (token)
			print (NewToken)

def CheckSouthWest(token, MoveToString):
	#		#0123456789012345678901234567890123456789012345678901234567890123

	TurnColour = "W"
	OtherColour = "B"
	SOUTHWEST = 7
	NofChanges = 0

	PlaceHolder = ""
	NextToken = ""
	NewToken = ""
	MoveID = 0
	MoveXID = 0

#	if token[MoveToString + NORTH] == TurnColour or "N":
#		print("Not SOUTHWEST")
#		return False
#	else:
	MoveID = MoveToString
	while token[MoveToString + SOUTHWEST] == OtherColour:
		MoveToString = MoveToString + SOUTHWEST
		NofChanges = NofChanges + 1
	if token[MoveToString + SOUTHWEST] == TurnColour:
		MoveXID = MoveToString + SOUTHWEST				#!!!!!!to slice must be [MoveToString+SOUTHWEST+9]
		while NofChanges != 0:
			PlaceHolder = TurnColour + token[MoveToString + 1:MoveToString + SOUTHWEST]
			NextToken = NextToken + PlaceHolder
			MoveToString = MoveToString - SOUTHWEST
			NofChanges = NofChanges - 1
			print (PlaceHolder, "PlaceHolder")
			print (NextToken, "NextToken")
			print (MoveToString, "Index of Change")
			print (NofChanges, "Number of Changes left")
		if NofChanges == 0:
			NewToken = token[:MoveID + SOUTHWEST] + NextToken + token[MoveXID:]
			print ("         #        #        #       #")
			print ("01234567890123456789012345678901234567890")
			print (token)
			print (NewToken)




"""
#CheckWest(token, 27)
#CheckEast(token, 27)
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
"""


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
CheckSouthWest("WWWWBBBBBBBBBBBBBBBBBBBBBBBBBBBWBBBBBBBWBBBBBBBBBBBBBBBBBBBBBBBB", 3)
