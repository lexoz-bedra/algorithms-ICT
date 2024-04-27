from time import process_time
from tracemalloc import *
start()
with open('../input.txt', 'r') as f:
    n = int(f.readline())
    a = [float(i) for i in f.readline().split()]
idxs = [i for i in range(len(a))]
for i in range(len(a)):
    for j in range(i):
        if a[j] > a[i]:
            a[j], a[i] = a[i], a[j]
            idxs[j], idxs[i] = idxs[i], idxs[j]
print(process_time())
shapshot = take_snapshot()
for stat in shapshot.statistics('lineno'):
    print(stat)
with open('../output.txt', 'w+') as g:
    g.write(str(idxs[0] + 1) + ' ' + str(idxs[n // 2] + 1) + ' ' + str(idxs[n-1] + 1))
