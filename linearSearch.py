# A simple Linear search 
# github @AminuAhmadh


def linearSearch(list, n): # list to search and number to find
    index = 0
    for i in range(len(list)): # iterate through the list
        if list[i] == n: # if value of i equals n
            index = i # assign index
            print('Found it at index', index+1)
            exit()
    print('Not Found') # not found


linearSearch([1,2,5,], 2)