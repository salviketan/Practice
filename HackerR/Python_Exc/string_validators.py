s = input()
alnum = alpha = digit = lower = upper = False
for c in s:
    if (not alnum) and c.isalnum():      # not alnum - provided by chatgpt
        alnum = True
    if (not alpha) and c.isalpha():      # not alpha - provided by chatgpt
        alpha = True
    if (not digit) and c.isdigit():      # not digit - provided by chatgpt
        digit = True
    if (not lower) and c.islower():      # not lower - provided by chatgpt
        lower = True
    if (not upper) and c.isupper():      # not upper - provided by chatgpt
        upper = True

    # Early exit: stop if all conditions are True (By chatgpt)
    if alnum and alpha and digit and lower and upper:
        break    

print(alnum)
print(alpha)
print(digit)
print(lower)
print(upper)

# Another way
print("Another way to write.")

print(any(c.isalnum() for c in s))
print(any(c.isalpha() for c in s))
print(any(c.isdigit() for c in s))
print(any(c.islower() for c in s))
print(any(c.isupper() for c in s))
