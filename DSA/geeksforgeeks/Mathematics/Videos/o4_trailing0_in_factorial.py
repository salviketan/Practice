from o3_factorial_number import factorial_1

# 1. Naive way
def find_trailing_zeros_1(res):
    zero_count = 0
    while res:
        tail_digit = res % 10
        if tail_digit != 0:
            break
        zero_count += 1
        res = res // 10
    return zero_count

# 2. Efficient Approach
def find_trailing_zeros_2(n):
    zero_count = 0
    prime_no = 5
    while prime_no <= n:
        zero_count += n//prime_no
        prime_no *= 5

    return zero_count


if __name__ == "__main__":
    user_inp = int(input("Enter a number: "))
    result_1 = find_trailing_zeros_1(factorial_1(user_inp))
    result_2 = find_trailing_zeros_2(user_inp)
    print("result 1: ", result_1)
    print("result 2: ", result_2)
    


