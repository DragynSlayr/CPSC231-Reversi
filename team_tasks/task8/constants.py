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

#Only mutiples of this frame of the animation will be drawn
FRAME_TO_DRAW = 0

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
TITLE_LOCATIONX = WINDOW_WIDTH / 2 #50% of window width
TITLE_LOCATIONY = WINDOW_HEIGHT * (3/4) #75% of window height

#Constants for the column and row labels.
X_LETTER_LABEL = 220
Y_LETTER_LABEL = 500

X_NUM_LABEL = 175
Y_NUM_LABEL = 110

#Constants for drawing frame.
FRAME_ORIGIN = -5

#Constants for pass button
PASS_BUTTON_X = 650
PASS_BUTTON_Y = 50
PASS_BUTTON_HEIGHT = 85
PASS_BUTTON_WIDTH = 45

#The values for the rules
RULES_LINESTARTX = 0
RULES_LINESTARTY = WINDOW_HEIGHT * (89 / 100) #89% of the window height
RULES_SHIFT = 55

#The window and turtle, not actually constants
WINDOW = turtle.Screen()
TURTLE = turtle.Turtle()

#Information for storing game state
PIECE_BLACK = 'B'
PIECE_WHITE = 'W'
PIECE_NONE = 'N'

#A valid move will always change more pieces than this
PIECE_CHANGE_THRESHOLD = 1

#The delay between player and computer turns, in seconds
MOVE_DELAY = 1

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
MESSAGE_X = 200
MESSAGE_Y = 20

#Constants for checking for pieces in the directions
NORTH = -8
NORTHEAST = -7
EAST = 1
SOUTHEAST = 9
SOUTH = 8
SOUTHWEST = 7
WEST = -1
NORTHWEST = -9

#Constants for button positions
BUTTON_TOP_Y = 300
BUTTON_BOTTOM_Y = 200
PLAY_BUTTON_LEFT_X = 300
PLAY_BUTTON_RIGHT_X = 500
RULES_BUTTON_LEFT_X = 50
RULES_BUTTON_RIGHT_X = 250
EXIT_BUTTON_LEFT_X = 550
EXIT_BUTTON_RIGHT_X = 750
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 100

#Constants for back button on rules screen
BACK_BUTTON_LEFT_X = 300
BACK_BUTTON_RIGHT_X = 500
BACK_BUTTON_TOP_Y = 100
BACK_BUTTON_BOTTOM_Y = 0

#The default game state
GAME_STATE_START = [
['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N'],
['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N'],
['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N'],
['N', 'N', 'N', 'W', 'B', 'N', 'N', 'N'],
['N', 'N', 'N', 'B', 'W', 'N', 'N', 'N'],
['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N'],
['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N'],
['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N']]

#Keys that can be pressed during the game
EXIT_KEY = "space"
SAVE_KEY = "s"
LOAD_KEY = "l"

#Files and variables in them
TEMP_FILE = "variables.txt"
SAVE_FILE = "save.txt"
FILE_READ = "r"
FILE_WRITE = "w"
FILE_READ_WRITE = "r+"
VARIABLE_MOVE = "Move"
VARIABLE_STATE = "State"
VARIABLE_MOVING = "Moving"
VARIABLE_BLANK = ""
VARIABLE_BOOL_TRUE = "True"
VARIABLE_BOOL_FALSE = "False"
VARIABLE_SEPARATOR = ":"

#For colors
PIECE_COLOR_BLACK = "Black"
PIECE_COLOR_WHITE = "White"
PIECE_COLOR_VALID = "#34DDDD"
GRID_BG_COLOR = "Dark Green"
GRID_FG_COLOR = "Black"
PLAY_SCREEN_BG_COLOR = "Light Green"
BORDER_COLOR = "Yellow"

#Used when writing
CENTER_TEXT = "center"
LEFT_TEXT = "left"
BUTTON_TEXT_STYLE = ("Arial", 15, "bold")
SCORE_BOARD_TEXT_STYLE = ("Arial", 20, "bold")
NAME_TEXT_STYLE = ("Arial", 50, "bold")
GRID_NAME_STYLE = ("Arial", 27, "bold", "underline")
RULES_TEXT_STYLE = ("Arial", 10, "normal")
GAME_NAME = "REVERSI"
MENU_OPTIONS = ["Rules", "Play", "Exit"]
RULES_OPTION = "Return to Menu"
SCORE_TITLE_BLACK = PIECE_COLOR_BLACK + "\n    "
SCORE_TITLE_WHITE = PIECE_COLOR_WHITE + "\n    "
TURN_STRING = "TURN NUMBER \n     "
TURN_COLOUR_STRING = "TURN \nCOLOUR \n"
BUTTON_ERROR_MESSAGE = "Please Click a Button!"

#Strings for end conditions
TIE_STRING = "           It was a Tie!"
BLACK_STRING = PIECE_COLOR_BLACK + " won, with "
WHITE_STRING = PIECE_COLOR_WHITE + " won, with "
PIECES_STRING = " pieces!"

#Rules of the game
RULES = [
"Reversi is a 2 player game that is played on an 8 x 8 grid.\n\n",
"The game discs have both a black and white side.\n\n",
"To win you have to have the majority of the discs changed to your color at the end of the game.\n\n",
"The game ends when there are no more possible moves to make.\n\n",
"The game can end before the entire grid is filled.\n\n",
"Players take turns placing discs, with their color facing up.\n\n",
"When a player places a disk on the board, all the pieces that are between that player's newly placed disc\nand any of their previously placed discs, are turned to that player's color.\n",
"When placing your discs on your turn, there has to be at least one piece of the opposite colour between\nyour placed piece and any of your previously placed pieces. Otherwise the move is not valid.",
"The placed pieces have to make either a horizontal, vertical or diagonal line with the opposing player's discs to flip any pieces over."
]
