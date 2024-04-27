from time import process_time
from tracemalloc import start, get_traced_memory


def modify_brackets(seq):
    n = len(seq)
    vals = [[0] * n for i in range(n)]
    pos = [[0] * n for i in range(n)]
    for right in range(n):
        for left in range(right, -1, -1):
            if right == left:
                vals[left][right] = 1
            else:
                min_value = 10 ** 9
                min_pos = -1
                if (seq[left] == '(' and seq[right] == ')') or (seq[left] == '[' and seq[right] == ']') or (
                        seq[left] == '{' and seq[right] == '}'):
                    min_value = vals[left + 1][right - 1]
                for k in range(left, right):
                    if min_value > vals[left][k] + vals[k + 1][right]:
                        min_value = vals[left][k] + vals[k + 1][right]
                        min_pos = k
                vals[left][right] = min_value
                pos[left][right] = min_pos
    return vals, pos


def output(l, r, res, vals, pos):
    if vals[l][r] == r - l + 1:
        return res
    if vals[l][r] == 0:
        res += arr[l:r + 1]
        return res
    if pos[l][r] == -1:
        res += arr[l]
        res = output(l + 1, r - 1, res, vals, pos)
        res += arr[r]
        return res
    res = output(l, pos[l][r], res, vals, pos)
    res = output(pos[l][r] + 1, r, res, vals, pos)
    return res


if __name__ == '__main__':
    start()
    with open('input.txt') as f:
        arr = f.readline()
    values, position = modify_brackets(arr)
    with open('output.txt', 'w+') as g:
        g.write(output(0, len(arr) - 1, '', values, position))

    print('Time:', str(process_time()), 'sec')
    print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')
