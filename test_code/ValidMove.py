

#MoveToString = 27                   
                                    #                              
token = "WNBBBBBBWBNBBBBBBBBBBWBBNBBWBBBWNNBWWBNNNBNNNBNNBNNNNNBNNNNNNNNW"
TurnColour = "W"
OtherColour = "B"

# if the piece next to the current move is the OtherColour:  (8 times one for each direction)
#while the index does not equal the OtherColour add that index to the turn's string. if the index finds the turn colour, turn all the colours up to that index into the TurnColour.
#if token[MoveToString - 1] == OtherColour or token[MoveToString - 9] == OtherColour or token[MoveToString - 8] == OtherColour or token[MoveToString - 7] == OtherColour or token[MoveToString + 1] == OtherColour
#or token[MoveToString + 9] == OtherColour or token[MoveToString + 8] == OtherColour or token[MoveToString + 7] == OtherColour:


def CheckWest(token, MoveToString):

	TurnColour = "W"
	OtherColour = "B"
	WEST = -1
	NORTHWEST = -7
	n = 1

	while token[MoveToString + (WEST)] == OtherColour:			#While the next token is the OtherColour
		print (n, "n Number of other colours")					#Print the number of times it crosses the OtherColour
		print (MoveToString + (WEST), "index of OtherColour")	#Print the index number of the OtherColour
		MoveToString = MoveToString + (WEST)					#Moves the checker up. Subtracts one from MoveToString
		if token[MoveToString] == "N":							#Invalid move if the next letter on the string is N
			print("that move is invalid")
		n = n + 1												#Adds one to the count of the other colours.

		if token[MoveToString + (WEST)] == TurnColour:			#If the next token is the TurnColour
			NewToken = token[:MoveToString] + (TurnColour * n) + token[MoveToString + (WEST) + n + 1:]	#Create this string
			print (token)										#Print original token
			print(NewToken)										#Print NewToken
			print (n, "How many times we have to print the TurnColour's letter.")	#Number of tokens that will be changed.


			
def CheckEast(token, MoveToString):
	TurnColour = "W"
	OtherColour = "B"
	WEST = -1
	NORTHWEST = -7
	EAST = 1
	n = 1

	while token[MoveToString + (EAST)] == OtherColour:			#While the next token is the OtherColour
		print (n, "n Number of other colours")					#Print the number of times it crosses the OtherColour
		print (MoveToString + (EAST), "index of OtherColour")	#Print the index number of the OtherColour
		MoveToString = MoveToString + (EAST)					#Moves the checker up. Adds one to MoveToString
		if token[MoveToString] == "N":							#Invalid move if the next letter on the string is N
			print("that move is invalid")
		n = n + 1												#Adds one to the count of the other colours.

		if token[MoveToString + (EAST)] == TurnColour:			#If the next token is the TurnColour
			NewToken = token[:MoveToString - n + 1] + (TurnColour * n) + token[MoveToString + 1:]	#Create this string
			print (token)										#Print original token
			print(NewToken)										#Print NewToken
			print (n, "How many times we have to print the TurnColour's letter.")	#Number of tokens that will be changed.
			
			

def CheckNorthWest(token, MoveToString):
	TurnColour = "W"
	OtherColour = "B"
	WEST = -1
	NORTHWEST = -9
	EAST = 1
	n = 1
	
	PlaceHolder = ""
	NewToken = ""


	while token[MoveToString + (NORTHWEST)] == OtherColour:			#While the next index at nine less equals the OtherColour
		print (n, "n Number of other colours")						#Print the number of the other colours it has counted so far
		print (MoveToString + (NORTHWEST), "index of OtherColour")	#Prints what MoveToString will become
		MoveToString = MoveToString + NORTHWEST						#Makes MoveToString equal to 9 less than what it was. Subtracts 9
		if token[MoveToString] == "N":								#If the next token is an N the move is invalid.
			print("that move is invalid")
		n = n + 1													#add one to the number of tokens that are the other colours

	if token[MoveToString + (NORTHWEST)] == TurnColour:			#If the next token is the Turn colour
		print (n)												#Print the number of OtherColour tokens there are
		MoveToString = MoveToString + NORTHWEST					#Move the index up to the location of the indext of TurnColour across from the move.
		while n != 0:											#while the number of other colours checked does not equal 0

			PlaceHolder = TurnColour + token[MoveToString + 1:MoveToString - NORTHWEST]
			NewToken = NewToken + PlaceHolder					#STRING:NewToken is the Previous Placeholders + the current Placeholder
			MoveToString = MoveToString - NORTHWEST				#Adds 9 to MoveToString to change the next piece
			n = n - 1											#Counts down to zero based on the number of pieces counted
			print (n , "Number of tokens left")					#Number of tokens left to change
			print (PlaceHolder, "PlaceHolder")					#Placeholder Token
			print (NewToken, "NewToken")						#Entire NewToken
		if n == 0:												#When the number of pieces to change is zero
			print ("        !#       !#       !#       #")		#Measurement test # is for test one ! for test 2
			print ("01234567890123456789012345678901234567890")	#Measurement to count characters
			print (token)										#print the old token for comparison
			print (NewToken[:MoveToString] + token[MoveToString:], "NEWTOKENNEW")	#print the NewToken with the end of the last token. THERE IS A PROBLEM HERE. IF THE END PIECE IS NOT AT 0 IT WONT PRINT THE FIRST PART OF STRING.
			print (NewToken, "RealNewToken")					#Print the RealNewToken that was created.
				



#CheckWest(token, 27)
#CheckEast(token, 27)
print ("___________________________")
print ("TEST 1 TEST 1 TEST 1 TEST 1")
print (" ")
CheckNorthWest(token, 27)
print ("___________________________")
print ("TEST 2 TEST 2 TEST 2 TEST 2")
print (" ")
CheckNorthWest(token, 36)