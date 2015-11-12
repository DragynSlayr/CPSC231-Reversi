#This program contains a method for converting the state from string to list and vice versa
import Constants

#Converts the game state from a string to a 2d list
#Params: state_string, The game state as a string
#Returns: The game state as a 2d list
def toList(state_string):
    #Lists to hold the state
    row = []
    state_list = []

    #Traverse the game state
    for letter in state_string:

        #Add each letter to the row
        row.append(letter)

        #Add the row to the list if it is the right size
        if len(row) == Constants.NUM_OF_COLUMNS:
            state_list.append(row)

            #Reset the row
            row = []

    #Return the 2d list
    return state_list

#Converts a 2d list into a string
#Params: state_list, The 2d list of the game state
#Returns: The game state as a string
def toString(state_list):
    #The string to hold the state
    state_string = ""

    #Traverse the outer list
    for row in state_list:

        #Travers the inner lists
        for piece in row:
            #Add the piece to the state
            state_string += piece

    #Return the game state string
    return state_string

def asBoardRepresentation(state):
    #Make sure state is a list
    if type(state) == type("String"):
        state = toList(state)

    #Will hold the board
    board = ""

    #Go through each index in the state
    for row in range(len(state)):
        for piece in state[row]:
            #Add each element to the board string
            board += piece

        #Add a new line if not at the last line
        if row != len(state) - 1:
            board += "\n"

    #Return the string
    return board


def main():
    state = (("N" * 8) + ("B" * 8) + ("W" * 8) + ("NBWNBWNB")) * 2
    state_list = toList(state)
    #print(state_list)

    state_string = toString(state_list)
    #print(state_string)

    board_list = asBoardRepresentation(state_list)
    board_string = asBoardRepresentation(state_string)
    print(board_list == board_string)
    print(board_list)

if __name__ == "__main__":
    main()
