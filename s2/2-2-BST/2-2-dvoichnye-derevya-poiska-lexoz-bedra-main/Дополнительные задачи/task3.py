from time import process_time
from tracemalloc import start, get_traced_memory


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.size = 1


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def size(self, node):
        if node is None:
            return 0
        return node.size

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)

        node.size = 1 + self.size(node.left) + self.size(node.right)
        return node

    def get_min_gt(self, key):
        return self._get_min_gt(self.root, key)

    def _get_min_gt(self, node, key):
        if node is None:
            return 0

        if node.key <= key:
            return self._get_min_gt(node.right, key)

        if node.left is None:
            return node.key

        if node.left.key <= key:
            return self._get_min_gt(node.left.right, key)

        return self._get_min_gt(node.left, key)


start()

bst = BinarySearchTree()

with open("output.txt", "w+") as g:
    with open("input.txt") as f:
        all_info = f.readlines()
        for i in all_info:
            if i.split()[0] == "+":
                bst.insert(i.split()[1])
            else:
                g.write(str(bst.get_min_gt(i.split()[1])) + "\n")


print('Time:', str(process_time()), 'sec')
print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')