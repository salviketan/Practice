from binarysearch import binary_search
from util import time_it


##### My Login for indices search (Naive Approach)#####
@time_it
def find_all_occurrences_1(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0
    indices = []

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_value = numbers_list[mid_index]

        if mid_value == number_to_find:
            indices.append(mid_index)
            count = 1
            while (mid_index + count) < len(numbers_list) or (mid_index - count) >= 0:
                if mid_value == number_to_find:
                    # find indices on right hand side
                    if (mid_index + count) < len(numbers_list) and numbers_list[mid_index + count] == number_to_find:
                        indices.append(mid_index + count)

                    # find indices on left hand side
                    if (mid_index - count) >= 0 and numbers_list[mid_index - count] == number_to_find:
                        indices.append(mid_index - count)

                    count+=1
                    if (mid_index + count) < len(numbers_list) and numbers_list[mid_index + count] == number_to_find:
                        mid_value = numbers_list[mid_index + count]
                    else:
                        mid_value = numbers_list[mid_index - count]
                else:
                    break
            return sorted(indices)

        if mid_value < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    
    return -1


##### Efficient Approach #####
@time_it
def find_all_occurrences(numbers_list, number_to_find):
    index = binary_search(numbers_list, number_to_find)

    if index == -1:
        return index
    
    indices = [index]
    # find indices on left hand side
    i = index - 1
    while i >= 0:
        if  numbers_list[i] == number_to_find:
            indices.append(i)
        else:
            break
        i -= 1

    # find indices on right hand side
    i = index + 1
    while i < len(numbers_list):
        if numbers_list[i] == number_to_find:
            indices.append(i)
        else:
            break
        i += 1

    return sorted(indices)



if __name__ == '__main__':
    numbers_list = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    number_to_find = 15
    # numbers_list = [10001 if i >= 10000 and i <= 100000 else i for i in range(10000001)]
    # number_to_find = 10001

    indices = find_all_occurrences(numbers_list, number_to_find)
    print("Number found at indices", indices)
    # indices = find_all_occurrences_1(numbers_list, number_to_find)
    # print("Number found at indices", indices)
