def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        substring = string[i:i+k]

        seen = set()
        result = ''
        for char in substring:
            if char not in seen:
                seen.add(char)
                result += char
        print(result)

if __name__ == '__main__':
    string, k = input(), int(input())
    # string, k = 'AABCAAADA', int('3')
    merge_the_tools(string, k)
