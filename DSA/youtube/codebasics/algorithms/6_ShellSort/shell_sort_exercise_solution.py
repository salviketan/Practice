
def shell_sort(arr):
    n = len(arr)
    div = 2
    gap = n//div
    while gap > 0:
        index_to_delete = []
        for i in range(gap,n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] >= temp:
                if arr[j - gap] == temp:
                    index_to_delete.append(j)
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        index_to_delete=list(set(index_to_delete))
        index_to_delete.sort()
        if index_to_delete:
            for i in index_to_delete[-1::-1]:
                del arr[i]
        div *= 2
        n = len(arr)
        gap = n//div
        

def my_shell_sort(arr):
    size = len(arr)
    gap = size//2
    gap_repeat_count = 0

    while gap >= 0 and gap_repeat_count == 0:
        if gap == 0:
            gap = 1
            gap_repeat_count += 1
        i = gap
        while i < size:
            anchor_index = i
            anchor = arr[i]
            j = i
            if arr[j - gap] == anchor: 
                arr.pop(anchor_index)
                size -= 1
                anchor = arr[i]
            while j >= gap and arr[j - gap] > anchor:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = anchor
            i += 1
        gap = gap//2       


# def shell_sort_1(arr):
#     # print("shell_sort 1")
#     size = len(arr)
#     gap = size//2
#     # count = 0


#     while gap > 0:
#         i = 0
#         while (gap + i) < size:
#             # print(arr[i], arr[gap + i])
#             if arr[i] > arr[gap + i]:
#                 arr[i], arr[gap + i] = arr[gap + i], arr[i]
#                 # count += 1
#             i +=1
#         gap -= 1

#     # print(count)



if __name__ == '__main__':
    arr_list = [2,1,5,7,2,0,5,1,2,9,5,8,3]

    shell_sort(arr_list)
    print(f'sorted array: {arr_list}')