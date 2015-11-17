import ScreenState
import StringInterpret
import ReversiGrid
import Converter
import time

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
		#print(i== localationList[0], " because ", i, " is not ", localationList[0])
		if localationList[0] == i:
			rowIDX = counter
		counter = counter+1

	#print(rowIDX)
	localationList[0] = rowIDX
	#print(location, "becomes ", localationList)
	return localationList

#Takes a the turn letter and returns the opposite turn letter
def inverseTurnChar(char):
	if char== 'W':
		return 'B'
	elif char == 'B':
		return 'W'
	else:
		return 'Error Invalid Param'

#IMPORTANT FUNCTION: - Any Logic Errors in the will be persvasive
#Takes row as a list of the chars to works with, the location of the char in the string, and the letter that was placed.
#row = ['N', 'W', 'W', 'W', 'N', 'W', 'N']
#Say we insert a 'B' here   ^ at the 4th char in the list

#Function takes a specific row or list, the location that a piece has been placed, and the turn letter as parameters
#Function then updates the row as if it was horizontal
#Works for "rows" of all sizes
#returns the updated row
def update_row(row, Relativelocation, turn_letter):
	
	#print("Starts with ", row, "at ", Relativelocation)
	Relativelocation = Relativelocation 
	#Used to alert the programmer if they passed in a paramter that will result in a crash
	if len(row)<= Relativelocation:
		print("ERROR RL TOO BIG")
		print(row)
		print(Relativelocation)

	if Relativelocation < 0:
		print("ERROR RL TOO SMALL")
		print(row)
		print(Relativelocation)

	#Add the turn_letter into said spot
	row[Relativelocation] = turn_letter

	#Break the row into left and right sides:
		#Ex: ['N', 'N', 'B', 'W', 'W', 'W, 'W, 'N']
						#adding a "B" into the 3rd last spot will break the row into:
			#['N', 'N', 'B', 'W', 'B'] <- that "B is the one added" and ['W', 'W', 'N']
	rowLeft = row[:Relativelocation]
	#print("RowLeft was: ", rowLeft)
	#Update the characters on the left hand size of the move location
	locCount = 0
	StartConvert = False
	for letter in rowLeft:
		if StartConvert == True:
			rowLeft[locCount] = turn_letter
		if letter == turn_letter:
			StartConvert = True
		locCount = locCount +1
	
	#print("RowLeft is now :",  rowLeft)
	row[Relativelocation] = turn_letter

	rowRight = row[Relativelocation+1:]
	#print("RowRight was : ", rowRight)
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

			
	#print("Que is ", que)
	#Update the rowRight based on if an end was found
	loopCount = 0
	if EndFound == False:
		que = []
	else:
		for letter in que:
			rowRight[loopCount] = inverseTurnChar(letter)
			loopCount = loopCount +1

	#print("RowRight is now : ", rowRight)
	#Combine left and right side rows into the new row
	newRow = []
	for letter in rowLeft:
		newRow.append(letter)
	
	newRow.append(turn_letter)
	
	for letter in rowRight:
		newRow.append(letter)

	#print("Returns ", newRow)
	return newRow

#Updates the board token vertically
#Takes the token as a 2D list, the relative location, and the turnletter
#Returns the updated list
def update_column(token, Relativelocation, turn_letter):
	#print("Update Column was passed : ", token, " ", Relativelocation, " ", turn_letter)
	tempRow = []
	#Create a temporary row of all of ther vertical letters for easy updating
	for row in token:
		tempRow.append(row[Relativelocation])
	
	#print("column found ", tempRow, " To be the column")
	#Update the row
	tempRow = update_row(tempRow, Relativelocation, turn_letter)

	#Using the updated row change the token
	loopCount = 0
	for row in token:
		change = tempRow[loopCount]
		row[Relativelocation] = change
		loopCount = loopCount + 1

	return token

#Function updates the board's Up to Down diagnals based on a token, move and turn_letter
#Up to down is styled like this:
		#
			#
				#
					#
