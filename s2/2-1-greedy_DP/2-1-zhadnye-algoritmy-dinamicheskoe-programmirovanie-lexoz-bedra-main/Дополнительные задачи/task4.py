from time import process_time
from tracemalloc import start, get_traced_memory


def dots_segments(n: int, segments: list) -> list:
    res = 0
    dots_used = []
    dots_sorted = []
    stack = []
    covered = [False] * n
    for i in segments:
        dots_sorted.append((i[0], -1, segments.index(i))) # левый конец помечен -1
        dots_sorted.append((i[1], 1, segments.index(i))) # правый конец помечен 1
    dots_sorted.sort()
    for i, dot in enumerate(dots_sorted):
        if dot[1] == -1:
            stack.append(dot[2])
        elif dot[1] == 1:
            if not covered[dot[2]]:
                res += 1
                dots_used.append(dot[0])
                for j in stack:
                    covered[j] = True
            stack.pop(-1)
    return dots_used


if __name__ == '__main__':
    start()
    with open('input.txt', 'r') as f:
        n = int(f.readline())
        segments = []
        for i in range(n):
            a, b = map(int, f.readline().split())
            segments.append((a, b))
    res = dots_segments(n, segments)
    with open('output.txt', 'w+') as g:
        g.write(str(len(res)) + '\n' + ' '.join([str(i) for i in res]))

    print('Time:', str(process_time()), 'sec')
    print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')
