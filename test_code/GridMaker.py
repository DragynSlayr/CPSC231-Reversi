import turtle
wn = turtle.Screen()

grid = turtle.Turtle()
grid.shape("turtle")
grid.speed(0)



def square():
	for i in range(4):
		print (grid.position())
		grid.forward(50)
		grid.left(90)
	return grid.position
	
square()	
wn.mainloop()