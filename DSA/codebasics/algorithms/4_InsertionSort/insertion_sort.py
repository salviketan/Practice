
def insertion_sort(elements):
    size = len(elements)
    # count = 0
    for i in range(1, size):
        anchor = elements[i]
        j = i-1
        while j >= 0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            # count += 1
            j -= 1
        elements[j+1] = anchor
        # count += 1

    # print(count)

    return elements
    

if __name__ == '__main__':
    tests = [
        [2,1,5,7,2,0,5],
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        insertion_sort(elements)
        print(f'sorted array: {elements}')