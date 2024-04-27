from collections import deque
from time import process_time
from tracemalloc import start, get_traced_memory


def half_graph(u):
    global sides, total_colours
    search_queue = deque()
    search_queue.append((u, 0))
    visited = []
    while search_queue:
        cur_node, colour = search_queue.popleft()
        if cur_node not in visited:
            total_colours[cur_node] = colour
            visited.append(cur_node)
            for node in sides[cur_node]:
                if colour == 0:
                    search_queue.append((node, 1))
                else:
                    search_queue.append((node, 0))
        elif total_colours[cur_node] != colour:
            return 0
    return 1


if __name__ == '__main__':
    start()
    with open('input.txt') as f:
        n, m = map(int, f.readline().split())
        sides = {}
        for i in range(n+1):
            sides[i] = []
        for i in range(m):
            v1, v2 = map(int, f.readline().split())
            sides[v1].append(v2)
            sides[v2].append(v1)

    total_colours = [None] * (n+1)
    res = half_graph(1)

    with open('output.txt', 'w') as g:
        g.write(str(res))

    print('Time:', str(process_time()), 'sec')
    print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')
