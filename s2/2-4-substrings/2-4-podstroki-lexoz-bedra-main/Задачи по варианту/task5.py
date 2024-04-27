from time import process_time
from tracemalloc import start, get_traced_memory


def prefix_func(string):
    pi = [0] * len(string)

    for i in range(1, len(string)):
        j = pi[i - 1]
        while j > 0 and string[i] != string[j]:
            j = pi[j - 1]
        if string[i] == string[j]:
            j += 1
        pi[i] = j
    return pi


if __name__ == '__main__':
    start()
    with open('../input.txt', 'r') as f:
        string = f.readline()
    res = prefix_func(string)
    with open('../output.txt', 'w+') as g:
        g.write(' '.join([str(i) for i in res]))

    print('Time:', str(process_time()), 'sec')
    print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')
