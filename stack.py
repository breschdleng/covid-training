from linked_list import Node

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = Node(data)
            self.tail.next = node
            self.tail = self.tail.next
        self.size +=1

    def pop(self):

        if self.head is None:
            raise ValueError("nothing to pop")
        else:
            node = self.head
            if self.head.next is not None:
                self.head = self.head.next
            self.size -=1
            return node.data

    def peek(self):
        if self.size == 0:
            raise ValueError("nothing to peek in empty list")
        else:
            return self.head.data


    def get_item(self, idx):

        if self.is_empty():
            raise ValueError("empty Queue")
        elif idx < 0 or idx > self.size:
            raise ValueError("invalid idx")
        else:
            node = self.head
            for i in range(idx):
                node = node.next
        return node.data

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False