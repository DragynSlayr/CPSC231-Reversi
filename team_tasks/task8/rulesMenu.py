#This file has methods to show the rules
import constants
import mainMenu

#Displays the rules
#Params: None
#Returns: None
def displayRules():
    #Get the window and turtle
    turtle = constants.TURTLE

	#Get the rules list
    rules = constants.RULES

	#Move the turtle to the appropriate location for the rules output
    rule_y = constants.RULES_LINESTARTY
    mainMenu.moveTurtle(turtle, constants.TITLE_LOCATIONX, constants.RULES_LINESTARTY)

	#Go through the rules list
    for r in range(len(rules)):
        #Move the turtle
        mainMenu.moveTurtle(turtle, constants.RULES_LINESTARTX, rule_y)

        #Format the line
        rule = '\n' + str(r + 1) + ') ' + rules[r]

        #Draw the rule
        turtle.write(rule, False, constants.LEFT_TEXT, constants.RULES_TEXT_STYLE)

        #Each loop moves the next rule down
        rule_y -= constants.RULES_SHIFT

    #Draw a button
    mainMenu.drawButton(turtle, constants.BACK_BUTTON_LEFT_X, constants.BACK_BUTTON_TOP_Y, constants.RULES_OPTION)

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
        #Go back to the main menu
        mainMenu.main()

#Shows the rules
#Params: None
#Returns: None
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
