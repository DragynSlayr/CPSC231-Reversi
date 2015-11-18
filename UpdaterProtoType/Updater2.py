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


		
def updateRow(row, relativeLoaction, turn_letter):
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
		if startConvert == True:
			que.append(letter)
		
		
	#print(que)	
	#print(rowLeft)
	counter = 0
	for i in rowLeft:
		if i != inverseTurnChar(turn_letter):
			que = []
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
		if startConvert == True:
			que2.append(letter)
		
		
	#print(que)	
	#print(rowRight)
	for i in rowRight:
		if i != inverseTurnChar(turn_letter):
			que = []
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
	#			
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
		row[x] = change
		loopCount = loopCount + 1

	return newToken
	
	
	
	
print(['N', 'N', 'W', 'B', 'N', 'N', 'W', 'N', ])
		#	   		  W
updateRow(['N', 'N', 'W', 'B', 'N', 'N', 'W', 'N', ], 7, 'B')
""""		
def update_row(row, Relativelocation, turn_letter):
	
	print("Starts with ", row, "at ", Relativelocation)
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
	#row[Relativelocation] = turn_letter

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
	#row[Relativelocation] = turn_letter

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
	
	newRow.append(row[Relativelocation])
	
	for letter in rowRight:
		newRow.append(letter)

	print("Returns ", newRow)
	return newRow

"""	
			