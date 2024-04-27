import math
import time
import os
import psutil

process = psutil.Process(os.getpid())
t_start = time.perf_counter()


def left(idx):
    return 2 * idx + 1


def right(idx):
    return 2 * idx + 2


def min_heapify(array, idx):
    lf = left(idx)
    rt = right(idx)
    global heap_size
    if lf <= heap_size and array[lf] < array[idx]:
        small = lf
    else:
        small = idx
    if rt <= heap_size and array[rt] < array[small]:
        small = rt
    if small != idx:
        global m, swaps
        m += 1
        swaps.append([idx, small])
        array[idx], array[small] = array[small], array[idx]
        min_heapify(array, small)


def build_min_heap(array):
    global heap_size
    heap_size -= 1
    for i in range(math.floor(heap_size/2), -1, -1):
        min_heapify(array, i)


m = 0
swaps = []
with open('input.txt') as f:
    with open('output.txt', 'w') as g:
        n = int(f.readline())
        heap_size = n
        pyr = list(map(int, f.readline().split()))
        build_min_heap(pyr)
        g.write(str(m) + '\n')
        for i in range(len(swaps)):
            g.write(str(swaps[i][0]) + ' ' + str(swaps[i][1]) + '\n')

print("время работы", (time.perf_counter() - t_start), "секунд")
print('память', process.memory_info().rss / 1024 ** 2, 'mb')
