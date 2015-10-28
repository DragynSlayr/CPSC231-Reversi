

MoveToString = 27                   
                                    #                              
token = "WNNNNBBNNBNNBNNNNNBNBWBBBBBWBBBWNNBNBNNNNBNNNBNNBNNNNNBNNNNNNNNW"
TurnColour = "W"
OtherColour = "B"
WEST = -1
NORTHWEST = -7
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
	NORTHWEST = -7
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


			
def CheckEAST(token, MoveToString):
	TurnColour = "W"
	OtherColour = "B"
	WEST = -1
	NORTHWEST = -7
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


CheckWest(token, 27)
CheckEAST(token, 27)