row = 4
print("Right half triangle pattern using *")
for r in range(1, row + 1):
    print("* " * r)

print()

row = 4
print("Inverted right half triangle pattern using *")
for ir in range(row, 0, -1):
    print("* " * ir)

print()

row = 4
print("full pyramid pattern using * (derived from Left half triangle)")
for ls in range(1, row + 1):
    print(" " * (row - ls) + "* " * ls)

print()

row = 4
print("Inverted full pyramid pattern using * (derived from Inverted Left half triangle)")
for ils in range(row, 0, -1):
    print(" " * (row - ils) + "* " * ils)

print()

row = 4
print("Left half triangle pattern using *")
for l in range(1, row + 1):
    print(" " * ((row - l) * 2) + "* " * l)

print()

row = 4
print("Inverted Left half triangle pattern using *")
for il in range(row, 0, -1):
    print(" " * ((row - il) * 2)+ "* " * il)

print()

row = 4
print("Pyramid pattern using *")
for i in range(0, row):
    print(" " * (row-(i+1)) + "*" * ((i * 2) + 1))

print()

row = 4
print("Inverted pyramid pattern using *")
for i in range(row - 1, 0, -1):
    print(" " * (row-(i+1)) + "*" * ((i * 2) + 1))
if row == 0:
    pass
else:
    print(" " * (row-1) + "*")

print()

row = 4
print("Floyd triangle right")
number = 1
for i in range(1, row + 1):
    for j in range(i):
        print(number, end=" ")
        number += 1
    print()

print()

row = 4
print("Floyd pyramid")
number = 1
space = row - 1
for i in range(1, row + 1):
    print(" " * space, end="")
    for j in range(1, i + 1):
        print(number, end=" ")
        number += 1
    space -= 1
    print()

print()

row = 4
print("Floyd triangle left")
number = 1
space = (row * 2) - 2
for i in range(1, row + 1):
    print(" " * space, end="")
    for j in range(1, i + 1):
        print(number, end=" ")
        number += 1
    space -= 2
    print()

print()

row = 4
print("Palindrome Floyd pyramid")
number_1 = 1
space = (row * 2) - 2
for i in range(1, row + 1):
    print(" " * space, end="")
    for j in range(1, i + 1):
        print(number_1, end=" ")
        number_1 += 1
    number_2 = number_1 - 1
    for k in range(i-1):
        number_2 -= 1
        print(number_2, end=" ")
    space -= 2
    print()

print()

row = 4
print("Right half triangle using number (pattern 1)")
for i in range(1, row +1):
    for j in range(i):
        print(j + 1, end= " ")
    print()         

print()

row = 4
print("Pyramid using number (pattern 1)")
space = row - 1
for i in range(1, row +1):
    print(" " * space, end="")
    for j in range(i):
        print(j + 1, end= " ")
    space -= 1
    print()         

print()

row = 4
print("Left half triangle using number (pattern 1)")
space = (row * 2) - 2
for i in range(1, row +1):
    print(" " * space, end="")
    for j in range(i):
        print(j + 1, end= " ")
    space -= 2
    print()         

print()

row = 4
print("Palindrome pyramid using number (pattern 1)")
space = (row * 2) - 2
for i in range(1, row + 1):
    print(" " * space, end="")
    for j in range(1, i +1):
        print(j, end=" ")
    for k in range(i-1, 0, -1):
        print(k, end=" ")
    space -= 2
    print()

print()

row = 4
print("Right half triangle using number (pattern 2)")
for i in range(1, row + 1):
    for j in range(i,0,-1):
        print(j, end= " ")
    print()         

print()

row = 4
print("Palindrome pyramid using number (pattern 2)")
space = (row * 2) - 1
for i in range(1, row + 1):
    print(" " * space, end="")
    for j in range(i, 0, -1):
        print(j, end=" ")
    for k in range(1, i):
        print(k + 1, end=" ")
    space -= 2
    print()

print()

row = 4
print("Right half triangle using number (pattern 3)")
for i in range(1, row + 1):
    print((str(i) + " ") * i)

print()

row = 4
print("Palindrome pyramid using number (pattern 3)")
space = (row * 2) - 1
for i in range(1, row + 1):
    print(" " * space, end="")
    print((str(i) + " ") * (i + (i - 1)))
    space -= 2

print()