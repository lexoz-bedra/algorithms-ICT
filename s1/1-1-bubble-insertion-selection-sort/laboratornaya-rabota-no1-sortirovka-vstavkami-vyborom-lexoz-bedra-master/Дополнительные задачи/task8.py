from time import process_time
from tracemalloc import *
start()
with open('../input.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f.readline().split()]
g = open('../output.txt', 'w+')
for i in range(len(a)):
    for j in range(len(a)-1, i, -1):
        if a[j-1] > a[j]:
            a[j-1], a[j] = a[j], a[j-1]
            g.write(f'Swap elements at indices {j-1} and {j}.\n')
print(process_time())
snapshot = take_snapshot()
for stat in snapshot.statistics('lineno'):
    print(stat)
g.write('No more swaps needed.')
g.close()