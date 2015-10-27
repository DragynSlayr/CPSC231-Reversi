import turtle
import math

#Set up screen
wn = turtle.Screen()
wn.setworldcoordinates(0, 0, 100, 100)
wn.setup(1920, 1080)
wn.tracer(0)

#Set up turtle
t = turtle.Turtle()
t.speed(0)

#Constants for cell letters and numbers
column_letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
row_numbers = [1, 2, 3, 4, 5, 6, 7, 8]

#Constants
columns = len(column_letters)
rows = len(row_numbers)
cell_width = 13
cell_height = 13

#Changes color
isWhite = True

#Draws a circle
#Params: radius, The radius of the circle
#Returns: None
def draw_circle(radius):
    circumference = 2 * math.pi * radius

    #Draw the circle using the circumference
    for i in range(360):
        t.forward(circumference / 360)
        t.left(1)

#Moves to a location, without drawing a line
#Params: x, The x coordinate of the location
#        y, The y coordinate of the location
#Returns: None
def move_to(x, y):
    #Move to the location
    t.up()
    t.goto(x, y)
    t.down()

    #Redraw the window
    wn.update()

#Draws a circle at a location, then writes that location in the circle
#Params: x, The x location of the turtle
#        y, The y location of the turtle
#        line, The text to write
#        isWhite, whether the circle should be white
#Returns: None
def draw_at_location(x, y, line, isWhite):
    move_to(x, y)

    #Set fill color to white if isWhite is true, black otherwise
    t.fillcolor("white" if isWhite else "black")

    #Draw and fill circle
    t.begin_fill()
    draw_circle(cell_width / 2)
    t.end_fill()

    #Move to center of cell
    move_to(x - (cell_width / (cell_width / 2)), y + (cell_height / (cell_height / 3)))

    #Set line color to black if isWhite is true, white other wise
    t.pencolor("black" if isWhite else "white")
    t.write(line)
    t.pencolor("black")

    #Update the window
    wn.update()

#Checks if a piece can be placed at a location
#Params: x, The x coordinate of the location
#        y, The y coordinate of the location
#Returns: True if a piece can be placed at a location, False otherwise
def isValidSquare(x, y):
    #Convert the x and y to the coordinate of a cell
    x /= cell_width
    y /= cell_height

    #Check if the x and y are in any cell
    return (0 <= x and x <= len(column_letters)) and (0 <= y and y <= len(row_numbers))

#Places a piece at a location if it is a cell
#Params: x, The x location to check
#        y, The y location to check
#Returns: None
def place_piece(x, y):
    #Check if the point is valid
    if isValidSquare(x, y):
        #Convert x and y to column and row
        letter = str(column_letters[int(x / cell_width)])
        number = str(row_numbers[(len(row_numbers) - 1 ) - int(y / cell_height)])
        line = "(" + letter + ", " + number + ")"

        #Calculate location
        x_location = (column_letters.index(letter) * cell_width) + (cell_width / 2)
        y_location = (row_numbers[int(y / cell_height)] - 1) * cell_height

        #Use global variable
        global isWhite


        #Place the piece
        draw_at_location(x_location, y_location, line, isWhite)

        #Flip the value of isWhite
        isWhite = not isWhite

#The main loop of the function
#Waits for input from the user
#Params: None
#Returns: None
def run():
    wn.onclick(place_piece)
    wn.onkey(wn.bye, "space")
    wn.listen()
    wn.mainloop()

#Draws a square at the turtle's location
#Params: None
#Returns: None
def draw_cell():
    t.fillcolor("green")
    t.begin_fill()
    for i in range(2):
        t.forward(cell_width)
        t.left(90)
        t.forward(cell_height)
        t.left(90)
    t.end_fill()
    t.fillcolor("white")
    wn.update()

#Draws the game board
#Parmas: None
#Returns: None
def draw_grid():
    for i in range(rows):
        for j in range(columns):
            draw_cell()
            t.forward(cell_width)
        move_to(0, cell_height * (i + 1))
        wn.update()

#The main function, draws board then waits for user input
#Params: None
#Returns: None
def start():
    draw_grid()
    place_piece(50, 50)
    place_piece(40, 50)
    place_piece(40, 40)
    place_piece(50, 40)
    run()

if __name__ == "__main__":
    start()
