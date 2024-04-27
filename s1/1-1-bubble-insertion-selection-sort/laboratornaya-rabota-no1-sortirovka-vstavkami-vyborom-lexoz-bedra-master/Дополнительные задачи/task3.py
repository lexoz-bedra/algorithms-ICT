from time import process_time
from tracemalloc import *
start()
with open('../input.txt', 'r') as f:
    n = int(f.readline())
    a = [int(i) for i in f.readline().split()]
for i in range(len(a)):
    for j in range(i):
        if a[j] < a[i]:
            a[j], a[i] = a[i], a[j]
print(process_time())
snapshot = take_snapshot()
for stat in snapshot.statistics('lineno'):
    print(stat)
with open('../output.txt', 'w+') as g:
    g.write(' '.join(str(i) for i in a))
