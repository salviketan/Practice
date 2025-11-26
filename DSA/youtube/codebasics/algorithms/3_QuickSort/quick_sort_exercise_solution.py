# Lomuto partition scheme

from util import time_it

def partition(elements, start, end):
    pivot = elements[end]
    p_index = start

    for i in range(start, end):
        if elements[i] <= pivot:
            elements[p_index], elements[i] = elements[i], elements[p_index]
            p_index += 1

    elements[p_index], elements[end] = elements[end], elements[p_index]

    return p_index   
        
# @time_it
def quick_sort(elements, start, end):
    if len(elements) == 1:
        return
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi - 1)
        quick_sort(elements, pi + 1, end)


##### My logic #####
def partition_1(elements, p_index, right_index):
    pivot_index = right_index
    pivot_val = elements[pivot_index]

    while p_index < right_index:
        while p_index < right_index and elements[p_index] <= pivot_val:
            p_index += 1

        i = p_index
        while i <= right_index and elements[i] > pivot_val:
            i += 1

        if i <= right_index:
            elements[p_index], elements[i] = elements[i], elements[p_index]
        else:
            p_index += 1


    return right_index - 1 
        
# @time_it
def quick_sort_1(elements):
    p_index = 0
    right_index = len(elements) - 1
    while p_index < right_index:
        pi = partition_1(elements, p_index, right_index)
        right_index = pi


        
##########
if __name__ == '__main__':
    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]
    # elements = ["mona", "dhaval", "aamir", "tina", "chang"]

    for elements in tests:
        quick_sort(elements, 0, len(elements)-1)
        print(f'sorted array: {elements}')
        # quick_sort_1(elements)
        # print(f'sorted array: {elements}')
