#This is the module that will create the Reversi Game board.


#Imports turtle module and opens the turtle screen. imports constants
import turtle
import Constants

#Creates a turtle class called grid
grid = turtle.Turtle()

#function for creating a square
def square():
	for i in range(4):
		grid.pendown()
		grid.forward(Constants.CELL_WIDTH)
		grid.left(90)

#function for labeling each square according to their coordinates in the array.
def coord_label(x, y):
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

#function for sending the turtle to the next row lower.
def next_row():
	grid.penup()
	grid.left(180)
	grid.forward(Constants.WINDOW_WIDTH / 2)
	grid.left(90)
	grid.forward(50)
	grid.left(90)
	grid.pendown()

#function to label the y coordinates vertically, to the left of the board.
def label_y():
	grid.goto(175, 125)
	#Iterate through the row numbers in reverse
	for sidey in Constants.ROW_NUMBERS[::-1]:
		coordyy = grid.ycor()
		grid.pendown()
		grid.write(sidey, True)
		grid.penup()
		coordyy = coordyy + Constants.CELL_HEIGHT
		grid.goto(175, coordyy)
		grid.setheading(90)

#function to label the x coordinates horizontally, above the board.
def label_x():
	grid.goto(225, 525)
	for sidex in Constants.COLUMN_LETTERS:
		coordxx = grid.xcor()
		grid.pendown()
		grid.write(sidex, True)
		grid.penup()
		coordxx = coordxx + Constants.CELL_WIDTH
		grid.goto(coordxx, 525)
		grid.setheading(0)

#function that draws a frame around the board.
def reversi_frame():
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
def ReversiBoard():
	for y in Constants.ROW_NUMBERS: #This stacks the rows of squares downwards.
		for x in Constants.COLUMN_LETTERS: #This creates the squares in a horizontal row.
			grid.fillcolor("green")
			grid.begin_fill()
			grid.pencolor ("black")
			square()
			grid.end_fill()
			grid.forward(Constants.CELL_WIDTH)
			coord_label(x, y)
		next_row()
		grid.penup()
	label_y()
	label_x()
	reversi_frame()

	grid.penup()
	grid.goto(25, 575)
	grid.pendown()
	grid.pencolor("black")
	grid.write("R   e   v   e   r   s   i")


#This function creates the window, sets the coordinates of the window, creates the grid with labels, and frames it.
def main():
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
	ReversiBoard()
	wn.update()
	
	if __name__ == "__main__":
		wn.exitonclick()

	wn.reset()
	


#Only runs when it is not imported
if __name__ == "__main__":
	main()
