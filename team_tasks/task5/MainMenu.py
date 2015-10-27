import Constants
import turtle
import time
import TurtleMove


#This function prompts a user for an input
#Only parameter is the text that is to be displayed with the prompt
#Returns the user's unput
def inputRequest(text):
	wn = Constants.WINDOW
	user_input = wn.textinput("User Input", text)
	return user_input

	
#Function displays the rules on the window
#The user is given the option to quit or return to the main menu
#Returns nothing and takes no parameters
def displayRules():
	text = Constants.TURTLE
	#Initializes rules list

	text.clear()
	text.up()
	text.goto(Constants.TITLE_LOCATIONX, Constants.TITLE_LOCATIONY)
	text.down()
	text.write("REVERSI GAME", False, align = "center", font = ("Arial", 50, "bold"))

	#Creates a list called rules, which is emppty for now
	rules = []

	#Add rules to list
	rules.append("Reversi is a 2 player game that is played on an 8 x 8 grid. \n \n")
	rules.append("The game discs have both a black and white side. \n \n")
	rules.append("To win you have to have the majority of the discs changed to your color at the end of the game. \n \n")
	rules.append("The game ends when there are no more possible moves to make. \n \n ")
	rules.append("The game can end before the entire grid is filled. \n \n ")
	rules.append("Players take turns placing discs, with their color facing up. \n \n ")
	rules.append("When a player places a disk on the board, all the pieces that are between that player's newly placed disc \n and any of their previously placed discs, are turned to that player's color. \n")
	rules.append("When placing your discs on your turn, there has to be at least one piece of the opposite colour between \n your placed piece and any of your previously placed pieces. Otherwise the move is not valid. ")
	rules.append("The placed pieces have to make either a horizontal, vertical or diagonal line with the opposing player's discs to flip any pieces over.")

	#Move the turtle to the appropriate location for the rules output
	line = Constants.RULES_LINESTARTY
	text.up()
	text.goto(Constants.TITLE_LOCATIONX, Constants.RULES_LINESTARTY)
	text.down()



	#Loops for the number of rules in the list, which is what the len() function returns
	for r in range(len(rules)):
		#Print rules


		#Each loop moves the next rule down 30 units
		line = line - 30

		text.up()
		text.goto(Constants.RULES_LINESTARTX, line)
		text.down()

		#The next line will print the rules
		#We use \n to ensure it starts a new line
		#str(r+1) is the number of the rule that is getting printed, ex				 1) "reversi...."
		#False denotes whether or not the turtle is moveable
		text.write("\n" + str(r + 1) + ") " + rules[r], False, align = "left", font = ("Arial", 10, "normal"))

		text.up()
		text.goto(Constants.RULES_LINESTARTX, line)
		text.down()


	#If the user choices 3, then the program will exit.
	user_choice = inputRequest("Press any key to return, or press '3' to quit.")
	if user_choice == '3' :
		exit()





#This prints out all of the main menu text
#Takes no parameters
#Returns the user's choice
def mainMenu():
	#For each of he text.write methods, False denotes whether or not the turtle is moveable
	text = Constants.TURTLE
	text.clear()
	text.up()
	text.goto(Constants.TITLE_LOCATIONX, Constants.TITLE_LOCATIONY)
	text.down()
	text.write("REVERSI GAME", False, align = "center", font = ("Arial", 50, "bold"))
	text.up()
	text.goto(Constants.TITLE_LOCATIONX, Constants.RULES_LIST)
	text.down()
	text.write("1. Play", False, align = "center", font = ("Arial", 10, "normal"))
	text.up()
	text.goto(Constants.TITLE_LOCATIONX, Constants.RULES_LIST-20)
	text.down()
	text.write("2. Rules", False, align = "center", font = ("Arial", 10, "normal"))
	text.up()
	text.goto(Constants.TITLE_LOCATIONX, Constants.RULES_LIST-40)
	text.down()
	text.write("3. Exit", False, align = "center", font = ("Arial", 10, "normal"))
	text.up()
	text.goto(Constants.TITLE_LOCATIONX, Constants.RULES_LIST-60)
	text.down()

	#Here the user makes an input, which is what the function returns
	menu_choice = inputRequest("Please make a choice:")
	return menu_choice


#Function displays the 'Invalid Choice' screen, and then waits a second
#Takes no parameters and returns nothing
def invalidChoice():
	text = Constants.TURTLE
	text.clear()
	text.up()
	text.goto(Constants.TITLE_LOCATIONX, Constants.TITLE_LOCATIONY)
	text.down()
	text.write("Invalid Choice", False, align = "center", font = ("Arial", 50, "bold"))
	#Wait one second then continue
	time.sleep(1)

#Function shows the main menu and will show the desired menu
#Function will not continue unless the user press's play
#Returns nothin and takes no parameters	
def main():
	Constants.WINDOW.setup(Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT)
	Constants.WINDOW.setworldcoordinates(0, 0, Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT)
	Constants.WINDOW.clear()

	#Declare the variable that is used to end the loop
	end_loop = False

	#This loop will always loop back to the main menu, prompting the user for a choice until they press play, or exit.
	while end_loop == False :
		#We declare user_in_rules to be False, which will prevent the ""invalidChoice"" functioning from running when the user presses 'any key' in the rules.
		user_in_rules= False

		#We get the user's choice
		user_choice = mainMenu()
		if user_choice == '1' :
			#User wants to play!
			#Here we set up the board and prompt them for a move


			#So we must end the loop
			end_loop = True
		else:
			#Check if the user wannts to see the rules or quit
			if user_choice == '2' :
				displayRules()

				#update user_in_rules to prevent the invalidChoice function from running in line
				user_in_rules= True

			if user_choice == '3':
				#The user sucks and wants to quit
				exit()
		#Here we check if the user made a valid choice and dsiplay the appropriate text if they did not.
		if user_choice is not '1' or '2' or '3':
			#This if statement will prevent invalidChoice from running when the user is viewing the rules
			if user_in_rules==False:
				if end_loop == False:
					invalidChoice()




#Run if main file
if __name__ == "__main__":
	main()

