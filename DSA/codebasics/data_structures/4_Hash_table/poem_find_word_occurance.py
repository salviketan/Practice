word_dict = {}

with open(r'C:\Users\ketans\OneDrive - DRCHOKSEY FINSERV PRIVATE LIMITED\Documents\Workspace\DSA\codebasics\4_Hash_table\poem.txt','r') as f:
    for line in f:
        word_list = line.split()
        for key in word_list:
            if key in word_dict:
                word_dict[key] += 1
            else:
                word_dict[key] = 1
    print(word_dict)