def mutate_string_list(string, position, character):
    str_list = list(string)
    str_list[position] = character
    return ''.join(str_list)

def mutate_string_slice(string, position, character):
    return string[:position] + character + string[position+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new_list = mutate_string_list(s, int(i), c)
    s_new_slice = mutate_string_slice(s, int(i), c)
    print(s_new_list)
    print(s_new_slice)