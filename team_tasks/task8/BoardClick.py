#This file handles all the clicking and logic of the game
import Constants
import TurtleMove
import ListInterpret
import StringMove
import VictoryStatus
import PlayerVictory
import FileHandler
import random
import MoveValidator
import ScreenWriter
import Converter
import SquareValidator
import time

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
    x_valid = x >= Constants.LEFT_MOST_X and x <= Constants.RIGHT_MOST_X
    y_valid = y >= Constants.BOTTOM_MOST_Y and y <= Constants.TOP_MOST_Y

    #Check if the x and y are in any cell
    return x_valid and y_valid

#The computer generates a move and places a piece if possible
#Params: state, The current game state
#        move_num, The current move number
#Returns: The new game state
def computerTurn(state, move_num):
    #Get a list of possible moves
    valid_moves = SquareValidator.mainSquareValidator(Converter.toString(state), ListInterpret.whoseTurn(move_num))

    #If no moves are valid then the move is skipped
    if len(valid_moves) == 0:
        return state
    else:
        #Generate a random number
        random_num = random.randrange(len(valid_moves))

        #Get a move from the list
        move = valid_moves[random_num]

        #Make the move
        return ListInterpret.stringInterpret(state, move, move_num)

#Places a piece at a location if it is a cell
#Params: x, The x location to check
#        y, The y location to check
#Returns: None
def placePiece(x, y):
    #Make sure a move is not being made
    if FileHandler.loadVariable("Moving") == "False":
        #Save variable
        FileHandler.saveVariable("Moving", "True")

        #Load the variables we need
        game_state = Converter.toList(FileHandler.loadVariable("State"))
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

                #The move being made
                move = letter + str(number)

                #Make sure a piece is not in this location and the move is valid
                if StringMove.validateMoveLocation(game_state, move) and MoveValidator.isValidMove(move, Converter.toString(game_state)) and move in SquareValidator.mainSquareValidator(Converter.toString(game_state), ListInterpret.whoseTurn(move_num)):
                    #Clear space at move
                    TurtleMove.resetSquare(letter, number)

                    #Update the game state
                    game_state = ListInterpret.stringInterpret(game_state, letter + str(number), move_num)
                    move_num += 1

                    #Allow the computer to place a piece if the game is not over
                    if VictoryStatus.endGameStatus(game_state) != True:
                        #Small delay
                        time.sleep(1)

                        game_state = computerTurn(game_state, move_num)
                        move_num += 1

                    #Save the variables
                    FileHandler.saveVariable("State", Converter.toString(game_state))
                    FileHandler.saveVariable("Move", str(move_num))

                    #Update the scoreboard
                    black_score = VictoryStatus.countPieces(Constants.PIECE_BLACK, game_state)
                    white_score = VictoryStatus.countPieces(Constants.PIECE_WHITE, game_state)
                    ScreenWriter.writeScore(black_score, white_score)

                    #Display valid moves
                    valid_moves = SquareValidator.mainSquareValidator(Converter.toString(game_state), ListInterpret.whoseTurn(move_num))
                    TurtleMove.displayValidMoves(valid_moves)
        else:
            #Print who won
            game_status = PlayerVictory.playerWon(game_state)
            ScreenWriter.writeMessage(game_status)

            #Wait for user
            Constants.WINDOW.exitonclick()

            #Reset state and move
            FileHandler.saveVariable("State", "")
            FileHandler.saveVariable("Move", "")

        #Save variable
        FileHandler.saveVariable("Moving", "False")

#Saves the current game configuration
#Params: None
#Returns: None
def saveGame():
    #Get current game info
    current_state = FileHandler.loadVariable("State")
    current_move_num = FileHandler.loadVariable("Move")

    #Save game info
    FileHandler.saveVariable("State", current_state, "save.txt")
    FileHandler.saveVariable("Move", current_move_num, "save.txt")

#Loads the saved game configuration
#Params: None
#Returns: None
def loadGame():
    #Load game info
    saved_state = FileHandler.loadVariable("State", "save.txt")
    saved_move_num = FileHandler.loadVariable("Move", "save.txt")

    #Write loaded variables to variables file
    FileHandler.saveVariable("State", saved_state)
    FileHandler.saveVariable("Move", saved_move_num)

    #Convert state from string to list
    saved_state = Converter.toList(saved_state)

    #Load board configuration
    ListInterpret.stringToPiece(saved_state)

    #Update the scoreboard
    black_score = VictoryStatus.countPieces(Constants.PIECE_BLACK, saved_state)
    white_score = VictoryStatus.countPieces(Constants.PIECE_WHITE, saved_state)
    ScreenWriter.writeScore(black_score, white_score)

    #Reset valid moves from TurtleMove
    TurtleMove.SHOWN_MOVES = []

    #Display valid moves
    valid_moves = SquareValidator.mainSquareValidator(Converter.toString(saved_state), ListInterpret.whoseTurn(int(saved_move_num)))
    TurtleMove.displayValidMoves(valid_moves)

#Gracefully quits the game
#Params: None
#Returns: None
def quitGame():
    #Reset variables
    FileHandler.saveVariable("State", "")
    FileHandler.saveVariable("Move", "")
    FileHandler.saveVariable("Moving", "False")

    #Close the game
    wn = Constants.WINDOW
    wn.bye()

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

    #Update the scoreboard
    black_score = VictoryStatus.countPieces(Constants.PIECE_BLACK, state)
    white_score = VictoryStatus.countPieces(Constants.PIECE_WHITE, state)
    ScreenWriter.writeScore(black_score, white_score)

    #Display valid moves
    valid_moves = SquareValidator.mainSquareValidator(Converter.toString(state), ListInterpret.whoseTurn(move_num))
    TurtleMove.displayValidMoves(valid_moves)

    #Save variables to be used later
    FileHandler.saveVariable("State", Converter.toString(state))
    FileHandler.saveVariable("Move", str(move_num))
    FileHandler.saveVariable("Moving", "False")

    #Set up the window
    wn = Constants.WINDOW
    wn.onclick(placePiece)
    wn.onkey(saveGame, "s")
    wn.onkey(loadGame, "l")
    wn.onkey(quitGame, "space")
    wn.listen()
    wn.mainloop()
