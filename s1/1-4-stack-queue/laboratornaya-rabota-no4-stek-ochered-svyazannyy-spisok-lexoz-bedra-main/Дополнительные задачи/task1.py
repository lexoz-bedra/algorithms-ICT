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
            if line[0] == "+":
                arr.append(line[2:-1])
            else:
                x = arr.pop(-1)
                stack.append(x)
            print(arr)
print(stack)
with open('output.txt', 'w') as x:
    x.writelines("%s\n" % line for line in stack)
print("время работы", (time.perf_counter() - t_start), "секунд")
print('память', process.memory_info().rss / 1024 ** 2, 'mb')
