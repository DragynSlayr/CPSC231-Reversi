#Recursively counts how many numbers in a list are smaller than a number
#Params: num_list, The list of numbers to check
#        num, The num to check against
def countSmallerThan(num_list, num):
    #If the list is empyt then return 0
    if len(num_list) == 0:
        return 0
    else:
        #Check if the last index is smaller than num
        if num_list[-1] < num:
            return 1 + countSmallerThan(num_list[:-1], num)
        else:
            return 0 + countSmallerThan(num_list[:-1], num)

def main():
    l = [1, 2, 3]
    num = 4
    print(countSmallerThan(l, num))

if __name__ == '__main__':
    main()
