from time import process_time
from tracemalloc import start, get_traced_memory



class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


def is_bst(node, min_key, max_key):
    if node is None:
        return True
    if node.key < min_key or node.key >= max_key:
        return False
    return is_bst(node.left, min_key, node.key) and is_bst(node.right, node.key, max_key)


def build_tree(n, nodes):
    tree = [None] * n
    for i in range(n):
        key, left, right = nodes[i]
        left_child = None if left == -1 else tree[left]
        right_child = None if right == -1 else tree[right]
        tree[i] = Node(key, left_child, right_child)
    return tree[0]


start()

with open("input.txt") as f:
    n = int(f.readline().strip())
    nodes = [tuple(map(int, line.strip().split())) for line in f.readlines()]

root = build_tree(n, nodes)

with open("output.txt", "w+") as g:
    if is_bst(root, -float("inf"), float("inf")):
        g.write("CORRECT")
    else:
        g.write("INCORRECT")

print('Time:', str(process_time()), 'sec')
print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')
