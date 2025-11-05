
# Naive Method
def count_set_bits(n):
    result = 0
    while n > 0:
        if (n%2 != 0):
            result += 1

        # if (n&1 != 0):
        #     result += 1

        # result = result + (n&1)

        n = n//2

    return result


# Brian and Kerningham Algorithm Method
def count_set_bits_2(n):
    result = 0
    while n > 0:
        result += 1
        n = n & (n-1)
    return result


# Lookup table solution
# Initialize the table for set bits count
tbl = [0] * 256

def initialize():
    for i in range(1, 256):
        # print(i, tbl[i & (i - 1)] + 1)
        tbl[i] = tbl[i & (i - 1)] + 1
    # print(tbl)

# Function to count the set bits in an integer
def count_set_bits_3(n):
    return tbl[n & 255] + tbl[(n >> 8) & 255] + tbl[(n >> 16) & 255] + tbl[(n >> 24)]



if __name__ == "__main__":
    print(count_set_bits(13))
    print(count_set_bits_2(13))
    initialize()
    print(count_set_bits_3(29))
