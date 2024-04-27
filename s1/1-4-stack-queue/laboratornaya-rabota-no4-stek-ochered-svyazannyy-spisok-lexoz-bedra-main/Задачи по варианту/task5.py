import time
import os
import psutil
process = psutil.Process(os.getpid())
t_start = time.perf_counter()

stack = []
arr = []

with open('input.txt', 'r') as f:
    for i, line in enumerate(f):
        if i > 0:
            if "push" in line:
                arr.append(int(line.replace('push ', '')[:-1]))
                print(arr)
            elif "pop" in line:
                if len(arr) == 0:
                    continue
                del arr[-1]
                print(arr)
            elif "max" in line:
                if len(arr) == 0:
                    continue
                stack.append(max(arr))

print(stack)
with open('output.txt', 'w') as x:
    x.writelines("%s\n" % line for line in stack)
print("время работы", (time.perf_counter() - t_start), "секунд")
print('память', process.memory_info().rss / 1024 ** 2, 'mb')

