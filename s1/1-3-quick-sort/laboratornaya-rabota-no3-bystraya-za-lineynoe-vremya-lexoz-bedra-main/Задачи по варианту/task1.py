from random import randint
from time import process_time
from tracemalloc import start, get_traced_memory


def partition_3(arr, first, last):
    cur = arr[first]
    left = []
    mid = []
    right = []
    j = 0
    count = 0
    for i in range(first, last + 1):
        if arr[i] < cur:
            left.append(arr[i])
            j += 1
        elif arr[i] == cur:
            mid.append(arr[i])
            count += 1
        else:
            right.append(arr[i])
    arr[first: last + 1] = left + mid + right
    return first + j, first + j + count - 1


def randomized_quick_sort(arr, first, last):
    if first < last:
        k = randint(first, last)
        arr[first], arr[k] = arr[k], arr[first]
        m1, m2 = partition_3(arr, first, last)
        randomized_quick_sort(arr, first, m1 - 1)
        randomized_quick_sort(arr, m2 + 1, last)


if __name__ == "__main__":
    start()
    with open('input.txt', 'w') as f:
        n = randint(0, 10 ** 3)
        f.write(str(n) + '\n')
        array = [randint(-10 ** 6, 10 ** 6) for i in range(n)]
        f.write(' '.join(str(i) for i in array))
    randomized_quick_sort(array, 0, n - 1)
    with open('output.txt', 'w+') as g:
        g.write(' '.join(str(i) for i in array))
    print('Time:', str(process_time()), 'sec')
    print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')

