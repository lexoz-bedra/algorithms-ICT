from time import process_time
from tracemalloc import start, get_traced_memory


def binary_search():
    l, r = 0, h[0]
    while r - l > 0.0000000001:
        h[1] = (l + r) / 2
        Up = True
        for i in range(2, n):
            h[i] = 2 * h[i - 1] - h[i - 2] + 2
            if h[i] < 0:
                Up = False
                break
        if Up:
            r = h[1]
        else:
            l = h[1]
    return h[n - 1]


start()

with open("input.txt") as f:
    n, h = f.readline().split()
    n = int(n)
    h = [float(h)] + [0] * (n - 1)

float_number = binary_search()
float_number = "{:.9f}".format(float_number)
total = [i for i in str(float_number) if i != "0"]
total_string = ""

for i in total:
    total_string += str(i)
with open("output.txt", "w+") as g:
    g.write(total_string)


print('Time:', str(process_time()), 'sec')
print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')