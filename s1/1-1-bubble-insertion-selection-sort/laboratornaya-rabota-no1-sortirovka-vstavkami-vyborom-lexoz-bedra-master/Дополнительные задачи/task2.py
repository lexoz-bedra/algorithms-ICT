from time import process_time
from tracemalloc import *
start()
with open('../input.txt', 'r') as f:
    n = int(f.readline())
    a = [int(i) for i in f.readline().split()]
    b = a.copy()
idxs = [i for i in range(len(a))]
for i in range(len(a)):
    for j in range(i):
        if a[j] > a[i]:
            a[j], a[i] = a[i], a[j]
for i in range(len(b)):
    for j in range(len(a)):
        if a[i] == b[j]:
            idxs[j] = i
print(process_time())
snapshot = take_snapshot()
for stat in snapshot.statistics('lineno'):
    print(stat)
with open('../output.txt', 'w+') as g:
    g.write(' '.join(str(i + 1) for i in idxs) + '\n' + ' '.join(str(i) for i in a))
