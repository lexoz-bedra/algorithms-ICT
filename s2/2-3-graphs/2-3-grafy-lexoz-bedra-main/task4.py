from time import process_time
from tracemalloc import start, get_traced_memory


def depth_first_search(u, visited, graph):
    visited[u] = 1
    for v in graph[u]:
        if not visited[v]:
            depth_first_search(v, visited, graph)
    stack.append(u)


def topological_sort(graph, visited):
    for v in range(len(graph)):
        if not visited[v]:
            depth_first_search(v, visited, graph)


if __name__ == '__main__':
    start()
    with open('input.txt') as f:
        n, m = f.readline().split()
        graph = {key: set() for key in [i for i in range(int(n))]}
        for _ in range(int(m)):
            u, v = map(int, f.readline().split())
            graph[u - 1].add(v - 1)

    visited = [0 for x in range(len(graph))]
    stack = []
    topological_sort(graph, visited)
    res = [str(x + 1) for x in stack]
    with open('output.txt', 'w') as g:
        g.write(' '.join(map(str, res[::-1])))

    print('Time:', str(process_time()), 'sec')
    print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')