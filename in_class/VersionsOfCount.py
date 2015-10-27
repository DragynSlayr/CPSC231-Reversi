#This program contains three functions that each count occurrences of a letter in a sentence
#One function uses a for loop with index
#The next function uses a for loop that iterates through each character in a sentence
#The final function uses a while loop

#Counts occurrences of a letter in a sentence using a standard for loop
#Params: sentence, The sentence to count occurrences in
#        letter, The letter to count occurrences of
#Returns: The number of occurrences of letter in sentence, 0 if no occurrences
#Example: countUsingFor("alphabet", "a") returns 2
def countUsingFor(sentence, letter):
    count = 0
    for i in range(len(sentence)):
        if sentence[i] == letter:
            count += 1
    return count

#Counts occurrences of a letter in a sentence using a for loop that
#iterates through a each character in the sentence
#Params: sentence, The sentence to count occurrences in
#        letter, The letter to count occurrences of
#Returns: The number of occurrences of letter in sentence, 0 if no occurrences
#Example: countUsingFor("hello, world!", "l") returns 3
def countUsingForEach(sentence, letter):
    count = 0
    for char in sentence:
        if char == letter:
            count += 1
    return count

#Counts occurrences of a letter in a sentence using a while loop
#Params: sentence, The sentence to count occurrences in
#        letter, The letter to count occurrences of
#Returns: The number of occurrences of letter in sentence, 0 if no occurrences
#Example: countUsingFor("abx", "b") returns 1
def countUsingWhile(sentence, letter):
    count = 0
    index = 0
    while index < len(sentence):
        if sentence[index] == letter:
            count += 1
        index += 1
    return count

def main():
    #Test method that uses regular for loop
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\t\tcountUsingFor Testing")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    #More than one occurrence
    print("countUsingFor('abcabc', 'a') should return 2, returns", countUsingFor("abcabc", "a"))

    #More than one occurrence with spaces
    print("countUsingFor('abcabc abca', 'a') should return 4, returns", countUsingFor("abcabc abca", "a"))

    #One occurrence
    print("countUsingFor('abc', 'a') should return 1, returns", countUsingFor("abc", "a"))

    #No occurrences
    print("countUsingFor('bc  sd', 'a') should return 0, returns", countUsingFor("bc  sd", "a"))

    #Empty sentence
    print("countUsingFor('', 'a') should return 0, returns", countUsingFor("", "a"))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


    #Test method that uses for loop with char
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\t\tcountUsingForEach Testing")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    #More than one occurrence
    print("countUsingForEach('abcabc', 'a') should return 2, returns", countUsingForEach("abcabc", "a"))

    #More than one occurrence with spaces
    print("countUsingForEach('abcabc abca', 'a') should return 4, returns", countUsingForEach("abcabc abca", "a"))

    #One occurrence
    print("countUsingForEach('abc', 'a') should return 1, returns", countUsingForEach("abc", "a"))

    #No occurrences
    print("countUsingForEach('bc  sd', 'a') should return 0, returns", countUsingForEach("bc  sd", "a"))

    #Empty sentence
    print("countUsingForEach('', 'a') should return 0, returns", countUsingForEach("", "a"))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")


    #Test method that uses while loop
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\t\tcountUsingWhile Testing")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    #More than one occurrence
    print("countUsingWhile('abcabc', 'a') should return 2, returns", countUsingWhile("abcabc", "a"))

    #More than one occurrence with spaces
    print("countUsingWhile('abcabc abca', 'a') should return 4, returns", countUsingWhile("abcabc abca", "a"))

    #One occurrence
    print("countUsingWhile('abc', 'a') should return 1, returns", countUsingWhile("abc", "a"))

    #No occurrences with spaces
    print("countUsingWhile('bc  sd', 'a') should return 0, returns", countUsingWhile("bc  sd", "a"))

    #Empty sentence
    print("countUsingWhile('', 'a') should return 0, returns", countUsingWhile("", "a"))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    
if __name__ == "__main__":
    main()
