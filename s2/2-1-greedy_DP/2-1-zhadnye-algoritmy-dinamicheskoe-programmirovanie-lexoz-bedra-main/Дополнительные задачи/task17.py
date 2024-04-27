from time import process_time
from tracemalloc import start, get_traced_memory


def hod_konem(n):
    prev = [4, 2, 1, 0]
    curr = [0, 0, 0, 0]
    if n <= 1:
        return 8
    for i in range(0, n - 1):
        curr[0] += prev[1] * 2 + prev[2] * 2
        curr[1] += prev[0] + prev[3] * 2
        curr[2] += prev[0]
        curr[3] += prev[1]
        prev = []
        for i in range(0, 4):
            prev.append(curr[i])
        curr = [0, 0, 0, 0]
    return sum(prev) % 10**9


if __name__ == '__main__':
    start()
    with open('input.txt', 'r') as f:
        n = int(f.readline())

    res = hod_konem(n)

    with open('output.txt', 'w+') as g:
        g.write(str(res))

    print('Time:', str(process_time()), 'sec')
    print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')