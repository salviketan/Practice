from math import floor, sqrt

from o6_primality_test import is_prime


def exactly3divisors(n):
    count = 0
    # print(sqrt(n))
    for i in range(1,floor(sqrt(n))+1):
        if is_prime(i):
            count += 1
    return count



if __name__ == "__main__":
    print(exactly3divisors(10))