from time import process_time
from tracemalloc import *
start()
with open('input.txt') as f:
    n = int(f.readline())
    a = [int(i) for i in f.readline().split()]
def bubble_sort(l):
    for i in range(len(l)):
        for j in range(len(l) - 1, i, -1):
            if l[j - 1] > l[j]:
                l[j - 1], l[j] = l[j], l[j - 1]
    return l
print(process_time())
snapshot = take_snapshot()
for stat in snapshot.statistics('lineno'):
    print(stat)
with open('output.txt', 'w+') as g:
    g.write(' '.join(str(i) for i in bubble_sort(a)))
# доказательство корректности
for i in range(len(a) - 1):
    print(f'a[{i}] <= a[{i + 1}] - {bubble_sort(a)[i] <= bubble_sort(a)[i + 1]}')
