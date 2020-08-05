import unittest
from queue import Queue


class TestQueue(unittest.TestCase):

    def assert_linked_list(self, data, qq):
        for i in range(len(data)):
            self.assertEqual(data[i], qq.get_item(i))

    def test_enqueue(self):
        a = [1, 2, 4, 5, 6]
        qq = Queue()
        b = []
        for i in a:
            qq.enqueue(i)
            b.append(i)
            self.assert_linked_list(b[::-1], qq)
            self.assertEqual(len(b), qq.size)
        self.assert_linked_list(b[::-1], qq)
        self.assertEqual(len(b), qq.size)

    def test_dequeue(self):
        a = [1, 2, 4, 5, 6]
        qq = Queue()
        for i in a:
            qq.enqueue(i)

        a = a[::-1]
        for i in range(len(a)):
            self.assertEqual(a[i], qq.dequeue().data)
            self.assertEqual(len(a[i+1:]), qq.size)



if __name__ == '__main__':
    unittest.main()
