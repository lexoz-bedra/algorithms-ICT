from time import process_time
from tracemalloc import start, get_traced_memory


class BinarySearchTree:
    def __init__(self):
        self.value = 0
        self.left = 0
        self.right = 0


def isBST(tree, j):
    def check(tree, j, k, c):
        if k == 0:
            if tree[j].value > c:
                return False
        elif k == 1:
            if tree[j].value < c:
                return False
        if tree[j].left != 0 and not check(tree, tree[j].left, k, c):
            return False
        if tree[j].right != 0 and not check(tree, tree[j].right, k, c):
            return False
        return True

    if tree[j].left == 0 and tree[j].right == 0:
        return True
    if tree[j].left != 0 and tree[j].value < tree[tree[j].left].value:
        return False
    if tree[j].right != 0 and tree[j].value > tree[tree[j].right].value:
        return False
    if tree[j].left != 0 and not check(tree, tree[j].left, 0, tree[j].value):
        return False
    if tree[j].right != 0 and not check(tree, tree[j].right, 1, tree[j].value):
        return False
    if tree[j].left != 0 and not isBST(tree, tree[j].left):
        return False
    if tree[j].right != 0 and not isBST(tree, tree[j].right):
        return False
    return True

start()
with open("input.txt") as f, open("output.txt", "w") as g:
    n = int(f.readline())
    if n == 0:
        g.write("YES")
    else:
        tree = [BinarySearchTree() for _ in range(n + 1)]
        for i in range(1, n + 1):
            tree[i].value, tree[i].left, tree[i].right = map(int, f.readline().split())
        if isBST(tree, 1):
            g.write("YES")
        else:
            g.write("NO")

print('Time:', str(process_time()), 'sec')
print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')
