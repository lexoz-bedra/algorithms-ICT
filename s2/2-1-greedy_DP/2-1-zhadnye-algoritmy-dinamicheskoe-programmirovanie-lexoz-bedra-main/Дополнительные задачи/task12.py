from time import process_time
from tracemalloc import start, get_traced_memory


def two_subsequences(n: int, arr: list[int]) -> list[int]:
    total_sum = sum(arr)
    if total_sum % 2 != 0:
        return [-1]
    half_sum = total_sum // 2
    dp = [[False] * (half_sum + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True
    for i in range(1, n + 1):
        for j in range(1, half_sum + 1):
            if j >= arr[i - 1]:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]
    if not dp[n][half_sum]:
        return [-1]
    i, j = n, half_sum
    result = []
    while i > 0 and j > 0:
        if not dp[i-1][j]:
            result.append(arr[i-1])
            j -= arr[i-1]
        i -= 1
    return result


if __name__ == '__main__':
    start()
    with open('input.txt', 'r') as f:
        n = int(f.readline())
        arr = list(map(int, f.readline().split()))
    res = two_subsequences(n, arr)
    with open('output.txt', 'w+') as g:
        if res == [-1]:
            g.write("-1\n")
        else:
            g.write(str(len(res)) + "\n" + " ".join([str(x) for x in res]))

    print('Time:', str(process_time()), 'sec')
    print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')
