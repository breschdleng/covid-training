from linked_list import Node

class Queue:
    def __init__(self):

        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node  = Node(data)
            node.next = self.head
            self.head = node
        self.size += 1

    def is_empty(self):
        if self.size and self.head is None:
            return True
        else:
            return False

    def dequeue(self):
        is_empty = self.is_empty()
        if is_empty:
            raise ValueError("empty Queue")
        else:
            node = self.head

            if self.head.next is not None:
                self.head = self.head.next
            self.size -=1
            return node.data

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

    def print(self):

        if self.is_empty():
            raise ValueError("empty Queue")
        else:
            node = self.head
            for i in range(self.size):
                print(node.data)
                node = node.next

if __name__ =='__main__':
    a = [1, 2, 4, 5, 6]
    qq = Queue()
    for i in a:
        qq.enqueue(i)

    for i in range(len(a)):
        item = qq.dequeue()
        print(item.data)





