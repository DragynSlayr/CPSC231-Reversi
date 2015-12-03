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

    #Checks if a location is on the board and unoccupied
    #Params: row, The row to check
    #        column, The column to check
    #Returns: True if the location is valid False otherwise
    def isValidLocation(self, row, column):
        #Check that row and column are on the board
        row_valid = row >= 0 and row <= self.BOARD_HEIGHT
        column_valid = column >= 0 and row <= self.BOARD_WIDTH

        #Check that the location is unoccupied
        location_valid = self.board[column][row] == self.EMPTY_PIECE

        #Return true if move is valid, False if any check is invalid
        return row_valid and column_valid and location_valid

    #Places a piece for the player, if valid
    #Params: row, The row to place at
    #        column, The column to place at
    #Returns: None
    def playerMove(self, row, column):
        if self.isValidLocation(row, column):
            self.board[column][row] = self.player

    #Places a piece for the ai, if valid
    #Params: row, The row to place at
    #        column, The column to place at
    #Returns: None
    def aiMove(self, row, column):
        if self.isValidLocation(row, column):
            self.board[column][row] = self.ai

    #Checks if two states are identical
    #Params: otherState, The state to compare with
    #Returns: True if both boards have the same values
    def isSame(self, otherState):
        return self.board == otherState.board

    #Gets a nice representation of the board
    #Params: None
    #Returns: String representation of the state
    def __str__(self):
        formatted = ""

        #Traverse board
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                #Add piece at index to formatted string
                formatted += str(self.board[i][j])

            #Only add a new line if not at the last row
            if i < len(self.board) - 1:
                formatted += "\n"

        return formatted

def main():
    #Instantiate the TicTacToeState objects
    ttt = TicTacToeState('x', 'o')
    ttt2 = TicTacToeState('X', 'O')

    #Check if the two states are the same
    #They should be as at this point they have the same starting values
    print("First check:", ttt.isSame(ttt2))

    #Make some moves
    ttt.playerMove(1, 1)
    ttt.aiMove(0, 0)

    #Check that the states are the same again
    #They should not be because the board from ttt has been changed
    #and the two boards are not aliased, they can and do differ in value
    print("Second check:", ttt.isSame(ttt2))

    #Print both boards
    print("ttt\n~~~\n" + str(ttt) + "\n")
    print("ttt2\n~~~~\n" + str(ttt2))

if __name__ == '__main__':
    main()
