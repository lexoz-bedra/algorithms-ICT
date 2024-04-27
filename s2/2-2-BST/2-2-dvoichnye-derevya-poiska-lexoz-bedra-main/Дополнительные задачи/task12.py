from time import process_time
from tracemalloc import start, get_traced_memory


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        node = insert(root.left, key)
        root.left = node
        node.parent = root
    else:
        node = insert(root.right, key)
        root.right = node
        node.parent = root
    return root


def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))


def AVL(root):
    if root is None:
        return True
    lh = height(root.left)
    rh = height(root.right)
    return str(rh - lh)


def print_balance(node, fileo):
    if node is None:
        return
    fileo.write(str((AVL(node))) + "\n")
    print_balance(node.left, fileo)
    print_balance(node.right, fileo)


start()

with open("input.txt") as f:
    n = int(f.readline())
    root = None
    for i in range(n):
        key, left, right = map(int, f.readline().split())
        root = insert(root, key)

with open("output.txt", "w+") as g:
    print_balance(root, g)

print('Time:', str(process_time()), 'sec')
print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')
