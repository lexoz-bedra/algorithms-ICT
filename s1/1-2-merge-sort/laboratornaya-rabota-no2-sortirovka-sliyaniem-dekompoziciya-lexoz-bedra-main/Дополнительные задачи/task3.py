from time import process_time
from tracemalloc import start, get_traced_memory


def inversions(arr):
    if len(arr) < 2:
        return 0
    mid = len(arr) // 2
    l = arr[:mid]
    r = arr[mid:]
    return inversions(l) + inversions(r) + merge(arr, l, r)


def merge(arr, l, r):
    i = j = k = 0
    while i < len(l) or j < len(r):
        if i == len(l):
            arr[i + j] = r[j]
            j += 1
        elif j == len(r):
            arr[i + j] = l[i]
            i += 1
        elif l[i] <= r[j]:
            arr[i + j] = l[i]
            i += 1
        else:
            arr[i + j] = r[j]
            k += len(l) - i
            j += 1
    return k



if __name__ == '__main__':
    start()
    with open('input.txt', 'r') as f:
        n = int(f.readline())
        a = [int(i) for i in f.readline().split()]
    inv = inversions(a)
    with open('output.txt', 'w+') as g:
        g.write(str(inv))
    print('Time:', str(process_time()), 'sec')
    print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')
