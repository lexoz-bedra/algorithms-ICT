from time import process_time
from tracemalloc import start, get_traced_memory


M = 1000000001


class HashTable:
    def __init__(self):
        self.table = {}
        self.last_sum = 0

    def add(self, x):
        self.table[(x + self.last_sum) % M] = True

    def remove(self, x):
        self.table.pop((x + self.last_sum) % M, None)

    def find(self, x, fileo):
        if (x + self.last_sum) % M in self.table:
            fileo.write(("Found") + "\n")
        else:
            fileo.write(("Not found") + "\n")

    def sum(self, l, r, fileo):
        s = 0
        for i in range(l + self.last_sum, r + self.last_sum + 1):
            if i % M in self.table:
                s += i % M
        self.last_sum = s % M
        fileo.write(str(self.last_sum) + "\n")


start()

hash_table = HashTable()

with open("input.txt") as f, open("output.txt", "w+") as g:
    n = int(f.readline())
    for i in range(n):
        query = f.readline().split()
        if query[0] == "+":
            hash_table.add(int(query[1]))
        elif query[0] == "-":
            hash_table.remove(int(query[1]))
        elif query[0] == "?":
            hash_table.find(int(query[1]), g)
        elif query[0] == "s":
            hash_table.sum(int(query[1]), int(query[2]), g)

print('Time:', str(process_time()), 'sec')
print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')
