import turtle
wn = turtle.Screen()
layout = turtle.Turtle()

wn.onscreenclick(layout.goto)

wn.onkey("SPACE", wn.bye)
wn.mainloop()
	
	
