from time import process_time
from tracemalloc import start, get_traced_memory


def gas_station(d: int, m: int, n: int, stops: list) -> int:
    used_stops = 0
    distance = m
    stops.insert(0, 0)
    stops.append(d)
    for i in range(1, len(stops) - 1):
        if stops[i] - stops[i - 1] > m or stops[i + 1] - stops[i] > m:
            return -1
        distance -= (stops[i] - stops[i - 1])
        if distance < stops[i + 1] - stops[i]:
            used_stops += 1
            distance = m
    return used_stops


if __name__ == '__main__':
    start()
    with open('input.txt', 'r') as f:
        d = int(f.readline())
        m = int(f.readline())
        n = int(f.readline())
        stops = [int(i) for i in f.readline().split()]
    res = gas_station(d, m, n, stops)
    with open('output.txt', 'w+') as g:
        g.write(str(res))

    print('Time:', str(process_time()), 'sec')
    print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')