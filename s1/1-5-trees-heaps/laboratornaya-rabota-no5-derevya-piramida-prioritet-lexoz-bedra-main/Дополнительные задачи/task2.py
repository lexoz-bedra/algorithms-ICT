import time
import os
import psutil

process = psutil.Process(os.getpid())
t_start = time.perf_counter()

with open('input.txt') as f:
    with open('output.txt', 'w') as g:
        n = int(f.readline())
        arr = list(map(int, f.readline().split()))
        tree = set(range(n)) - set(arr)
        arr = {i: [arr[i], 0] for i in range(n)}
        max_h = 0
        for i in tree:
            h = 1
            elem = i
            while arr[elem][0] != -1:
                if h+1 > arr[elem][1]:
                    h += 1
                    arr[elem][1] = h
                    elem = arr[elem][0]
                else:
                    break
            max_h = max(max_h, h)
        print(time.perf_counter() - t_start)
        g.write(str(max_h))

print("время работы", (time.perf_counter() - t_start), "секунд")
print('память', process.memory_info().rss / 1024 ** 2, 'mb')