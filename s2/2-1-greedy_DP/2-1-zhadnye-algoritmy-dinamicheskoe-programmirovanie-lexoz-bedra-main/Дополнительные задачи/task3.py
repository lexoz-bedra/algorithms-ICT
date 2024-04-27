from time import process_time
from tracemalloc import start, get_traced_memory


def max_income(n: int, prices: list, clicks: list) -> int:
    pairs = []
    res = 0
    for _ in range(n):
        pairs.append((max(prices), max(clicks)))
        prices[prices.index(max(prices))] = -(10**5) - 1
        clicks[clicks.index(max(clicks))] = -(10 ** 5) - 1
    for i in pairs:
        res += (i[0] * i[1])
    return res


if __name__ == '__main__':
    start()
    with open('input.txt', 'r') as f:
        n = int(f.readline())
        a = [int(i) for i in f.readline().split()]
        b = [int(i) for i in f.readline().split()]
    res = max_income(n, a, b)
    with open('output.txt', 'w+') as g:
        g.write(str(res))

    print('Time:', str(process_time()), 'sec')
    print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')
