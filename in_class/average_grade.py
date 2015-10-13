#This program asks the user for grades, between 0 and 4.3, and finds the average

#Checks if a grade is in the range 0 - 4.3, inclusive
#Params: grade, The grade to check
#Returns: True if valid, False otherwise
def is_valid_grade(grade):
    return grade >= 0.0 and grade <= 4.3

#Gets the average, total / num_of_grades
#Params: total, The sum of all grades
#        num_of_grades, How many grades were summed
#Returns: The average, total / num_of_grades
def get_average(total, num_of_grades):
    #Check for division by zero
    if (total > 0 and num_of_grades > 0):
        return total / num_of_grades
    else:
        return 0.0

#Asks the user for any number of grades and finds their average
def main():
    #Intro message
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("This porgram finds the average grade from the entered values")
    print("Only values between 0 and 4.3 are valid, enter -1 to exit")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    total = 0.0
    num_of_grades = 0

    grade = float(input("Enter grade: "))

    #Run until user enter -1
    while (grade != -1):
        if not is_valid_grade(grade):
            print("\n" + str(grade) + " is not between 0 and 4.3!\n")
        else:
            total += grade
            num_of_grades += 1

        grade = float(input("Enter grade: "))

    #User has entered -1 if they got here
    average = get_average(total, num_of_grades)

    #%f is a placeholder for a float, average. .2 means only 2 decimal places
    print("\nYour average is %.2f" % average)

main()
