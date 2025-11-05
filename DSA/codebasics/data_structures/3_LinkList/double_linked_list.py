class Node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev


class DoubleLinkedList():
    def __init__(self):
        self.head = None

    def print_forword(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.head
        dll_str = ''
        while itr:
            dll_str += str(itr.data) + '-->'
            itr = itr.next        
        print(dll_str)

    def print_backword(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.head
        dllbstr = ''
        while itr.next:
            itr = itr.next
        while itr:
            dllbstr += str(itr.data) + '-->'
            itr = itr.prev
        print(dllbstr)

    def get_lenth(self):
        itr = self.head
        count = 0
        while itr:
            itr = itr.next
            count += 1
        return count
    
    def insert_at_begining(self, data):
        if self.head == None:
            self.head = Node(data)
            return
        node = Node(data, next=self.head)
        self.head.prev = node
        self.head = node

    
    def insert_at_end(self, data):
        if self.head == None:
            self.head = Node(data)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        node = Node(data, next=None, prev=itr)
        itr.next = node

    def insert_at(self, index, data):
        if index < 0 or index > self.get_lenth():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.insert_at_begining(data)
            return

        itr = self.head
        count = 0
        while itr:
            if count == (index -1):
                node = Node(data, next=itr.next, prev=itr)
                if itr.next:
                    itr.next.prev = node
                itr.next = node
                break
            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index < 0 or index >= self.get_lenth():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        itr = self.head
        count = 0
        while itr:
            if count == index:
                if itr.next:
                    itr.next.prev = itr.prev
                itr.prev.next = itr.next
                break
            itr = itr.next
            count += 1

    def insert_values(self, data_list):
        for i in data_list:
            itr = self.head
            while itr:
                if itr.next is None:
                    node = Node(i, None, itr)
                    itr.next = node
                    break
                itr = itr.next
            else:
                self.head = Node(i)

if __name__ == "__main__":
    dll = DoubleLinkedList()
    dll.insert_values(['banana', 'mango', 'grapes', 'orange'])
    dll.print_forword()
    dll.print_backword()
    dll.insert_at_end("figs")
    dll.print_forword()
    dll.insert_at(0, "jackfruit")
    dll.print_forword()
    dll.insert_at(6, "dates")
    dll.print_forword()
    dll.insert_at(2, "kiwi")
    dll.print_forword()
    dll.remove_at(0)
    dll.print_forword()
    dll.print_backword()

