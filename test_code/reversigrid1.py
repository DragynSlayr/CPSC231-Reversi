#Here is my draft turtle drawing of our game board for now with a nested for loop.
#I am trying some stuff with the mouse input and the color right now.
#Still a few things that I am trying to work out on it. 
#I'll probably try to make one that is more ratio based on the Constants, which I still need to do research on.

#import turtle module and opens the turtle screen.
import turtle
wn = turtle.Screen()

#creates a turtle class called grid
grid = turtle.Turtle()

#pre-set the turtle
grid.speed(0)
grid.penup()
grid.goto(-200, 100)
grid.pendown()
grid.shape("turtle")
	
#The for loop with a for loop in it. This will create the grid. By stacking the rows.
for y in ['1', '2', '3', '4', '5', '6', '7', '8']:
	for x in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']: #This creates the rows.
		grid.fillcolor("green")
		grid.begin_fill()
		grid.pencolor ("black")
		grid.forward(50)
		grid.left(90)
		grid.forward(50)
		grid.left(90)
		grid.forward(50)
		grid.left(90)
		grid.forward(50)
		grid.left(90)
		grid.end_fill()
		grid.forward(50)
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
		
	grid.left(180) #getting to the next row.
	grid.forward(400)
	grid.left(90)
	grid.forward(50)
	grid.left(90)
grid.penup()
grid.left(90)
grid.forward(75)
grid.left(90)
grid.forward(25)
grid.right(90)

#prints out the x row values on the side.
for sidex in ['8', '7', '6', '5', '4', '3', '2', '1']:
	grid.write(sidex, True)
	grid.setheading(90) #90 points turtle north in standard mode 0 in logo mode
	grid.forward(50)#without these directions the printed numbers go diagonally based on print space.
	grid.left(90)
	grid.forward(5)
	grid.right(90)

grid.right(90)
grid.forward(35)

#prints out the y row values on the top.
for sidey in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
	grid.write(sidey, True)
	grid.forward(48)
	
wn.exitonclick()