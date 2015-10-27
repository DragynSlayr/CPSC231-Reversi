#This is the module that will create the Reversi Game board.

#Imports turtle module and opens the turtle screen. imports constants
import turtle
import Constants

#function for creating a square
#Function takes no parameters and returns nothing
def square():
	grid = Constants.TURTLE
	for i in range(4):
		grid.pendown()
		grid.forward(Constants.CELL_WIDTH)
		grid.left(90)

#Function for labeling each square according to their coordinates in the array.
#Function takes no parameters and returns nothing
def coordLabel(x, y):
	grid = Constants.TURTLE
	grid.penup()
	coord = grid.pos()
	coordx = grid.xcor()
	coordy = grid.ycor()
	grid.goto((coordx - 40), coordy + 25)
	grid.pencolor("yellow")
	grid.write((x, y), True)
	grid.goto(coord)
	grid.pendown()
	grid.pencolor("black")

#Function for sending the turtle to the next row lower.
#Function takes no parameters and returns nothing
def nextRow():
	grid = Constants.TURTLE
	grid.penup()
	grid.left(180)
	grid.forward(Constants.WINDOW_WIDTH / 2)
	grid.left(90)
	grid.forward(50)
	grid.left(90)
	grid.pendown()

#Function to label the y coordinates vertically, to the left of the board.
#Function takes no parameters and returns nothing
def label_y():
	grid = Constants.TURTLE
	grid.goto(175, 125)
	#Iterate through the row numbers in reverse
	for sidey in Constants.ROW_NUMBERS[::-1]:
		coord_yy = grid.ycor()
		grid.pendown()
		grid.write(sidey, True)
		grid.penup()
		coord_yy = coord_yy + Constants.CELL_HEIGHT
		grid.goto(175, coord_yy)
		grid.setheading(90)

#Function to label the x coordinates horizontally, above the board.
#Function takes no parameters and returns nothing
def label_x():
	grid = Constants.TURTLE
	grid.goto(225, 525)
	for sidex in Constants.COLUMN_LETTERS:
		coord_xx = grid.xcor()
		grid.pendown()
		grid.write(sidex, True)
		grid.penup()
		coord_xx = coord_xx + Constants.CELL_WIDTH
		grid.goto(coord_xx, 525)
		grid.setheading(0)

#Function that draws a frame around the board.
#Function takes no parameters and returns nothing
def reversiFrame():
	grid = Constants.TURTLE
	grid.pencolor("dark green")
	grid.pensize(10)
	grid.goto(0,0)
	grid.pendown()
	grid.forward(Constants.WINDOW_WIDTH)
	grid.left(90)
	grid.forward(Constants.WINDOW_HEIGHT)
	grid.left(90)
	grid.forward(Constants.WINDOW_WIDTH)
	grid.left(90)
	grid.forward(Constants.WINDOW_HEIGHT)
	grid.penup()

#This is the function that creates the board, using the functions above.
#It contains a nested for loop that will create the grid and label it.
#It will also frame the game window.
#Function takes no parameters and returns nothing
def reversiBoard():
	grid = Constants.TURTLE
	for y in Constants.ROW_NUMBERS: #This stacks the rows of squares downwards.
		for x in Constants.COLUMN_LETTERS: #This creates the squares in a horizontal row.
			grid.fillcolor("green")
			grid.begin_fill()
			grid.pencolor ("black")
			square()
			grid.end_fill()
			grid.forward(Constants.CELL_WIDTH)
			coordLabel(x, y)
		nextRow()
		grid.penup()
	label_y()
	label_x()
	reversiFrame()

	grid.penup()
	grid.goto(25, 575)
	grid.pendown()
	grid.pencolor("black")
	grid.write("R   e   v   e   r   s   i")


#This function creates the window, sets the coordinates of the window, creates the grid with labels, and frames it.
#Function takes no parameters and returns nothing
def main():
	grid = Constants.TURTLE
	wn = Constants.WINDOW
	
	wn.clear()

	#Set the size of the screen
	wn.setup(Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT)

	wn.tracer(10) 
	
	#The method below changes the default coordinates to user made coordinates.
	#in this case bottom left corner is 0,0. Changes screen to World coordinates mode from standard.
	#0, 0 is bottom left of the window 
	wn.setworldcoordinates(0, 0, Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT)
	

	#pre-set the turtle
	grid.speed(0)
	grid.penup()
	grid.goto(Constants.WINDOW_WIDTH / 4, Constants.WINDOW_HEIGHT * (3 / 4))
	grid.pendown()
	grid.hideturtle()
	reversiBoard() #Creates the board.
	wn.update()
	
	if __name__ == "__main__":
		wn.exitonclick()

	wn.reset()
	


#Only runs when it is not imported
if __name__ == "__main__":
	main()
