# 1. Naive way
def divisors(n):
    for i in range(1,n+1):
        if n % i == 0:
            print(i)


# 2. Efficient Approach
def divisors_1(n):
    i = 1
    while n >= (i * i):
        if n % i == 0:
            print(i)
            if (n//i) != i:
                print(n//i)
        i += 1

# 3. More Efficient Approach
def divisors_2(n):
    i = 1
    while n > (i * i):
        if n % i == 0:
            print(i)
        i += 1
    while i > 0:
        if n % i == 0:
            print(n//i)
        i -= 1


if __name__ == "__main__":
    print("result 1")
    divisors(25)
    print("result 2")
    divisors_1(45)
    print("result 3")
    divisors_2(45)