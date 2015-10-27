def convert(letter):
    letter = letter[0].upper()
    letters = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
    for i in range(len(letters)):
        if letter in letters[i]:
            return i + 2
    return -1

if __name__ == "__main__":
    print(convert("A"))
    print(convert("E"))
    print(convert("I"))
    print(convert("L"))
    print(convert("O"))
    print(convert("S"))
    print(convert("TR"))
    print(convert("WXYZ"))
    print(convert("~"))
    print(convert("wx"))
