def merge_two_sorted_list(a, b, arr, key, descending=False):
    len_a = len(a)
    len_b = len(b)
    i = j = k= 0

    while i < len_a and j < len_b:
        if descending:
            if a[i][key] >= b[j][key]:
                arr[k] = a[i]
                i += 1
            else:
                arr[k] = b[j]
                j += 1
            k += 1
        else:
            if a[i][key] <= b[j][key]:
                arr[k] = a[i]
                i += 1
            else:
                arr[k] = b[j]
                j += 1
            k += 1

    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1

    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1

    
def merge_sort(arr, key='name', descending=False):
    size = len(arr)

    if size <= 1:
        return
    
    mid = size//2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left, key, descending)
    merge_sort(right, key, descending)

    merge_two_sorted_list(left, right, arr, key, descending)



if __name__ == '__main__':
    elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]

    merge_sort(elements, key='time_hours',descending=True)
    print(elements)