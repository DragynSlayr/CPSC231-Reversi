#Added my List Manager. Has a couple different functions in it. It can prep a token by adding the 'x' markers, convert that to a list of lists, and convert it back into a string.


#Let N be an exmpty square
#let B be a black square
#let W be a white circle
#let x signal the end of a line
#each line should contain no more than 10 character spots, 8 characters plus the two 'x's to mark the start and end of each line
 
 
 
#function adds the line markers - the 'x' - into the string token. 
def prep_token(token):
	count = 1
	updated_token = "x"
	for letter in token:
		if count <=8:
			updated_token = updated_token + letter
		else:
			updated_token = updated_token + 'x' + letter
			count = 1
		count = count +1
	updated_token = updated_token + 'x'
	
	return updated_token
			


#returns a string that represents the token State at the beginning
def initialize_token_string():
	
	lines = []
	tokenState = ''
	#Add each of the lines representing the gird to the list
	lines.append( 'NNNNNNNN')
	lines.append( 'NNNNNNNN')
	lines.append('NNNNNNNN')
	lines.append( 'NNNBWNNN')
	lines.append( 'NNNWBNNN')
	lines.append( 'NNNNNNNN')
	lines.append('NNNNNNNN')
	lines.append( 'NNNNNNNN')
	
	
	linetotal = len(lines)
	loopcount = 0
	
	#each run of the loop adds the element of the list to a string 
	while loopcount != linetotal:
		tokenState = tokenState + 'x' + lines[loopcount]
		loopcount = loopcount+1
	tokenState = tokenState + 'x'
	#Loop ends when all of the lines have been added to the string

	return tokenState

	
#Converts a string tokenstate into a list of lists
def convert_string_to_list(tokenState):
	if len(tokenState) >73:
		print ("Error, convert_string_to_list tokenState too long")
		print(len(tokenState))
	if len(tokenState) < 73:
		print("Error, convert_string_to_list tokenState too short")
		print(len(tokenState))
	#Declare all of the necessary lists
	
	tokenList = []
	line1 = []
	line2 = []
	line3 = []
	line4 = []
	line5 = []
	line6 = []
	line7 = []
	line8 = []
	
	
	#add each line list 

	tokenList.append(line1)
	tokenList.append(line2)
	tokenList.append(line3)
	tokenList.append(line4)
	tokenList.append(line5)
	tokenList.append(line6)
	tokenList.append(line7)
	tokenList.append(line8)
	
	
	#these variables are all for the for loop to change which list is being used
	lineChoiceIncrease = 0
	lineChoice = tokenList[lineChoiceIncrease]
	
	#for each letter in the string parameter
	
	for letter in tokenState:
		
		if letter == 'x':
			#if the letter is x then switch the line list that the letter ie being added to
			lineChoiceIncrease += lineChoiceIncrease
			lineChoice = tokenList[lineChoiceIncrease]
		
			
		if letter != 'x':
			#if the letter is regular then add it to the list
			lineChoice.append(letter)
	
	
	#Returns the list
	return tokenList
	
	
	
#Function takes a list parameter, and then converts the list of lines into a string
def convert_token_list_to_string(tokenStateList):
	#Declare letter, which tracks which letter we are using in the list
	letter = 0
	
	#Declare a variable which will store the string
		#Variable is assigned 'x' in order to mark that this is the first line that characters are added to 
	tokenStateString = 'x'
	
	
	for line in tokenStateList:
		#And for each element in the line list
		
		for location in line:
			#add the character to the string
			tokenStateString = tokenStateString + location
			
		 
			letter = letter+1
			
			if letter >=8:
				#Mark the change of line with an 'x'
				tokenStateString =tokenStateString +'x' 
				
				#Then reset this counter
				letter = 0
			
	return tokenStateString
	

	
#Removes all of the 'x's from a token	
def clean_token(token):
	updated_token = ""
	for letter in token:
		if letter != 'x':
			updated_token = updated_token + letter
	return updated_token
	
print(prep_token('NNNNNNNNBWBWNNNBNNNNNNBWNNBWBWWBBNNNWWNNNNNNNNNNNNNNNNNNNNNNNNNN'))
print(convert_token_list_to_string(convert_string_to_list(initialize_token_string())))
print("xNNNNNNNNxBWBWNNNbxNNNNNNBWxNNBwBWWBxBNNNWWNNxNNNNNNNNxNNNNNNNNxNNNNNNNNx")
print(convert_token_list_to_string(convert_string_to_list('xNNNNNNNNxBWBWNNNbxNNNNNNBWxNNBwBWWBxBNNNWWNNxNNNNNNNNxNNNNNNNNxNNNNNNNNx')))

