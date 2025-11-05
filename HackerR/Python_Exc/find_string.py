# naive solution
def count_substring_1(string, sub_string):
    count = 0
    for i in range(len(string)):
        start = i
        end = len(sub_string) + i
        if sub_string == string[start:end]:
            count += 1
        if len(string) == (i+1):
            print("Naive solution took %d Attempt to solve"%(i+1))

    return count


# Efficient solution
def count_substring_2(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
        if (len(string) - len(sub_string) + 1) == (i+1):
            print("Efficient solution took %d Attempt to solve"%(i+1))
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring_1(string, sub_string)
    print(count)
    print("----------")
    count_2 = count_substring_2(string, sub_string)
    print(count_2)