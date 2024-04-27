from time import process_time
from tracemalloc import start, get_traced_memory


def fractional_knapsack(n: int, w: int, prices: list, weights: list) -> float:
    ratio = []
    for i in range(n):
        ratio.append(prices[i] / weights[i])
    res = 0
    while w > 0:
        if weights[ratio.index(max(ratio))] > w:
            res += ratio[ratio.index(max(ratio))] * w
            ratio.pop(ratio.index(max(ratio)))
            w = 0
        else:
            res += ratio[ratio.index(max(ratio))] * weights[ratio.index(max(ratio))]
            w -= weights[ratio.index(max(ratio))]
            ratio.pop(ratio.index(max(ratio)))

    return res


if __name__ == '__main__':
    start()
    ws, ps = [], []
    with open('input.txt', 'r') as f:
        n, w = map(int, f.readline().split())
        for i in range(n):
            price, weight = map(int, f.readline().split())
            ps.append(price)
            ws.append(weight)
    res = fractional_knapsack(n, w, ps, ws)
    with open('output.txt', 'w+') as g:
        g.write(str(res))

        print('Time:', str(process_time()), 'sec')
        print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')
