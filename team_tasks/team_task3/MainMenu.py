#Here we set up the turtle window.
import Constants
import turtle
import time
import TurtleMove

#These variables and constants are global
wn = Constants.WINDOW
text = turtle.Turtle()
wn.setup(Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT)
wn.setworldcoordinates(0, 0, Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT)
wn = turtle.Screen()
text = turtle.Turtle()
wn.clear()

#
#______      ___________    ____  _______ .______          _______. __       _______      ___      .___  ___.  _______
#|   _  \    |   ____\   \  /   / |   ____||   _  \        /       ||  |     /  _____|    /   \     |   \/   | |   ____|
#|  |_)  |   |  |__   \   \/   /  |  |__   |  |_)  |      |   (----`|  |    |  |  __     /  ^  \    |  \  /  | |  |__
#|      /    |   __|   \      /   |   __|  |      /        \   \    |  |    |  | |_ |   /  /_\  \   |  |\/|  | |   __|
#|  |\  \----|  |____   \    /    |  |____ |  |\  \----.----)   |   |  |    |  |__| |  /  _____  \  |  |  |  | |  |____
#| _| `._____|_______|   \__/     |_______|| _| `._____|_______/    |__|     \______| /__/     \__\ |__|  |__| |_______|



#This function accepts and returns a user input in the turtle screen.
def MenuInput(text):
	userinput = wn.textinput("User Input", text)
	return userinput
	
def MenuRules():
	#Here we print the title of the game again, after we clear the previous menu.
	text.clear()
	text.up()
	text.goto(constants.TITLE_LOCATIONX, constants.TITLE_LOCATIONY)
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
	line = constants.RULES_LINESTARTY
	text.up()
	text.goto(constants.TITLE_LOCATIONX, constants.RULES_LINESTARTY)
	
	text.down()
	#Loop to print rules
	firsttime = "true"
	for r in range(len(rules)):
		#Print rule
		
		line = line - 30
		text.up()
		text.goto(constants.RULES_LINESTARTX, line)
		text.down()
		text.write("\n" + str(r + 1) + ") " + rules[r], False, align = "left", font = ("Arial", 10, "normal"))
		text.up()
		text.goto(constants.RULES_LINESTARTX, line)
		text.down()
	
	RulesChoice = MenuInput("Press any key to return, or press '3' to quit.")
	if RulesChoice == '3' :
		exit()
	
def MainMenu():
	#We now print all of the menu text
	text.clear()
	text.up()
	text.goto(constants.TITLE_LOCATIONX, constants.TITLE_LOCATIONY)
	text.down()
	text.write("RERVERSI GAME", False, align = "center", font = ("Arial", 50, "bold"))
	text.up()
	text.goto(constants.TITLE_LOCATIONX, constants.RULES_LIST)
	text.down()
	text.write("1. Play", False, align = "center", font = ("Arial", 10, "normal"))
	text.up()
	text.goto(constants.TITLE_LOCATIONX, constants.RULES_LIST-20)
	text.down()
	text.write("2. Rules", False, align = "center", font = ("Arial", 10, "normal"))
	text.up()
	text.goto(constants.TITLE_LOCATIONX, constants.RULES_LIST-40)
	text.down()
	text.write("3. Exit", False, align = "center", font = ("Arial", 10, "normal"))
	text.up()
	text.goto(constants.TITLE_LOCATIONX, constants.RULES_LIST-60)
	text.down()
	#And then we take the user's choice
	MenuChoice = MenuInput("Please make a choice:")
	return MenuChoice
	

def InvalidChoice():
	#If the user makes an invalid choice then it prints out this screen:
	text.clear()
	text.up()
	text.goto(constants.TITLE_LOCATIONX, constants.TITLE_LOCATIONY)
	text.down()
	text.write("Invalid Choice", False, align = "center", font = ("Arial", 50, "bold"))
	#Delay it by one second
	time.sleep(1)
	

def main():
	
	while 0 < 1 :
		#If the user chooses play, break the loop and start the game
		UserChoice = MainMenu()
		if UserChoice == '1' :
			break
			TurtleMove.setup()
			TurtleMove.prompt_move()
		else:
			#other wise print the rules, or show the invalid choice screen
			if UserChoice == '2' :
				MenuRules()
			if UserChoice == '3':
				exit()
			InvalidChoice()
		

#Run if main file
if __name__ == "__main__":
	StartMenu()

#Remember to comment out this exit once this file has been imported

