def countSmallerThan(numbers, number):
    count = 0
    for n in numbers:
        if n < number:
            count += 1
    return count

if __name__ == "__main__":
    print(countSmallerThan([1, 2, 3, 4, 6, 7], 5))
