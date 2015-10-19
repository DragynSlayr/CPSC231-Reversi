# Checks if a number is a prime number
# Params: number, The number to check
# Returns: True if the number is prime, False otherwise
# Example: isPrime(5) returns True
def isPrime(number):
	multiples = 0
	# Check every number from 1 to the number (inclusive)
	for i in range(1, number + 1):
		if number % i == 0:
			multiples += 1
	# Check whether the number has more than two multiples
	return multiples <= 2

# Gets the prime number greater than or equal to the input
# Params: number, The number to use
# Returns: The number if it is prime or the next prime number
# Example: firstPrimeFrom(8) returns 11
def firstPrimeFrom(number):
	# The first prime is 2, negative numbers are not prime, neither is 1
	if number <= 2:
		return 2
	elif isPrime(number):
		# Return the number if it prime
		return number
	else:
		# Look for a prime after the number
		number += 1
		while not isPrime(number):
			number += 1
		return number

if __name__ == "__main__":
	print(320, firstPrimeFrom(320))
