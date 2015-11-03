import Constants
import TurtleMove
import StringInterpret
import StringMove
import VictoryStatus
import PlayerVictory
import FileHandler
import random

#Converts an x coordinate to a cell on the board
#Params: x, The x coordinate
#Returns: An index of the x coordinate of a cell
def convertXToBoard(x):
    x = (x / Constants.CELL_WIDTH) - Constants.OFFSET_OF_COLUMNS
    return int(x)

#Converts a y coordinate to a cell on the board
#Params: y, The y coordinate
#Returns: An index of the y coordinate of a cell
def convertYToBoard(y):
    y = (y / Constants.CELL_HEIGHT) - Constants.OFFSET_OF_ROWS
    return int(y)

#Checks if a piece can be placed at a location
#Params: x, The x coordinate of the location
#        y, The y coordinate of the location
#Returns: True if a piece can be placed at a location, False otherwise
def isValidSquare(x, y):
    #Check if each coordinate is valid separately
    xValid = x >= Constants.LEFT_MOST_X and x <= Constants.RIGHT_MOST_X
    yValid = y >= Constants.BOTTOM_MOST_Y and y <= Constants.TOP_MOST_Y

    #Check if the x and y are in any cell
    return xValid and yValid

#Gets a random letter between A-H
#Params: None
#Returns: A letter from A-H
def getRandomLetter():
    return Constants.COLUMN_LETTERS[random.randrange(Constants.NUM_OF_COLUMNS)]

#Gets a random number between 1-8
#Params: None
#Returns: A number from 1-8
def getRandomNumber():
    return Constants.ROW_NUMBERS[random.randrange(Constants.NUM_OF_ROWS)]

#The computer generates a move and places a piece if possible
#Params: state, The current game state
#        move_num, The current move number
#Returns: The new game state
def computerTurn(state, move_num):
    #Generate a letter and number
    letter = getRandomLetter()
    number = getRandomNumber()

    #Generate move until one is valid
    while not StringMove.validateMoveLocation(state, letter + str(number)):
        letter = getRandomLetter()
        number = getRandomNumber()

    #Place piece and return state
    return StringInterpret.stringInterpret(state, letter + str(number), move_num)

#Places a piece at a location if it is a cell
#Params: x, The x location to check
#        y, The y location to check
#Returns: None
def place_piece(x, y):
    #Load the variables we need
    game_state = FileHandler.loadVariable("State")
    move_num = int(FileHandler.loadVariable("Move"))
    #Make sure the game is not over
    if VictoryStatus.endGameStatus(game_state) != True:
        #Check if the point is valid
        if isValidSquare(x, y):
            #Convert the x and y to the coordinate of a cell
            x = convertXToBoard(x)
            y = convertYToBoard(y)

            #Convert x and y to column and row
            letter = Constants.COLUMN_LETTERS[x]
            number = Constants.ROW_NUMBERS[Constants.NUM_OF_ROWS - (y + 1)]

            #Make sure a piece is not in this location
            if StringMove.validateMoveLocation(game_state, letter + str(number)):

                #Update the game state
                game_state = StringInterpret.stringInterpret(game_state, letter + str(number), move_num)
                move_num += 1

                #Allow the computer to place a piece if the game is not over
                if VictoryStatus.endGameStatus(game_state) != True:
                    game_state = computerTurn(game_state, move_num)
                    move_num += 1

                #Save the variables
                FileHandler.saveVariable("State", game_state)
                FileHandler.saveVariable("Move", str(move_num))
    else:
        #Print who won
    	print(PlayerVictory.playerWon(game_state))

    	#Wait for user
    	Constants.WINDOW.exitonclick()

        #Reset state and move
    	FileHandler.saveVariable("State", "")
    	FileHandler.saveVariable("Move", "")

#The main loop of the function
#Waits for input from the user
#Params: state, The current game state
#        move_num, The current move number
#        isPlayerMove, Whether it is the player's move or not
#Returns: None
def run(state, move_num, isPlayerMove):
    #Allow the computer to make it's move
    if not isPlayerMove:
        state = computerTurn(state, move_num)
        move_num += 1

    #Save variables to be used later
    FileHandler.saveVariable("State", state)
    FileHandler.saveVariable("Move", str(move_num))

    #Set up the window
    wn = Constants.WINDOW
    wn.onclick(place_piece)
    wn.onkey(wn.bye, "space")
    wn.listen()
    wn.mainloop()
