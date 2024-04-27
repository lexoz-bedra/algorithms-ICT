from time import process_time
from tracemalloc import *
start()
with open('../input.txt') as f:
    a = [int(i) for i in f.readline().split()]
    b = [int(i) for i in f.readline().split()]
def binary_sum(l1, l2):
    res = [0] * (len(l1) + 1)
    for i in range(len(l1) - 1, -1, -1):
        res[i + 1] += l1[i] + l2[i]
        if res[i + 1] > 1:
            res[i + 1] -= 2
            res[i] += 1
    return res
print(process_time())
snapshot = take_snapshot()
for stat in snapshot.statistics('lineno'):
    print(stat)
with open('../output.txt', 'w+') as g:
    g.write(' '.join(str(i) for i in binary_sum(a, b)))
