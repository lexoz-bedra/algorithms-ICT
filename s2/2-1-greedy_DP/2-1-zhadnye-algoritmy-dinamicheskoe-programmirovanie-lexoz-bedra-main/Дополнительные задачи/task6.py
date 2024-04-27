from time import process_time
from tracemalloc import start, get_traced_memory


# функция для сортировки строк по убыванию
def sort_str(a: list[str]) -> list[str]:
    for i in range(len(a)):
        for j in range(len(a)):
            if (a[i] + a[j]) < (a[j] + a[i]) and i < j:
                a[i], a[j] = a[j], a[i]
    return a


def max_number(nums: list[int]) -> str:
    nums = [str(i) for i in nums]
    res = ''.join(sort_str(nums))
    return res


if __name__ == '__main__':
    start()
    with open('input.txt', 'r') as f:
        n = int(f.readline())
        numbers = [int(i) for i in f.readline().split()]
    res = max_number(numbers)
    with open('output.txt', 'w+') as g:
        g.write(res)

    print('Time:', str(process_time()), 'sec')
    print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')
