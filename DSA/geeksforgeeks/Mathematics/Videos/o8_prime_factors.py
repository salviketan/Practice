from o7_check_prime import check_prime_2

# 1. Naive way
def prime_factors(n):
    if n <= 1:
        return
    for i in range(2,n):
        if check_prime_2(i):
            while (n % i) == 0:
                print(i)
                n = n // i


# 2. Efficient Approach
def prime_factors_1(n):
    temp = n
    if n <= 1:
        return
    x = 2
    while (x * x) < n:
        if check_prime_2(x):
            while (temp % x) == 0:
                print(x)
                temp = temp // x
        x += 1
    if temp > 1:
        print(temp)


# 3. More Efficient Approach
def prime_factors_2(n):
    temp = n
    if n <= 1:
        return
    while (temp % 2) == 0:
        print(2)
        temp = temp // 2
    while (temp % 3) == 0:
        print(3)
        temp = temp // 3
    x = 5
    while (x * x) < n:
        while (temp % x) == 0:
            print(x)
            temp = temp // x
        while (temp % (x + 2)) == 0:
            print(x + 2)
            temp = temp // x
        x += 6
    if temp > 3:
        print(temp)


if __name__ == "__main__":
    print("result 1")
    prime_factors(12)
    print("result 2")
    prime_factors_1(450)
    print("result 3")
    prime_factors_2(450)
