import ScreenState
import StringInterpret
import ReversiGrid
import Converter
import TurtleMove

#Converts the location into a list of ints that represent the x y coordinates
#Only parameter is the location as a string, ex 'A7' or 'H8'
#Returns a list of ints: ex [1, 7] or [8, 8]
def convertMove(location):
	#Create a temporary list that the function will work with
	localation_List = []
	for letter in location:
		localation_List.append(letter)

	#Convert the y coordinate in an integer
	temp = localation_List[1]
	localation_List[1] = int(temp)
	
	#Declare necessary variables in preporation for x conversion
	x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
	counter = 1
	row_IDX = 1
	
	#Convert the x by finding the index in the basic list x
	for i in x:
		if localation_List[0] == i:
			row_IDX = counter
		counter = counter+1

	#Replace the old x letter with its number representative
	localation_List[0] = row_IDX
	
	return localation_List

	
#This does the opposite of the previous function: It takes an x and a y coordinate ex(1, 2)
#And then converts it into the form that TurtleMove.placePiece can use. 
#Returns: a char and a integer
#Ex ['A', 2]
def convertMoveType(x, y):
	row = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
	x = row[x]
	move = []
	move.append(x)
	move.append(y)
	
	return move
	
#Takes a the turn letter and returns the opposite turn letter
#Ex 'W' returns 'B'
# and 'B' returns 'W'
def inverseTurnChar(char):
	if char== 'W':
		return 'B'
	elif char == 'B':
		return 'W'
	else:
		return 'Error Invalid Param'

#IMPORTANT FUNCTION: - Any Logic Errors in the will be persvasive
#<<<<< FUNCTION ASSUMES ALL PASSED PARAMETERS ARE ALREADY VALIDATED
#Takes row as a list of the chars to works with, the location of the char in the string, and the letter that was placed.
#row = 			['N', 'W', ''B'', 'W', 'N', 'W', 'N']
#Say we insert a 'B' here   ^ at the the relative location of 5
#Would return 	['N', 'W', 'B', 'B', 'B', 'W', 'N']

#Function takes a specific row or list, the location that a piece has been placed, and the turn letter as parameters
#Function then updates the row as if it was horizontal
#Works for "rows" of all sizes
#returns the updated row
		
def updateRow(row, relative_location, turn_letter):
	#Declare all necessary variables that we need to immediately use
	start_convert = False
	row_left = row[:relative_location]
	end_found = False
	que = []
	stop = False
	loop_counter = 0
	
	
	#Row left has to be reveresed so that we can treat it the same way as row right.
	row_left.reverse()
	
	#For loop finds all the valid letters in the specified row and adds them to the que
	#To be a valid letter, the letter must be the inverse turn character,
		#And must have a turn letter on the other side of another inverse turn letter
	
	#There are two main triggers that handle this:
		#stop is a generic preventer that is used to prevent additional characters from being added to the que
		#start_convert marks when to add the character to the que
	for letter in row_left:
		
		if letter == inverseTurnChar(turn_letter) and stop == False:
			start_convert = True
			
		
		if letter == 'N':
			start_convert == False
			stop = True
		
		if letter == turn_letter and loop_counter > 0:
			start_convert = False
			stop = True
			end_found = True
			
			
		#We need to check that the letter beside is not empty, or outside of the board
		#This can be handled simply with the below try - except
		#loop_counter tracks the index of the list
		try:
			if row_left[loop_counter+1] == 'N':
				start_convert = False
			
			
		except:
			start_convert = False
			
		#If the above conditions have been met we can add the letter to the que	
		if start_convert == True and letter == inverseTurnChar(turn_letter):
			que.append(letter)
		
		
		loop_counter = loop_counter +1
		
	
	#Use a different index counter 
	counter = 0
	
	#If the end has been found and the que actually has letters in it, 
	#then we can change the letters in the que and reinsert them back into the row
	
	if end_found == True and len(que) > 0:
		for letter in que:
			row_left[counter] = turn_letter
			counter = counter+1
	
	#Undo the reversal that we did at the start of the code, so it can be safely added back 
	row_left.reverse()
	
	

	#Complete the same process on the righthand side of the row.
	#To do this we reset the variables needed
	
	start_convert = False
	row_right = row[relative_location+1:] 	
	#row_right does not include the actual placed move so we need to add +1 to the relative_location
	
	end_found = False
	que2 = []
	stop = False
	loop_counter = 0
	
	
	
	#Identicle process that used on row_left just with row_right and a different que
	
	for letter in row_right:
		
		if letter == inverseTurnChar(turn_letter) and stop == False:
			start_convert = True
		
		if letter == 'N':
			start_convert == False
			stop = True
		if letter == turn_letter and loop_counter > 0:
			start_convert = False
			end_found = True
			stop = True
		
		try:
			if row_right[loop_counter+1] == 'N':
				start_convert = False
			
			
		except:
			start_convert = False
		
		if start_convert == True and letter == inverseTurnChar(turn_letter):
			que2.append(letter)
		
		loop_counter = loop_counter +1
	
		
		
	
	counter = 0
	if end_found == True and len(que2) > 0:
		for letter in que2:
			row_right[counter] = turn_letter
			counter = counter+1
	
	
	
	
	
	#newRow is what will be returned
	#Combine left and right rows
	new_row = row_left
	#Add the turn letter in the location needed
	new_row.append(turn_letter)
	new_row = new_row + row_right
	
	
	return new_row
	
	
