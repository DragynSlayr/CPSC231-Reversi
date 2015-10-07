
import turtle
wn = turtle.Screen()


grid = turtle.Turtle()

grid.left(180)
grid.forward(200)
grid.left(180)
grid.speed(0)
	

for i in ['1', '2', '3', '4', '5', '6', '7', '8']:
	for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
		grid.forward(50)
		grid.left(90)
		grid.forward(50)
		grid.left(90)
		grid.forward(50)
		grid.left(90)
		grid.forward(50)
		grid.left(90)
		grid.forward(50)
		
	grid.left(180)
	grid.forward(400)
	grid.left(90)
	grid.forward(50)
	grid.left(90)

grid.left(90)
grid.forward(50)
grid.left(90)
grid.forward(25)
grid.left(90)
grid.forward(25)
grid.write("A", True)

wn.exitonclick()