#Function returns the updates token
#The function looks long and painful, but it operates on a similar idea as update_row and update_column
	#The function starts by getting all characters above the location that is in the diagnol and adds it the row that we can use update_row on
	#We the then get all the characters below and add it to the row
	#After updating it, we can change the characters using the same way that we found the diagnals

def update_diagnalUD(token, location, turn_letter):
	tempToken = token[:]
	xy = convertMove(location)

	#Turn the move, ex D3, into xy coords for the board. Subtract 1 in order to start counting at 0
	x = xy[0] -1
	y = xy[1] -1

	#Declare all necessary variable
	EdgeFound = False
	tempRow = []
	tempPiece = None
	tokenRow = tempToken[y]
	tokenPiece = tokenRow[x]
	yTracker = y
	xTracker = x 
	#Direction variable is used to determine if we are increasing or decreasing the index
	direction = 1
	row = []

	#Diagnal approaching upper left
	while EdgeFound == False:
		if 0<= yTracker <=7:
			tokenRow = tempToken[yTracker]
			if 0 <= xTracker <= 7:
				tokenPiece = tokenRow[xTracker]
				row.append(tokenPiece)
			else:
				EdgeFound = True
		else:
			EdgeFound = True
			
		xTracker = xTracker - direction
		yTracker = yTracker - direction
	
	row.reverse()
	#print("Upper left is ", row)
	#Reset the variables a change the direction
	#Diagnal approaching bottom right
	tokenRow = tempToken[y]
	tokenPiece = tokenRow[x]
	yTracker = y +1
	xTracker = x +1
	direction = 1
	EdgeFound = False

	#Same process as before just with the changed direction
	while EdgeFound == False:
		if 0<= yTracker <=7:
			tokenRow = tempToken[yTracker]
			if 0 <= xTracker <= 7:
				tokenPiece = tokenRow[xTracker]
				row.append(tokenPiece)
			else:
				EdgeFound = True
		else:
			EdgeFound = True

		xTracker = xTracker + direction
		yTracker = yTracker + direction

		
	#print("Total is now ", row)
	#Update the peieces as needed
	relativeLocation = x
	if relativeLocation < len(row) -1:
		row = update_row(row, relativeLocation, turn_letter)
	#print("Updated to ", row)
	#Now we need to update the token with the changed peices
	tokenRow = tempToken[y]
	tokenPiece = tokenRow[x]
	xTracker = x
	yTracker = y
	direction = 1
	idx = x
	EdgeFound = False

	halfRow = row[:relativeLocation]
	halfRow.reverse()
	halfRow = halfRow + row[relativeLocation +1 :]
	row = halfRow
	
	
	
	while EdgeFound == False:
		if 0<= yTracker <=7:
			tokenRow = tempToken[yTracker]
			if 0 <= xTracker <= 7:
				if idx >=0 and len(row)> idx:
					#print(xTracker, " and ", idx, " in ", row)
					tokenRow[xTracker] = row[idx]
				else:
					EdgeFound = True
			else:
				EdgeFound = True
		else:
			EdgeFound = True

		xTracker = xTracker - direction
		yTracker = yTracker - direction
		idx = idx - 1

		
		
	tokenRow = tempToken[y]
	tokenPiece = tokenRow[x]
	xTracker = x +1
	yTracker = y +1
	direction = 1
	idx = x
	EdgeFound = False
	#print("Relativelocation is ", relativeLocation)
	#Same idea just change the direction
	while EdgeFound == False:
		if 0<= yTracker <=7:
			tokenRow = tempToken[yTracker]
			if 0 <= xTracker <= 7:
				if idx < len(row):
					tokenRow[xTracker] = row[idx]
				else:
	#				print("IDX outside of length of row:")
	#				print("IDX : ", idx)
	#				print("row : ", row)
					EdgeFound = True
			else:
				EdgeFound = True
		else:
			EdgeFound = True

		xTracker = xTracker + direction
		yTracker = yTracker + direction
		idx = idx + 1

	return tempToken

