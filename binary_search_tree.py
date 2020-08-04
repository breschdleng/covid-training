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

if __name__ == '__main__':

    a = [1, 3 , 5 , 2, 6]
    bst = BST()

    for i in a:
        bst.insert_using_recur(i)

    print(bst)



