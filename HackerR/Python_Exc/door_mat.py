n, m = list(map(int,input().split()))

disg_1 = '.|.'
for i in range(1,n,2):
    pattern_count = i
    pattern = pattern_count*disg_1
    print('-' * ((m-len(pattern))//2) + pattern + '-' * ((m-len(pattern))//2))

welcome_desg = 'WELCOME'
welcome_desg_pos = (m - len(welcome_desg))//2
print('-' * welcome_desg_pos + welcome_desg + '-' * welcome_desg_pos)

while pattern_count > 0:
    print('-' * ((m-len(pattern))//2) + pattern + '-' * ((m-len(pattern))//2))
    pattern_count -= 2
    pattern = pattern_count*disg_1
############## Another way for bottom pattern.
# j = n
# while j > 1:
#     print('-' * ((m-len(pattern))//2) + pattern + '-' * ((m-len(pattern))//2))
#     pattern_count -= 2
#     pattern = pattern_count*disg_1
#     j -= 2

print()

i = 1
pattern = i*disg_1
while i < n:
    print('-' * ((m-len(pattern))//2) + pattern + '-' * ((m-len(pattern))//2))
    i += 2
    pattern = i*disg_1

welcome_desg = 'WELCOME'
welcome_desg_pos = (m - len(welcome_desg))//2
print('-' * welcome_desg_pos + welcome_desg + '-' * welcome_desg_pos)

j = i - 2
pattern = j*disg_1
while j > 0:
    print('-' * ((m-len(pattern))//2) + pattern + '-' * ((m-len(pattern))//2))
    j -= 2
    pattern = j*disg_1