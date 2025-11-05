# 1. Naive way
def get_power(x, n):
    result = 1
    for i in range(1, (n+1)):
        result = result * x
    return result

# 2. Efficient Approach
def get_power_1(x, n):
    if n == 0:
        return 1
    temp = get_power_1(x, n//2)     # 1st iter get_power_1(x, 2)
    # 2nd iter get_power_1(x, 1)
    # 3rd iter get_power_1(x, 0)
    temp = temp * temp
    if n % 2 == 0:
        return temp
    else:
        return temp * x
    

# 3. More Efficient Approach
def get_power_2(x, n):
    result = 1
    while n > 0:
        if n % 2 != 0:
            result = result * x
        x = x * x
        n = n//2
    return result


if __name__ == "__main__":
    print("result 1:", get_power(5,5))
    print("result 2:", get_power_1(3,7))
    print("result 3:", get_power_2(5,3))


# odd case
# val_n       1       2       5
# val_x      81       9       3
# val_x=xx  6561      81       9
# ######
# val_res     3       3       1
# n_%_2       1       0       1
# val_res*x  243      3       3


# Even case
# val_n       1       3       6
# val_x      81       9       3
# val_x=xx 6561       81      9
# ######
# val_res     9       1       1
# n_%_2       1       1       0
# val_res*x 729       9       1

# odd case
# val_n       1       3       7
# val_x      81       9       3
# val_x=xx  6561      81       9
# ######
# val_res    27       3       1
# n_%_2       1       1       1
# val_res*x 2187      27       3



# sr.n  3   2   1   0
# even      4       1 
# odd   8       2


# n           6     5      4     3      2       1       0
# multip   6561           81            9       3       1
# even_res 6561           81            9               1
# odd_res         243           27              3       
