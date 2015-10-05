import turtle
import random

#Set up screen
wn = turtle.Screen()
wn.mode("logo")
wn.colormode(255)
wn.setworldcoordinates(-150, -150, 150, 150)

#Set up turtle
t = turtle.Turtle()
t.setheading(0)
t.width(5)

#Create some constant values
move_distance = 15
turn_angle = 90

#Moves the turtle forward
def forward():
    t.forward(move_distance)

#Turns the turtle left
def left():
    t.setheading(t.heading() - turn_angle)

#Moves the turtle backward
def back():
    t.backward(move_distance)

#Turns the turtle right
def right():
    t.setheading(t.heading() + turn_angle)

def main():
    #Set key events
    wn.onkey(forward, "Up")
    wn.onkey(left, "Left")
    wn.onkey(back, "Down")
    wn.onkey(right, "Right")
    wn.onkey(wn.bye, "space")

    #Make the window listen for key events
    wn.listen()

    #Listen for events endlessly
    wn.mainloop()

#Only run if main file
if __name__ == "__main__":
    main()
