# bubble sort


def bubble_sort(numList):
    iteration = len(numList) -1
    for i in range(iteration):
        for j in range(iteration):
            if numList[j] > numList[j+1]:
                temp = numList[j]
                numList[j] = numList[j+1] 
                numList[j+1] = temp
    return numList
print(bubble_sort([9,7,8,6,4,5,2,0,1,3,33]))
