from time import process_time
from tracemalloc import start, get_traced_memory


def apples(a: list[int], b: list[int], s: int, n: int, order: list[int], start_apples: list[int]) \
        -> list[int]:
    if n == 0:
        return order
    diffs = [0] * n
    max_diff = 0
    for i in range(n):
        diffs[i] += (b[i] - a[i])
        if s - a[i] > 0:
            max_diff = max(max_diff, diffs[i])
        else:
            diffs[i] = -10 ** 6
    if diffs.count(-10 ** 6) == n:
        return [-1]
    order.append(start_apples.index(max(diffs)) + 1)
    s += diffs[diffs.index(max(diffs))]
    a.pop(diffs.index(max(diffs)))
    b.pop(diffs.index(max(diffs)))
    diffs.pop(diffs.index(max(diffs)))
    n -= 1
    return apples(a, b, s, n, order, start_apples)


if __name__ == '__main__':
    start()
    with open('input.txt', 'r') as f:
        n, s = map(int, f.readline().split())
        a, b = [0] * n, [0] * n
        start_apples = []
        for i in range(n):
            a[i], b[i] = map(int, f.readline().split())
            start_apples.append(b[i] - a[i])
    res = apples(a, b, s, n, [], start_apples)
    with open('output.txt', 'w+') as g:
        g.write(' '.join([str(i) for i in res]))

    print('Time:', str(process_time()), 'sec')
    print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')