#Updates the board game_state vertically
#Takes the game_state as a 2D list, the relative location, and the turn letter
#Returns the updated list

def updateColumn(game_state, x, y, turn_letter):
	#Create a temporary row of all of ther vertical letters for easy updating
	temp_row = []
	for row in game_state:
		temp_row.append(row[x])
	
	
	#Update the row
	temp_row = updateRow(temp_row, y, turn_letter)
	
	#Using the updated row, change the game_state
	new_game_state = game_state [:]
	loop_count = 0
	
	#loop_count is what tracks where we are in the updated row, and acts as an index
	for row in new_game_state:
		if loop_count < len(temp_row):
			#Update the piece in the location in the game_state
			temp_piece = temp_row[loop_count]
			row[x] = temp_piece
			
			
			#We now need to update the board, so we need a coordinate in the A6 format
			conv_move = convertMoveType(x, loop_count)
			Tx = conv_move[0]
			Ty = conv_move[1] + 1 #Add 1 in order to start counting at 1
		
			#Get the colour of the piece
			if temp_piece != 'N':
				if temp_piece == "B":
					temp_piece = "Black"
				else:
					temp_piece = "White"
				#Place the piece on the board in the appropriate spot
				TurtleMove.placePiece(Tx, Ty, temp_piece)
				
			
		loop_count = loop_count + 1

	return new_game_state
	


#Get the diagnal in the North East direction based on a x, y coordinate on the board
#Takes the game_state as a 2D list, and an x and  y coordinate, (1, 2)
#Returns the diagnal that it finds
	
def getDiagnalNE(game_state, x, y):
	#Declare all necessary variables
	edge_found = False	
	yTracker = y - 1	#We change the x and y coord so that it skips the coordinate given
	xTracker = x + 1	
	diag_row = []
	
	#Until we hit an edge: (when we index a list out of range)
	#We can still incriment the trackers and find more pieces
	while edge_found == False:
		if 0<= yTracker <=7:
			#Find the y coord
			temp_row = game_state[yTracker]
			if 0 <= xTracker <= 7:
				#Find the x coord
				temp_piece = temp_row[xTracker]
				diag_row.append(temp_piece)
			else:
				edge_found = True
		else:
			edge_found = True
			
		#Incriment in the direction desired
		xTracker = xTracker + 1
		yTracker = yTracker - 1
	
	
	
	
	return diag_row
	
	
	
	
#Same as previsou function just with a modified direction

def getDiagnalSW(game_state, x, y):
	edge_found = False	
	yTracker = y + 1
	xTracker = x - 1
	diag_row = []
	while edge_found == False:
		if 0<= yTracker <=7:
			temp_row = game_state[yTracker]
			if 0 <= xTracker <= 7:
				temp_piece = temp_row[xTracker]
				diag_row.append(temp_piece)
			else:
				edge_found = True
		else:
			edge_found = True
			
		xTracker = xTracker - 1
		yTracker = yTracker + 1
	
	diag_row.reverse()
	
	return diag_row
		
#Function updates the board's Up to Down diagnals based on a game_state, move and turn_letter
#Up to down is styled like this:
		#
			#
				#
					#
#Function returns the updates game_state
#The function looks long and painful, but it operates on a similar idea as updateRow and update_column
	#The function starts by getting all characters above the location that is in the diagnol and adds it the row that we can use updateRow on
	#We the then get all the characters below and add it to the row
	#After updating it, we can change the characters using the same way that we found the diagnals

