import turtle
#Constants

NUM_OF_CELLS = 64
NUM_OF_ROWS = 8
NUM_OF_COLUMNS = 8
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_WIDTH = 50
CELL_HEIGHT = 50
COLUMN_LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
ROW_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8]
X_OFFSET = WINDOW_WIDTH / 4
Y_OFFSET = (WINDOW_HEIGHT * (2/3)) + (WINDOW_HEIGHT / 8)
TITLE_LOCATIONX = WINDOW_WIDTH / 2
TITLE_LOCATIONY = WINDOW_HEIGHT * 0.75
RULES_LINESTARTX = 0
RULES_LINESTARTY = WINDOW_HEIGHT / 2
RULES_LIST = WINDOW_HEIGHT / 2
WINDOW = turtle.Screen()