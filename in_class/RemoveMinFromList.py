#This program has a function, removeMin, which removes all occurences of the
#smallest number from a list. This program also has testing for the removeMin function.

#Removes all occurences of the smallest number from a list
#Params: numbers, The list of numbers
#Returns: A list with the smallest number(s) removed
def removeMin(numbers):
    #If the list only has one number then that number is the smallest
    if len(numbers) <= 1:
        return []
    else:
        #Assume the first index to be the smallest
        smallest = numbers[0]

        #Find the smallest number
        for i in numbers:
            if i < smallest:
                smallest = i

        #New list for holding valid numbers
        fixedList = []

        #Add numbers that are not the smallest to the new list
        for j in numbers:
            if j != smallest:
                fixedList.append(j)

        return fixedList

#Tests the removeMin method
#Params: numbers, The list of numbers
#        expected, The expected result of the calling removeMin
#Retuns: None
def testRemoveMin(numbers, expected):
    #Store the result of the function being tested
    result = str(removeMin(numbers))

    #Store the testing lines
    test_string = "Test of removeMin(" + str(numbers) + ") returns " + result
    test_string2 = "It should return " + str(expected)

    #Formatting
    print("~" * len(test_string))
    print(test_string)
    #Center method centers a string inbetween a number
    print(test_string2.center(len(test_string)))

    #Check result
    if str(result) == str(expected):
        print("+++++++TEST PASSED+++++++".center(len(test_string)))
    else:
        print("-------TEST FAILED-------".center(len(test_string)))
    print("~" * len(test_string))

def main():
    #Length 0
    testRemoveMin([], [])

    #Length 1
    testRemoveMin([1], [])

    #Length 5
    testRemoveMin([1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6])

    #1 item to Remove
    testRemoveMin([1, 2], [2])

    #2 items to Remove
    testRemoveMin([1, 2, 1], [2])

    #All items to Remove
    testRemoveMin([1, 1, 1, 1, 1], [])

    #Function allows the use of floats and strings and characters, this is intentional
    #List of floats
    testRemoveMin([2.0, 3.0, 1.0], [2.0, 3.0])

    #List of strings
    testRemoveMin(["in", "string"], ["string"])

    #List of characters
    testRemoveMin(['a', 'b', 'A', 'B'], ['a', 'b', 'B'])

if __name__ == "__main__":
    main()
