#This program holds a method to write a variable to a file, saveVariable,
#and a method to read a variable from a file, loadVariable.
import constants

#Removes all instances of \n character
#Params: line, The line to remove \n from
#Returns: A string with no \n characters
#Author: Inderpreet Dhillon
#Editor: None
def removeNewLine(line):
    new_line = constants.VARIABLE_BLANK
    for i in range(len(line)):
        if line[i] == '\n':
            #Exclude just the \n character, which counts as only one index in the string
            new_line = line[:i] + line[i + 1:]
    return new_line

#Finds a line beginning with a specified string in a list of lines
#Params: lines, The lines to look in
#        name, What the desired line starts with
#Returns: The first line that beigns with name
#Author: Inderpreet Dhillon
#Editor: None
def findVarLine(lines, name):
    #Go through each line from the file
    for line in lines:
        #Take out any \n characters
        stripped = removeNewLine(line)

        #Check if the variable name matches
        if stripped.startswith(name + constants.VARIABLE_SEPARATOR):
            #Return the string
            return stripped

#Reads all lines from a file
#Params: file_name, The file to read from
#Returns: A list of the lines from the file
#Author: Inderpreet Dhillon
#Editor: None
def getFileLines(file_name = constants.TEMP_FILE):
    #Open a file for reading and writing
    var_file = open(file_name, constants.FILE_READ)

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
#Author: Inderpreet Dhillon
#Editor: None
def saveVariable(name, value, file_name = constants.TEMP_FILE):
    lines = getFileLines(file_name)

    #Initialize a list
    line_list = []

    #Go through lines
    for line in lines:
        #Check if we found the line we wanted to change
        if line.startswith(name + constants.VARIABLE_SEPARATOR):
            stripped = removeNewLine(line)
            stripped_split = stripped.split(constants.VARIABLE_SEPARATOR)
            line_list.append(stripped_split[0] + constants.VARIABLE_SEPARATOR + value + '\n')
        else:
            line_list.append(line)

    #Wipe the file
    open(file_name, constants.FILE_WRITE).close()

    #Reopen the file
    var_file = open(file_name, constants.FILE_WRITE)

    #Writes the list
    var_file.writelines(line_list)

    #Close the file
    var_file.close()

#Reads a variable from variables.txt
#Params: name, The name of the variable to read
#        file_name, The name of the file, defaults to variables.txt
#Returns: The value of the variable if found, None otherwise
#Author: Inderpreet Dhillon
#Editor: None
def loadVariable(name, file_name = constants.TEMP_FILE):
    #Open a file for reading and writing
    var_file = open(file_name, constants.FILE_READ_WRITE)

    #Read each line and store it as a list element
    lines = var_file.readlines()

    #Close the file
    var_file.close()

    #Find the line containing the variable
    found_line = findVarLine(lines, name)

    #Make sure line is valid
    if found_line != None:
        return found_line.split(constants.VARIABLE_SEPARATOR)[1]
