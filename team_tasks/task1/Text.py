def show_art():
	print(""".______      ___________    ____  _______ .______          _______. __       _______      ___      .___  ___.  _______
|   _  \    |   ____\   \  /   / |   ____||   _  \        /       ||  |     /  _____|    /   \     |   \/   | |   ____|
|  |_)  |   |  |__   \   \/   /  |  |__   |  |_)  |      |   (----`|  |    |  |  __     /  ^  \    |  \  /  | |  |__
|      /    |   __|   \      /   |   __|  |      /        \   \    |  |    |  | |_ |   /  /_\  \   |  |\/|  | |   __|
|  |\  \----|  |____   \    /    |  |____ |  |\  \----.----)   |   |  |    |  |__| |  /  _____  \  |  |  |  | |  |____
| _| `._____|_______|   \__/     |_______|| _| `._____|_______/    |__|     \______| /__/     \__\ |__|  |__| |_______|""")
	
def show_rules():
	#Initializes rules list
	rules = []
	
	#Add rules to list
	rules.append("Reversi is a 2 player game that is played on an 8 x 8 grid.")
	rules.append("The game discs have both a black and white side.")
	rules.append("To win you have to have the majority of the discs changed to your color at the end of the game.")
	rules.append("The game ends when there are no more possible moves to make.")
	rules.append("The game can end before the entire grid is filled.")
	rules.append("Players take turns placing discs, with their color facing up.")
	rules.append("When a player places a disk on the board, all the pieces that are between that player's newly placed disc and any of their previously placed discs, are turned to that player's color.")
	rules.append("When placing your discs on your turn, there has to be at least one piece of the opposite colour between your placed piece and any of your previously placed pieces. Otherwise the move is not valid.")
	rules.append("A move is only valid if one of the opposing player's discs are flipped over, otherwise the turn is passed to the opposing player.")
	rules.append("The placed pieces have to make either a horizontal, vertical or diagonal line with the opposing player's discs to flip any pieces over.")

	#Loop to print rules
	for r in range(len(rules)):
		#Print rule
		print("\n" + str(r + 1) + ") " + rules[r])
		
		#Ask user if they wish to continue
		option = input("Press enter to continue or q to quit: ")

		if option is "q":
			#Ends loop prematurely
			break
			
	#Prints blank line
	print()
