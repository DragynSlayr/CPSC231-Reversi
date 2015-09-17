def start_game():
    print("Play")

def display_rules():
    print("Rules")

def display_menu():
    #Display a menu
    print("Menu".center(len("-----------------")))
    print("-----------------")
    print("1) Play the game")
    print("2) View the rules")
    print("3) Exit the game")
    print("-----------------")

def main():
    #Display a greeting
    print("Welcome to Reversi!\n")

    #Display a menu
    display_menu()

    #Prompt the user for input and store it in a variable
    user_option = int(input("Enter your choice: "))

    #Evaluate input
    while user_option is not 3:
        if user_option is 1:
            start_game()
        elif user_option is 2:
            display_rules()
        else:
            print("Invalid option, try again!\n")
            display_menu()
        user_option = int(input("Enter your choice: "))

    #Display good bye
    print("Good bye!")

main()
