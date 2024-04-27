from time import process_time
from tracemalloc import start, get_traced_memory


class Node:  
    def __init__(self, data): 
        self.data = data
        self.left = self.right = None


class BinaryTree:
    def __init__(self): 
        self.root = None

    def __find(self, node, parent, value):
        if node is None:
            return None, parent, False

        if value == node.data:
            return node, parent, True

        if value < node.data and node.left:
            return self.__find(node.left, node, value)

        if value > node.data and node.right:
            return self.__find(node.right, node, value)

        return node, parent, False

    def append(self, obj):
        if self.root is None:
            self.root = obj
            return obj
        s, p, fl_find = self.__find(self.root, None, obj.data)
        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj
        return obj

    def in_order_traversal(self, node, res):
        if node:
            self.in_order_traversal(node.left, res)
            res.append(node.data)
            self.in_order_traversal(node.right, res)

    def kth_smallest(self, k):
        res = []
        self.in_order_traversal(self.root, res)
        if k <= len(res):
            return res[k - 1]
        else:
            return None


start()
t = BinaryTree()

with open("output.txt", "w+") as g:
    with open("input.txt") as f:
        all_info = f.readlines()
        cleared_info = []
        for i in all_info:
            if "\n" in i:
                cleared_info.append(i.replace("\n", ""))
            else:
                cleared_info.append(i)
        for i in cleared_info:
            if "+" in i:
                t.append(Node(int(i[2])))
            else:
                g.write(str(t.kth_smallest(int(i[2]))) + "\n")

print('Time:', str(process_time()), 'sec')
print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')
