from time import process_time
from tracemalloc import start, get_traced_memory


def maxSubArray(arr):
    idx = 0
    idx_len = 0
    summ = 0
    max_sum = 0
    for i in range(len(arr)):
        if summ < 0:
            summ = 0
        if summ == 0:
            idx = i
        summ += arr[i]
        if summ > max_sum:
            max_sum = summ
            idx_len = i
        if max_sum == 0:
            idx = -1
            idx_len = -1
    return arr[idx: idx_len + 1]


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        n = f.readline()
        a = [int(i) for i in f.readline().split()]
    res = maxSubArray(a)
    with open('output.txt', 'w+') as g:
        g.write(' '.join([str(i) for i in res]))
    print('Time:', str(process_time()), 'sec')
    print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')
