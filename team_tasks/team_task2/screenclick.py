import turtle
wn = turtle.Screen()
layout = turtle.Turtle()

wn.onscreenclick(layout.goto)

wn.onkey(wn.bye, "space")
wn.listen()
wn.mainloop()
