from time import process_time
from tracemalloc import start, get_traced_memory


def max_result(nums: list[int], ops: list[str]) -> int:
    n = len(nums)
    dp_max = [[-10**6] * n for _ in range(n)]
    dp_min = [[10**6] * n for _ in range(n)]
    for i in range(n):
        dp_max[i][i] = dp_min[i][i] = nums[i]
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(i, j):
                if ops[k] == '+':
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] + dp_max[k+1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] + dp_min[k+1][j])
                elif ops[k] == '-':
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] - dp_min[k+1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] - dp_max[k+1][j])
                else:
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] * dp_max[k+1][j], dp_min[i][k] * dp_max[k+1][j], dp_max[i][k] * dp_min[k+1][j], dp_min[i][k] * dp_min[k+1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] * dp_min[k+1][j], dp_min[i][k] * dp_max[k+1][j], dp_max[i][k] * dp_min[k+1][j], dp_max[i][k] * dp_max[k+1][j])
    return dp_max[0][n-1]


if __name__ == '__main__':
    start()
    with open('input.txt', 'r') as f:
        s = f.readline()

    nums = []
    ops = []
    for i in range(len(s)):
        if i % 2 == 0:
            nums.append(int(s[i]))
        else:
            ops.append(s[i])

    res = max_result(nums, ops)
    with open('output.txt', 'w+') as g:
        g.write(str(res) + "\n")

    print('Time:', str(process_time()), 'sec')
    print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')
