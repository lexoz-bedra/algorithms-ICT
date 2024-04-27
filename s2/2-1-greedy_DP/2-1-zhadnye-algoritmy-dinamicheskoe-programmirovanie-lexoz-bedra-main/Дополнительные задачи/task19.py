from time import process_time
from tracemalloc import start, get_traced_memory


def output(path, i, j):
    if i == j:
        return 'A'
    return '(' + output(path, i, path[i][j]) + output(path, path[i][j] + 1, j) + ')'


def multiply(n, arr):
    max = 10 ** 9 + 1
    dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
    res = [[0 for i in range(n + 1)] for j in range(n + 1)]
    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            dp[i][j] = max
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    res[i][j] = k
    return output(res, 1, n)


if __name__ == '__main__':
    start()
    with open('input.txt', 'r') as f:
        n = int(f.readline())
        arr = [0 for _ in range(n + 1)]
        for index, matrix in enumerate(f.readlines()):
            arr[index], arr[n] = tuple(map(int, matrix.strip().split()))

    with open('output.txt', 'w+') as g:
        g.write(str(multiply(n, arr)))

    print('Time:', str(process_time()), 'sec')
    print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')