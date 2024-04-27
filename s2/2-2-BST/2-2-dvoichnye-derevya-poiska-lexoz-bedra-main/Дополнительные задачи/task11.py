from time import process_time
from tracemalloc import start, get_traced_memory


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def balance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        return x

    def insert(self, key):
        def insert_helper(node, key):
            if node is None:
                return Node(key)

            if key < node.key:
                node.left = insert_helper(node.left, key)
            elif key > node.key:
                node.right = insert_helper(node.right, key)
            else:
                return node

            node.height = 1 + max(self.height(node.left), self.height(node.right))
            balance = self.balance(node)

            if balance > 1 and key < node.left.key:
                return self.right_rotate(node)

            if balance < -1 and key > node.right.key:
                return self.left_rotate(node)

            if balance > 1 and key > node.left.key:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)

            if balance < -1 and key < node.right.key:
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)

            return node

        self.root = insert_helper(self.root, key)

    def delete(self, key):
        def delete_helper(node, key):
            if node is None:
                return node

            if key < node.key:
                node.left = delete_helper(node.left, key)
            elif key > node.key:
                node.right = delete_helper(node.right, key)
            else:
                if node.left is None:
                    temp = node.right
                    node = None
                    return temp
                elif node.right is None:
                    temp = node.left
                    node = None
                    return temp

                temp = self.get_min_value_node(node.right)
                node.key = temp.key
                node.right = delete_helper(node.right, temp.key)

            if node is None:
                return node

            node.height = 1 + max(self.height(node.left), self.height(node.right))
            balance = self.balance(node)

            if balance > 1 and self.balance(node.left) >= 0:
                return self.right_rotate(node)

            if balance < -1 and self.balance(node.right) <= 0:
                return self.left_rotate(node)

            if balance > 1 and self.balance(node.left) < 0:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)

            if balance < -1 and self.balance(node.right) > 0:
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)

            return node

        self.root = delete_helper(self.root, key)

    def get_min_value_node(self, node):
        current = node

        while current.left is not None:
            current = current.left

        return current

    def search(self, key):
        def search_helper(node, key):
            if node is None:
                return False

            if key == node.key:
                return True
            elif key < node.key:
                return search_helper(node.left, key)
            else:
                return search_helper(node.right, key)

        return search_helper(self.root, key)

    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def max_value_node(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current

    def search(self, key):
        def search_helper(node, key):
            if node is None:
                return "false"

            if key == node.key:
                return "true"
            elif key < node.key:
                return search_helper(node.left, key)
            else:
                return search_helper(node.right, key)

        return search_helper(self.root, key)

    def next(self, key):
        def next_helper(node, key):
            if node is None:
                return None

            if node.key <= key:
                return next_helper(node.right, key)

            left = next_helper(node.left, key)
            if left is not None:
                return left

            return node

        node = next_helper(self.root, key)
        return node.key if node is not None else None

    def prev(self, key):
        def prev_helper(node, key):
            if node is None:
                return None

            if node.key >= key:
                return prev_helper(node.left, key)

            right = prev_helper(node.right, key)
            if right is not None:
                return right

            return node

        node = prev_helper(self.root, key)
        return node.key if node is not None else None


start()

avl = AVLTree()

with open("output.txt", "w+") as g:
    with open("input.txt") as f:
        all_info = f.readlines()
        for i in all_info:
            if "\n" in i:
                action = i.replace("\n", "")
            else:
                action = i
            if "insert" in action:
                avl.insert(int(action[-1]))
            elif "exists" in action:
                g.write(str(avl.search(int(action[-1]))) + "\n")
            elif "delete" in action:
                avl.delete(int(action[-1]))
            elif "next" in action:
                if str(avl.next(int(action[-1]))) == "None":
                    g.write("none" + "\n")
                else:
                    g.write(str(avl.next(int(action[-1]))) + "\n")
            elif "prev" in action:
                if str(avl.prev(int(action[-1]))) == "None":
                    g.write("none" + "\n")
                else:
                    g.write(str(avl.prev(int(action[-1]))) + "\n")

print('Time:', str(process_time()), 'sec')
print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')