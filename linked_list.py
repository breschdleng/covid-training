
#import numpy as np

# insertAt
# deleteAt
# first
# last

class Node:
    def __init__(self, data):
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

    def insertAt(self, idx, data):

        new_node = Node(data)
        node = self.head

        if idx == 0:
            temp = self.head.next
            self.head = new_node
            self.head.next = temp
        else:
            for i in range(idx-1):
                node = node.next

            temp = node.next
            node.next = new_node
            new_node.next = temp
        self.size += 1

    def delete(self):
        for i in range(self.size):
            self.deleteAt(0)

    def delete_first(self):
        if self.size == 1:
            temp = self.head
            self.head = None
        else:
            node = self.head
            temp = self.head
            self.head = node.next
        self.size -=1
        return temp

    def delete_last(self):
        node = self.head
        for i in range(self.size - 2):
            node = node.next

        temp = node.next
        node.next = None
        self.size -= 1
        return temp

    def delete_between(self, idx):
        node = self.head
        for i in range(idx -1):
            node = node.next

        temp = node.next
        node.next = node.next.next
        self.size -= 1
        return temp

    def deleteAt(self, idx):

        if idx < 0 or idx > self.size-1 or idx is None:
            raise ValueError("invalid index")

        if idx == 0:
            temp = self.delete_first()
        elif idx == self.size-1:
            temp = self.delete_last()
        else:
            temp = self.delete_between(idx)

        return temp

    def pop(self, idx=None):
        if idx is None:
            idx = self.size-1

        item = self.deleteAt(idx)
        return item

    def get_item(self, idx=None):
        node = self.head
        if idx is None:
            idx = self.size-1
        for i in range(idx):
            node = node.next
        return node.data

    def count(self, data):
        node = self.head
        for i in range(self.size):
            node = node.next

    def count(self, data):
        node = self.head
        hist = {}
        for i in range(self.size):
            if node.data not in hist.keys():
                hist[node.data] = 1
            else:
                hist[node.data] += 1
            node = node.next

        return hist[data]

    def index(self, data, start=None, end=None):
        node = self.head
        if end is None or end > (self.size - 1):
            end = self.size
        if start is None or start < 0:
            start = 0

        found_idx = -1
        for i in range(self.size):
            if node.data == data and i >= start and i <= end:
                found_idx = i
                break
            node = node.next

        if found_idx == -1:
            raise ValueError("no such item found")
        return found_idx



