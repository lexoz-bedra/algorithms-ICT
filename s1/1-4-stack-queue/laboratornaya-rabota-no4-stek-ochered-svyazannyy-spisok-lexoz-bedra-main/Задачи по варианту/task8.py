import time
import os
import psutil

process = psutil.Process(os.getpid())
t_start = time.perf_counter()

stack = []
c = 0

with open('input.txt', 'r') as f:
    for i in range(1):
        f.readline()
    stack = f.readline()
    stack = (list(map(str, stack.split())))

    while len(stack) != 1:
        if stack[c] == '+':
            summ = int(stack[c - 2]) + int(stack[c - 1])
            del stack[c - 2:c + 1]
            stack.insert(c - 2, str(summ))
            c = 0
        if stack[c] == '-':
            diff = int(stack[c - 2]) - int(stack[c - 1])
            del stack[c - 2:c + 1]
            stack.insert(c - 2, str(diff))
            c = 0
        if stack[c] == '*':
            prod = int(stack[c - 2]) * int(stack[c - 1])
            del stack[c - 2:c + 1]
            stack.insert(c - 2, str(prod))
            c = 0
        print(c)
        print(stack)
        c += 1

with open('output.txt', 'w') as x:
    x.writelines("%s\n" % line for line in stack)

print("время работы", (time.perf_counter() - t_start), "секунд")
print('память', process.memory_info().rss / 1024 ** 2, 'mb')
