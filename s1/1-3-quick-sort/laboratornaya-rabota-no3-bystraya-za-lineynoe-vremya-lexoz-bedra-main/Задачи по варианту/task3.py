from copy import copy
from task1 import randomized_quick_sort
from time import process_time
from tracemalloc import start, get_traced_memory


def scarecrow(arr, num, key):
    sorted_array = copy(arr)
    for i in range(key):
        arr1 = []
        idx = i
        size = 0
        while idx <= num - 1:
            arr1.append(sorted_array[idx])
            idx += key
            size += 1
        randomized_quick_sort(arr1, 0, size - 1)
        for j in range(size):
            sorted_array[i + j * key] = arr1[j]
    randomized_quick_sort(arr, 0, num - 1)
    if sorted_array == arr:
        return True
    return False


if __name__ == "__main__":
    start()
    with open('input.txt', 'r') as f:
        n, k = map(int, f.readline().split())
        array = [int(i) for i in f.readline().split()]
    with open('output.txt', 'w+') as g:
        if scarecrow(array, n, k):
            g.write('ДА')
        else:
            g.write('НЕТ')
    print('Time:', str(process_time()), 'sec')
    print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')
