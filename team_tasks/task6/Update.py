import ScreenState 
import TurtleMove
 
def inverseTurnChar(char):
	if char== 'W':
		return 'B'
	elif char == 'B':
		return 'W'
	else:
		return 'Error Invalid Param'




token = 'NNNBWWWW' +'WWBWWWBN' + 'NNNNNNNN' + 'BWWBWWWB'+  'NNNNNNNN' + 'NNNNNNNN' 'NNNNNNNN' + 'NNNNNNNN'
		#01234567    89012345	  67890123	   45678901 	23456789 	 01234567	89012345	 67890123
		#0			 1			  2 		   3    		4  			 5 			6			 7
#Note token index starts at 0
#Formula for calculating char location:
#7+8y + x 



def UpdateHorizontal(turn_letter, location, token):
	tempToken = ScreenState.prep_token(token) 
	tempToken = ScreenState.convert_string_to_list(tempToken)
	XY = TurtleMove.getColumnAndRow(location)
	x = XY[0]
	y = XY[1]
	#print(tempToken)
	
	horizontal = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
	counter = 0
	for letter in horizontal:
		if x == letter:
			rowIDX = counter
		else:
			counter = counter+1
	
	#print(rowIDX)
	#print(tempToken)
	row = tempToken[rowIDX] 
	print (row)
	
	
UpdateHorizontal("null", "A2", token)
	
		

""""
def UpdateHorizontal(turn_letter, letter_location, token, recursive):
	
	direction = -1
	if recursive == True:
		direction = 1
	
	turnletter = turn_letter
	letter = letter_location
	letteridx = letter +direction
	counter = 0
	End = False
	loop = 0
	#Check line
	
	while token[letteridx] == turnletter and End == False:
		#print("letter index is:", letteridx)
		if recursive == True:
			print (letteridx)
			if letteridx+1 % 8 == 0:
				End = True
				counter = 0
		if letteridx % 8 == 0:
			End = True
			counter = 0
		elif End == False:
			counter = counter +1
		letteridx = letteridx + direction
	
	print (letteridx)
	print(counter)
	print(letter_location)
	if recursive == True:
		NewToken = token[:letter_location + counter] + (inverseTurnChar(turnletter)) * (counter) + token[letter_location:]
	else:
		NewToken = token[:letter_location - counter] + (inverseTurnChar(turnletter)) * (counter) + token[letter_location - counter:]
		
	
	#print(token[:letteridx], " + ", (inverseTurnChar(turnletter)) * (counter), " + ", token[letteridx + counter+1 :])
	print (token)
	print(NewToken)
	if recursive == False:
		UpdateHorizontal(turn_letter, letter_location, NewToken, True)
	
	return NewToken
		

'''
print (counter)

#string assembly loop:

'''
UpdateHorizontal('W', 27, token, False)
"""