#Get the turtle module
import turtle

#Ask the user for the size of the screen
screen_size = int(input("Enter screen size: "))

#Create a Screen
wn = turtle.Screen()

#Set up the screen's size
wn.setup(screen_size, screen_size)

#Set background color of the screen
wn.bgcolor("black")

#Store window width and height
width = wn.window_width()
height = wn.window_height()

#Set the coordinates of the screen
wn.setworldcoordinates(-width / 2, -height / 2, width / 2, height / 2)

#Create a turtle object
t = turtle.Turtle()

#Set the turtle line color
t.color("yellow")

#Hide the turtle
t.hideturtle()

#Make the turtle move quicker
t.speed(0)

#Go to starting position without drawing a line
t.up()
t.goto(0, - height / 2)
t.down()

#Set the color of a filled shape
t.fillcolor("yellow")

#Start filling a shape
t.begin_fill()

#Draw a circle for the head
t.circle(width / 2)

#Stop filling a shape
t.end_fill()

#Set the line color
t.color("black")

#Go to left eye position without drawing a line
t.up()
t.goto(-width / 5, height / 20)
t.down()

#Set fill color
t.fillcolor("black")

#Start filling
t.begin_fill()

#Draw a circle for the left eye
t.circle(width / 8)

#Stop filling
t.end_fill()

#Go to right eye position without drawing a line
t.up()
t.goto(width / 5, height / 20)
t.down()

#Start filling
t.begin_fill()

#Draw a circle for the right eye
t.circle(width / 8)

#Stop filling
t.end_fill()

#Go to start position of the smile without drawing a line
t.up()
t.goto(-width / 3.5, -height / 4)
t.down()

#Turn the turtle to the right
t.right(45)

#Start filling
t.begin_fill()

#Draw the smile
for i in range(10):
    t.forward(width / 15)
    t.left(10)

#Stop filling
t.end_fill()

#Go to start position of the nose without drawing a line
t.up()
t.goto(0 + width / 35, -height / 25)
t.down()

#Start filling
t.begin_fill()

#Draw the nose
t.circle(width / 25)

#Stop filling
t.end_fill()

#Make the window exit when clicked on
wn.exitonclick()