def updateDiagnalDU2(game_state, x, y, turn_letter):
	
	#Get the diagnals in both directions
	left_row = getDiagnalSW(game_state, x, y)
	right_row = getDiagnalNE(game_state, x, y)
	
	#Form the the row that is to updated, and add in the turn_letter
	temp_row = left_row
	temp_row.append(turn_letter)
	temp_row = temp_row + right_row
	
	#find the location of the turn_letter relative to the diagnal, which is needed to update the row
	relative = len(left_row) 
	

	#Update the row
	diag_row = updateRow(temp_row, relative-1, turn_letter)
	
	
	#NE Letter reinsertion
	
	edge_found = False
	xTracker = x 
	yTracker = y
	iteration = relative -1

	#If the x and y trackers are indexes on the board, update the piece to match the diag_row index
	
	for letter in diag_row:
		if 0<= yTracker <=7:
			temp_row = game_state[yTracker]
			if 0 <= xTracker <= 7:
				if 0 <= iteration <= len(diag_row) -1:
					#If all of the above if statements are true, then all indexes are within range
					#Update the piece based on the location in the diag_row
						#and the x and y trackers
					piece = diag_row[iteration]
					temp_row[xTracker] = piece
					game_state[yTracker] = temp_row
					
					#We need to place the piece on the board
					#convert the coords into the appropriate format
					conv_move = convertMoveType(xTracker, yTracker)
					Tx = conv_move[0]
					Ty = conv_move[1]  +1   	#Add 1 to move out of list IDX format
					temp_piece = piece
					
					#Find the piece colour
					if temp_piece != 'N':
						if temp_piece == "B":
							temp_piece = "Black"
						else:
							temp_piece = "White"
						#Place the piece
						TurtleMove.placePiece(Tx, Ty, temp_piece)
						
		#Change the trackers in the desired directions		
		xTracker = xTracker + 1
		yTracker = yTracker - 1
		iteration = iteration +1
	
	
	#We now repeat the same process just in a different direction
	
	edge_found = False
	xTracker = x 
	yTracker = y 
	iteration = relative-1 
	for letter in diag_row:
		if 0<= yTracker <=7:
			temp_row = game_state[yTracker]
			if 0 <= xTracker <= 7:
				if 0<= iteration <= len(diag_row)-1:
					
					piece = diag_row[iteration]
					temp_row[xTracker] = piece
					game_state[yTracker] = temp_row
					
					conv_move = convertMoveType(xTracker, yTracker)
					Tx = conv_move[0]
					Ty = conv_move[1] +1  
					temp_piece = piece
					
					if temp_piece != 'N':
						if temp_piece == "B":
							temp_piece = "Black"
						else:
							temp_piece = "White"
					
						TurtleMove.placePiece(Tx, Ty, temp_piece)	
					
		xTracker = xTracker - 1
		yTracker = yTracker + 1
		iteration = iteration -1
	
	
	return game_state
	
	
#The following code is the same as the other 3 functions just with modified directions	
	
def get_diagnalNW(game_state, x, y):
		
	EdgeFound = False	
	yTracker = y - 1
	xTracker = x - 1
	diag_row = []
	while EdgeFound == False:
		if 0<= yTracker <=7:
			tempRow = game_state[yTracker]
			if 0 <= xTracker <= 7:
				tempPiece = tempRow[xTracker]
				diag_row.append(tempPiece)
			else:
				EdgeFound = True
		else:
			EdgeFound = True
			
		xTracker = xTracker - 1
		yTracker = yTracker - 1
	
	
	
	
	return diag_row
	
def get_diagnalSE(game_state, x, y):
	EdgeFound = False	
	yTracker = y + 1
	xTracker = x + 1
	diag_row = []
	while EdgeFound == False:
		if 0<= yTracker <=7:
			tempRow = game_state[yTracker]
			if 0 <= xTracker <= 7:
				tempPiece = tempRow[xTracker]
				diag_row.append(tempPiece)
			else:
				EdgeFound = True
		else:
			EdgeFound = True
			
		xTracker = xTracker + 1
		yTracker = yTracker + 1
	
	diag_row.reverse()
	
	return diag_row
		
#Function updates the board's Up to Down diagnals based on a game_state, move and turn_letter
#Up to down is styled like this:
					#
				#
			#
		#
