class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_end(self, data):
        if self.head is None:
            self.head = Node(data)
            self.head.next = None
            self.head.prev = None
            self.tail = self.head
        else:
            node = self.head
            for i in range(self.size):
                curr = node
                node = node.next

            node = Node(data)
            node.prev = curr
            curr.next = node

            self.tail = node

        self.size += 1

    def insert_start(self, data):
        if self.head is None:
            self.head = Node(data)
            self.head.next = None
            self.head.prev = None
            self.tail = self.head
        else:
            node = Node(data)
            node.next = self.head
            self.head.prev = node
            self.head = node

        self.size += 1

    def insert_between(self, idx, data):
        node = self.head
        for i in range(idx-1):
            node = node.next

        temp = Node(data)
        temp.next = node.next
        node.next.prev = temp
        node.next = temp
        temp.prev = node
        self.size +=1


    def insert_at(self, idx, data):
        if idx is None or idx < 0 or idx > self.size:
            raise ValueError("invalid index")

        if idx == 0:
            self.insert_start(data)
        elif idx == self.size:
            self.insert_end(data)
        else:
            self.insert_between(idx, data)


    def delete(self):
        node = self.head
        for i in range(self.size):
            node = node.next
            self.delete_head()

    def delete_head(self):
        node = self.head
        if self.size == 1:
            self.head.next = None
            self.head.prev = None
            self.head = None
        elif self.size > 1:
            self.head = self.head.next
            self.head.prev = None
            node.prev = None
            node.next = None
        else:
            raise ValueError("nothing to delete")
        self.size -= 1
        return node

    def delete_tail(self):
        node = self.tail
        if self.size==1:
            self.tail.prev = None
            self.tail.next = None
            self.tail = None
        elif self.size > 1:
            self.tail = self.tail.prev
            node.next = None
            node.prev = None
        else:
            raise ValueError("nothing to delete")
        self.size -= 1
        return node

    def delete_at(self, idx):
        if idx is None or idx < 0 or idx > self.size -1:
            raise ValueError("invalid index for deletion")

        if idx == self.size - 1:
            node = self.delete_tail()
        elif idx == 0:
            node = self.delete_head()
        else:
            node = self.delete_between(idx)
        return node


    def delete_between(self, idx):

        if idx > 0 and idx < self.size -1:
            node = self.head
            for i in range(idx - 1):
                node = node.next

            prev = node
            curr = node.next
            next = node.next.next

            prev.next = next
            next.prev = prev
            curr.next = None
            curr.prev = None
        else:
            raise ValueError("invalid index for deleting {0}th item from size {1}".format(idx, self.size))
        self.size -=1
        return curr

    def get_head(self):
        return self.head

    def reverse(self):
        node = self.head
        for i in range(self.size):
            temp = node.next
            node.next = node.prev
            node.prev = temp
            node = node.prev

        temp_head = self.head
        self.head = self.tail
        self.tail =  temp_head

    def pop(self, idx=None):
        if idx is None:
            idx = self.size
        node = self.delete_at(idx)
        return node.data

    def get_tail(self):
        return self.tail

    def get_item(self, idx):
        node = self.head
        for i in range(idx):
            node = node.next
        return node.data


