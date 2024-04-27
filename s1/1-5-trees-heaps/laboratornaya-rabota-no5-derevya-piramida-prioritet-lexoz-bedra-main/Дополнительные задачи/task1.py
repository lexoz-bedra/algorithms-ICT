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


with open('input.txt') as f:
    with open('output.txt', 'w') as g:
        n = int(f.readline())
        arr = list(map(int, f.readline().split()))
        for i in range(math.floor(n / 2) - 1):
            if arr[i] > arr[left(i)] or arr[i] > arr[right(i)]:
                g.write('NO')
                exit()
        g.write('YES')

print("время работы", (time.perf_counter() - t_start), "секунд")
print('память', process.memory_info().rss / 1024 ** 2, 'mb')
