#This program holds a method to write a variable to a file, saveVariable,
#and a method to read a variable from a file, loadVariable.
#The file being used is variables.txt

#Removes all instances of \n character
#Params: line, The line to remove \n from
#Returns: A string with no \n characters
def removeNewLine(line):
    new_line = ""
    for i in range(len(line)):
        if line[i] == "\n":
            #Exclude just the \n character, which counts as only one index in the string
            new_line = line[:i] + line[i + 1:]
    return new_line

#Finds a line beginning with a specified string in a list of lines
#Params: lines, The lines to look in
#        name, What the desired line starts with
#Returns: The first line that beigns with name
def findVarLine(lines, name):
    #Go through each line from the file
    for line in lines:
        #Take out any \n characters
        stripped = removeNewLine(line)

        #Check if the variable name matches
        if stripped.startswith(name + ":"):
            #Return the string
            return stripped

def getFileLines(file_name = "variables.txt"):
    #Open a file for reading and writing
    var_file = open(file_name, "r")

    #Read each line and store it as a list element
    lines = var_file.readlines()

    #Close the file
    var_file.close()

    return lines

#Writes a variable to variables.txt
#Params: name, The name of the variable to write
#        value, The value of the variable to write, must be String
#        file_name, The name of the file, defaults to variables.txr
#Returns: None
def saveVariable(name, value, file_name = "variables.txt"):
    lines = getFileLines(file_name)

    #Initialize a list
    line_list = []

    #Go through lines
    for line in lines:
        #Check if we found the line we wanted to change
        if line.startswith(name + ":"):
            stripped = removeNewLine(line)
            stripped_split = stripped.split(":")
            line_list.append(stripped_split[0] + ":" + value + "\n")
        else:
            line_list.append(line)

    #Wipe the file
    open(file_name, "w").close()

    #Reopen the file
    var_file = open(file_name, "w")

    #Writes the list
    var_file.writelines(line_list)

    #Close the file
    var_file.close()

#Reads a variable from variables.txt
#Params: name, The name of the variable to read
#        file_name, The name of the file, defaults to variables.txt
#Returns: The value of the variable if found, None otherwise
def loadVariable(name, file_name = "variables.txt"):
    #Open a file for reading and writing
    var_file = open(file_name, "r+")

    #Read each line and store it as a list element
    lines = var_file.readlines()

    #Close the file
    var_file.close()

    #Find the line containing the variable
    found_line = findVarLine(lines, name)

    #Make sure line is valid
    if found_line != None:
        return found_line.split(":")[1]

def main():
    saveVariable("State", "N" * 64)
    print(loadVariable("State"))
    saveVariable("Move", str(4))
    print(loadVariable("Move"))

if __name__ == "__main__":
    main()
