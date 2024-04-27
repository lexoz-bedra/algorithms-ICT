from time import process_time
from tracemalloc import start, get_traced_memory


def find_way(arr: list) -> str:
    n = int(arr.pop(0))
    arr = [list(map(int, line.split())) for line in arr]

    visited = [False] * n
    lengths = [10**6 + 1] * n
    res = [None] * n
    curr = 0
    lengths[curr] = 0

    for i in range(0, n):
        min_path_length = 10**6 + 1
        for j in range(0, n):
            if not visited[j] and lengths[j] < min_path_length:
                min_path_length = lengths[j]
                curr = j
        visited[curr] = True
        res[curr] = i + 1

        for j in range(0, n):
            if not visited[j] and arr[curr][j] < lengths[j]:
                lengths[j] = arr[curr][j]

    s = str(sum(lengths))
    s += "\n"
    for i in range(len(res) - 1, -1, -1):
        s += str(res[i])
        s += " "
    return s


if __name__ == '__main__':
    start()
    with open('input.txt', 'r') as f:
        arr = f.readlines()

    res = find_way(arr)

    with open('output.txt', 'w+') as g:
        g.write(res)

    print('Time:', str(process_time()), 'sec')
    print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')
