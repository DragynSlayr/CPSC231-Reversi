#Multiplies any part of a string and returns that new string
#Params: line, The line to multiply
#        multiplier, How many times to copy the string
#        start, The optional starting index; defaults to 0
#        end, The optional ending index; defaults to length of the string
#Retuns: A string that is a multiplied, concatenated substring of line
def mult(line, multiplier, start = 0, end = None):
    #Default to the end being the length of the string if no end was used
    if end == None:
        end = len(line)
    #Slice the line and multiply it
    multiplied = line[start:end] * multiplier
    return multiplied

#Tests the mult method
#Params: line, The line to multiply
#        multiplier, How many times to copy the string
#        start, The optional starting index; defaults to 0
#        end, The optional ending index; defaults to length of the string
#        expected, The expected result of the calling mult
#Retuns: None
def testMult(line, multiplier, start, end, expected):
    #Store the result of the function being tested
    result = mult(line, multiplier, start, end)

    #Store the testing lines
    test_string = "Test of mult("+ line +", "+ str(multiplier) + ", " + str(start) + ", " + str(end) + ") returns " + result
    test_string2 = "It should return " + expected

    #Formatting
    print("~" * len(test_string))
    print(test_string)
    #Center method centers a string inbetween a number
    print(test_string2.center(len(test_string)))

    #Check result
    if result == expected:
        print("+++++++TEST PASSED+++++++".center(len(test_string)))
    else:
        print("\t\t-------TEST FAILED-------".center(len(test_string)))
    print("~" * len(test_string))

def main():
    #No start or end
    testMult("Hello", 3, None, None, "HelloHelloHello")

    #Start of 2
    testMult("Hello", 3, 2, None, "llollollo")

    #End of 4
    testMult("Hello", 3, None, 4, "HellHellHell")

    #Start of 3 end of 4
    testMult("Hello", 3, 3, 5, "lololo")

    #Negative end
    testMult("Hello", 3, None, -2, "HelHelHel")

    #Negative start
    testMult("Hello", 3, -2, None, "lololo")

    #Only 1 repetition
    testMult("Hello", 1, None, None, "Hello")

    #Several repetitions
    testMult("Hi", 8, None, None, "HiHiHiHiHiHiHiHi")

if __name__ == "__main__":
    main()
