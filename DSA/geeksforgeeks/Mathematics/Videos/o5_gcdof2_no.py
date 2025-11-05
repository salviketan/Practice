
# 1. Naive way
def naive_gcd(a,b):
    x = min(a, b)
    while x:
        if (a % x == 0) and (b % x == 0):
            return x
        x -= 1


# 2. Euclidean Approach
def gcd_subtraction(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


# 3. Optimised Euclidean Approach
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


if __name__ == "__main__":
    result_1 = naive_gcd(12,15)
    result_2 = gcd_subtraction(12,15)
    result_3 = gcd(12,15)
    print("result 1: ", result_1)
    print("result 2:", result_2)
    print("result 3: ", result_3)