import turtle
wn = turtle.Screen()
layout = turtle.Turtle()

wn.onscreenclick(layout.goto)

wn.onkey(wn.bye, "SPACE")
wn.mainloop()
