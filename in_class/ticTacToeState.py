#This file contains a class for holding the state of a game of tic tac toe

#A class for holding the state of a tic tac toe game
class TicTacToeState:

    #Constant for empty position
    EMPTY_PIECE = 'b'

    #Constants for board size
    BOARD_WIDTH = 3
    BOARD_HEIGHT = 3

    #Constructor for the class
    #Parameters: player_token, A char representing the player's piece
    #            ai_token, A char representing the ai's piece
    #Returns: None, it's a constructor
    def __init__(self, player_token, ai_token):
        #Assign values to class variables, make them uppercase
        self.player = player_token.upper()
        self.ai = ai_token.upper()

        #Initialize lists
        self.board = []
        row = []

        #Make the board into a 2d list that represents a 3x3 board
        for i in range(self.BOARD_HEIGHT):
            for j in range(self.BOARD_WIDTH):
                row.append(self.EMPTY_PIECE)

            #Add the row to the board
            self.board.append(row)
            row = []

def main():
    #Instantiate the TicTacToeState object
    ttt = TicTacToeState('x', 'o')

    #Print the values of the object
    print("Player Token:", ttt.player)
    print("AI Token:", ttt.ai)
    print("Board:", ttt.board)

if __name__ == '__main__':
    main()
