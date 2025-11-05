# Naive solution
def power_of_two(n):
    if n == 0:
        return False
    while n != 1:
        if n%2 != 0:
            return False
        n = n//2
    return True


# Efficient solution
def power_of_two_2(n):
    if n == 0:
        return False
    return ((n & (n-1)) == 0)
# single line expression
def power_of_two_3(n):
    return (n and ((n & (n-1)) == 0))



if __name__ == "__main__":
    print(power_of_two(2))
    print(power_of_two_2(6))
    print(power_of_two_3(0))