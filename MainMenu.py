#Here we set up the turtle window.

import turtle
wn = turtle.Screen()
wn.setup(1000, 1080)
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
	
def show_rules():
	#Initializes rules list
	
	text.clear()
	text.up()
	text.goto(0, 250)
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
	line = 170
	text.up()
	text.goto(-350, 170)
	text.down()
	#Loop to print rules
	for r in range(len(rules)):
		#Print rule
		
		line = line - 30
		text.write("\n" + str(r + 1) + ") " + rules[r], False, align = "left", font = ("Arial", 10, "normal"))
		text.up()
		text.goto(-350, line)
		text.down()
		
			
	#Ask user if they wish to continue or exit
	option = MenuInput("Press enter to return to the Menu or press any q to quit: ")
		
	quit = "false"
	if option is "q":
		quit = "true"		
		exit()	
	
	#Prints blank line
	return quit
	print()

	
	#This prints out all of the main menu text 
def MainMenu():
	text.clear()
	text.up()
	text.goto(0, 250)
	text.down()
	text.write("RERVERSI GAME", False, align = "center", font = ("Arial", 50, "bold"))
	text.up()
	text.goto(0, 200)
	text.down()
	text.write("1. Play", False, align = "center", font = ("Arial", 10, "normal"))
	text.up()
	text.goto(0, 180)
	text.down()
	text.write("2. Rules", False, align = "center", font = ("Arial", 10, "normal"))
	text.up()
	text.goto(0, 160)
	text.down()
	text.write("3. Exit", False, align = "center", font = ("Arial", 10, "normal"))
	text.up()
	text.goto(0, 130)
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
		text.goto(0, 250)
		text.down()
		text.write("Invalid option. Try Again", False, align = "center", font = ("Arial", 40, "bold"))
		userchoice = "Invalid"
		option = MenuInput("Press enter to return to the Menu or press any q to quit: ")
		
		quit = "false"
		if option is "q":
			quit = "true"		
			exit()
		
	return userchoice
	
def StartMenu():	
	#This loop will not procede until the user either hits play or exit in the menu. 
	#If the user chooses "rules" then they are redirected back to the main menu, so the loop continues
	
	userchoice = MainMenu	
	while userchoice is not "Play":
		text.clear()
		userchoice = MainMenu()
		if userchoice == "quit":
			exit()
			break

StartMenu()
	



#Remember to comment out this exit once this file has been imported
wn.exitonclick()
