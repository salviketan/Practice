
def multilevel_selection_sort(elements, sort_by_list):
    for sort_by in sort_by_list[-1::-1]:
        print(elements)
        for x in range(len(elements)):
            min_index = x
            for y in range(x, len(elements)):
                if elements[y][sort_by] < elements[min_index][sort_by]:
                    min_index = y

            if x != min_index:
                elements[x], elements[min_index] = elements[min_index], elements[x]


def multilevel_selection_sort_1(elements, order_by_list):
    size = len(elements)

    for i in range(size-1):
        min_index = i
        i_val = ''
        for key in order_by_list:
            i_val += elements[i][key] + ' '
        for j in range(min_index+1,size):
            j_val = ''
            for key in order_by_list:
                j_val += elements[j][key] + ' '
            if j_val < i_val:
                min_index = j
                i_val = j_val

        if i != min_index:
            elements[i], elements[min_index] = elements[min_index], elements[i]



if __name__ == '__main__':
    list_dic = [
        {'First Name': 'Raj', 'Last Name': 'Nayyar'},
        {'First Name': 'Suraj', 'Last Name': 'Sharma'},
        {'First Name': 'Karan', 'Last Name': 'Kumar'},
        {'First Name': 'Jade', 'Last Name': 'Canary'},
        {'First Name': 'Raj', 'Last Name': 'Thakur'},
        {'First Name': 'Raj', 'Last Name': 'Sharma'},
        {'First Name': 'Kiran', 'Last Name': 'Kamla'},
        {'First Name': 'Armaan', 'Last Name': 'Kumar'},
        {'First Name': 'Jaya', 'Last Name': 'Sharma'},
        {'First Name': 'Ingrid', 'Last Name': 'Galore'},
        {'First Name': 'Jaya', 'Last Name': 'Seth'},
        {'First Name': 'Armaan', 'Last Name': 'Dadra'},
        {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
        {'First Name': 'Aahana', 'Last Name': 'Arora'}
    ]

    multilevel_selection_sort(list_dic, ['First Name', 'Last Name'])
    for k in list_dic:
        print(k)