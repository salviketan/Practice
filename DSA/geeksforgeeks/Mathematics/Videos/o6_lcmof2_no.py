from o5_gcdof2_no import gcd

# 1. Naive way
def naive_lcm(a,b):
    x = max(a,b)
    while x:
        if x % a ==0 and x % b ==0:
            return x
        x += 1

# 2.  Efficient Approach
def lcm(a,b):
    return (a*b) // gcd(a,b)


if __name__ == "__main__":
    result_1 = naive_lcm(15,20)
    result_2 = lcm(15,20)
    print("result 1: ", result_1)
    print("result 2:", result_2)
