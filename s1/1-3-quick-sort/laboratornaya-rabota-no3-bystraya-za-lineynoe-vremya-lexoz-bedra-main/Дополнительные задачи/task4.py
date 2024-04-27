from random import randint
from time import process_time
from tracemalloc import start, get_traced_memory


def partition_3(arr, first, last):
    cur = arr[first][0]
    left = [[], []]
    mid = [[], []]
    right = [[], []]
    j = 0
    cnt = 0
    for i in range(first, last + 1):
        if arr[i][0] < cur:
            left[0].append(arr[i][0])
            left[1].append(arr[i][1])
            j += 1
        elif arr[i][0] == cur:
            mid[0].append(arr[i][0])
            mid[1].append(arr[i][1])
            cnt += 1
        else:
            right[0].append(arr[i][0])
            right[1].append(arr[i][1])
    total0 = left[0] + mid[0] + right[0]
    total1 = left[1] + mid[1] + right[1]
    for i in range(len(total0)):
        arr[first + i][0] = total0[i]
        arr[first + i][1] = total1[i]
    return first + j, first + j + cnt - 1


def randomized_quick_sort(arr, first, last):
    if first < last:
        k = randint(first, last)
        arr[first], arr[k] = arr[k], arr[first]
        m1, m2 = partition_3(arr, first, last)
        randomized_quick_sort(arr, first, m1 - 1)
        randomized_quick_sort_under(arr, m1, m2)
        randomized_quick_sort(arr, m2 + 1, last)


def partition_3_under(arr, first, last):
    cur = arr[first][1]
    left = []
    mid = []
    right = []
    j = 0
    cnt = 0
    for i in range(first, last + 1):
        if arr[i][1] < cur:
            left.append(arr[i][1])
            j += 1
        elif arr[i][1] == cur:
            mid.append(arr[i][1])
            cnt += 1
        else:
            right.append(arr[i][1])
    total = left + mid + right
    for i in range(len(total)):
        arr[first + i][1] = total[i]
    return first + j, first + j + cnt - 1


def randomized_quick_sort_under(arr, first, last):
    if first < last:
        k = randint(first, last)
        arr[first][1], arr[k][1] = arr[k][1], arr[first][1]
        m1, m2 = partition_3_under(arr, first, last)
        randomized_quick_sort_under(arr, first, m1 - 1)
        randomized_quick_sort_under(arr, m2 + 1, last)


if __name__ == '__main__':
    start()
    with open('input.txt', 'r') as f:
        s, p = map(int, f.readline().split())
        sgms = [[int(i) for i in f.readline().split()] for i in range(s)]
        dots = list(map(int, f.readline().split()))
    randomized_quick_sort(sgms, 0, s - 1)
    with open('output.txt', 'w+') as g:
        for i in range(p):
            count = 0
            idx = 0
            while idx < s and dots[i] >= sgms[idx][0]:
                if dots[i] <= sgms[idx][1]:
                    count += 1
                idx += 1
            g.write(str(count) + ' ')
    print('Time:', str(process_time()), 'sec')
    print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')