from time import process_time
from tracemalloc import start, get_traced_memory


def square(x, y):
    for i in range(len(x)):
        x[i] += y[i]
    for i in range(1, len(x)):
        if x[i] == 0 and x[i - 1] == 0:
            return False
        if x[i] == 2 and x[i - 1] == 2:
            return False
    return True


def field(h):
    p = 2
    for i in range(1, h):
        p *= 2
    f = []
    for i in range(0, p):
        temp = bin(i)[2:]
        temp = temp[::-1]
        while len(temp) < h:
            temp += "0"
        arr = []
        for i in range(0, h):
            arr.append(int(temp[i]))
        f.append(arr)
    res = []
    for i in f:
        res.append([])
        for j in f:
            if square(i, j):
                res[-1].append(1)
            else:
                res[-1].append(0)
    return res


def solve(m, n):
    h = min(n, m)
    w = max(n, m)
    f = field(h)
    res = [1] * len(f)
    temp = [0] * len(f)
    for i in range(0, w - 1):
        for j in range(0, len(f)):
            for k in range(len(f[j])):
                if f[j][k] == 1:
                    temp[j] += res[k]
        for j in range(0, len(f)):
            res[j] = temp[j]
        temp = [0] * len(f)
    return sum(res)


if __name__ == '__main__':
    start()
    with open('input.txt', 'r') as f:
        m, n = map(int, f.readline().split())

    res = solve(m, n)

    with open('output.txt', 'w+') as g:
        g.write(str(res))

    print('Time:', str(process_time()), 'sec')
    print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')
