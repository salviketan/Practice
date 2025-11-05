# Efficient Approach
def factorial_1(inp1):
    temp = 1
    if inp1 == 0:
        return temp
    for i in range(1,inp1+1):
        temp *= i
    return temp


def factorial_2(inp2):
    if inp2 == 0:
        return 1
    return factorial_2(inp2 - 1) * inp2


if __name__ == "__main__":
    user_inp = int(input("Enter a number: "))
    result1 = factorial_1(user_inp)
    result2 = factorial_2(user_inp)

    print("result_1: ",result1)
    print("result_2: ",result2)