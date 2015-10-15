#This program takes grades from the user until they enter -1,
#then finds the average of those grades

#Checks if a grade is with in the range of 0 to 4.3
#Params: grade, The grade to check
#Returns: True if the grade is valid, False otherwise
def isValidGrade(grade) :
    #return grade > 0 and grade < 4.3
    #Did not allow 0 or 4.3 to be valid, even though they are
    #With input of 0 or 4.3 this method return False when it should be True
    #Used testing and visual inspection the code to find this error
    return grade >= 0 and grade <= 4.3

#Gets a grade from the user if they don't enter -1
#Params: None
#Returns: grade if it is valid or -1
def getGrade() :
    grade = float(input("Enter a letter grade point value (or -1 to quit): "))
    #while (grade != -1 or not isValidGrade(grade)):
    #With and both statements must be true for the condition to be satisfied,
    #while with or only one condition needs to be true
    #With input of -1 the loops runs when it should not
    #Print statement to look at the condition and both parts of the condition
    while (grade != -1 and not isValidGrade(grade)):
        print(grade, "is not valid.  A letter grade point value must be between 0 and 4.3.")
        grade = float(input("Enter a letter grade point value (or -1 to quit): "))
    return grade

#Gets the average of some values from the user
#Params: None
#Returns: The average of the values from the user
def average() :
    grade = getGrade()
    #sum = 0.0
    #Sum is the name of a native python method and should not be used for a variable name
    #This error doesn't have an immediate effect on this program's functionality
    #Used our knowledge of python's methods to recognize the conflict
    total = 0.0
    #counter = 1
    #counter starts at 1 instead of 0
    #This means that the divsion of sum/counter is incorrect
    #Using any sequence of grades, for example: 3, 2 returns 1.667 instead of 2.5
    #Test values and manual calculations were used to find this error
    counter = 0.0
    while (grade != -1):
        counter = counter + 1
        total = total + grade
        #getGrade()
        #Not updating the value of grade causes an infinite loop
        #Input grades do not matter, this loop was infinite in almost every causes
        #Testing and visual inspection was used to find this error
        grade = getGrade()
    return total / counter

print(average())
