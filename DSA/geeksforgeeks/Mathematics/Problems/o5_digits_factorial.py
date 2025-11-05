from math import  log10, floor

def digits_number(n):
    count = 0
    while n != 0:
        count = count + log10(n)
        n -= 1
    return floor(count) + 1


if __name__ == "__main__":
    print("result 1:", digits_number(5))