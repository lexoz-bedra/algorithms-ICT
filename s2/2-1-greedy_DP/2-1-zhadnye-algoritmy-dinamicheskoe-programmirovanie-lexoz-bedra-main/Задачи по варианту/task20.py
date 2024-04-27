from time import process_time
from tracemalloc import start, get_traced_memory


def palindrome(string, n, k):
    prev = [0] * n
    curr = [0] * n
    res = 0
    for right in range(n):
        res += 1
        for left in range(right - 1, -1, -1):
            curr[left] = prev[left + 1]
            if string[left] != string[right]:
                curr[left] += 1
            if curr[left] <= k:
                res += 1
        prev, curr = curr, prev
    return res


if __name__ == '__main__':
    start()
    with open('input.txt') as f:
        n, k = [int(elem) for elem in f.readline().split()]
        string = f.readline()

    res = palindrome(string, n, k)
    with open('output.txt', 'w') as f:
        f.write(str(res))

    print('Time:', str(process_time()), 'sec')
    print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')

