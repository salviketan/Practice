from math import floor

def compute_power(x, n):
    result = 1
    while n > 0:
        if n % 2 != 0:
            result = result * x
        x = x * x
        n = n//2
    return result

def term_of_GP(A,B,N):
    r = B/A
    return floor(A * compute_power(r,N-1))



if __name__ == "__main__":
    print(term_of_GP(1,2,5))