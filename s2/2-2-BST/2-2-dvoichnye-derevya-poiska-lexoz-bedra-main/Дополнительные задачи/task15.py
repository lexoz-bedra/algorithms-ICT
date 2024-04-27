from time import process_time
from tracemalloc import start, get_traced_memory


class Node:
    def __init__(self, num):
        self.key = num
        self.left = None
        self.right = None
        self.height = 1


class Tree:
    def height(self, root):
        return root.height if root is not None else 0

    def balance_factor(self, root):
        return self.height(root.right) - self.height(root.left)

    def fix_height(self, root):
        left = self.height(root.left)
        right = self.height(root.right)
        root.height = max(left, right) + 1

    def rotateR(self, root):
        q = root.left
        root.left = q.right
        q.right = root
        self.fix_height(root)
        self.fix_height(q)
        return q

    def rotateL(self, root):
        p = root.right
        root.right = p.left
        p.left = root
        self.fix_height(root)
        self.fix_height(p)
        return p

    def balance(self, root):
        self.fix_height(root)
        if self.balance_factor(root) == 2:
            if self.balance_factor(root.right) < 0:
                root.right = self.rotateR(root.right)
            return self.rotateL(root)
        if self.balance_factor(root) == -2:
            if self.balance_factor(root.left) > 0:
                root.left = self.rotateL(root.left)
            return self.rotateR(root)
        return root

    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return self.balance(root)

    def find_right(self, root):
        if root.right is not None:
            return self.find_right(root.right)
        return root

    def find_right_and_delete(self, root):
        if root.right is not None:
            if root.right.right is None:
                root.right = root.right.left if (root.right.left is not None) else None
            else:
                root.right = self.find_right_and_delete(root.right)
        return self.balance(root)

    def remove(self, root, key):
        if root is None:
            return None
        if key < root.key:
            root.left = self.remove(root.left, key)
        elif key > root.key:
            root.right = self.remove(root.right, key)
        else:
            if (root.left is None) and (root.right is None):
                return None
            elif root.left is None:
                return root.right
            else:
                new_root = self.find_right(root.left)
                root.key = new_root.key
                if root.left.key == new_root.key:
                    root.left = None if (root.left.left is None) else root.left.left
                else:
                    root.left = self.find_right_and_delete(root.left)
        return self.balance(root)

    def get_str(self, root):
        if root is None:
            return None
        que = []
        number = 1
        que.append(root)
        ans = []
        while len(que) > 0:
            node = que.pop(0)
            line = f"{node.key} "
            if node.left is not None:
                number += 1
                line += f"{number} "
                que.append(node.left)
            else:
                line += "0 "
            if node.right is not None:
                number += 1
                line += f"{number}\n"
                que.append(node.right)
            else:
                line += "0\n"
            ans.append(line)
        return ans

start()

f = open("input.txt")
n = int(f.readline())
lines = [f.readline() for _ in range(n)]
lines.reverse()
nodes = {}
tree = Tree()

for i in range(n):
    Ki, Li, Ri = map(int, lines[i].split())
    node = Node(int(Ki))
    nodes[n - i] = node

    if Li != 0 and Ri != 0:
        node.left = nodes[Li]
        node.right = nodes[Ri]
        tree.fix_height(node)
    elif Li != 0:
        node.left = nodes[Li]
        tree.fix_height(node)
    elif Ri != 0:
        node.right = nodes[Ri]
        tree.fix_height(node)
    else:
        node.height = 1

if len(nodes) == 0:
    nodes[1] = None

key = int(f.readline())
root = tree.remove(nodes[1], key)
g = open("output.txt", "w")
ans = tree.get_str(root)

if ans is not None:
    g.write(f"{len(ans)}\n")
    for i in ans:
        g.write(i)
else:
    g.write("0")

g.close()
f.close()

print('Time:', str(process_time()), 'sec')
print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')
