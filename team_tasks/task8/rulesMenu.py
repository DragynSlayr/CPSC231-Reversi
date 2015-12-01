#This file has methods to show the rules
import constants
import mainMenu

#Displays the rules
#Params: None
#Returns: None
def displayRules():
    #Get the window and turtle
    turtle = constants.TURTLE

	#Create a list for holding the rules
    rules = []
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
    line = constants.RULES_LINESTARTY
    mainMenu.moveTurtle(turtle, constants.TITLE_LOCATIONX, constants.RULES_LINESTARTY)

	#Go through the rules list
    for r in range(len(rules)):
        #Each loop moves the next rule down 30 units
        line -= 55

        #Move the turtle
        mainMenu.moveTurtle(turtle, constants.RULES_LINESTARTX, line)

        #Format the line
        rule = "\n" + str(r + 1) + ") " + rules[r]

        #Draw the rule
        turtle.write(rule, False, align = "left", font = ("Arial", 10, "normal"))

        #Move back to the start of the line
        mainMenu.moveTurtle(turtle, constants.RULES_LINESTARTX, line)

    #Draw a button
    mainMenu.drawButton(turtle, constants.BACK_BUTTON_LEFT_X, constants.BACK_BUTTON_TOP_Y, "Back")

def isBackClicked(x, y):
    #Check x and y separately
    x_valid = x >= constants.BACK_BUTTON_LEFT_X and x <= constants.BACK_BUTTON_RIGHT_X
    y_valid = y >= constants.BACK_BUTTON_BOTTOM_Y and y <= constants.BACK_BUTTON_TOP_Y

    #Return the result
    return x_valid and y_valid

#Responds to clicks
#Params: x, The x location of the click
#        y, The y location of the click
#Returns: None
def checkClicks(x, y):
    #Check if the back button was clicked
    if isBackClicked(x, y):
        mainMenu.main()

def show():
    #Setup the window
    wn = constants.WINDOW
    wn.clear()
    wn.tracer(constants.FRAME_TO_DRAW)

    #Show the rules
    displayRules()

    #Update the window
    wn.update()

	#Allow clicking
    wn.onclick(checkClicks)
    wn.onkey(wn.bye, constants.EXIT_KEY)
    wn.listen()
    wn.mainloop()