#Function returns the updates game_state
#The function looks long and painful, but it operates on a similar idea as updateRow and update_column
	#The function starts by getting all characters above the location that is in the diagnol and adds it the row that we can use updateRow on
	#We the then get all the characters below and add it to the row
	#After updating it, we can change the characters using the same way that we found the diagnals

#Function works the same as the other diagnal updater, just with a modified dirction addition
def update_diagnalUD2(game_state, x, y, turn_letter):
	#print("In DU2")
	#for t in game_state:
#		print(t)
	
	
	
	
	#Get the diagnals in both directions
	leftRow = get_diagnalSE(game_state, x, y)
	rightRow = get_diagnalNW(game_state, x, y)
	
	
	
	print(leftRow, " and ", rightRow)
	
	#Form the the row that is to updated, and add in the turn_letter
	tempRow = leftRow
	tempRow.append(turn_letter)
	tempRow = tempRow + rightRow
	
	
	#This gives us the row where bottom is the left row.
	
	
	#find the location of the turn_letter relative to the diagnal, which is needed to update the row
	relative = len(leftRow) 
	
	print("creates")
	print(tempRow)
	#Update the row
	diagRow = updateRow(tempRow, relative-1, turn_letter)
	print("Using relative of : ", relative)
	print("Is now")
	#diagRow[relative] = turn_letter
	print(diagRow, '\n')
	#NW
	
	EdgeFound = False
	xTracker = x 
	yTracker = y
	iteration = relative -1
	#for t in game_state:
	#	print(t)
	#print("Is now!")
	print(x, y)
	error = False
	for letter in diagRow:
		if 0<= yTracker <=7:
			tempRow = game_state[yTracker]
			if 0 <= xTracker <= 7:
				if 0 <= iteration <= len(diagRow) -1:
					piece = diagRow[iteration]
					tempRow[xTracker] = piece
					game_state[yTracker] = tempRow
					#TurtleMove.placePiece(xTracker, yTracker, turn_letter)
					
					convMove = convertMoveType(xTracker, yTracker)
					Tx = convMove[0]
					Ty = convMove[1] +1  
					tempPiece = piece
					if tempPiece != 'N':
						if tempPiece == "B":
							tempPiece = "Black"
						else:
							tempPiece = "White"
					
						TurtleMove.placePiece(Tx, Ty, tempPiece)
				
				else:
					EdgeFound = True
					
				error = False
			else:
				EdgeFound = True
		else:
			EdgeFound = True
			
		xTracker = xTracker - 1
		yTracker = yTracker - 1
		iteration = iteration +1
	
	#for t in game_state:
	#	print(t)
	
	#SE
	EdgeFound = False
	xTracker = x 
	yTracker = y 
	iteration = relative-1 
	for letter in diagRow:
		if 0<= yTracker <=7:
			tempRow = game_state[yTracker]
			if 0 <= xTracker <= 7:
				if 0<= iteration <= len(diagRow)-1:
					
					piece = diagRow[iteration]
					tempRow[xTracker] = piece
					game_state[yTracker] = tempRow
					
					convMove = convertMoveType(xTracker, yTracker)
					Tx = convMove[0]
					Ty = convMove[1] +1  
					tempPiece = piece
					if tempPiece != 'N':
						if tempPiece == "B":
							tempPiece = "Black"
						else:
							tempPiece = "White"
					
						TurtleMove.placePiece(Tx, Ty, tempPiece)
					#TurtleMove.placePiece(xTracker, yTracker, turn_letter)
				else:
					EdgeFound = True
			else:
				EdgeFound = True
		else:
			EdgeFound = True
			
		xTracker = xTracker + 1
		yTracker = yTracker + 1
		iteration = iteration -1
	
	for c in game_state:
		print(c)
	
	return game_state
	#We now need to update the game_state to match the diag that was just updated

