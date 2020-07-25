
#import numpy as np

# insertAt
# deleteAt
# first
# last

class Node:
    def __init__(self, data=None):
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self):
        self.tail = None
        self.head = None
        self.size = 0

    def append(self, data):
        if self.size == 0:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = Node(data)
            self.tail.next = node
            self.tail = self.tail.next
        self.size += 1

    def delete(self):
        node = self.head
        while node is not None:
            if node.next==self.tail:
                node.next = None
                self.tail = node
            node = node.next
        self.size -= 1

    def print_items(self):
        node = self.head

        while node is not None:
            print("elem", node.data)
            node = node.next

if __name__ == '__main__':
    ll = LinkedList()
    ll.append(5)
    ll.append(10)
    ll.append(30)
    ll.append(50)

    ll.delete()
    ll.delete()

    ll.delete()
    ll.append(50)
    ll.append(30)

    ll.print_items()
