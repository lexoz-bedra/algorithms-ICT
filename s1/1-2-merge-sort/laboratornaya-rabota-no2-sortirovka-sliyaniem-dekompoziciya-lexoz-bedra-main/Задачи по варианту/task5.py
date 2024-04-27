from task1 import merge_sort
from time import process_time
from tracemalloc import start, get_traced_memory

def left_binary_search(arr, l, r, n, idx):
    if l <= r:
        mid = (r - l) // 2 + l
        if arr[mid] == n:
            return left_binary_search(arr, l, mid - 1, n, mid)
        elif arr[mid] > n:
            return left_binary_search(arr, l, mid - 1, n, idx)
        return left_binary_search(arr, mid + 1, r, n, idx)
    return idx


def right_binary_search(arr, l, r, n, idx):
    if l <= r:
        mid = (r - l) // 2 + l
        if arr[mid] == n:
            return right_binary_search(arr, mid + 1, r, n, mid)
        elif arr[mid] > n:
            return right_binary_search(arr, l, mid - 1, n, idx)
        return right_binary_search(arr, mid + 1, r, n, idx)
    return idx


def majority(arr, n):
    if left_binary_search(arr, 0, len(arr) - 1, n, -1) != -1 and right_binary_search(arr, 0, len(arr) - 1, n, -1) != -1 and right_binary_search(arr, 0, len(arr) - 1, n, -1) - left_binary_search(arr, 0, len(arr) - 1, n, -1) + 1 > len(arr) // 2:
        return 1
    return 0


if __name__ == '__main__':
    start()
    with open('input.txt', 'r') as f:
        n = int(f.readline())
        a = [int(i) for i in f.readline().split()]
    a = merge_sort(a)
    flag = False
    for i in a:
        if majority(a, i) == 1:
            flag = True
    with open('output.txt', 'w+') as g:
        if flag:
            g.write('1')
        else:
            g.write('0')
    print('Time:', str(process_time()), 'sec')
    print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')




