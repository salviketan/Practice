# Hoare partition scheme

def partition(elements, start, end):
    print("partition", start, end)
    pivot_index = start
    pivot_val = elements[pivot_index]

    print("1",elements)
    while start < end:
        while start < end and elements[start] <= pivot_val:
            start += 1

        while elements[end] > pivot_val:
            end -= 1

        if start < end:
            elements[start], elements[end] = elements[end], elements[start]

    print("2",elements)
    elements[pivot_index], elements[end] = elements[end], elements[pivot_index]
    print("3",elements)
    return end   
        

def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi - 1)
        quick_sort(elements, pi + 1, end)

if __name__ == '__main__':
    elements = [11, 9, 29, 7, 2, 15, 28]
    quick_sort(elements, 0, len(elements)-1)
    print(elements)