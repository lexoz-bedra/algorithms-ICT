from time import process_time
from tracemalloc import start, get_traced_memory


def generate_array(num):
    arr = [i + 1 for i in range(num)]
    for i in range(2, num):
        arr[i], arr[i // 2] = arr[i // 2], arr[i]
    return arr


if __name__ == '__main__':
    start()
    with open('input.txt', 'r') as f:
        n = int(f.readline())
    with open('output.txt', 'w+') as g:
        g.write(' '.join([str(i) for i in generate_array(n)]))
    print('Time:', str(process_time()), 'sec')
    print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')
