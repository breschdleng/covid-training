import unittest
import numpy as np
from linked_list import LinkedList

class TestLinkedList(unittest.TestCase):

    def test_insert(self):
        ll = LinkedList()
        data = np.arange(10)

        for i in data:
            ll.append(i)
            self.assertEqual(i, ll.get_item())

    def test_delete(self):
        ll = LinkedList()
        data = [0,1,2,-3]
        for i in data:
            ll.append(i)

        ll.delete()
        self.assertEqual(ll.size, 0)

    def test_deleteAt(self):
        ll = LinkedList()
        data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for i in data:
            ll.append(i)

        size = len(data)
        ll.deleteAt(3)
        size -=1
        self.assertEqual(size, ll.size)
        ll.deleteAt(3)
        size -= 1
        self.assertEqual(size, ll.size)
        ll.deleteAt(3)
        size -= 1
        self.assertEqual(size, ll.size)

        expectedData = [0, 1, 2, 6, 7, 8, 9, 10]

        self.assertEqual(len(expectedData), ll.size)
        self.assertEqual(0, ll.get_item(0))
        self.assertEqual(1, ll.get_item(1))
        self.assertEqual(2, ll.get_item(2))
        self.assertEqual(6, ll.get_item(3))
        self.assertEqual(7, ll.get_item(4))
        self.assertEqual(8, ll.get_item(5))
        self.assertEqual(9, ll.get_item(6))
        self.assertEqual(10, ll.get_item(7))

    def test_pop(self):
        ll = LinkedList()
        data = [0, 1, 2, -3, 10, 23]
        for i in data:
            ll.append(i)

        size = len(data)
        item = ll.pop(5)
        size -=1
        self.assertEqual(item.data, 23)
        self.assertEqual(size, ll.size)
        item = ll.pop(3)
        size -= 1
        self.assertEqual(item.data, -3)
        self.assertEqual(size, ll.size)
        item = ll.pop(2)
        size -= 1
        self.assertEqual(item.data, 2)
        self.assertEqual(size, ll.size)

    def test_insertAt(self):
        ll = LinkedList()
        data = [0, 1, 2, -3, 10, 23]
        for i in data:
            ll.append(i)

        size = len(data)
        ll.insertAt(3, 2300)
        item = ll.get_item(3)
        self.assertEqual(2300, item)

        size += 1
        self.assertEqual(size, ll.size)

        ll.insertAt(2, 5300)
        item = ll.get_item(2)
        self.assertEqual(5300, item)

        size += 1
        self.assertEqual(size, ll.size)

        ll.insertAt(5, -20)
        item = ll.get_item(5)
        self.assertEqual(-20, item)

        size += 1
        self.assertEqual(size, ll.size)

        ll.insertAt(0, -450)
        item = ll.get_item(0)
        self.assertEqual(-450, item)

        size += 1
        self.assertEqual(size, ll.size)

    def test_index(self):
        ll = LinkedList()
        data = [2, 3, 4, 4, 5, 5, 6]
        for i in data:
            ll.append(i)

        self.assertEqual(2, ll.index(4, 0, 3))
        self.assertEqual(3, ll.index(4, 3, 7))

        self.assertEqual(4, ll.index(5, 0, 10))

    def test_count(self):
        ll = LinkedList()

        for i in range(10):
            ll.append(2)

        for i in range(3):
            ll.append(4)

        self.assertEqual(10, ll.count(2))
        self.assertEqual(3, ll.count(4))


if __name__ == '__main__':
    unittest.main()

