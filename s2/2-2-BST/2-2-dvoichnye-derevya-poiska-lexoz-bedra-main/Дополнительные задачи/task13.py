from collections import deque
from time import process_time
from tracemalloc import start, get_traced_memory


start()

result = []


class Node:
    def __init__(self, value, parent=None, left=None, right=None, next=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        self.height = 0
        self.key = 0
        self.next = next


def get_tree(root):
    global result
    stack = deque()
    stack.append((root, (-1, -1)))

    while stack:
        elem, q = stack.popleft()
        if q[0] >= 0 and q[1] >= 0:
            result[q[0]][q[1]] = len(result) + 1
        if elem is None:
            continue

        result.append([elem.value, 0, 0])
        curr = len(result)
        if elem.left is not None:
            stack.append((elem.left, (curr - 1, 1)))
        if elem.right is not None:
            stack.append((elem.right, (curr - 1, 2)))


def rotate_left(node):
    if node is None or node.right is None:
        return node
    parent = node.parent
    right = node.right
    right_left = right.left
    if parent:
        if parent.right == node:
            parent.right = right
        else:
            parent.left = right
    right.parent, right.left = parent, node
    node.parent, node.right = right, right_left
    if right_left:
        right_left.parent = node
    return right


def rotate_right(node):
    if node is None or node.left is None:
        return node
    parent = node.parent
    left = node.left
    left_right = left.right
    if parent:
        if parent.left == node:
            parent.left = left
        else:
            parent.right = left
    left.parent, left.right = parent, node
    node.parent, node.left = left, left_right
    if left_right:
        left_right.parent = node
    return left


def arr_load(root, n):
    arr = deque()
    for i in range(1, n + 1):
        if root[i].left is None and root[i].right is None:
            root[i].height = 1
            arr.append(root[i])
    while arr:
        elem = arr.pop()
        if elem is None:
            continue
        if elem.parent is not None:
            elem.parent.height = max(elem.parent.height, elem.height + 1)
        arr.append(elem.parent)


def arr_res(root):
    curr_res = 0
    arr = deque()
    arr.append((root, 0))
    while len(arr):
        elem = arr.pop()
        if elem[0] is None:
            continue
        arr.append((elem[0].left, elem[1] + 1))
        arr.append((elem[0].right, elem[1] + 1))
        curr_res = max(curr_res, elem[1] + 1)
    return curr_res

start()

f = open("input.txt")
g = open("output.txt", "w")
n = int(f.readline())


node_arr = []
for _ in range(n + 1):
    node_arr.append(Node(0))
for j in range(n):
    key, left, right = map(int, f.readline().split())
    node_arr[j + 1].value = key
    if left:
        node_arr[j + 1].left, node_arr[left].parent = node_arr[left], node_arr[j + 1]
    if right:
        node_arr[j + 1].right, node_arr[right].parent = node_arr[right], node_arr[j + 1]

if node_arr[1].right is not None and arr_res(node_arr[1].right.right) - arr_res(node_arr[1].right.left) == -1:
    rotate_right(node_arr[1].right)
    node_arr[1] = rotate_left(node_arr[1])
else:
    node_arr[1] = rotate_left(node_arr[1])


get_tree(node_arr[1])
g.write(f"""{len(result)} \n""")
for m, l, n in result:
    g.write(f"""{m} {l} {n} \n""")

print('Time:', str(process_time()), 'sec')
print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')
