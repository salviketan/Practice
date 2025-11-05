from o7_check_prime import check_prime_2


# 1. Naive way
def print_primes(n):
    for i in range(2,n+1):
        if check_prime_2(i):
            print(i)


# 2. Efficient Approach
def print_primes_1(n):
    n = n + 1
    is_primes = [True] * n
    idx = 2
    while (idx * idx) < n:
        if is_primes[idx]:
            val = idx * 2
            while val < n:
                is_primes[val] = False
                val = val + idx
        idx += 1
    for i in range(2, n):
        if is_primes[i]:
            print(i)



# 3. More Efficient Approach
def print_primes_2(n):
    n = n + 1
    is_primes = [True] * n
    idx = 2
    while idx < n:
        if is_primes[idx]:
            print(idx)
            val = idx * idx
            while val < n:
                is_primes[val] = False
                val = val + idx
        idx += 1


if __name__ == "__main__":
    print("result 1")
    print_primes(10)
    print("result 2")
    print_primes_1(20)
    print("result 3")
    print_primes_2(20)