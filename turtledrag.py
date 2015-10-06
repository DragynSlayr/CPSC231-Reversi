import turtle
wn = turtle.Screen()

p1 = turtle.Turtle()

p1.speed(0)
p1.penup()
p1.shape("circle")

def drag():
	p1.ondrag(p1.goto)
	
drag()
wn.mainloop()