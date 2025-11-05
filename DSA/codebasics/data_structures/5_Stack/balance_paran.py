from reverse_string import Stack

def is_match(ch1,ch2):
    match_dict = {
        '}': '{',
        ']': '[',
        ')': '('
    }
    return True if match_dict[ch1] == ch2 else False

def is_balanced(data):
    que = Stack()

    for char in data:
        if char in ['{','[','(']:
            que.push(char)
        if char in ['}',']',')']:
            if que.size() == 0:
                return False
            if not is_match(char,que.pop()):
                return False
    
    return que.size() == 0

print(is_balanced("({a+b})"))
print(is_balanced("))((a+b}{"))
print(is_balanced("((a+b))"))
print(is_balanced("))"))
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))