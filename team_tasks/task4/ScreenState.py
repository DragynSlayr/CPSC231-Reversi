#Let 0 be an exmpty square
#let b be a black square
#let w be a white circle
#let x signal the end of a line
#each line should contain no more than 10 character spots 



#returns a string that represents the Grid State at the beginning
def initialize_grid_string():
	
	lines = []
	GridState = ''
	#Add each of the lines representing the gird to the list
	lines.append( '00000000')
	lines.append( '00000000')
	lines.append('00000000')
	lines.append( '000BW000')
	lines.append( '000WB000')
	lines.append( '00000000')
	lines.append('00000000')
	lines.append( '00000000')
	
	
	linetotal = len(lines)
	loopcount = 0
	
	#each run of the loop adds the element of the list to a string 
	while loopcount != linetotal:
		GridState = GridState + 'x' + lines[loopcount]
		loopcount = loopcount+1
	GridState = GridState + 'x'
	#Loop ends when all of the lines have been added to the string

	return GridState

	
#Converts a string gridstate into a list of lists
def convert_string_to_list(gridState):
	if len(gridState) >73:
		print ("Error, convert_string_to_list gridState too long")
		print(len(gridState))
	if len(gridState) < 73:
		print("Error, convert_string_to_list gridState too short")
		print(len(gridState))
	#Declare all of the necessary lists
	
	GridList = []
	line1 = []
	line2 = []
	line3 = []
	line4 = []
	line5 = []
	line6 = []
	line7 = []
	line8 = []
	
	
	#add each line list 

	GridList.append(line1)
	GridList.append(line2)
	GridList.append(line3)
	GridList.append(line4)
	GridList.append(line5)
	GridList.append(line6)
	GridList.append(line7)
	GridList.append(line8)
	
	
	#these variables all the for loop to change which list is being used
	lineChoiceIncrease = 0
	lineChoice = GridList[lineChoiceIncrease]
	
	#for each letter in the string parameter
	
	for letter in gridState:
		
		if letter == 'x':
			#if the letter is x then switch the line list that the letter ie being added to
			lineChoiceIncrease += lineChoiceIncrease
			lineChoice = GridList[lineChoiceIncrease]
		
			
		if letter != 'x':
			#if the letter is regular then add it to the list
			lineChoice.append(letter)
	
	
	#Returns the list
	return GridList
	
	
	
#Function takes a list parameter, and then converts the list of lines into a string
def convert_grid_list_to_string(GridStateList):
	#Declare letter, which tracks which letter we are using in the list
	letter = 0
	
	#Declare a variable which will store the string
		#Variable is assigned 'x' in order to mark that this is the first line that characters are added to 
	GridStateString = 'x'
	
	
	for line in GridStateList:
		#And for each element in the line list
		
		for location in line:
			#add the character to the string
			GridStateString = GridStateString + location
			
		 
			letter = letter+1
			
			if letter >=8:
				#Mark the change of line with an 'x'
				GridStateString =GridStateString +'x' 
				
				#Then reset this counter
				letter = 0
			
	return GridStateString
	
	
print(convert_grid_list_to_string(convert_string_to_list(initialize_grid_string())))
print("x00000000xbwbw000bx000000bwx00bwbwwbxb000ww00x00000000x00000000x00000000x")
print(convert_grid_list_to_string(convert_string_to_list('x00000000xbwbw000bx000000bwx00bwbwwbxb000ww00x00000000x00000000x00000000x')))

