from time import process_time
from tracemalloc import start, get_traced_memory


def max_prize(n: int) -> list:
    if n == 1:
        return [1]
    if n == 2:
        return [2]
    prizes = [0]
    while n > max(prizes):
        maxx = max(prizes)
        if n - (maxx + 1) not in prizes:
            prizes.append(maxx + 1)
            n -= (maxx + 1)
        else:
            prizes.append(n)
    prizes.remove(0)
    return sorted(prizes)


if __name__ == '__main__':
    start()
    with open('input.txt', 'r') as f:
        n = int(f.readline())
    res = max_prize(n)
    with open('output.txt', 'w+') as g:
        g.write(str(len(res)) + '\n' + ' '.join([str(i) for i in res]))

    print('Time:', str(process_time()), 'sec')
    print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')
