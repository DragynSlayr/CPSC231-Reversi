#This is pretty basic code, and will have to modified once the array is finished, but will work for now due to its simplicity.
#Why so many functions for just outputing basic characters?
#The idea is to have some of these be reused when we switch over to an array based design, that way the code is flexible
#When the array is in place, inputs will have to be added to the functions, as well as a function to process it
#Comments are not finalized, and need to be updated before the assignment is handed in.

#This function is used to prine a letter a certain number of times in a row, which makes it easier to print lines
#It is just a loop that repeatedly prints the letter in question.
def printletter (letter, number_to_print ):
	for i in range(number_to_print):
		print (letter, end="")

#This function will print the lines that make up the top and bottom border, which cleans up the actual line printing
def printtop ():
	printletter('+-', 1)
	for i in range(8):
		print("+", end="")
		printletter("-", 3)
	print("+")

#This is a temporary function that prints a blank line, specifically for the first move.
def createline_blank(row_num):
	print("|" + str(row_num) + "|", end="")
	for i in range(8):
		printletter(' ', 3)
		printletter('|', 1)
	print()

#Using the functions created this creates the unique lines in the middle that contains the 'x' characters and 'O' characters that appear before the first move
def printstartlines(flipped):
	if not flipped:
		print("|4|", end="")
		for i in range(3):
			printletter(" ", 3)
			printletter("|", 1)
		print(" X | O |", end="")
		for i in range(3):
			printletter(" ", 3)
			printletter("|", 1)
	else:
		print("|5|", end="")
		for i in range(3):
			printletter(" ", 3)
			printletter("|", 1)
		print(" O | X |", end="")
		for i in range(3):
			printletter(" ", 3)
			printletter("|", 1)
	print()

#Print the row of letters at the top of the grid
def printletterrow():
	print("| ", end="")
	for i in ["A", "B", "C", "D", "E", "F", "G", "H"]:
		print("| " + i + " ", end="")
		if i is "H":
			print("|", end="")
	print()

#Again, using all the previous functions it very straightforward to print the starting grid.
def printblankgrid ():
	print()
	printtop()
	printletterrow()
	printtop()
	for i in range(1, 9):
		if i is 4 or i is 5:
			printstartlines(i is 5)
		else:
			createline_blank(i)
		printtop()

printblankgrid()
