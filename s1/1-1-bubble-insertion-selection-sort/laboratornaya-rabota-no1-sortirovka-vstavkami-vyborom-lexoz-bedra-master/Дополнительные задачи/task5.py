from time import process_time
from tracemalloc import *
start()
with open('../input.txt', 'r') as f:
    n = int(f.readline())
    a = [int(i) for i in f.readline().split()]
def selection_sort(l):
    minn = 10 ** 9 + 1
    for i in range(len(l)):
        for j in range(i, len(l)):
            if l[j] < minn:
                minn = l[j]
                l[j], l[i] = l[i], l[j]
        minn = 10 ** 9 + 1
    return l
print(process_time())
snapshot = take_snapshot()
for stat in snapshot.statistics('lineno'):
    print(stat)
with open('../output.txt', 'w+') as g:
    g.write(' '.join(str(i) for i in selection_sort(a)))
