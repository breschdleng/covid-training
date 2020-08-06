import unittest
from double_linked_list import DoubleLinkedList
import numpy as np

class TestDoubleLinkedList(unittest.TestCase):
    def insert_begin(self, data, ll):
        for i in data:
            ll.insert_start(i)
        return ll

    def insert_end(self, data, ll):
        for i in data:
            ll.insert_end(i)
        return ll

    def assert_linked_list(self, data, ll):
        for i in range(len(data)):
            self.assertEqual(data[i], ll.get_item(i))

    def test_insert_end(self):
        ll = DoubleLinkedList()
        data = [1, 2, 3, 4, 5]
        ll = self.insert_end(data, ll)
        self.assert_linked_list(data, ll)

    def test_insert_begin(self):
        ll = DoubleLinkedList()
        data = [1, 2, 3, 4, 5]
        ll = self.insert_begin(data, ll)
        self.assert_linked_list(data[::-1], ll)

    def test_delete_at(self):
        data = [1, 2, 3, 4, 5, 6, 7]
        ll = DoubleLinkedList()
        ll = self.insert_end(data, ll)
        delete_indices = [0, 2, 2, 3]

        for i in delete_indices:
            ll.delete_at(i)
            del data[i]
            self.assert_linked_list(data, ll)

        self.assertEqual(len(data), ll.size)

    def test_delete_head(self):
        data = [1, 2, 3, 4, 5, 6, 7]
        ll = DoubleLinkedList()
        ll = self.insert_end(data, ll)
        delete_indices = len(data)*[0]

        for i in delete_indices:
            ll.delete_head()
            del data[i]
            self.assert_linked_list(data, ll)

        self.assertEqual(len(data), ll.size)

    def test_delete_tail(self):
        data = [1, 2, 3, 4, 5, 6, 7]
        ll = DoubleLinkedList()
        ll = self.insert_end(data, ll)
        delete_indices = np.arange(0, len(data))
        delete_indices = delete_indices[::-1]

        for i in delete_indices:
            ll.delete_tail()
            del data[i]
            self.assert_linked_list(data, ll)

        self.assertEqual(len(data), ll.size)

    def test_delete_between(self):
        data = [1, 2,  5, 6, 4, 5]
        ll = DoubleLinkedList()
        ll = self.insert_end(data, ll)
        delete_indices = [2, 3, 1]

        for i in delete_indices:
            ll.delete_between(i)
            del data[i]
            self.assert_linked_list(data, ll)


        self.assertEqual(len(data), ll.size)

    def test_pop(self):
        data = [1, 2, 3, 4, 5, 6, 7]
        ll = DoubleLinkedList()
        ll = self.insert_end(data, ll)
        delete_indices = [0, 1, 2, 3]

        for i in delete_indices:
            val = ll.pop(i)
            ref = data[i]
            del data[i]
            self.assertEqual(ref, val)

        self.assertEqual(len(data), ll.size)

    def test_insert_at(self):
        data = [1, 2, 3, 4, 5, 6, 7]
        ll = DoubleLinkedList()
        ll = self.insert_end(data, ll)
        insert_indices = [0, 7, 2, 4]
        for i in insert_indices:
            ll.insert_at(i, data[i])
            data.insert(i, data[i])
            self.assert_linked_list(data, ll)

        self.assertEqual(len(data), ll.size)

    def test_get_item(self):
        ll = DoubleLinkedList()
        data = [1, 2, 3, 4, 5]
        ll = self.insert_end(data, ll)
        for i in range(len(data)):
            self.assertEqual(data[i], ll.get_item(i))

    def test_get_head(self):
        ll = DoubleLinkedList()
        data = [1, 2, 3, 4, 5]
        ll = self.insert_end(data, ll)

        delete_indices = len(data) * [0]

        for i in delete_indices:
            val = ll.get_head()
            ll.delete_head()
            ref = data[i]
            del data[i]
            self.assertEqual(ref, val.data)

        self.assertEqual(len(data), ll.size)

    def test_get_tail(self):
        ll = DoubleLinkedList()
        data = [1, 2, 3, 4, 5]
        ll = self.insert_end(data, ll)
        delete_indices = np.arange(0, len(data))
        delete_indices = delete_indices[::-1]

        for i in delete_indices:
            val = ll.get_tail()
            ll.delete_tail()
            ref = data[i]
            del data[i]
            self.assertEqual(ref, val.data)

        self.assertEqual(len(data), ll.size)

    def test_reverse(self):
        ll = DoubleLinkedList()
        data = [1, 2, 3, 4, 5]
        ll = self.insert_end(data, ll)
        data = data[::-1]
        ll.reverse()

        self.assert_linked_list(data, ll)
        self.assertEqual(len(data), ll.size)

if __name__ == '__main__':
    unittest.main()
