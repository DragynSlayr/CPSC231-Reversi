#Moves the first word in a line to the end and returns a new string
#Params: sentence, The sentence to alter
#Returns: A new string which is the sentence with the first word moved to the end
#Example: move("Hello World") returns "World Hello"
def move(sentence):
    index = sentence.find(" ")

    #Check if the there is a space in the sentence
    if index > -1:
        #Return the sentence after the space combined with the word before the space
        return sentence[index + 1:] + " " + sentence[:index]
    else:
        return sentence

#Reverses the order of the words in a sentence
#Params: sentence, The sentence to reverse
#Returns: A reversed sentence
#Example: reverse("This is a test") returns "test a is This"
def reverse(sentence):
    toReturn = ""
    last_index = len(sentence)
    #Iterate through the sentence backwards
    for i in range(len(sentence) - 1, 0, -1):
        if sentence[i] == " ":
            #If there is a space then add the word behind it to the return variable
            toReturn += " " + sentence[i + 1:last_index]
            #Update final index
            last_index = i
    #Move the very first word to the end
    toReturn += " " + sentence[:last_index]
    #Remove any leading whitespace
    toReturn = toReturn.lstrip()
    return toReturn

def main():
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Test Cases for Move Function")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    #Empty string
    print("'' should return ''", "returns", "'" + move("") + "'")

    #Space at start
    print("' One' should return 'One '", "returns", "'" + move(" One") + "'")

    #No spaces
    print("'NONE' should return 'NONE'", "returns", "'" + move("NONE") + "'")

    #Single space
    print("'Hello World' should return 'World Hello'", "returns", "'" + move("Hello World") + "'")

    #Two spaces
    print("'A  B C' should return ' B C A'", "returns", "'" + move("A  B C") + "'")

    #Multiple spaces
    print("'This has 3 spaces' should return 'has 3 spaces This'", "returns", "'" + move("This has 3 spaces") + "'")

    #Punctuation
    print("'Put, string in it's place.' should return 'string in it's place. Put,'", "returns", "'" + move("Put, string in it's place.") + "'")

    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Test Cases for Bonus Reverse Function")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    #Empty string
    print("'' should return ''", "returns", "'" + reverse("") + "'")

    #Space at start
    print("' One' should return 'One'", "returns", "'" + reverse(" One") + "'")

    #No spaces
    print("'NONE' should return 'NONE'", "returns", "'" + reverse("NONE") + "'")

    #Single space
    print("'Hello World' should return 'World Hello'", "returns", "'" + reverse("Hello World") + "'")

    #Two spaces
    print("'A  B C' should return 'C B  A'", "returns", "'" + reverse("A  B C") + "'")

    #Multiple spaces
    print("'This has 3 spaces' should return 'spaces 3 has This'", "returns", "'" + reverse("This has 3 spaces") + "'")

    #Punctuation
    print("'Put, string in it's place.' should return 'place. it's in string Put,'", "returns", "'" + reverse("Put, string in it's place.") + "'")

if __name__ == "__main__":
    main()
