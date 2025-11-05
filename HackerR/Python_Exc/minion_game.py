def count_sub_str(string, start):
    sub_str_count = 0
    for j in range(len(string) - start):
        sub_str = string[start:start+j]
        if sub_str:
            sub_str_count += string.count(sub_str)
        print("sub_str",sub_str)
        print("sub_str_count",sub_str_count)
    return sub_str_count


def minion_game(string):
    vowels = ['A', 'E', 'I', 'O', 'U']

    consonants_score = 0
    vowels_score = 0        

    for i in range(len(string)):
        print(string[i])
        print(string[i:])
        if string[i] in vowels:
            vowels_score += count_sub_str(string[i:], i)
        else:
            consonants_score += count_sub_str(string[i:], i)

    print(consonants_score, vowels_score)

if __name__ == '__main__':
    s = input()
    minion_game(s)