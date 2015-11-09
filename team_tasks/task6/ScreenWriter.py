import Constants

def goto(x, y):
    t = Constants.TURTLE
    t.up()
    t.goto(x, y)
    t.down()

def write(message):
    t = Constants.TURTLE
    t.write(message, False, "left", ("Arial", 20, "bold"))

def clearArea(x, y):
    t = Constants.TURTLE
    t.up()
    t.fillcolor("White")
    t.begin_fill()
    for i in range(4):
        t.forward(75)
        t.right(90)
    t.end_fill()
    t.down()

def writeScore(black, white):
    starting_X, starting_y = Constants.TURTLE.pos()

    goto(Constants.BLACK_SCORE_X, Constants.BLACK_SCORE_Y)
    clearArea(Constants.BLACK_SCORE_X, Constants.BLACK_SCORE_Y)
    write("BLACK\n    " + str(black))

    goto(Constants.WHITE_SCORE_X, Constants.WHITE_SCORE_Y)
    clearArea(Constants.WHITE_SCORE_X, Constants.WHITE_SCORE_Y)
    write("WHITE\n    " + str(white))

    goto(starting_X, starting_y)

def writeMessage(message):
    starting_X, starting_y = Constants.TURTLE.pos()

    goto(Constants.MESSAGE_X, Constants.MESSAGE_Y)
    write(message)

    goto(starting_X, starting_y)
