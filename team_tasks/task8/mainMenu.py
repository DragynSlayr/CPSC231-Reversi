#This file has the method, main,
#to show and take input for the main menu
import sys
import constants
import rulesMenu
import main as mainGame

#Moves a turtle to a location without making a line
#Params: turtle, The turtle
#		 x, The x location
#		 y, The y location
#Returns: None
def moveTurtle(turtle, x, y):
	turtle.up()
	turtle.goto(x, y)
	turtle.down()

#Draws a button and labels it
#Params: turtle, The turtle to use for the drawing
#		 x, The x position of the top left of the button
#		 y, The y position of the top left of the button
#		 label, The word to write on the button
#Returns: None
def drawButton(turtle, x, y, label):
	#Store the original line width
	size = turtle.pensize()

	#Change the line width
	turtle.pensize(2)

	#Draw the button
	moveTurtle(turtle, x, y)
	for i in range(2):
		turtle.forward(constants.BUTTON_WIDTH)
		turtle.right(90)
		turtle.forward(constants.BUTTON_HEIGHT)
		turtle.right(90)

	#Move to the center of the button and write a word
	moveTurtle(turtle, x + (constants.BUTTON_WIDTH / 2), y - (constants.BUTTON_HEIGHT * (3/5)))
	turtle.write(label, False, "center", font = ("Arial", 15, "bold"))

	#Change the width to normal
	turtle.pensize(size)

#Draws the main menu
#Params: None
#Returns: None
def showMenu():
	#Get the turtle
	turtle = constants.TURTLE

	#Move to the title location
	turtle.clear()
	moveTurtle(turtle, constants.TITLE_LOCATIONX, constants.TITLE_LOCATIONY)

	#Write the title to the screen
	turtle.write("REVERSI GAME", False, align = "center", font = ("Arial", 50, "bold"))

	#List of options
	options = ["Rules", "Play", "Exit"]

	#Draw all the buttons
	drawButton(turtle, constants.RULES_BUTTON_LEFT_X, constants.BUTTON_TOP_Y, options[0])
	drawButton(turtle, constants.PLAY_BUTTON_LEFT_X, constants.BUTTON_TOP_Y, options[1])
	drawButton(turtle, constants.EXIT_BUTTON_LEFT_X, constants.BUTTON_TOP_Y, options[2])

#Checks if a click is in the button area
#Params: x, The x location of the click
#		 y, The y location of the click
#Returns: True if the click was in the button area, False otherwise
def isButtonClicked(x, y):
	#Check if x and y are within the button area
	x_valid = x >= constants.RULES_BUTTON_LEFT_X and x <= constants.EXIT_BUTTON_RIGHT_X
	y_valid = y >= constants.BUTTON_BOTTOM_Y and y <= constants.BUTTON_TOP_Y

	#Return the result
	return x_valid and y_valid

#Checks if the x is over the rules button
#Params: x, The x location to check
#Returns: True if in the rules button, False otherwise
def isRulesButton(x):
	left_bound = x >= constants.RULES_BUTTON_LEFT_X
	right_bound = x <= constants.RULES_BUTTON_RIGHT_X
	return left_bound and right_bound

#Checks if the x is over the play button
#Params: x, The x location to check
#Returns: True if in the play button, False otherwise
def isPlayButton(x):
	left_bound = x >= constants.PLAY_BUTTON_LEFT_X
	right_bound = x <= constants.PLAY_BUTTON_RIGHT_X
	return left_bound and right_bound

#Checks if the x is over the exit button
#Params: x, The x location to check
#Returns: True if in the exit button, False otherwise
def isExitButton(x):
	left_bound = x >= constants.EXIT_BUTTON_LEFT_X
	right_bound = x <= constants.EXIT_BUTTON_RIGHT_X
	return left_bound and right_bound

#Gets the index of the button that is clicked
#Params: x, The x location of the click
#Returns: The index of the button, -1 if not a button
def getClickedButton(x):
	if isRulesButton(x):
		return 0
	elif isPlayButton(x):
		return 1
	elif isExitButton(x):
		return 2
	else:
		return -1

#Checks if a button is pushed and then responds
#Params: x, The x position of the click
#		 y, The y position of the click
#Return: None
def makeChoice(x, y):
	#Check if a button is pressed
	if isButtonClicked(x, y):
		#Get the index of the clicked button
		button_index = getClickedButton(x)

		#Possible methods corresponding to button
		button_commands = [rulesMenu.show, mainGame.start, sys.exit]

		#Call a method from the list of options
		button_commands[button_index]()

#Function shows the main menu and will show the desired menu
#Function will not continue unless the user press's play
#Returns nothing and takes no parameters
def main():
	#Get the window
	wn = constants.WINDOW

	#Set up the window
	wn.setup(constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT)
	wn.setworldcoordinates(0, 0, constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT)
	wn.clear()
	wn.tracer(constants.FRAME_TO_DRAW)

	#Draw the main menu
	showMenu()

	#Update the window
	wn.update()

	#Allow clicking
	wn.onclick(makeChoice)
	wn.onkey(wn.bye, constants.EXIT_KEY)
	wn.listen()
	wn.mainloop()

#Run if main file
if __name__ == "__main__":
	main()
