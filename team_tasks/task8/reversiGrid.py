#This is the module that will create the Reversi Game board.
import turtle
import constants
import converter

#function for creating a square
#Function takes nothing and returns nothing
def square():
	grid = constants.TURTLE
	for i in range(4):
		grid.pendown()
		grid.forward(constants.CELL_WIDTH)
		grid.left(90)

#Function for sending the turtle to the next row lower.
#Function takes nothing and returns nothing
def nextRow():
	grid = constants.TURTLE
	grid.penup()
	grid.left(180)
	grid.forward(constants.WINDOW_WIDTH / 2)
	grid.left(90)
	grid.forward(50)
	grid.left(90)
	grid.pendown()

#Function to label the y coordinates vertically, to the left of the board.
#Function takes nothing and returns nothing
def label_y():
	grid = constants.TURTLE
	grid.goto(175, 110)

	#Iterate through the row numbers in reverse
	for sidey in constants.ROW_NUMBERS[::-1]:
		coord_yy = grid.ycor()
		grid.pendown()
		grid.write(sidey, False, constants.LEFT_TEXT, constants.BUTTON_TEXT_STYLE)
		grid.penup()
		coord_yy = coord_yy + constants.CELL_HEIGHT
		grid.goto(175, coord_yy)
		grid.setheading(90)

#Function to label the x coordinates horizontally, above the board.
#Function takes nothing and returns nothing
def label_x():
	grid = constants.TURTLE
	grid.goto(210, 500)
	for sidex in constants.COLUMN_LETTERS:
		coord_xx = grid.xcor()
		grid.pendown()
		grid.write(sidex, False, constants.LEFT_TEXT, constants.BUTTON_TEXT_STYLE)
		grid.penup()
		coord_xx = coord_xx + constants.CELL_WIDTH
		grid.goto(coord_xx, 500)
		grid.setheading(0)

#Function that draws a frame around the board.
#Function takes nothing and returns nothing
def reversiFrame():
	grid = constants.TURTLE
	size = grid.pensize()
	grid.pencolor(constants.GRID_BG_COLOR)
	grid.pensize(14)
	grid.goto(-5,-5)
	grid.setheading(90)
	grid.pendown()

	#Draw the border
	grid.forward(constants.WINDOW_HEIGHT)
	grid.right(90)
	grid.forward(constants.WINDOW_WIDTH - 1)
	grid.right(90)
	grid.forward(constants.WINDOW_HEIGHT)
	grid.right(90)
	grid.forward(constants.WINDOW_WIDTH - 1)
	grid.right(90)

	grid.pencolor(constants.BORDER_COLOR)
	grid.pensize(6)
	grid.goto(-5, -5)
	grid.setheading(90)
	grid.forward(constants.WINDOW_HEIGHT)
	grid.right(90)
	grid.forward(constants.WINDOW_WIDTH - 1)
	grid.right(90)
	grid.forward(constants.WINDOW_HEIGHT)
	grid.right(90)
	grid.forward(constants.WINDOW_WIDTH - 1)
	grid.right(90)

	grid.pencolor(constants.GRID_FG_COLOR)
	grid.pensize(3)
	grid.goto(-5, -5)
	grid.setheading(90)
	grid.forward(constants.WINDOW_HEIGHT)
	grid.right(90)
	grid.forward(constants.WINDOW_WIDTH - 1)
	grid.right(90)
	grid.forward(constants.WINDOW_HEIGHT)
	grid.right(90)
	grid.forward(constants.WINDOW_WIDTH - 1)
	grid.right(90)


	grid.penup()

	#Reset size
	grid.pensize(size)

#This is the function that creates the board, using the functions above.
#It contains a nested for loop that will create the grid and label it.
#It will also frame the game window.
#Function takes nothing and returns nothing
def reversiBoard():
	grid = constants.TURTLE
	grid.fillcolor(constants.GRID_BG_COLOR)
	grid.pencolor (constants.GRID_FG_COLOR)
	grid.begin_fill()
	square()
	grid.end_fill()
	for y in constants.ROW_NUMBERS: #This stacks the rows of squares downwards.
		for x in constants.COLUMN_LETTERS: #This creates the squares in a horizontal row.
			grid.begin_fill()
			square()
			grid.end_fill()
			grid.forward(constants.CELL_WIDTH)
		nextRow()
		grid.penup()
	label_y()
	label_x()
	reversiFrame()

	grid.penup()
	grid.goto(20, 545)
	grid.pendown()
	grid.pencolor(constants.GRID_FG_COLOR)

	#List comprehension to put spaces between each letter in the game name
	spread_name_list = [(i + "  ") for i in constants.GAME_NAME]
	spread_name_string = converter.toString(spread_name_list)

	grid.write(spread_name_string, False, constants.LEFT_TEXT, constants.GRID_NAME_STYLE)

#This function creates the window, sets the coordinates of the window, creates the grid with labels, and frames it.
#Function takes no parameters and returns nothing
def main():
	#Get window and turtle
	grid = constants.TURTLE
	wn = constants.WINDOW

	#Clear the screen
	wn.clear()
	wn.tracer(constants.FRAME_TO_DRAW)
	wn.bgcolor(constants.PLAY_SCREEN_BG_COLOR)

	#pre-set the turtle
	grid.speed(0)
	grid.penup()
	grid.goto(constants.WINDOW_WIDTH / 4, constants.WINDOW_HEIGHT * (3 / 4))
	grid.pendown()
	grid.hideturtle()
	reversiBoard() #Creates the board.
	wn.update()

	if __name__ == "__main__":
		wn.exitonclick()

#Only runs when it is not imported
if __name__ == "__main__":
	main()
