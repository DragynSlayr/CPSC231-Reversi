#A function that takes a game state as a parameter
# and returns which player won.
import constants

#Gets a string representing who won
#Params: game_state, The state of the game
#Returns: A string containg who won
#Author: Anton Lysov
#Editor: Inderpreet Dhillon
def playerWon(game_state):
    num_black = 0
    num_white = 0

    #Iterate through the game state and count black and white pieces
    for y in game_state:
        for x in y:
            if x == constants.PIECE_BLACK:
                num_black += 1
            elif x == constants.PIECE_WHITE:
                num_white += 1

    #Compare number of white and black pieces and return
    #the result of the game
    if num_black == num_white:
        return constants.TIE_STRING
    elif num_black > num_white:
        black_win_string = constants.BLACK_STRING + str(num_black) + constants.PIECES_STRING
        return black_win_string
    else:
        white_win_string = constants.WHITE_STRING + str(num_white) + constants.PIECES_STRING
        return white_win_string
