from time import process_time
from tracemalloc import start, get_traced_memory


def knapsack(n: int, W: int, weights: list[int]) -> int:
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if weights[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + weights[i - 1])
    return dp[n][W]


if __name__ == '__main__':
    start()
    with open('input.txt', 'r') as f:
        W, n = map(int, f.readline().split())
        ws = [int(i) for i in f.readline().split()]
    res = knapsack(n, W, ws)
    with open('output.txt', 'w+') as g:
        g.write(str(res))

    print('Time:', str(process_time()), 'sec')
    print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')
