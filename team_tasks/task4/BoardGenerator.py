#Generates a random string to represent the board for testing of methods

import random
import Constants

#Generates a random board configuration
#Params: isOver, Whether the random board should be a completed game
#        isPretty, Whther the board should be nicely formatted for humans
#Returns: Random string representing the board
#Author: Inderpreet Dhillon
def generate(isOver, isPretty):
    #Will hold the board
    game_state = ""
    #Go through every row and column of the board
    for i in range(1, Constants.NUM_OF_CELLS + 1):
        #Random number, either: 0, 1, 2
        random_int = random.randint(0, 2)
        #Check number
        if random_int == 0:
            game_state += Constants.PIECE_BLACK
        elif random_int == 1:
            game_state += Constants.PIECE_WHITE
        else:
            #Check if the game should be a finished one
            if isOver:
                #Get a new number, either: 0 or 1
                random_int_two = random.randint(0, 1)
                #Check the new number
                if random_int_two == 0:
                    game_state += Constants.PIECE_WHITE
                else:
                    game_state += Constants.PIECE_BLACK
            else:
                #Only place no piece if the game is not over
                game_state += Constants.PIECE_NONE
        #Check if board should be nicely formatted
        if isPretty:
            if i != Constants.NUM_OF_CELLS:
                if i % 8 == 0 and i != Constants.NUM_OF_CELLS:
                    game_state += "\n"
                else:
                    game_state += "|"
    return game_state

if __name__ == "__main__":
    isOver = random.randint(0, 1) == 0
    generated = generate(isOver, False)
    print("\n%s\n%s" % (generated, isOver))