#Function updates the board's Up to Down diagnals based on a token, move and turn_letter
#Up to down is styled like this:
					#
				#
			#
		#
#Function returns the updates token
#The function looks long and painful, but it operates on a similar idea as update_row and update_column
	#The function starts by getting all characters above the location that is in the diagnol and adds it the row that we can use update_row on
	#We the then get all the characters below and add it to the row
	#After updating it, we can change the characters using the same way that we found the diagnals

#Function works the same as the other diagnal updater, just with a modified dirction addition
def update_diagnalDU(token, location, turn_letter):
	tempToken = token[:]
	xy = convertMove(location)
	x = xy[0] -1
	y = xy[1] -1

	#Declare necessary variables
	EdgeFound = False
	tempRow = []
	tempPiece = None
	tokenRow = tempToken[y]
	tokenPiece = tokenRow[x]
	yTracker = y
	xTracker = x
	direction = -1
	row = []

	#Diagnal approaching upper right
	while EdgeFound == False:
		if 0<= yTracker <=7:
			tokenRow = tempToken[yTracker]
			if 0 <= xTracker <= 7:
				tokenPiece = tokenRow[xTracker]
				row.append(tokenPiece)
			else:
				EdgeFound = True
		else:
			EdgeFound = True

		xTracker = xTracker - direction
		yTracker = yTracker + direction
	
	row.reverse()
	#print("Upper right pre row is : ", row)
	
	relativeLocation = len(row)-1

	#Diagnal approaching bottom right
	#Reset the variables
	tokenRow = tempToken[y]
	tokenPiece = tokenRow[x]
	yTracker = y +1
	xTracker = x  +1
	direction = -1
	EdgeFound = False
	while EdgeFound == False:
		#print(xTracker)
		#print(yTracker)
		#print("next is")
		if 0<= yTracker <=7:
			#print(tempToken)
			#print(yTracker)
			tokenRow = tempToken[yTracker]
			if 0 <= xTracker <= 7:
				tokenPiece = tokenRow[xTracker]
				row.append(tokenPiece)
			else:
				EdgeFound = True
		else:
			EdgeFound = True

		xTracker = xTracker + direction
		yTracker = yTracker - direction
	
	#print("DIAG row is ", row)
	#Update the peieces as needed
	row = update_row(row, relativeLocation, turn_letter)
	#print("DIAG row is ", row, " now")
	
	
	#Now we need to update the token with the changed peices
	tokenRow = tempToken[y]
	tokenPiece = tokenRow[x]
	xTracker = x
	yTracker = y
	direction = -1
	idx = x
	EdgeFound = False
	
	
	halfRow = row[:relativeLocation]
	halfRow.reverse()
	halfRow = halfRow + row[relativeLocation +1 :]
	row = halfRow
	
	
	
	while EdgeFound == False:
		if 0<= yTracker <=7:
			tokenRow = tempToken[yTracker]
			if 0 <= xTracker <= 7:
				if idx >= 0 and len(row)> 0:
	#				print("Before Crsh tokenRow = : ", tokenRow, " xTracker is : ", xTracker)
	#				print(" row is  ", row, " row idx is : ", idx)
					tokenRow[xTracker] = row[idx]
				else:
					EdgeFound = True
			else:
				EdgeFound = True
		else:
			EdgeFound = True	
		xTracker = xTracker - direction
		yTracker = yTracker + direction
		idx = idx - 1
		
		
	#print(" token row is ", tokenRow, " after first pass")	
	#Again do the same thing in the opposite direction
	tokenRow = tempToken[y]
	tokenPiece = tokenRow[x]
	xTracker = x +1
	yTracker = y +1
	direction = -1
	idx = x
	EdgeFound = False
	while EdgeFound == False:
		if 0<= yTracker <=7:
			tokenRow = tempToken[yTracker]
			if 0 <= xTracker <= 7:
				if idx < len(row):
					tokenRow[xTracker] = row[idx]
				else:
					EdgeFound = True
			else:
				EdgeFound = True
		else:
			EdgeFound = True

		xTracker = xTracker + direction
		yTracker = yTracker - direction
		idx = idx + 1
	
	return tempToken

