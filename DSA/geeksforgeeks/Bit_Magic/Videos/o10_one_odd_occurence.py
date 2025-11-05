# Naive solution
def find_odd_occurence(n):
    for i in n:
        count = 0
        for j in n:
            if i == j:
                count += 1
        if count % 2 != 0:
            return i


# Efficient solution
# x ^ 0 = x
# x ^ y = y ^ x
# x ^ (y ^ z) = (x ^ Y) ^ z
# x ^ x = 0
def find_odd_occurence_2(n):
    res = 0
    for i in n:
        res = res ^ i
    
    return res

if __name__ == "__main__":
    x = [4,3,4,4,4,5,5]
    print(find_odd_occurence(x))
    x = [4,4,7,4,8,7,7,7,8]
    print(find_odd_occurence_2(x))