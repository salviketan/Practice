def merge_two_sorted_list(left_list, right_list, key, descending=False):
    merge = []

    if descending:
        while len(left_list) > 0 and len(right_list) > 0:
            if left_list[0][key] >= right_list[0][key]:
                merge.append(left_list.pop(0))
            else:
                merge.append(right_list.pop(0))
    else:
        while len(left_list) > 0 and len(right_list) > 0:
            if left_list[0][key] <= right_list[0][key]:
                merge.append(left_list.pop(0))
            else:
                merge.append(right_list.pop(0))

    merge.extend(left_list)
    merge.extend(right_list)

    return merge
    
def merge_sort(arr, key='name', descending=False):
    size = len(arr)

    if size <= 1:
        return arr
    
    mid = size//2

    left_list = merge_sort(arr[:mid], key, descending)
    right_list = merge_sort(arr[mid:], key, descending)

    return merge_two_sorted_list(left_list, right_list, key, descending)



if __name__ == '__main__':
    elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]

    sorted_list = merge_sort(elements, key='time_hours', descending=True)
    print(sorted_list)