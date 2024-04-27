from time import process_time
from tracemalloc import *
start()
with open('../input.txt', 'r') as f:
    n = int(f.readline())
    a = [int(i) for i in f.readline().split()]
def insertion_sort(l):
    for i in range(len(l)):
        for j in range(i):
            if l[j] > l[i]:
                l[j], l[i] = l[i], l[j]
    return l
print(process_time())
snapshot = take_snapshot()
for stat in snapshot.statistics('lineno'):
    print(stat)
with open('../output.txt', 'w+') as g:
    g.write(' '.join(str(i) for i in insertion_sort(a)))
