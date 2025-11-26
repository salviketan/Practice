##### Using a list as a stack
s = []
s.append("https://www.cnn.com/")
s.append("https://www.cnn.com/world")
s.append("https://www.cnn.com/india")
s.append("https://www.cnn.com/china")

print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
# print(s.pop())

##### Using deque as a stack
from collections import deque

stack = deque()
stack.append("https://www.cnn.com/")
stack.append("https://www.cnn.com/world")
stack.append("https://www.cnn.com/india")
stack.append("https://www.cnn.com/china")

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(dir(stack))

##### Implement Stack class using a deque

class Stack():
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return (self.container) == 0
    
    def size(self):
        return len(self.container)
    
    def __str__(self):
        return str(self.container)


s = Stack()

s.push("https://www.cnn.com/")
s.push("https://www.cnn.com/world")
print(s)
print(s.is_empty())
print(s.pop())
print(s.is_empty())