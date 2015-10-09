total_int = 0.0 # Initialize variable that will store numbers

# Prompt the user for a number
# Convert the string provided by input() to a float
# Add that float to the total
total_int = total_int + float(input("Enter a number: "))

# Repeat above process 4 more times
total_int = total_int + float(input("Enter a number: "))
total_int = total_int + float(input("Enter a number: "))
total_int = total_int + float(input("Enter a number: "))
total_int = total_int + float(input("Enter a number: "))

# Print the average as a float
# %f is a placeholder for the float I will use
# The average is the float
# %.3f limits the average to 3 decimal places after the decimal
print("The average is %.3f" % (total_int / 5.0))
