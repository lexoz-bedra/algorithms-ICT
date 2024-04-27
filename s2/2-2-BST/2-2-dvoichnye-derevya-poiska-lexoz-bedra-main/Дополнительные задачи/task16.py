from time import process_time
from tracemalloc import start, get_traced_memory


class Stack:
    def init(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def remove(self, item):
        self.stack.remove(item)

    def maximum(self, item):
        self.stack.sort(reverse=True)
        g.write(str(self.stack[item - 1]) + "\n")


with open("input.txt") as f:
    n = int(f.readline())
    arr1 = []
    for s in f.readlines():
        temp = s.split(" ")
        for i in temp:
            i = i.replace("\n", "")
            arr1.append(i)
g = open("output.txt", "w+")

arr2 = Stack()
i = 0
while i <= len(arr1) - 1:
    if arr1[i] == "-1":
        arr2.remove(int(arr1[i + 1]))
        i += 2
    elif arr1[i] == "+1":
        arr2.push(int(arr1[i + 1]))
        i += 2
    elif arr1[i] == "0":
        arr2.maximum(int(arr1[i + 1]))
        i += 2
g.close()

print('Time:', str(process_time()), 'sec')
print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')
