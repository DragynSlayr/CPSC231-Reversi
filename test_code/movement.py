import turtle
import random

wn = turtle.Screen()
wn.mode("logo")
wn.colormode(255)
wn.setworldcoordinates(-150, -150, 150, 150)

t = turtle.Turtle()
t.setheading(0)
t.width(5)

move_distance = 15
turn_angle = 30

def forward():
    t.forward(move_distance)

def left():
    t.setheading(t.heading() - turn_angle)

def back():
    t.backward(move_distance)

def right():
    t.setheading(t.heading() + turn_angle)

def main():
    wn.onkey(forward, "Up")
    wn.onkey(left, "Left")
    wn.onkey(back, "Down")
    wn.onkey(right, "Right")
    wn.onkey(wn.bye, "space")
    wn.listen()
    wn.mainloop()

if __name__ == "__main__":
    main()
