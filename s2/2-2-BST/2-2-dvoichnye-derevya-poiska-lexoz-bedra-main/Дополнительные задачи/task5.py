from time import process_time
from tracemalloc import start, get_traced_memory


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def deleteNode(root, key):
    if root is None:
        return root
    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minValueNode(root.right)
        root.val = temp.val
        root.right = deleteNode(root.right, temp.val)
    return root


def exists(root, key):
    if root is None:
        return False
    if root.val == key:
        return True
    elif root.val < key:
        return exists(root.right, key)
    else:
        return exists(root.left, key)


def nextNode(root, key):
    if root is None:
        return None
    if root.val <= key:
        return nextNode(root.right, key)
    else:
        left = nextNode(root.left, key)
        if left is not None:
            return left
        else:
            return root.val


def prevNode(root, key):
    if root is None:
        return None
    if root.val >= key:
        return prevNode(root.left, key)
    else:
        right = prevNode(root.right, key)
        if right is not None:
            return right
        else:
            return root.val


start()

root = None

with open("input.txt", "r") as f, open("output.txt", "w") as g:
    for line in f:
        op, val = line.split()
        val = int(val)

        if op == "insert":
            root = insert(root, val)
        elif op == "delete":
            root = deleteNode(root, val)
        elif op == "exists":
            g.write(str(exists(root, val)) + "\n")
        elif op == "next":
            nxt = nextNode(root, val)
            g.write("none\n" if nxt is None else str(nxt) + "\n")
        elif op == "prev":
            prv = prevNode(root, val)
            g.write("none\n" if prv is None else str(prv) + "\n")

print('Time:', str(process_time()), 'sec')
print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')
