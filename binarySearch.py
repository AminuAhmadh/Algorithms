
#binary search
def binary_search(ordered_list, item): 
    # given a list and an item contained in that list, return the index of the item.
    size_of_list = len(ordered_list) - 1 
    index_of_first_element = 0 
    index_of_last_element = size_of_list 
    while index_of_first_element <= index_of_last_element: 
        mid_point = (index_of_first_element + index_of_last_element)//2 
        if ordered_list[mid_point] == item: 
            return mid_point
        if item > ordered_list[mid_point]: 
            index_of_first_element = mid_point + 1 
        else: 
            index_of_last_element = mid_point - 1 
    if index_of_first_element > index_of_last_element: 
        # returns None if item searched not in list
        return None

# example
print(binary_search([1,2,5,6,8], 8)) # returns 4
