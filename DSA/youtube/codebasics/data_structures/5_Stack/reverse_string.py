from collections import deque

class Stack():
    def __init__(self):
        self.container = deque()

    def push(self, val):
        return self.container.append(val)
    
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return not bool(self.container)
    
    def size(self):
        return len(self.container)
    

def reverse_string(data):
    que = Stack()
    for char in data:
        que.push(char)

    rstr = ''
    while not que.is_empty():
        rstr += que.pop()

    return rstr



if __name__ == '__main__':
    print(reverse_string("We will conquere COVID-19"))