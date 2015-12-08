#This file contains methods for writing info to the screen
import constants

#Goes to a postion without drawing a line
#Params: x, The x position to go to
#        y, The y position to go to
#Returns: None
#Author: Inderpreet Dhillon
#Editor: None
def goto(x, y):#TODO Comment this method
    t = constants.TURTLE
    t.up()
    t.goto(x, y)
    t.down()

#Writes a message at the current position
#Params: message, The message to write
#Returns: None
#Notes: Font will be left-justified, bold, Arial in size 20
#Author: Inderpreet Dhillon
#Editor: None
def write(message):
    t = constants.TURTLE
    t.write(message, False, constants.LEFT_TEXT, constants.SCORE_BOARD_TEXT_STYLE)

#Draws a white box at a location
#Params: x, The x coordinate of the location
#        y, The y coordinate of the location
#Returns: None
#Notes: The bax drawn will be 75x75
#Author: Inderpreet Dhillon
#Editor: None
def clearArea(x, y):
    t = constants.TURTLE
    t.up()
    t.fillcolor(constants.PLAY_SCREEN_BG_COLOR)

    #Draw a filled box
    t.begin_fill()
    for i in range(4):
        t.forward(75)
        t.right(90)
    t.end_fill()

    t.down()

#Writes the current score to the screen
#Params: black, Black's current score
#        white, White's current score
#Returns: None
#Author: Inderpreet Dhillon
#Editor: None
def writeScore(black, white):
    #Store the starting position so the turtle can return there later
    starting_X, starting_y = constants.TURTLE.pos()

    #Go to Black's area and draw their score
    goto(constants.BLACK_SCORE_X, constants.BLACK_SCORE_Y)
    clearArea(constants.BLACK_SCORE_X, constants.BLACK_SCORE_Y)
    write(constants.SCORE_TITLE_BLACK + str(black))

    #Go to White's area and draw their score
    goto(constants.WHITE_SCORE_X, constants.WHITE_SCORE_Y)
    clearArea(constants.WHITE_SCORE_X, constants.WHITE_SCORE_Y)
    write(constants.SCORE_TITLE_WHITE + str(white))

    #Return to starting position
    goto(starting_X, starting_y)

#Writes the turn number on the game board in the bottom left corner.
#Parameters: The turn number
#Returns: None
#Author: Kyle Hinton
#Editor: None
def writeTurn(turn_num):
    starting_x, starting_y = constants.TURTLE.pos()
    goto(25, 25)
    clearArea(25, 25)
#    clearArea(25, 100)
    if int(turn_num) % 2 == 0:
        current_turn = constants.PIECE_COLOR_WHITE
    else:
        current_turn = constants.PIECE_COLOR_BLACK

    write(constants.TURN_STRING + str(turn_num))
    goto(25, 100)
    clearArea(25, 100)
    write(constants.TURN_COLOUR_STRING + current_turn)

    goto(starting_x, starting_y)


#Writes a message to the bottom of the screen
#Params: message, The message to write
#Returns: None
#Author: Inderpreet Dhillon
#Editor: None
def writeMessage(message):
    #Store starting location for later use
    starting_X, starting_y = constants.TURTLE.pos()

    #Move to message are and display message
    goto(constants.MESSAGE_X, constants.MESSAGE_Y)
    write(message)

    #Return to starting area
    goto(starting_X, starting_y)

#Prints an error message
#Params: None
#Returns: None
#Author: Inderpreet Dhillon
#Editor: None
def noButtonError():
    writeMessage(constants.BUTTON_ERROR_MESSAGE)
