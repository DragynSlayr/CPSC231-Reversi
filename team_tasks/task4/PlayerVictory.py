#A function that takes a game state as a parameter and returns which player won.
import Constants
import BoardGenerator as cfg

def PlayerWon(game_state):
    numBlack = 0
    numWhite = 0

    #Iterate through the game state and count black and white pieces
    for i in game_state:
        if i == Constants.PIECE_BLACK:
            numBlack += 1
        elif i == Constants.PIECE_WHITE:
            numWhite += 1
    #Compare number of white and black pieces and return whether a player won or not
    if numBlack == numWhite:
        return "It was a Tie!"
    elif numBlack > numWhite:
        return "Black won, with " + str(numBlack) + " pieces!"
    else:
        return "White won, with " + str(numWhite) + " pieces!"

if __name__ == "__main__":
	board = cfg.generate(True, True)
	print(board, "\n%s" % PlayerWon(board))

	board = cfg.generate(True, False)
	print(board, "\n%s" % PlayerWon(board))

	board = cfg.generate(False, True)
	print(board, "\n%s" % PlayerWon(board))

	board = cfg.generate(False, False)
	print(board, "\n%s" % PlayerWon(board))
