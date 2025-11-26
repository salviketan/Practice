
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def ll_print(self):
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    def get_lenth(self):
        itr = self.head
        count = 0
        while itr:
            itr = itr.next
            count += 1

        return count

    def insert_at_end(self, data):
        itr = self.head
        if itr == None:
            self.insert_at_begining(data)
            return
            
        while itr.next:
            itr = itr.next
        itr.next = Node(data)

    def insert_values(self, data_list):        
        for i in data_list:
            self.insert_at_end(i)            
     
    def remove_at(self, index):
        if index < 0 or index >= self.get_lenth():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        itr = self.head
        count = 0
        while itr:
            if count == (index -1):
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1


    def insert_at(self, index, data):
        if index < 0 or index >= self.get_lenth():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_begining(data)
            return

        itr = self.head
        count = 0
        while itr:
            if count == (index -1):
                itr.next = Node(data, itr.next)
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break
            itr = itr.next
        else:
            print(f"list out of range: list does not contain value {data_after}")


    def remove_by_value(self, data):
        itr = self.head
        prev_node = None
        while itr:
            if itr.data == data:
                if prev_node:
                    prev_node.next = itr.next
                    break
                self.head = itr.next
                break
            prev_node = itr
            itr = itr.next
        else:
            print(f"list out of range: list does not contain value {data}")
        


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_values(['banana', 'mango', 'grapes', 'orange'])
    ll.ll_print()
    # ll.remove_at(2)
    # ll.ll_print()
    ll.insert_at(0,"figs")
    ll.ll_print()
    # ll.insert_at(2,"jackfruit")
    # ll.ll_print()
    ll.insert_after_value("mango", "apple")
    ll.ll_print()
    ll.remove_by_value("orange")
    ll.ll_print()
    ll.remove_by_value("figs")
    ll.ll_print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    print("emptied list- ",end=' ')
    ll.ll_print()