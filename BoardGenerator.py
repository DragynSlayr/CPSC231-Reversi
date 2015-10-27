#Generates a random string to represent the board for testing of methods

import random
import Constants

#Generates a random board configuration
#Params: is_over, Whether the random board should be a completed game
#        is_pretty, Whther the board should be nicely formatted for humans
#Returns: Random string representing the board
#Author: Inderpreet Dhillon
def generate(is_over, is_pretty):
    #Will hold the board
    token = ""
    #Go through every row and column of the board
    for i in range(1, Constants.NUM_OF_CELLS + 1):
        #Random number, either: 0, 1, 2
        random_int = random.randint(0, 2)
        #Check number
        if random_int == 0:
            token += Constants.PIECE_BLACK
        elif random_int == 1:
            token += Constants.PIECE_WHITE
        else:
            #Check if the game should be a finished one
            if is_over:
                #Get a new number, either: 0 or 1
                random_int_two = random.randint(0, 1)
                #Check the new number
                if random_int_two == 0:
                    token += Constants.PIECE_WHITE
                else:
                    token += Constants.PIECE_BLACK
            else:
                #Only place no piece if the game is not over
                token += Constants.PIECE_NONE
        #Check if board should be nicely formatted
        if is_pretty:
            if i != Constants.NUM_OF_CELLS:
                if i % 8 == 0 and i != Constants.NUM_OF_CELLS:
                    token += "\n"
                else:
                    token += "|"
    return token

if __name__ == "__main__":
    is_over = random.randint(0, 1) == 0
    generated = generate(is_over, False)
    print("\n%s\n%s" % (generated, is_over))