#Function updates the token based on a move, that is assumed valid
#Only updates horizontal and vertical, will update diagnol eventually
#Takes the current token, the move, and the turn letter
#Returns the updated token
def updateToken(token, move, turn_letter):
	xy = convertMove(move)
	x = xy[0]-1
	y = xy[1]-1
	#print(x, y)
	#tempToken = token[:]
	tempToken = update_column(token, x, turn_letter)
	tempRow = update_row(token[y], x, turn_letter)
	tempToken[y] = tempRow
	tempToken = update_diagnalDU(token, move, turn_letter)
	tempToken = update_diagnalUD(token, move, turn_letter)
	
	finalRow = tempToken[y]
	finalRow[x] = turn_letter
	
	tempToken[y] = finalRow

	return token

#Generic test code
#Do not worry about this, it was just used for debugging
def testCode():
	
	print("CHECK HORIZONTAL BASIC::>>>")
	token =         [['W', 'B', 'B', 'B', 'B', 'B', 'B', 'W', ]]  
	token = token + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	token = token + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	token = token + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	token = token + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	token = token + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	token = token + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	token = token + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	
	for row in token:
		print(row)
	print("  ")
	print("  is now  >>>")
		
	token = updateToken(token, 'C1', 'W')
	for row in token:
		print(row)
	
	
	token = []
	print("CHECK VERTICAL BASIC::>>>")
	token =         [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'W', ]]  
	token = token + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'B', ]]
	token = token + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'B', ]]
	token = token + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'B', ]]
	token = token + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'B', ]]
	token = token + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'B', ]]
	token = token + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'B', ]]
	token = token + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'W', ]]
	for row in token:
		print(row)
	print("  ")
	print("  is now  >>>")
		
	token = updateToken(token, 'H2', 'W')
	for row in token:
		print(row)
	
	#""
	token = []
	print("CHECK DU DIAGNAL BASIC::>>>")
	token =         [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'W', ]]  
	token = token + [['N', 'N', 'N', 'N', 'N', 'N', 'B', 'N', ]]
	token = token + [['N', 'N', 'N', 'N', 'N', 'B', 'N', 'N', ]]
	token = token + [['N', 'N', 'N', 'N', 'B', 'N', 'N', 'N', ]]
	token = token + [['N', 'N', 'N', 'B', 'N', 'N', 'N', 'N', ]]
	token = token + [['N', 'N', 'B', 'N', 'N', 'N', 'N', 'N', ]]
	token = token + [['N', 'B', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	token = token + [['W', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	for row in token:
		print(row)
	
	print("  ")
	print("  is now  >>>")
		
	token = updateToken(token, 'B7', 'W')
	for row in token:
		print(row)
	
	
	token = []
	print("CHECK UD DIAGNAL BASIC BASIC::>>>")
	token =         [['B', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]  
	token = token + [['N', 'W', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	token = token + [['N', 'N', 'W', 'N', 'N', 'N', 'N', 'N', ]]
	token = token + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	token = token + [['N', 'N', 'N', 'N', 'W', 'N', 'N', 'N', ]]
	token = token + [['N', 'N', 'N', 'N', 'N', 'B', 'N', 'N', ]]
	token = token + [['N', 'N', 'N', 'N', 'N', 'N', 'W', 'N', ]]
	token = token + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'B', ]]
	for row in token:
		print(row)
		
	print("  ")
	print("  is now  >>>")
		
	token = updateToken(token, 'D4', 'B')
	for row in token:
		print(row)
	
	""""
	row = ['B', 'W', 'W', 'N', 'W', 'B', 'W', 'B']	
	print(row)
	row = update_row(row, 2, 'B')
	print(row)
	"""
if __name__=="__main__":
	testCode()
