import ScreenState

#Converts the location into a list of ints that represent the x y coordinates
#Only parameter is the location as a string, ex 'A7' or 'H8'
#Returns a list of ints: ex [1, 7] or [8, 8]
def convertMove(location):
	localationList = []
	for letter in location:
		localationList.append(letter)
	
	#Convert the y coordinate in an integer
	temp = localationList[1]
	localationList[1] = int(temp)
	x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
	counter = 1
	rowIDX = 1
	for i in x:
		print(i== localationList[0], " because ", i, " is not ", localationList[0])
		if localationList[0] == i:
			rowIDX = counter
		counter = counter+1
	
	print(rowIDX)
	localationList[0] = rowIDX
	
	return localationList
#Takes a the turn letter and returns the opposite turn letter	
def inverseTurnChar(char):
	if char== 'W':
		return 'B'
	elif char == 'B':
		return 'W'
	else:
		return 'Error Invalid Param'
	
#Takes row as a list of the chars to works with, the location of the char in the string, and the letter that was placed.
#row = ['N', 'W', 'W', 'W', 'N', 'W', 'N']
#Say we insert a 'B' here   ^ at the 4th char in the list


#Function takes a specific row or list, the location that a piece has been placed, and the turn letter as parameters
#Function then updates the row as if it was horizontal
#Works for "rows" of all sizes
#returns the updated row 
def update_row(row, Relativelocation, turn_letter):
	#Add the 'B' in to said spot
	row[Relativelocation] = turn_letter
	
	#Break the row into left and right sides:
		#Ex: ['N', 'N', 'B', 'W', 'W', 'W, 'W, 'N']
						#adding a "B" into the 3rd last spot will break the row into:
			#['N', 'N', 'B', 'W', 'B'] <- that "B is the one added" and ['W', 'W', 'N']
	rowLeft = row[:Relativelocation]
	
	
	#Update the characters on the left hand size of the move location
	locCount = 0
	StartConvert = False
	for letter in rowLeft:
		if StartConvert == True:
			rowLeft[locCount] = turn_letter
		if letter == turn_letter:
			StartConvert = True
		locCount = locCount +1
		
	
	rowRight = row[Relativelocation+1:]
	que = []
	EndFound = False
	FirstRound = True
	StartCount = True
	
	#Update move on the right hand side:
		#NOTE: This is handled slightly differently, as it cannot be counted on for there to be a turn letter further in the string
		#For this reason, we simply add the letters to a que, and  do not update them until we can verify that another turn letter has been found
		#Ex: if rowRight = ['W', 'W', 'W', 'W'] and the turn letter is 'B' then we do not change the W's until we find another B.
	for letter in rowRight:
		if letter != inverseTurnChar(turn_letter):
			StartCount = False	
		if FirstRound == True:
			if letter == inverseTurnChar(turn_letter):
				StartCount = True
			FirstRound = False
		if letter == turn_letter:
			EndFound = True
		if StartCount == True:
			que.append(letter)
	
	#Update the rowRight based on if an end was found 
	loopCount = 0
	if EndFound == False:
		que = []
	else:
		for letter in que:
			rowRight[loopCount] = inverseTurnChar(letter)
			loopCount = locCount +1
	
	#Combine left and right side rows into the new row
	newRow = []
	for letter in rowLeft:
		newRow.append(letter)
	newRow.append(turn_letter)
	for letter in rowRight:
		newRow.append(letter)
	
	return newRow
#W 
#W
#B
#W
#W
#B
#N
#B	



#Updates the board token vertically
#Takes the token as a 2D list, the relative location, and the turnletter
#Returns the updated list
def update_column(token, Relativelocation, turn_letter):
	tempRow = []
	for row in token:
		tempRow.append(row[Relativelocation])
	tempRow = update_row(tempRow, Relativelocation, turn_letter)
	
	loopCount = 0
	for row in token:
		change = tempRow[loopCount]
		row[Relativelocation] = change
		loopCount = loopCount + 1
	
	return token
	
#FUNCTION NOT FINISHED DO NOT USE!	
def update_diagnal(token, x, y, turn_letter):
	tempRow = []
	tracker = x
	rowsAbove = token[:y]
	rowsBelow = token[y:]
	tempRowsAbove = [None, None, None, None, None, None, None, None, None]
	loopCount = 7
	for row in rowsAbove:
		tempRowsAbove[loopCount] = row
		loopCount = loopCount -1
	
	print(rowsAbove)
	print(tempRowsAbove)
	loopCount = 0
	for row in tempRowsAbove:
		if row != None:
			if 0<= loopCount -1 <= 7:
				rowAbove = token[loopCount -1]
				if 0 <= tracker -1 <=7 :
					tempRow.append(rowAbove[tracker-1])
		
			if 0 <= tracker <=7 :
				tempRow.append(row[tracker -1])
				print(row, " and ", loopCount)
		loopCount = loopCount + 1
	print(tempRow)

#Function updates the token based on a move, that is assumed valid
#Only updates horizontal and vertical, will update diagnol eventually
#Takes the current token, the move, and the turn letter
#Returns the updated token
def updateToken(token, move, turn_letter):
	xy = convertMove(move)
	x = xy[0]
	y = xy[1]
	
	tempToken = update_column(token, x, turn_letter)
	tempRow = update_row(token[y], x, turn_letter)
	tempToken[y] = tempRow
	
	return tempToken

		
#Generic test code
		
def testCode():

	update_row(row, 4, 'B')
	token = 'BNNBWWWW' +'WWBWWWBN' + 'BNWNNNNN' + 'BWWBWWWB'+  'NNNNNNNN' + 'NNNNNNNN' 'NNNNNNNN' + 'NNNNNNNN'	
	token = ScreenState.prep_token(token) 
	token=ScreenState.convert_string_to_list(token)
	#for row in token:
	#	print(row)
	#print("is now")
	#token = update_column(token, 0, 'B')
	#for row in token:
	#	print(row)
	#update_diagnal(token, 4, 4, 'B')
	update_column(token, 3, 'W')
	

	
if __name__=="__main__":
	testCode()
	