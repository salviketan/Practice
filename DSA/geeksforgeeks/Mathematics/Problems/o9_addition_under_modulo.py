#### Used when integer overflow occurs
def sum_under_modulo(a, b):
    M = 1000000007
    # return (a+b) % M
    return ((a % M) + (b % M)) % M



if __name__ == "__main__":
    print(sum_under_modulo(92233720368547758,92233720368547758))