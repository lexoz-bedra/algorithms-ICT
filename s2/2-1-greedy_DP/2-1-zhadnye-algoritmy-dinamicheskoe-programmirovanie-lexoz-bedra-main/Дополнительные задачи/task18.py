from time import process_time
from tracemalloc import start, get_traced_memory


def find_ks(n, trans, prevs, free_days):
    ans = 10**9 + 1
    k1 = 0
    for i in range(n + 1):
        if trans[n][i] != -1 and trans[n][i] <= ans:
            ans = trans[n][i]
            k1 = i
    j = k1
    k2 = 0
    for i in range(n, 0, -1):
        if j + 1 == prevs[i][j]:
            k2 += 1
            free_days[k2] = i
        j = prevs[i][j]
    res = []
    res += str(ans) + "\n"
    res += str(k1) + " " + str(k2) + "\n"
    for i in range(k2, 0, -1):
        res += str(free_days[i]) + "\n"
    return res


def lunch_cost(n, arr):
    trans = [[-1] * (n + 1) for i in range(n + 1)]
    trans[0][0] = 0
    prevs = [[-1] * (n + 1) for i in range(n + 1)]
    free_days = [0] * (n + 1)
    for i in range(n):
        for j in range(i + 1):
            if trans[i][j] != -1:
                if j > 0:
                    if trans[i + 1][j - 1] > trans[i][j] or trans[i + 1][j - 1] == -1:
                        trans[i + 1][j - 1] = trans[i][j]
                        prevs[i + 1][j - 1] = j
                k = 0
                if arr[i + 1] > 100:
                    k = 1
                if trans[i + 1][j + k] > trans[i][j] + arr[i + 1] or trans[i + 1][j + k] == -1:
                    trans[i + 1][j + k] = trans[i][j] + arr[i + 1]
                    prevs[i + 1][j + k] = j
    return find_ks(n, trans, prevs, free_days)


if __name__ == '__main__':
    start()
    with open('input.txt', 'r') as f:
        n = int(f.readline())
        arr = [0]
        temp = f.readlines()
        for i in range(n):
            arr.append(int(temp[i]))

    res = lunch_cost(n, arr)

    with open('output.txt', 'w+') as g:
        g.write(''.join(map(str, res)))

    print('Time:', str(process_time()), 'sec')
    print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')

