#Here is another draft of the gameboard. 
#I could not get the world coordinates to work with 0, 0 on the top left. It made everything upside down. On top of that,
#it changes the orientation of some of the commands like setheading.
#0, 0 is bottom left (for now) and it makes everything work properly. (Seriously! left was right with the other way)
#When you click you will get the position printed in the command terminal.

#import turtle module and opens the turtle screen.
import turtle
wn = turtle.Screen()
wn.tracer(10) #makes the turtle end somewhere differently as well for some reason.
#changes the default coordinates to user made coordinates.
wn.setworldcoordinates(0, 0, 800, 600)
#in this case bottom left corner is 0,0. Changes screen to World coordinates mode from standard.


#creates a turtle class called grid
grid = turtle.Turtle()

#pre-set the turtle
grid.speed(0)
grid.penup()
grid.goto(200, 450)
grid.pendown()
grid.shape("turtle")

#function for creating a square
def square():
	for i in range(4):
		grid.pendown()
		grid.forward(50)
		grid.left(90)

#function for labeling each square according to their coordinates in the array.
def coord_label():
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
	grid.forward(400)
	grid.left(90)
	grid.forward(50)
	grid.left(90)
	grid.pendown()

#function to label the y coordinates vertically, to the left of the board.
def label_y():
	grid.goto(175, 125)
	for sidey in ['8', '7', '6', '5', '4', '3', '2', '1']:
		coordyy = grid.ycor()
		grid.pendown()
		grid.write(sidey, True)
		grid.penup()
		coordyy = coordyy + 50
		grid.goto(175, coordyy)
		grid.setheading(90)

#function to label the x coordinates horizontally, above the board.
def label_x():
	grid.goto(225, 525)
	for sidex in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
		coordxx = grid.xcor()
		grid.pendown()
		grid.write(sidex, True)
		grid.penup()
		coordxx = coordxx + 50
		grid.goto(coordxx, 525)
		grid.setheading(0)
	
#function that draws a frame around the board.	
def reversi_frame():
	grid.pencolor("dark green")
	grid.pensize(10)
	grid.goto(0,0)
	grid.pendown()
	grid.forward(800)
	grid.left(90)
	grid.forward(600)
	grid.left(90)
	grid.forward(800)
	grid.left(90)
	grid.forward(600)
	grid.penup()

	
#Didn't function this one out yet.....	
#nested for loop that creates the board with the above functions.
for y in ['1', '2', '3', '4', '5', '6', '7', '8']: #This stacks the rows on each other.
	for x in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']: #This creates the horizontal rows.
		grid.fillcolor("green")
		grid.begin_fill()
		grid.pencolor ("black")
		square()
		grid.end_fill()
		grid.forward(50)
		coord_label()
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

#the two functions below will, together, print the position of where you click on the screen.
def getPos(x, y):
	print(x, ", ", y)
	return
	
def main():
	wn.onscreenclick(getPos)
	wn.mainloop()

main()
