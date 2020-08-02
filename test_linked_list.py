import unittest
import numpy as np
from linked_list import LinkedList

class TestLinkedList(unittest.TestCase):

    def insert_data(self, data, ll):
        for i in data:
            ll.append(i)
        return ll

    def assert_linked_list(self, data, ll):
        for i in range(len(data)):
            self.assertEqual(data[i], ll.get_item(i))

    def test_insert(self):
        ll = LinkedList()
        data = np.arange(10)
        ll = self.insert_data(data, ll)
        self.assert_linked_list(data, ll)

    def test_delete(self):

        data = [0, 1, 2, -3]
        ll = LinkedList()
        ll = self.insert_data(data, ll)

        ll.delete()
        self.assertEqual(ll.size, 0)

    def test_deleteAt(self):

        data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        ll = LinkedList()
        ll = self.insert_data(data, ll)

        delete_indices = [3, 2, 4]
        for i in delete_indices:
            ll.deleteAt(i)
            del data[i]

        self.assertEqual(len(data), ll.size)
        self.assert_linked_list(data, ll)

    def test_pop(self):
        ll = LinkedList()
        data = [0, 1, 2, -3, 10, 23]
        ll = self.insert_data(data, ll)
        pop_indices = [5, 3, 2]
        pop_items = []
        for i in pop_indices:
            pop_items.append(data[i])
            item = ll.pop(i)
            self.assertEqual(item.data, pop_items[-1])

        ref_data_size = len(data) - len(pop_items)
        self.assertEqual(ref_data_size, ll.size)

    def test_insertAt(self):
        ll = LinkedList()
        data = [0, 1, 2, -3, 10, 23]
        ll = self.insert_data(data, ll)

        insert_indices = [3, 3, 2]
        insert_val = [100, 23, 45]
        for i in range(len(insert_indices)):
            data.insert(insert_indices[i], insert_val[i])
            ll.insertAt(insert_indices[i], insert_val[i])

        self.assert_linked_list(data, ll)
        self.assertEqual(len(data), ll.size)

    def test_index(self):
        ll = LinkedList()
        data = [2, 3, 4, 4, 5, 5, 6]
        ll = self.insert_data(data, ll)

        self.assertEqual(2, ll.index(4, 0, 3))
        self.assertEqual(3, ll.index(4, 3, 7))
        self.assertEqual(4, ll.index(5, 0, 10))

    def test_count(self):
        ll = LinkedList()

        freq = 5
        data = freq*[2]
        print(data)

        ll = self.insert_data(data, ll)
        self.assertEqual(freq, ll.count(2))
        self.assert_linked_list(data, ll)

        ll.delete()

        freq = 2
        data = freq*[4]

        ll = self.insert_data(data, ll)

        self.assert_linked_list(data, ll)
        self.assertEqual(freq, ll.count(4))

if __name__ == '__main__':
    unittest.main()

