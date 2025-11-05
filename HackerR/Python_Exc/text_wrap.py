from math import ceil
import textwrap


def wrap(string, max_width):
    rows = ''
    for i in range(0,len(string),max_width):
        rows += string[i:max_width+i] + '\n'
    return rows.strip()


def buildin_wrap(string, max_width):
    return textwrap.fill(string, max_width) 


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
    print()
    print("Build-in textwrap module")
    result_2 = buildin_wrap(string, max_width)
    print(result_2)