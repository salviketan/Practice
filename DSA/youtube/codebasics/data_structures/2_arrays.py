print("Problem 1:- ")
months = [2200, 2350, 2600, 2130, 2190]

diff = months[1] - months[0]
print(f"1. {diff}")

q1_expense = 0
for i in months[:3]:
    q1_expense+= i
# print(f"2. {q1_expense}")
# Alternate version
print(f"2. Alternative")
print(f"2. {sum(months[:3])}")

spent = 2000 in months
print(f"3. {spent}")

months.append(1980)
print(f"4. {months}")

months[3] -= 200
print(f"5. {months}")

print()
print("Problem 2:- ")
heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

print(f"1.", len(heros))

heros.append('black panther')
print(f"2. {heros}")

heros.pop()
heros.insert(3, 'black panther')
print(f"3. {heros}")

heros[1:3] = ['doctor strange']
print(f"4. {heros}")

heros.sort()
print(f"5. {heros}")

print()
print("Problem 3:- ")
max_input = int(input("Enter a number:"))
# out_list = list(range(1, max_input + 1, 2))
# Alternate
out_list = [i for i in range(1, max_input + 1) if i % 2 == 1]
print(f"Ans: {out_list}")

