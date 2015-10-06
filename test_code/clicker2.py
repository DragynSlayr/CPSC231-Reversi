#This will make the turtle go to where ever you click.

import turtle
wn = turtle.Screen()
clicker = turtle.Turtle()
clicker.shape("turtle")

def getPos(x, y):
	print(x, ", ", y)
	return

def traveller(posit):
	clicker.onclick(goto posit)

def circler():
	if turtle.position() = getPos:
	clicker.circle(50)
	
def main():
	wn.onscreenclick(getPos)
	wn.mainloop()
	
main()
posit = getPos


wn.mainloop()