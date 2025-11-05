from math import factorial


def my_factorial(n):
    result = 1
    for i in range(2, n+1):
        result = result * i
    return result



if __name__ == "__main__":
    print("result 1:", factorial(3))
    print("result 1:", my_factorial(3))