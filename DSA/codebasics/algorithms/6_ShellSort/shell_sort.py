
def shell_sort(arr):
    # print("shell_sort")
    size = len(arr)
    gap = size//2
    # count = 0

    while gap > 0:
        for i in range(gap,size):
            anchor = arr[i]
            j = i
            while j >= gap and arr[j - gap] > anchor:
                arr[j] = arr[j - gap]
                # count += 1
                j -= gap
            arr[j] = anchor
            # count += 1
        gap = gap // 2
        
    # print(count)


##### My logic #####
def shell_sort_1(arr):
    # print("shell_sort 1")
    size = len(arr)
    gap = size//2
    # count = 0


    while gap > 0:
        i = 0
        while (gap + i) < size:
            # print(arr[i], arr[gap + i])
            if arr[i] > arr[gap + i]:
                arr[i], arr[gap + i] = arr[gap + i], arr[i]
                # count += 1
            i +=1
        gap -= 1

    # print(count)



if __name__ == '__main__':
    tests = [
        [21,38,29,17,4,25,11,32,9],
        [10, 3, 15, 7, 8, 23, 98, 29],
        [2,1,5,7,2,0,5],
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for arr in tests:
        # shell_sort(arr)
        shell_sort_1(arr)
        print(f'sorted array: {arr}')