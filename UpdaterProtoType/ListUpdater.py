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
		
def update_row(row, relativeLoaction, turn_letter):
	startConvert = False
	rowLeft = row[:relativeLoaction]
	EndFound = False
	que = []
	#print(row)
	#print(rowLeft)
	rowLeft.reverse()
	#print(rowLeft)
	stop = False
	for letter in rowLeft:
		#['B', 'W', 'B', 'N', 'N', 'N', 'N', 'N']
		if letter == inverseTurnChar(turn_letter) and stop == False:
			startConvert = True
		
		if letter == 'N':
			startConvert == False
			stop = True
		if letter == turn_letter:
			startConvert = False
			EndFound = True
			stop = True
		if startConvert == True and letter == inverseTurnChar(turn_letter):
			que.append(letter)
		
		
	#print(que)	
	#print(rowLeft)
	counter = 0
	""""
	for i in rowLeft:
		if i != inverseTurnChar(turn_letter):
			que = []
	"""
	if EndFound == True and len(que) > 0:
		for letter in que:
			rowLeft[counter] = turn_letter
			counter = counter+1
	
	rowLeft.reverse()
	
	
	#print(rowLeft)
	
	
	startConvert = False
	rowRight = row[relativeLoaction+1:]
	#print(rowRight)
	EndFound = False
	que2 = []
	#print(row)
	#print(rowLeft)
	#print(rowLeft)
	stop = False
	for letter in rowRight:
		#['B', 'W', 'B', 'N', 'N', 'N', 'N', 'N']
		if letter == inverseTurnChar(turn_letter) and stop == False:
			startConvert = True
		
		if letter == 'N':
			startConvert == False
			stop = True
		if letter == turn_letter:
			startConvert = False
			EndFound = True
			stop = True
		if startConvert == True and letter == inverseTurnChar(turn_letter):
			que2.append(letter)
		
		
	print(que2)	
	#print(rowRight)
	"""
	for i in rowRight:
		if i != inverseTurnChar(turn_letter):
			que2 = []
	"""
	counter = 0
	if EndFound == True and len(que2) > 0:
		for letter in que2:
			rowRight[counter] = turn_letter
			counter = counter+1
	
	#print(rowRight)
	newRow = rowLeft
	newRow.append(turn_letter)
	newRow = newRow + rowRight
	#print(newRow)
	return newRow
#Updates the board token vertically
#Takes the token as a 2D list, the relative location, and the turnletter
#Returns the updated list
def update_column(token, x, y, turn_letter):
	#print("Update Column was passed : ", token, " ", Relativelocation, " ", turn_letter)
	
	#Create a temporary row of all of ther vertical letters for easy updating
	tempRow = []
	
	
	for row in token:
		tempRow.append(row[x])
	
	#Update the row
	tempRow = update_row(tempRow, y, turn_letter)
	
	#print("column found ", tempRow, " To be the column")
	
	
	#print("Column now   ", tempRow, " To be the column")
	#Using the updated row change the token
	newToken = token [:]
	loopCount = 0
	for row in newToken:
		tempPiece = tempRow[loopCount]
		row[x] = tempPiece
		loopCount = loopCount + 1

	return newToken
	

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
	idx = x -1
	EdgeFound = False

	
	
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
	idx = x -1
	EdgeFound = False
	
	
	while EdgeFound == False:
		if 0<= yTracker <=7:
			tokenRow = tempToken[yTracker]
			if 0 <= xTracker <= 7:
				if idx >= 0 and len(row)> idx:
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
	print(x, y)
	tempToken = token[:]
	
	tempToken = update_column(token, x, y, turn_letter)
	tempRow = update_row(tempToken[y], x, turn_letter)
	tempToken[y] = tempRow
	#tempToken = update_diagnalDU(token, move, turn_letter)
	#tempToken = update_diagnalUD(token, move, turn_letter)
	
	#finalRow = tempToken[y]
	#finalRow[x] = turn_letter
	
	#tempToken[y] = finalRow
	
	return tempToken

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
	token = token + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	token = token + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'W', ]]
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
		
	
	
	
	token = []
	print("CHECK UD DIAGNAL BASIC BASIC::>>>")
	token =         [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]  
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
		
	token = updateToken(token, 'A1', 'B')
	for row in token:
		print(row)
	
		
	token = []
	print("CHECK CUSTOM BASIC BASIC::>>>")
	print("      A    B    C    D    E    F    G    H")
	token =         [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]  
	token = token + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	token = token + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	token = token + [['N', 'N', 'N', 'W', 'B', 'N', 'N', 'N', ]]
	token = token + [['N', 'N', 'N', 'B', 'W', 'N', 'N', 'N', ]]
	token = token + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	token = token + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	token = token + [['N', 'N', 'W', 'B', 'N', 'N', 'W', 'N', ]]
	tempCount = 1
	for row in token:
		
		print(tempCount, " ", row)
		tempCount = tempCount +1
	
	tempCount = 1
	print("  ")
	print("  is now  >>>")
	
	token = updateToken(token, 'H8', 'B')
	print("      A    B    C    D    E    F    G    H")
	for row in token:
		print(tempCount, " ", row)
		tempCount = tempCount +1
	
	""""
	['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N']
" A     B   C    D    E    F    G    H"
['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N']
['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N']
['N', 'N', 'N', 'W', 'B', 'N', 'N', 'N']
['N', 'N', 'N', 'B', 'W', 'N', 'N', 'N']
['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N']
['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N']
['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N']
	row = ['B', 'W', 'W', 'N', 'W', 'B', 'W', 'B']	
	print(row)
	row = update_row(row, 2, 'B')
	print(row)
	"""
if __name__=="__main__":
	testCode()
