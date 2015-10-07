#import turtle module and opens the turtle screen.
import turtle
wn = turtle.Screen()

#creates a turtle class called grid
grid = turtle.Turtle()

#pre-set the turtle
grid.speed(10)
grid.shape("turtle")

def getPos(x, y):
	print(x, ", ", y)
	return
	
def main():
	wn.onscreenclick(getPos)
	grid.onclick(grid.circle(20))
	wn.mainloop()
main()
