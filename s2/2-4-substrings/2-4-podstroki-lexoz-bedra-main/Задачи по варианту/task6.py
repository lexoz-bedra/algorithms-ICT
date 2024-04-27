from time import process_time
from tracemalloc import start, get_traced_memory


def z_func(string):
    N = len(string)
    z = [0] * N
    left, right = 0, 0

    for i in range(1, N):
        j = min(z[i - left], right - i + 1) if i <= right else 0
        while i + j < N and string[j] == string[i + j]:
            j += 1
        z[i] = j
        if i + j - 1 > right:
            left, right = i, i + j - 1
    return z


if __name__ == '__main__':
    start()
    with open('../input.txt') as f:
        string = f.readline()
    result = ' '.join([str(i) for i in z_func(string)])
    with open('../output.txt', 'w') as g:
        g.write(f"{result[1:]}")

    print('Time:', str(process_time()), 'sec')
    print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')