from time import process_time
from tracemalloc import start, get_traced_memory


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
        return root


def height(root):
    if root is None:
        return 0
    else:
        left_height = height(root.left)
        right_height = height(root.right)

        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1


start()

root = None

with open("input.txt") as f:
    n = int(f.readline())
    for i in range(n):
        key, left, right = map(int, f.readline().split())
        if i == 0:
            root = Node(key)
        else:
            insert(root, key)
with open("output.txt", "w+") as g:
    g.write(str(height(root)))

print('Time:', str(process_time()), 'sec')
print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')
