import turtle

#Setup turtle and window
wn = turtle.Screen()
layout = turtle.Turtle()

#Set screen click action
#Make the Turtle move to that point
wn.onscreenclick(layout.goto)

#Set key to close window and end program
wn.onkey(wn.bye, "space")

#Make the window wait for an event
wn.listen()

#Make the window loop until the porgram is exited
wn.mainloop()
