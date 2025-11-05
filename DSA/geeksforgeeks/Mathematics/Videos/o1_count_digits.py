n = int(input("Enter a number: "))

def count_digit(n):
    if n == 0:
        return 1
    count = 0
    while n != 0:
        n = n//10
        count += 1
    return count

print(f"Digit in given number: {count_digit(n)}")