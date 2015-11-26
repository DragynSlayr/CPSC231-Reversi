import time
import string
import MainMenu
import Constants

#Times how long a function takes to execute
#Params: function, The function to time
#        parameters, The functions parameters, separated by commas
#Returns: Time taken to execute a function, in seconds
def timeFunction(function, *parameters):
    #Get the current system time
    start_time = time.clock()

    #Call the function with it's parameters
    if type(*parameters) != type(None):
        function(*parameters)
    else:
        function()

    #Get the ending time
    end_time = time.clock()

    #Convert time to seconds
    total = (("%.3f") % (end_time - start_time))

    #Return elapsed time
    return float(total)

def main():
    trial_file = open("MainMenu.Main1.txt", "w")
    trial_file.write("Name:MainMenu.Main\n")
    for i in range(1, 11):
        time_taken = timeFunction(MainMenu.main, None)
        trial_file.write("Trial " + str(i) + ":" + str(time_taken) + "s\n")
        Constants.WINDOW.reset()
        Constants.TURTLE.reset()
    trial_file.close()

if __name__ == "__main__":
    main()
