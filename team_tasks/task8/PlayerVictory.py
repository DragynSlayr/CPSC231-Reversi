#A function that takes a game state as a parameter
# and returns which player won.
import Constants

#Gets a string representing who won
#Takes the game state as a parameter
#Reurns who won and the amount of pieces they had
#Author: Anton Lysov
#Editor: Inderpreet Dhillon, Added comments to top of function
def playerWon(game_state):
    num_black = 0
    num_white = 0

    #Iterate through the game state and count black and white pieces
    for y in game_state:
        for x in y:
            if x == Constants.PIECE_BLACK:
                num_black += 1
            elif x == Constants.PIECE_WHITE:
                num_white += 1

    #Compare number of white and black pieces and return
    #the result of the game
    if num_black == num_white:
        return "It was a Tie!"
    elif num_black > num_white:
        return "Black won, with " + str(num_black) + " pieces!"
    else:
        return "White won, with " + str(num_white) + " pieces!"
