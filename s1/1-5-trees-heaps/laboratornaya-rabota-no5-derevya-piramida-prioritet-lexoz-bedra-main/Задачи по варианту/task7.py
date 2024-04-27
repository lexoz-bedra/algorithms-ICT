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


def max_heapify(array, idx):
    lf = left(idx)
    rt = right(idx)
    global heap_size
    if lf <= heap_size and array[lf] > array[idx]:
        big = lf
    else:
        big = idx
    if rt <= heap_size and array[rt] > array[big]:
        big = rt
    if big != idx:
        array[idx], array[big] = array[big], array[idx]
        max_heapify(array, big)


def build_max_heap(array):
    global heap_size
    heap_size -= 1
    for idx in range(math.floor(heap_size/2), -1, -1):
        max_heapify(array, idx)
    return array


def heapsort(array):
    global heap_size, n
    build_max_heap(array)
    for i in range(n-1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heap_size -= 1
        max_heapify(array, 0)


with open('input.txt') as f:
    with open('output.txt', 'w') as g:
        n = int(f.readline())
        heap_size = n
        arr = list(map(int, f.readline().split()))
        heapsort(arr)
        if arr == sorted:
            print('*')
        for i in range(n):
            g.write(str(arr[i]) + ' ')

print("время работы", (time.perf_counter() - t_start), "секунд")
print('память', process.memory_info().rss / 1024 ** 2, 'mb')
