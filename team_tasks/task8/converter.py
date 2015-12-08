#This program contains methods for converting between list and string
import constants

#Converts the game state from a string to a 2d list
#Params: state_string, The game state as a string
#Returns: The game state as a 2d list
#Author: Inderpreet Dhillon
#Editor: None
def toList(state_string):
    #Lists to hold the state
    row = []
    state_list = []

    #Traverse the game state
    for letter in state_string:

        #Add each letter to the row
        row.append(letter)

        #Add the row to the list if it is the right size
        if len(row) == constants.NUM_OF_COLUMNS:
            state_list.append(row)

            #Reset the row
            row = []

    #Return the 2d list
    return state_list

#Converts a 2d list into a string
#Params: state_list, The 2d list of the game state
#Returns: The game state as a string
#Author: Inderpreet Dhillon
#Editor: None
def toString(state_list):
    #The string to hold the state
    state_string = constants.VARIABLE_BLANK

    #Traverse the outer list
    for row in state_list:

        #Travers the inner lists
        for piece in row:
            #Add the piece to the state
            state_string += piece

    #Return the game state string
    return state_string

#Gets a nice representation of the state
#Params: state, The state as a string or list
#Returns: The state as a formatted board
#Author: Inderpreet Dhillon
#Editor: None
def asBoardRepresentation(state):
    #Make sure state is a list
    if type(state) == type(constants.VARIABLE_BLANK):
        state = toList(state)

    #Will hold the board
    board = constants.VARIABLE_BLANK

    #Go through each index in the state
    for row in range(len(state)):
        for piece in state[row]:
            #Add each element to the board string
            board += piece

        #Add a new line if not at the last line
        if row != len(state) - 1:
            board += '\n'

    #Return the string
    return board
