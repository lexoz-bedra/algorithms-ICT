from time import process_time
from tracemalloc import start, get_traced_memory


def direct_search(string, substr):
    count = 0
    pos_arr = []
    for i in range(len(string)):
        if string[i : i + len(substr)] == substr:
            count += 1
            pos_arr.append(i + 1)
    
    return count, pos_arr


if __name__ == "__main__":
    start()
    with open('../input.txt') as f:
        substr, string = f.read().split("\n")

    with open('../output.txt', 'w') as g:
        nums = ' '.join([str(i) for i in direct_search(string, substr)[1]])
        g.write(f"{direct_search(string, substr)[0]}\n{nums}")

print('Time:', str(process_time()), 'sec')
print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')

