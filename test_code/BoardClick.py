import turtle
import math
import random

wn = turtle.Screen()
wn.setworldcoordinates(0, 0, 100, 100)
wn.setup(800, 800)
wn.tracer(10)

cell_width = 10
cell_height = 10
columns = 10
rows = 10

column_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
row_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

t = turtle.Turtle()
t.up()
t.goto(0, 0)
t.down()
t.speed(0)

def draw_circle(radius):
    circumfrence = 2 * math.pi * radius
    for i in range(360):
        t.forward(circumfrence / 360)
        t.left(1)

def move_to(x, y):
    t.up()
    t.goto(x, y)
    t.down()
    wn.update()

def print_location(x, y, line, isWhite):
    move_to(x, y)
    t.fillcolor("white" if isWhite else "black")
    t.begin_fill()
    draw_circle(cell_width / 2)
    t.end_fill()
    move_to(x - (cell_width / 5), y + (cell_height / 3))
    t.pencolor("black" if isWhite else "white")
    t.write(line)
    t.pencolor("black")
    wn.update()

def isValidSquare(x, y):
    x /= len(column_letters)
    y /= len(row_numbers)
    return (0 <= x and x <= len(column_letters)) and (0 <= y and y <= len(row_numbers))

def check_cell(x, y):
    if isValidSquare(x, y):
        letter = str(column_letters[int(x / cell_width)])
        number = str(row_numbers[int(y / cell_height)])
        line = "(" + letter + ", " + number + ")"
        print_location((column_letters.index(letter) * cell_width) + cell_width / 2, (int(number) - 1) * cell_height, line, random.randint(0,1) == 0)

def run():
    wn.onclick(check_cell)
    wn.onkey(wn.bye, "space")
    wn.listen()
    wn.mainloop()

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

def draw_grid():
    for i in range(rows):
        for j in range(columns):
            draw_cell()
            t.forward(cell_width)
        move_to(0, cell_height * (i + 1))
        wn.update()

def start():
    draw_grid()
    run()

if __name__ == "__main__":
    start()
