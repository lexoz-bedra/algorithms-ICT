from time import process_time
from tracemalloc import *
start()
with open('../input.txt', 'r') as f:
    a = [int(i) for i in f.readline().split()]
    v = int(f.readline())
def linear_search(l, x):
    idxs = []
    for i in range(len(l)):
        if l[i] == x:
            idxs.append(i)
    return idxs
print(process_time())
snapshot = take_snapshot()
for stat in snapshot.statistics('lineno'):
    print(stat)
with open('../output.txt', 'w+') as g:
    if len(linear_search(a, v)) == 0:
        g.write('-1')
    elif len(linear_search(a, v)) == 1:
        g.write(str(linear_search(a, v)[0]))
    else:
        g.write(str(len(linear_search(a, v))) + '\n' + ', '.join(str(i) for i in linear_search(a, v)))
