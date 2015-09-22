#Import the file with text information
import Text as info

#Import the file with the grid
import BlankGrid as grid

def display_menu():
    #Display a menu
    print("-----------------")
    print("Menu".center(len("-----------------")))
    print("-----------------")
    print("1) Play the game")
    print("2) View the rules")
    print("3) Exit the game")
    print("-----------------")

def main():
    #Display ascii art
    info.show_art()

    #Display a menu
    display_menu()

    #Prompt the user for input and store it in a variable
    user_option = int(input("Enter your choice: "))

    #Evaluate input
    while user_option is not 3:
        if user_option is 1:
			#Start the game
            grid.printblankgrid()
        elif user_option is 2:
			#Call the show rules menu from the Text module
            info.show_rules()
            
            #Show the menu
            display_menu()
        else:
            print("Invalid option, try again!\n")
            
            #Show the menu
            display_menu()
            
        #Ask for input again
        user_option = int(input("Enter your choice: "))

    #Display good bye
    print("Good bye!")

main()
