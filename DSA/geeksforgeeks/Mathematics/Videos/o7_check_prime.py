# 1. Naive way
def check_prime(n):
    if n <= 1:
        return False
    x = 2
    while x < n:
        if n % x == 0:
            return False
        x += 1
    return True

# 2. Efficient Approach
def check_prime_1(n):
    if n <= 1:
        return False
    x = 2
    while (x * x) <= n:
        if n % x == 0:
            return False
        x += 1
    return True

# 3. More Efficient Approach
def check_prime_2(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    x = 5
    while (x * x) <= n:
        # print(x)
        if n % x == 0 and n % (x + 2):
            return False
        x += 6
    return True


if __name__ == "__main__":
    result_1 = check_prime(65)
    result_2 = check_prime_1(3)
    result_3 = check_prime_2(121)
    print("result 1: ", result_1)
    print("result 2:", result_2)
    print("result 3:", result_3)
    result_3 = check_prime_2(1031)
    print("result 3:", result_3)