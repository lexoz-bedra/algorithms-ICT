from time import process_time
from tracemalloc import start, get_traced_memory


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def in_order_traversal(root, res):
    if root:
        in_order_traversal(root.left, res)
        res.append(str(root.val))
        in_order_traversal(root.right, res)


def pre_order_traversal(root, res):
    if root:
        res.append(str(root.val))
        pre_order_traversal(root.left, res)
        pre_order_traversal(root.right, res)


def post_order_traversal(root, res):
    if root:
        post_order_traversal(root.left, res)
        post_order_traversal(root.right, res)
        res.append(str(root.val))


start()

with open("input.txt") as f:
    n = int(f.readline())
    nodes = []
    for i in range(n):
        k, l, r = map(int, f.readline().split())
        node = Node(k)
        node.left = l
        node.right = r
        nodes.append(node)

for i in range(n):
    if nodes[i].left != -1:
        nodes[i].left = nodes[nodes[i].left]
    else:
        nodes[i].left = None
    if nodes[i].right != -1:
        nodes[i].right = nodes[nodes[i].right]
    else:
        nodes[i].right = None

root = nodes[0]

inorder_res = []
preorder_res = []
postorder_res = []

in_order_traversal(root, inorder_res)
pre_order_traversal(root, preorder_res)
post_order_traversal(root, postorder_res)

with open("output.txt", "w+") as g:
    g.write(" ".join(inorder_res) + "\n")
    g.write(" ".join(preorder_res) + "\n")
    g.write(" ".join(postorder_res) + "\n")

print('Time:', str(process_time()), 'sec')
print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')
