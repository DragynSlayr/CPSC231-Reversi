#Replaces all spaces in a string with another string
#Params: starting_string, The string to alter
#        replacement, The string to substitute into the starting_string
#Returns: A new string that is the starting_string with spaces changed to the replacement string
#Example: replace("Hello World", " to The ") returns "Hello to The World",
#         while replace("Hello", "Anything") returns "Hello"
def replace(starting_string, replacement):
    final_string = ""
    for s in starting_string:
        #Check if the character is a space
        if s == " ":
            final_string += replacement
        else:
            final_string += s
    return final_string

def main():
    #No space
    print("ThisString", "That", "->", replace("ThisString", "That"))

    #Single space
    print("Hello world", "X", "->", replace("Hello world", "X"))

    #Double space
    print("This is a  string", "Y", "->", replace("This is a  string", "Y"))

    #No length
    print("", "", "->", replace("", ""))

    #Only spaces
    print("   ", "A", "->", replace("   ", "A"))

    #No replacement
    print("A String", "", "->", replace("A String", ""))

if __name__ == "__main__":
    main()
