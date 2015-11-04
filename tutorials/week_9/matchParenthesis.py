#Checks if a line has matching parenthesis ()
#Params: line, The line to check
#Returns: True if the line has matching parenthesis, False otherwise
def hasMatchingParenthesis(line):
    #Initialize a counter to keep track of brackets
    count = 0

    #Go through the line
    for i in line:
        #Change the counter based on the bracket
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1

        #Counter should never go below zero
        if count < 0:
            return False

    #Counter has to equal zero at the end
    return count == 0
