from queue import GenQueue

class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BST:
    def __init__(self):
        self.root = None

    def insert_using_while(self, data=None):
        if self.root is None:
            node = Node(data)
            self.root = node
        else:
            node = self.root

            while node is not None:
                if data < node.data:
                    if node.left is None:
                        node.left = Node(data)
                        return
                    else:
                        node = node.left
                else:
                    if node.right is None:
                        node.right = Node(data)
                        return
                    else:
                        node = node.right

    def insert_using_recur(self, data=None):
        if self.root is None:
            node = Node(data)
            self.root = node
        else:
            self._insert(self.root, data)

    def _insert(self, node, data=None):
        if  data < node.data:
            if node.left is None:
                node.left = Node(data)
                return
            else:
                self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
                return
            else:
                self._insert(node.right, data)

    def pre_order_traversal(self, str, node):

        if node is None:
            return

        # 1. visit node
        # 2. left child
        # 3. right child
        print(str, node.data)
        self.pre_order_traversal("left", node.left)
        self.pre_order_traversal("right", node.right)

    def in_order_traversal(self, str, node):

        if node is None:
            return

        # 1. left child
        # 2. visit node
        # 3. right child
        self.in_order_traversal("left", node.left)
        print(str, node.data)
        self.in_order_traversal("right", node.right)

    def post_order_traversal(self, str, node):

        if node is None:
            return

        # 1. left child
        # 2. right child
        # 3. visit node
        self.post_order_traversal("left", node.left)
        self.post_order_traversal("right", node.right)
        print(str, node.data)

    def level_order_traversal(self):

        qq = GenQueue()
        traversed = GenQueue()

        if self.root is not None:
            qq.enqueue(self.root)

        while not qq.is_empty():
            node = qq.dequeue()
            traversed.enqueue(node)
            if node.left is not None:
                qq.enqueue(node.left)
            if node.right is not None:
                qq.enqueue(node.right)
        return traversed

    def print(self, traversed):

        while not traversed.is_empty():
            print(traversed.dequeue().data)

if __name__ == '__main__':

    a = [5, 4, 2, 7, 8]

    #     5
    #     /\
    #    4  7
    #   /    \
    # 2       8

    # reference: https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
    # pre-order traversal
    # print node
    # left visit
    # right visit
    # https://www.youtube.com/watch?v=6oL-0TdVy28&t=1411s
    # 5, 4, 2, 8, 7, 8


    # in-order traversal
    # left visit
    # print node
    # right visit
    # 2, 4,  5, 8, 7
    # https://www.youtube.com/watch?v=6oL-0TdVy28&t=1411s

    bst = BST()#

    for i in a:
        bst.insert_using_while(i)
    # bst.in_order_traversal("root", bst.root)
    bst.post_order_traversal("root", bst.root)
    #traversed = bst.level_order_traversal()
    #bst.print(traversed)