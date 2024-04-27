from time import process_time
from tracemalloc import start, get_traced_memory


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


class BinaryTree:
    def __init__(self):
        self.root = None

    def addNode(self, key):
        x = self.root
        y = None
        cmp = 0
        while x is not None:
            cmp = x.key - key
            if cmp == 0:
                return
            else:
                y = x
                if cmp < 0:
                    x = x.right
                else:
                    x = x.left
        newNode = Node(key)
        if y is None:
            self.root = newNode
        else:
            if cmp > 0:
                y.left = newNode
            else:
                y.right = newNode

    def removeSubtree(self, key):
        x = self.root
        y = None
        cmp = 0
        while x is not None:
            cmp = x.key - key
            if cmp == 0:
                break
            else:
                y = x
                if cmp < 0:
                    x = x.right
                else:
                    x = x.left

        if x is None:
            return 0

        count = self.nodesCount(x)
        if x.key > y.key:
            y.right = None
        else:
            y.left = None
        x = None
        return count

    def nodesCount(self, node):
        if node.left is None and node.right is None:
            return 1
        left = right = 0
        if node.left is not None:
            left = self.nodesCount(node.left)
        if node.right is not None:
            right = self.nodesCount(node.right)
        return left + right + 1


start()

with open("input.txt") as f, open("output.txt", "w") as g:
    nodesCount = int(f.readline())
    arrayNodes = []
    for i in range(nodesCount):
        line = list(map(int, f.readline().split()))
        arrayNodes.append(line)

    removesCount = int(f.readline())
    arrayRemove = list(map(int, f.readline().split()))

    tree = BinaryTree()
    for i in range(nodesCount):
        tree.addNode(arrayNodes[i][0])

    for i in range(removesCount):
        nodesCount -= tree.removeSubtree(arrayRemove[i])
        g.write(str(nodesCount) + "\n")

print('Time:', str(process_time()), 'sec')
print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')
