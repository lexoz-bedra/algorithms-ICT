from time import process_time
from tracemalloc import start, get_traced_memory


def max_boots(working_time: int, time: list[int]) -> int:
    res = 0
    while min(time) < working_time:
        minn = min(time)
        res += 1
        time[time.index(minn)] = 10 ** 3 + 1
        working_time -= minn
    return res


if __name__ == '__main__':
    start()
    with open('input.txt', 'r') as f:
        K, n = map(int, f.readline().split())
        t = [int(i) for i in f.readline().split()]
        res = max_boots(K, t)
    with open('output.txt', 'w+') as g:
        g.write(str(res))

    print('Time:', str(process_time()), 'sec')
    print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')
