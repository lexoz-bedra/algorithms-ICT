from time import process_time
from tracemalloc import start, get_traced_memory


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        r = arr[:mid]
        l = arr[mid:]
        merge_sort(l)
        merge_sort(r)
        merge(arr, l, r)
    return arr


def merge(arr, l, r):
    i = j = k = 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k += 1
    while i < len(l):
        arr[k] = l[i]
        i += 1
        k += 1
    while j < len(r):
        arr[k] = r[j]
        j += 1
        k += 1


if __name__ == '__main__':
    start()
    with open('input.txt', 'r') as f:
        n = int(f.readline())
        a = [int(i) for i in f.readline().split()]
    a = merge_sort(a)
    with open('output.txt', 'w+') as g:
        g.write(' '.join(str(i) for i in a))
    print('Time:', str(process_time()), 'sec')
    print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')
