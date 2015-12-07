def incrementAll(list_one):
    list_two = []
    for i in range(len(list_one)):
        toAppend = []
        for j in range(len(list_one[i])):
            if type(list_one[i][j]) == type(1):
                toAppend.append(list_one[i][j] + 1)
            elif type(list_one[i][j]) == type('c') and len(list_one[i][j]) == 1:
                toAppend.append(chr(ord(list_one[i][j]) + 1))
            elif type(list_one[i][j]) == type("string"):
                new_string = ""
                for k in list_one[i][j]:
                    new_string += chr(ord(k) + 1)
                toAppend.append(new_string)
        list_two.append(toAppend)
        toAppend = []
    return list_two

if __name__ == "__main__":
    a = [[1, 2, 3], [4, 5], [6]]
    b = incrementAll(a)
    print("A:", a)
    print("B:", b)

    c = [['A', 'B', 'C'], ['D', 'E'], ['F']]
    d = incrementAll(c)
    print("C:", c)
    print("D:", d)

    e = [["Hello", "World", "This"], ["Is", "a"], ["Test"]]
    f = incrementAll(e)
    print("E:", e)
    print("F:", f)
