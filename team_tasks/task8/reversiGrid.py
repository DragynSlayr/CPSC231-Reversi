#This is the module that will create the Reversi Game board.
import turtle
import constants

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
	grid.goto(175, 125)

	#Iterate through the row numbers in reverse
	for sidey in constants.ROW_NUMBERS[::-1]:
		coord_yy = grid.ycor()
		grid.pendown()
		grid.write(sidey, False)
		grid.penup()
		coord_yy = coord_yy + constants.CELL_HEIGHT
		grid.goto(175, coord_yy)
		grid.setheading(90)

#Function to label the x coordinates horizontally, above the board.
#Function takes nothing and returns nothing
def label_x():
	grid = constants.TURTLE
	grid.goto(225, 525)
	for sidex in constants.COLUMN_LETTERS:
		coord_xx = grid.xcor()
		grid.pendown()
		grid.write(sidex, False)
		grid.penup()
		coord_xx = coord_xx + constants.CELL_WIDTH
		grid.goto(coord_xx, 525)
		grid.setheading(0)

#Function that draws a frame around the board.
#Function takes nothing and returns nothing
def reversiFrame():
	grid = constants.TURTLE
	size = grid.pensize()
	grid.pencolor("dark green")
	grid.pensize(9)
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
	grid.penup()

	#Reset size
	grid.pensize(size)

#This is the function that creates the board, using the functions above.
#It contains a nested for loop that will create the grid and label it.
#It will also frame the game window.
#Function takes nothing and returns nothing
def reversiBoard():
	grid = constants.TURTLE
	grid.fillcolor("dark green")
	grid.pencolor ("black")
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
	grid.goto(25, 575)
	grid.pendown()
	grid.pencolor("black")
	grid.write("R   e   v   e   r   s   i", False)

#This function creates the window, sets the coordinates of the window, creates the grid with labels, and frames it.
#Function takes no parameters and returns nothing
def main():
	#Get window and turtle
	grid = constants.TURTLE
	wn = constants.WINDOW

	#Clear the screen
	wn.clear()
	wn.tracer(constants.FRAME_TO_DRAW)

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
