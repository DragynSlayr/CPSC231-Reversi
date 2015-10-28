

MoveToString = 27                   
                                    #                              
token = "WNNNNNBNNBNNNBNNNNBNBWBBBBBWNNNNNNBNBNNNNBNNNBNNBNNNNNBNNNNNNNNW"
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


while token[MoveToString + (WEST * n)] == OtherColour:
#	if token[MoveToString + (WEST * n)] == OtherColour:
		n = n + 1
		print (n, "Number of other colours")
		print (MoveToString + (WEST * n), "index of OtherColour")
		MoveToString = MoveToString + (WEST * n)		
		
		
if token[MoveToString + (WEST * n)] == TurnColour:
	while n != 0:
			NewToken = token[:MoveToString + (WEST * n) + 1] + TurnColour + token[MoveToString + (WEST * n) + 1:]
			print(NewToken)
			n = n + WEST
			print (n)

""""
if token[MoveToString + NORTHWEST(n)] == OtherColour:
	while token[MoveToString + NORTHWEST(n)] == OtherColour:
		n = n + 1
		print (n)
	if token[MoveToString + NORTHWEST(n)] == TurnColour:
		while n != 0:
			NewToken = token[:MoveToString + NORTHWEST(n)] + TurnColour + token[((MoveToString + NORTHWEST(n))) + 1:]
			print(NewToken)
			n = n - NORTHWEST
			print (n)
		
"""



""""

for StringCoord in range(MoveToString, 0, -7):
	if token[MoveToString - Northwest] == OtherColour:
		print ("True")
		print (token[MoveToString - Northwest])
		print (StringCoord)
		Northwest = Northwest - 7
		

	else:
		print ("False")
		print (StringCoord)
		print (token[MoveToString])
"""
