#Here we set up the turtle window.
import Constants
import turtle
import time
import TurtleMove

#
#______      ___________    ____  _______ .______          _______. __       _______      ___      .___  ___.  _______
#|   _  \    |   ____\   \  /   / |   ____||   _  \        /       ||  |     /  _____|    /   \     |   \/   | |   ____|
#|  |_)  |   |  |__   \   \/   /  |  |__   |  |_)  |      |   (----`|  |    |  |  __     /  ^  \    |  \  /  | |  |__
#|      /    |   __|   \      /   |   __|  |      /        \   \    |  |    |  | |_ |   /  /_\  \   |  |\/|  | |   __|
#|  |\  \----|  |____   \    /    |  |____ |  |\  \----.----)   |   |  |    |  |__| |  /  _____  \  |  |  |  | |  |____
#| _| `._____|_______|   \__/     |_______|| _| `._____|_______/    |__|     \______| /__/     \__\ |__|  |__| |_______|


#This function accepts and returns a user input in the turtle screen.
def MenuInput(text):
	userinput = Constants.WINDOW.textinput("User Input", text)
	return userinput

def show_rules():
	text = Constants.TURTLE
	#Initializes rules list
	text.clear()
	text.up()
	text.goto(Constants.TITLE_LOCATIONX, Constants.TITLE_LOCATIONY)
	text.down()
	text.write("RERVERSI GAME", False, align = "center", font = ("Arial", 50, "bold"))
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
	line = Constants.RULES_LINESTARTY
	text.up()
	text.goto(Constants.TITLE_LOCATIONX, Constants.RULES_LINESTARTY)
	text.down()
	#Loop to print rules
	firsttime = "true"
	for r in range(len(rules)):
		#Print rule

		line = line - 30
		text.up()
		text.goto(Constants.RULES_LINESTARTX, line)
		text.down()
		text.write("\n" + str(r + 1) + ") " + rules[r], False, align = "left", font = ("Arial", 10, "normal"))
		text.up()
		text.goto(Constants.RULES_LINESTARTX, line)
		text.down()
		#Ask user if they wish to continue
		option = MenuInput("Press enter to continue or q to quit: ")

		quit = "false"
		firsttime = "false"
		if option is "q":
			#Ends loop prematurely
			text.clear()
			text.up()
			text.goto(Constants.TITLE_LOCATIONX, Constants.TITLE_LOCATIONY)
			text.down()
			text.write("RERVERSI GAME", False, align = "center", font = ("Arial", 50, "bold"))
			quit = "true"
			break


	#Prints blank line
	return quit
	print()


	#This prints out all of the main menu text
def MainMenu():
	text = Constants.TURTLE
	text.clear()
	text.up()
	text.goto(Constants.TITLE_LOCATIONX, Constants.TITLE_LOCATIONY)
	text.down()
	text.write("RERVERSI GAME", False, align = "center", font = ("Arial", 50, "bold"))
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
	#Here we accept the user's input and based on it, what the function returns changes.
	userinput = MenuInput("Please enter a menu number:")
	userchoice = "Invalid"
	if userinput == "1":
		userchoice = "Play"
	elif userinput == "2":
		quit = show_rules()
		if quit == "true" :
			userchoice = "return"
	elif userinput == "3":
		userchoice = "quit"

	#If the user makes an invalid choice, then this screen will show up, where it unstucts the uers to make a valid choice.
	else :
		text.clear()
		text.up()
		text.goto(Constants.TITLE_LOCATIONX, Constants.TITLE_LOCATIONY)
		text.down()
		text.write("Invalid option, please choose 1, 2 or 3. Returning to Menu... ", False, align = "center", font = ("Arial", 10, "bold"))
		time.sleep(2)
		text.clear()
		userchoice = "Invalid"


	return userchoice

def StartMenu():
	text = Constants.TURTLE
	#This loop will not procede until the user either hits play or exit in the menu.
	#If the user chooses "rules" then they are redirected back to the main menu, so the loop continues

	userchoice = MainMenu()
	while userchoice != "Play" or userchoice != "quit":
		text.clear()
		print(userchoice)
		if userchoice == "quit":
			exit()
		if userchoice == "Play":
			break
		userchoice = MainMenu()
	if userchoice == "Play":
		TurtleMove.setup()
		TurtleMove.prompt_move()

#Run if main file
if __name__ == "__main__":
	Constants.WINDOW.setup(Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT)
	Constants.WINDOW.setworldcoordinates(0, 0, Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT)
	Constants.WINDOW.clear()
	StartMenu()

#Remember to comment out this exit once this file has been imported
#wn.exitonclick()
