def flip(list_2d):
    flipped = []
    for i in range(len(list_2d)):
        flipped.append(list_2d[i][::-1])
    return flipped

if __name__ == "__main__":
    a = [[1, 2, 3], [5, 6, 7]]
    b = flip(a)

    print("A:", a)
    print("B:", b)
