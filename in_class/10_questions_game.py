"""
This program is a number guessing game.
The computer picks a random number between 1 and 100, including 1 and 100
The user has 10 tries to guess the number with a final try at the end.
The game is over when the user guesses the number or runs out of tries
"""

import random

def finish_game(random_number):
    """
    This function will ask the user for their final guess.
    It will compare the guess to the random number.
    If they match the usr wins, otherwise they lose.

    This takes the random number as a parameter
    It returns nothing
    """

    user_guess = int(input("Enter your final guess: "))

    #Check the final guess
    if user_guess == random_number:
        print("You win")
    else:
        print("You lose")


def check_guess(random_number):
    """
    This function asks the user for a guess.
    It takes the users guess and compares it to the random number

    This takes the random number as a parameter
    It will return nothing
    """

    user_guess = int(input("Enter a number between 1 and 100: "))

    #Check the user's guess
    if user_guess < random_number:
        print("Too low")
    else:
        print("Higher or equal")

def main():
    """
    This function call the functions that:
    Ask the user for input,
    Check the input,
    Finish the game.

    Takes no parameters
    Returns nothing
    """

    print("Welcome to The  game of 10 questions")
    print("The computer will pick a random number between 1 and 100")
    print("You have 10 guesses to find the number and a final guess to lock in your choice")
    print("The game is over after all 11 guesses")
    print("")#Blank line for formatting

    random_number = random.randrange(1, 101)

    for i in range(10):
        #Tell the user what guess they are on, don't print a new line
        print(i + 1, end=") ")

        check_guess(random_number)
        print("")#Blank line for formatting

    finish_game(random_number)

main()
