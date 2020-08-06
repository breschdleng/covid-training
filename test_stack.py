import unittest
from stack import Stack

class TestStack(unittest.TestCase):

    def assert_linked_list(self, data, qq):
        for i in range(len(data)):
            self.assertEqual(data[i], qq.get_item(i))

    def test_push(self):
        a = [1, 2, 4, 5, 6]
        ss = Stack()
        b = []
        for i in a:
            ss.push(i)
            b.append(i)
            self.assert_linked_list(b, ss)
            self.assertEqual(len(b), ss.size)
        self.assert_linked_list(b, ss)
        self.assertEqual(len(b), ss.size)

    def test_pop(self):
        a = [1, 2, 4, 5, 6]
        ss = Stack()
        for i in a:
            ss.push(i)

        for i in range(len(a)):
            self.assertEqual(a[i], ss.pop())
            self.assertEqual(len(a[i+1:]), ss.size)

    def test_peek(self):
        a = [1, 2, 4, 5, 6]
        ss = Stack()
        for i in a:
            ss.push(i)

        for i in range(len(a)):
            self.assertEqual(a[i], ss.peek())
            ss.pop()

if __name__ == '__main__':
    unittest.main()
