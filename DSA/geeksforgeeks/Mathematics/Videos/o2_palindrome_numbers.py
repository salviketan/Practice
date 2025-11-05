def is_palindrome(p_inp):
    p_temp = p_inp
    p_reverce = 0
    while p_inp != 0:
        p_reverce = (p_reverce * 10) + (p_inp % 10)
        p_inp = p_inp // 10
    if p_reverce == p_temp:
        return "Yes"
    return "No"


user_input = int(input("Enter a number: "))
print(is_palindrome(user_input))