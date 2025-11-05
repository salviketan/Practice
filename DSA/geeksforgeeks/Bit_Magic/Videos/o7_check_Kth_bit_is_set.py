# Naive Solution 1
def is_set(n, k):
    x = 1
    i = 0
    while i <= (k - 1):
        if ((n & x) != 0):
            print("Yes")
        else:
            print("No")
        x *= 2
        i += 1


# Naive Solution 2
def is_set_2(n, k):
    x = 1
    i = 0
    while i <= (k - 1):
        if ((n & x) != 0):
            print("Yes")
        else:
            print("No")
        i += 1
        n = n//2


# Efficient Solution 1
def is_set_3(n, k):
    x = 1 << (k -1)
    if ((n & x) != 0):
        print("Yes")
    else:
        print("No")

# Efficient Solution 1
def is_set_4(n, k):
    n = n >> (k -1)
    if ((n & 1) != 0):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    # is_set(5, 2)
    # is_set_2(5, 6)
    # is_set_3(6, 3)
    is_set_3(7,1)