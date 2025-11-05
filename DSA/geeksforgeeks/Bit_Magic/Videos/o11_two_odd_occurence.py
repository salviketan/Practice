# Naive solution
def two_odd_occurence(n):
    for i in n:
        count = 0
        for j in n:
            if i == j:
                count += 1
        if count % 2 != 0:
            print(i)


# Efficient solution
def two_odd_occurence_2(n):
    x = 0
    for i in n:
        x = x ^ i

    k = (x & ~(x-1))

    res_1 = res_2 = 0
    for i in n:
        if (i & k) != 0:
            res_1 = res_1 ^ i
            print(res_1)
        else:
            res_2 = res_2 ^ i

    print(res_1, res_2) 


if __name__ == "__main__":
    x = [10, 3, 3, 5]
    two_odd_occurence(x)
    x = [1,6,5,6,6,1]
    two_odd_occurence_2(x)