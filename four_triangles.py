#Draws four triangles with input from the user for length of sides
#Side lengths must be positive

#Need the math and turtle modules
import math
import turtle

def get_angle(opposite, hypotenuse):
    #Get the angle between adjacent and hypotenuse, in degrees
    angle_in_radians = math.asin(opposite / hypotenuse)
    angle_in_degrees = math.degrees(angle_in_radians)

    return angle_in_degrees


def get_hypotenuse(adjacent, opposite):
    #Gets the hypotenuse of a triangle with side lengths
    hypotenuse_squared = (adjacent ** 2) + (opposite ** 2)
    hypotenuse = math.sqrt(hypotenuse_squared)

    return hypotenuse

#Set up turtle and window
wn = turtle.Screen()
t = turtle.Turtle()

#Loop 4 times
for i in range(4):
    #Get lengths
    adjacent = int(input("Enter adjacent side length: "))
    opposite = int(input("Enter opposite side length: "))
    print()

    #Calculate hypotenuse
    hypotenuse = get_hypotenuse(adjacent, opposite)

    #Calculate angle
    angle = get_angle(opposite, hypotenuse)

    #Draw the adjacent side
    t.right(90)
    t.forward(adjacent)

    #Draw the opposite side
    t.left(90)
    t.forward(opposite)

    #Draw the hypotenuse
    t.left(180)
    t.right(90 - angle)
    t.forward(hypotenuse)
    t.left(180 + (90 - angle))

    #Move to next area
    t.up()
    t.forward(opposite + 10)
    t.down()

#Wait for click to stop
wn.exitonclick()
