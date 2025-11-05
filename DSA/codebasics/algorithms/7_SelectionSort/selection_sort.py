##### No. of swaps are low####
def selection_sort(elements):
    size = len(elements)

    for i in range(size-1):
        min_index = i
        for j in range(min_index+1,size):
            if elements[j] < elements[min_index]:
                min_index = j

        if i != min_index:
            elements[i], elements[min_index] = elements[min_index], elements[i]

def find_min(elements, start):
    size = len(elements)

    min_val_idx = start
    for j in range(start+1,size):
        if elements[j] < elements[min_val_idx]:
            min_val_idx = j

    return min_val_idx

def selection_sort_1(arr):
    size = len(arr)

    for i in range(size-1):
        min_val_idx = find_min(arr, i)
        if i != min_val_idx:
            arr[i], arr[min_val_idx] = arr[min_val_idx], arr[i]


##### No. of swaps are high####
def selection_sort_2(elements):
    size = len(elements)

    for i in range(size-1):
        min_index = i
        for j in range(min_index+1,size):
            if elements[j] < elements[min_index]:
                elements[j], elements[min_index] = elements[min_index], elements[j]



if __name__ == '__main__':
    tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1,5,8,9],
        [234,3,1,56,34,12,9,12,1300],
        [78, 12, 15, 8, 61, 53, 23, 27],
        [5]
    ]
    for elements in tests:
        selection_sort(elements)
        print(elements)