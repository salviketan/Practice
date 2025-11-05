
def find_sum(n):
    if n <= 1:
        return n
    return n + find_sum(n-1)


def fib(m):
    if m < 0:
        return m
    elif m <= 1:
        return m
    return fib(m-1) + fib(m-2)


if __name__ == '__main__':
    print(find_sum(6))
    print(fib(6))