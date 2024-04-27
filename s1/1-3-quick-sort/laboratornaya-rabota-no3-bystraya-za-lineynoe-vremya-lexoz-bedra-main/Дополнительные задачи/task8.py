from random import randint
from time import process_time
from tracemalloc import start, get_traced_memory


def partition_3(arr, first, last):
    cur = arr[first][0] ** 2 + arr[first][1] ** 2
    left = []
    mid = []
    right = []
    j = 0
    cnt = 0
    for i in range(first, last + 1):
        r = arr[i][0] ** 2 + arr[i][1] ** 2
        if r < cur:
            left.append(arr[i])
            j += 1
        elif r == cur:
            mid.append(arr[i])
            cnt += 1
        else:
            right.append(arr[i])
    arr[first:last + 1] = left + mid + right
    return first + j, first + j + cnt - 1


def randomized_quick_sort(arr, first, last):
    if first < last:
        k = randint(first, last)
        arr[first], arr[k] = arr[k], arr[first]
        m1, m2 = partition_3(arr, first, last)
        randomized_quick_sort(arr, first, m1 - 1)
        randomized_quick_sort(arr, m2 + 1, last)


if __name__ == '__main__':
    start()
    with open('input.txt', 'r') as g:
        n, k = map(int, g.readline().split())
        dots = [[int(i) for i in g.readline().split()] for i in range(n)]
    randomized_quick_sort(dots, 0, n - 1)
    with open('output.txt', 'w') as g:
        for i in range(k - 1):
            g.write(str(dots[i]) + ',')
        g.write(str(dots[k - 1]))
    print('Time:', str(process_time()), 'sec')
    print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')
