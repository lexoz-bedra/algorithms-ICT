from time import process_time
from tracemalloc import start, get_traced_memory


class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


def is_bst(node, min_val=float("-inf"), max_val=float("inf")):
    if not node:
        return True
    if node.key < min_val or node.key > max_val:
        return False
    return is_bst(node.left, min_val, node.key - 1) and is_bst(node.right, node.key + 1, max_val)


def build_tree(n, nodes):
    tree = {}
    for i in range(n):
        key, left, right = nodes[i]
        if left == -1:
            left_child = None
        else:
            left_child = Node(nodes[left][0])
        if right == -1:
            right_child = None
        else:
            right_child = Node(nodes[right][0])
        node = Node(key, left_child, right_child)
        tree[i] = node
    return tree


start()

with open("input.txt", "r") as f:
    n = int(f.readline().strip())
    nodes = [tuple(map(int, line.strip().split())) for line in f.readlines()]
tree = build_tree(n, nodes)
with open("output.txt", "w+") as g:
    if n == 0 or is_bst(tree[0]):
        g.write("CORRECT")
    else:
        g.write("INCORRECT")

print('Time:', str(process_time()), 'sec')
print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')
