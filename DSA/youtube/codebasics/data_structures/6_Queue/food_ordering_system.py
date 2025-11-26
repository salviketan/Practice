from collections import deque
from threading import Thread
import time

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
        return self.buffer[-1]
    
    def __str__(self):
        return str(self.buffer)
    

food_order_queue = Queue()

def place_order(ord_list):
    for order in ord_list:
        print("Placing order for:", order)
        food_order_queue.enqueue(order)
        time.sleep(0.5)


def server_order():
    time.sleep(1)
    while not food_order_queue.is_empty():
        order = food_order_queue.dequeue()
        print("Now serving:", order)
        time.sleep(2)    


if __name__ == '__main__':
    order_list = ["pizza", "samosa", "pasta", "biryani", "burger"]
    t1 = Thread(target= place_order, args=(order_list,))
    t2 = Thread(target= server_order)

    t1.start()
    t2.start()