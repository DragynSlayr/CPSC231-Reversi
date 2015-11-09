#This file holds the constant values for the game
#These values are used for all drawing and sizing of the game

import turtle

#Grid information
NUM_OF_ROWS = 8
NUM_OF_COLUMNS = 8
NUM_OF_CELLS = NUM_OF_ROWS * NUM_OF_COLUMNS

#Window information
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

#Cell information
CELL_WIDTH = 50
CELL_HEIGHT = 50

#Arrays of letters and numbers for the columns and the rows
COLUMN_LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
ROW_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8]

#The offset of the first cell of the grid
X_OFFSET = (WINDOW_WIDTH / 4) + CELL_WIDTH #Evaluates to 250
Y_OFFSET = (WINDOW_HEIGHT * (2/3)) + (WINDOW_HEIGHT / 8) #Evaluates to 475

#Offset for the title
TITLE_LOCATIONX = WINDOW_WIDTH / 2 #Evaluates to 400
TITLE_LOCATIONY = WINDOW_HEIGHT * 0.75 #Evaluates to 450

#The offset for the rules
RULES_LINESTARTX = 0
RULES_LINESTARTY = WINDOW_HEIGHT / 2 #Evaluates to 600

#The y position of the rules
RULES_LIST = WINDOW_HEIGHT / 2 #Evaluates to 300

#The window and turtle
WINDOW = turtle.Screen()
TURTLE = turtle.Turtle()

#Information for storing game state
PIECE_BLACK = 'B'
PIECE_WHITE = 'W'
PIECE_NONE = 'N'

#Information for the boards coordinates
#The board is drawn between:
#(LEFT_MOST_X, BOTTOM_MOST_Y) and (RIGHT_MOST_X, TOP_MOST_Y)
LEFT_MOST_X = 200
RIGHT_MOST_X = 600
TOP_MOST_Y = 500
BOTTOM_MOST_Y = 100

#These represent the above numbers in terms of columns and rows
OFFSET_OF_COLUMNS = 4
OFFSET_OF_ROWS = 2

#Constants for writing information to the Screen
WHITE_SCORE_X = 660
WHITE_SCORE_Y = 440
BLACK_SCORE_X = 40
BLACK_SCORE_Y = 440
MESSAGE_X = 300
MESSAGE_Y = 20
