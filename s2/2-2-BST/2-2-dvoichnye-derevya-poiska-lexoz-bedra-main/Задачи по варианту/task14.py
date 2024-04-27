import sys
from time import process_time
from tracemalloc import start, get_traced_memory


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.height = 1


class AVLTree:

    left_index = 1
    right_index = 1
    res_left_index = 2
    res_right_index = 3

    def get_height(self, node):
        if node is None:
            return 0
        else:
            return node.height

    def balance(self, node):
        if node is None:
            return 0
        else:
            return self.get_height(node.left) - self.get_height(node.right)

    def left_rotate(self, node):
        a = node.right
        b = a.left
        a.left = node
        node.right = b
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        a.height = 1 + max(self.get_height(a.left), self.get_height(a.right))
        return a

    def right_rotate(self, node):
        a = node.left
        b = a.right
        a.right = node
        node.left = b
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        a.height = 1 + max(self.get_height(a.left), self.get_height(a.right))
        return a

    def insert(self, value, root):
        if root is None:
            return Node(value)
        elif value <= root.value:
            root.left = self.insert(value, root.left)
        elif value > root.value:
            root.right = self.insert(value, root.right)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.balance(root)

        if balance > 1 and root.left.value > value:
            return self.right_rotate(root)
        if balance > 1 and root.left.value < value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and root.right.value < value:
            return self.left_rotate(root)
        if balance < -1 and root.right.value > value:
            root.lerightft = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root

    def preorder(self, root):
        if root is None:
            return
        if root.left:
            self.left_index += 1
            if self.right_index == self.left_index:
                self.left_index += 1
            self.res_left_index = self.left_index
        else:
            self.res_left_index = 0
        if root.right:
            self.right_index += 1
            if self.right_index == self.right_index:
                self.right_index += 1
            self.res_right_index = self.right_index
        else:
            self.res_right_index = 0
        print(root.value, self.res_left_index, self.res_right_index)
        self.preorder(root.left)
        self.preorder(root.right)


start()

with open("input.txt") as f:
    n = int(f.readline())
    nodes = [int(f.readline().split()[0]) for i in range(n + 1)]

tree = AVLTree()
root = None
for node in nodes:
    root = tree.insert(node, root)

orig_stdout = sys.stdout
with open("output.txt", "w") as g:
    g.write(str(len(nodes)) + "\n")
    sys.stdout = g
    tree.preorder(root)
sys.stdout = orig_stdout

print('Time:', str(process_time()), 'sec')
print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')