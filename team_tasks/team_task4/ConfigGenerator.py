#Generates a random string to represent the board for testing of methods

import random
import Constants

def generate():
    game_state = ""
    for i in range(1, Constants.NUM_OF_CELLS + 1):
        random_int = random.randint(0, 2)
        if random_int == 0:
            game_state += Constants.PIECE_BLACK
        elif random_int == 1:
            game_state += Constants.PIECE_WHITE
        else:
            game_state += Constants.PIECE_NONE
        if i != Constants.NUM_OF_CELLS:
            if i % 8 == 0 and i != Constants.NUM_OF_CELLS:
                game_state += "\n"
            else:
                game_state += "|"
    return game_state

if __name__ == "__main__":
    while(input("Press q to quit: ") != 'q'):
        print("\n%s\n" % generate())