#Function updates the game_state based on a move, that is assumed valid
#Only updates horizontal and vertical, will update diagnol eventually
#Takes the current game_state, the move, and the turn letter
#Returns the updated game_state
def updateGameState(game_state, move, turn_letter):
	#print("HOLY COW!!!!!!!!!!!!!!!!!")
	xy = convertMove(move)
	x = xy[0]-1
	y = xy[1]-1
	#print(x, y)
	tempgame_state = game_state[:]
	#""""
	tempgame_state = updateColumn(game_state, x, y, turn_letter)
	tempRow = updateRow(tempgame_state[y], x, turn_letter)
	tempgame_state[y] = tempRow
	counter = 0
	for i in tempRow:
		
		convMove = convertMoveType(counter, y+1)
		Tx = convMove[0]
		Ty = convMove[1] 
		if i != 'N':
				if i == "B":
					tempPiece = "Black"
				else:
					tempPiece = "White"
				TurtleMove.placePiece(Tx, Ty , tempPiece)
		counter = counter +1
	
	#"""
	
	
	#print("Before Diag")
	tempgame_state = updateDiagnalDU2(tempgame_state, x, y, turn_letter)
	tempgame_state = update_diagnalUD2(game_state, x, y, turn_letter)
	
	finalRow = tempgame_state[y]
	finalRow[x] = turn_letter
	
	tempgame_state[y] = finalRow
	
	n = tempgame_state[y]
	#print(n[x], " was the piece that was placed") 
	return tempgame_state

#Generic test code
#Do not worry about this, it was just used for debugging
def testCode():
	
	row = ['N', 'N', 'N', 'W', 'B', 'N', 'N', 'N']
	#print(row)
	row = updateRow(row, 2, 'B')
	#print(row)
	"""
	print("CHECK HORIZONTAL BASIC::>>>")	
	print("  A    B    C    D    E    F    G    H")
	game_state =         [['W', 'B', 'B', 'B', 'B', 'B', 'B', 'W', ]]  
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	
	for row in game_state:
		print(row)
	print("  ")
	print("  is now  >>>")
	print("  A    B    C    D    E    F    G    H")
		
	game_state = updategame_state(game_state, 'C1', 'W')
	for row in game_state:
		print(row)
	
	
	game_state = []
	print("CHECK VERTICAL BASIC::>>>")
	print(" A    B    C    D    E    F    G    H")
	game_state =         [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'W', ]]  
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'W', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'B', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'B', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'B', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'B', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'W', ]]
	for row in game_state:
		print(row)
	print("  ")
	print("  is now  >>>")
	print(" A    B    C    D    E    F    G    H")
		
	game_state = updategame_state(game_state, 'H2', 'W')
	for row in game_state:
		print(row)
	
	"""
	""""
	game_state = []
	print("CHECK DU DIAGNAL BASIC::>>>")
	print("  A    B    C    D    E    F    G    H")
	game_state =         [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]  
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'W', 'B', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'W', 'W', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'W', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	for row in game_state:
		print(row)
	
	print("  ")
	print("  is now  >>>")
	print(" A    B    C    D    E    F    G    H")
		
	game_state = updategame_state(game_state, 'D6', 'W')
	for row in game_state:
		print(row)
	
	game_state = []
	print("CHECK UD DIAGNAL BASIC BASIC::>>>")
	print(" A    B    C    D    E    F    G    H")
	game_state =         [['B', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]  
	game_state = game_state + [['N', 'W', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'W', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'W', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'B', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'W', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'B', ]]
	for row in game_state:
		print(row)
		
	print("  ")
	print("  is now  >>>")
	print(" A    B    C    D    E    F    G    H")
		
	game_state = updategame_state(game_state, 'D4', 'B')
	for row in game_state:
		print(row)
		
	
	
	
	game_state = []
	print("CHECK UD DIAGNAL BASIC BASIC::>>>")
	print("  A    B    C    D    E    F    G    H")
	game_state =         [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]  
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	for row in game_state:
		print(row)
		
	print("  ")
	print("  is now  >>>")
	print(" A    B    C    D    E    F    G    H")
		
	game_state = updategame_state(game_state, 'A1', 'B')
	for row in game_state:
		print(row)
	
		
	game_state = []
	print("CHECK CUSTOM BASIC BASIC::>>>")
	print("  A    B    C    D    E    F    G    H")
	
	game_state =         [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]  
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'W', 'B', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'B', 'W', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', ]]
	game_state = game_state + [['N', 'N', 'N', 'N', 'N', 'N', 'W', 'N', ]]
	tempCount = 1
	for row in game_state:
		
		print(tempCount, " ", row)
		tempCount = tempCount +1
	
	tempCount = 1
	print("  ")
	print("  is now  >>>")
	
	
	game_state = updategame_state(game_state, 'H8', 'B')
	print("      A    B    C    D    E    F    G    H")
	for row in game_state:
		print(tempCount, " ", row)
		tempCount = tempCount +1
	
	"""
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
	row = updateRow(row, 2, 'B')
	print(row)
	"""
if __name__=="__main__":
	testCode()
