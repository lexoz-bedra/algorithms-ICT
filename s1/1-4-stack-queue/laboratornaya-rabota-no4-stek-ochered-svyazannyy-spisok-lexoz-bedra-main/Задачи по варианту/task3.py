from collections import deque
import time
import os
import psutil
process = psutil.Process(os.getpid())
t_start = time.perf_counter()

brackets = deque()
arr = []
stack = []
with open('input.txt', 'r') as f:
    num = int(f.readline())
    for _ in range(num):
        arr.append(f.readline())
for seq in arr:
    for i in seq:
        if i == '(' or i == '[':
            brackets.append(i)
        elif len(brackets) == 0 and (i == ')' or i == ']'):
            brackets.append('ERROR')
            break
        elif i == ')' and brackets[len(brackets) - 1] == '(' or i == ']' and brackets[len(brackets) - 1] == '[':
            brackets.pop()
    if len(brackets) == 0:
        stack.append('YES')
    elif len(brackets) != 0 and 'ERROR' not in stack:
        stack.append('NO')
    brackets.clear()

with open('output.txt', 'w') as g:
    g.write('\n'.join(stack))

print("время работы", (time.perf_counter() - t_start), "секунд")
print('память', process.memory_info().rss / 1024 ** 2, 'mb')

