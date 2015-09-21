#This is pretty basic code, and will have to modified once the array is finished, but will work for now due to its simplicity.
#Why so many functions for just outputing basic characters? 
#The idea is to have some of these be reused when we switch over to an array based design, that way the code is flexible
#When the array is in place, inputs will have to be added to the functions, as well as a function to process it
#Comments are not finalized, and need to be updated before the assignment is handed in.

#This function is used to prine a letter a certain number of times in a row, which makes it easier to print lines
#It is just a loop that repeatedly prints the letter in question.
def printletter (letter, number_to_print ):
	loopcount = 0
	while loopcount < number_to_print:
		print (letter, end="")
		loopcount = loopcount + 1
		
	return

#This function will print the lines that make up the top and bottom border, which cleans up the actual line printing
def printtop ():
	printletter('-', 12)
	print (" ")
	return

#This is a temporary function that prints a blank line, specifically for the first move. 	
def createline_blank():
	printletter('|', 1)
	printletter(' ', 10)
	printletter('|', 1)
	print (" ")
	return

	
#Using the functions created this creates the unique lines in the middle that contains the 'x' characters and 'O' characters that appear before the first move	
def printstartlines():
	printletter('|', 1)
	printletter(' ', 4)
	printletter('X', 1)
	printletter('O', 1)
	printletter(' ', 4)
	printletter('|', 1)
	print(" ")
	printletter('|', 1)
	printletter(' ', 4)
	printletter('O', 1)
	printletter('X', 1)
	printletter(' ', 4)
	printletter('|', 1)
	print (" ")
	
	return 
#Again, using all the previous functions it very straightforward to print the starting grid.
def printblankgrid ():
	printtop()
	createline_blank()
	createline_blank()
	createline_blank()
	createline_blank()
	printstartlines()
	createline_blank()
	createline_blank()
	createline_blank()
	createline_blank()
	printtop()
	
	return

#Calls the actual function 
printblankgrid ()
	



#This just prevents it from closing right away.
x = input ()

#1111111111
#1000000001
#1000000001
#1000000001
#1000000001
#1000XY0001
#1000YX0001
#1000000001
#1000000001
#1000000001
#1000000001
#1111111111
