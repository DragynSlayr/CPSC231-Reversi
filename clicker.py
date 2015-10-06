#This will make the turtle go to where ever you click.

import turtle
wn = turtle.Screen()
clicker = turtle.Turtle()
clicker.shape("turtle")

for i in ['1']:
	wn.onscreenclick(clicker.goto)
	clicker.circle(50)


wn.mainloop()