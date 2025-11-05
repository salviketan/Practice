##### Using a list as a queue
q = []
q.insert(0, 1)
q.insert(0, 2)
q.insert(0, 3)
print(q)
q.pop()
q.pop()
print(q)


##### Using deque as a queue
from collections import deque

buf = deque()

buf.appendleft(1)
buf.appendleft(2)
buf.appendleft(3)
print()
print(buf)
buf.pop()
buf.pop()
print(buf)

##### Implement Queue class using a deque

class Queue():
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)
    
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)
    
    def front(self):
        return self.buffer.popleft()
    
    def __str__(self):
        return str(self.buffer)
    

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print()
print(q)
print(q.front())
print(q)
print(q.dequeue())
print(q.dequeue())
print(q)