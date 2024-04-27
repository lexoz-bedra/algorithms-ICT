from task1 import merge_sort
from time import process_time
from tracemalloc import start, get_traced_memory

def binary_search(arr, l, r, n):
    if l <= r:
        mid = (r - l) // 2 + l
        if arr[mid] == n:
            return mid
        if arr[mid] > n:
            return binary_search(arr, l, mid - 1, n)
        return binary_search(arr, mid + 1, r, n)
    return -1


if __name__ == '__main__':
    start()
    with open('input.txt', 'r') as f:
        n1 = int(f.readline())
        a = [int(i) for i in f.readline().split()]
        n2 = int(f.readline())
        b = [int(i) for i in f.readline().split()]
    b = merge_sort(b)
    idxs = [binary_search(b, 0, len(b) - 1, i) for i in a]
    with open('output.txt', 'w+') as g:
        g.write(' '.join([str(i) for i in idxs]))
    print('Time:', str(process_time()), 'sec')
    print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')