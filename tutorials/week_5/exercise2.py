def sumTo(lower_num, higher_num):
	total = 0
	for i in range(lower_num, higher_num + 1):
		total += i
	return total

if __name__ == "__main__":
	num_one = int(input("Enter lowest number: "))
	num_two = int(input("Enter highest number: "))
	total = sumTo(num_one, num_two)
	print("Sum of numbers between %d and %d is %d" % (num_one, num_two, total))
