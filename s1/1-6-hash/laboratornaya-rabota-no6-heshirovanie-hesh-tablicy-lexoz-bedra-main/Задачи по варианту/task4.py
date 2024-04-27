from time import process_time
from tracemalloc import start, get_traced_memory


class Array:
    def __init__(self):
        self.array = {}

    def get(self, x):
        if self.array.get(x) is None:
            return '<none>'
        else:
            return self.array.get(x)

    def prev(self, x):
        lst = list(self.array)
        if x in lst:
            index = lst.index(x) - 1
            if lst.index(x) != 0:
                next_key = lst[index]
                return self.get(next_key)
            else:
                return '<none>'
        else:
            return '<none>'

    def next(self, x):
        lst = list(self.array)
        if x in lst:
            index = lst.index(x) + 1
            if index != len(lst):
                next_key = lst[index]
                return self.get(next_key)
            else:
                return '<none>'
        else:
            return '<none>'

    def put(self, x, y):
        self.array[x] = y

    def delete(self, element):
        try:
            self.array.pop(element)
        except KeyError:
            pass

    def __repr__(self):
        return repr(self.array)


def file_output(array):
    with open('output.txt', 'w+') as f:
        f.write('\n'.join([str(i) for i in array]))


if __name__ == '__main__':
    start()
    arr = Array()
    output = []

    with open('input.txt') as f:
        n = int(f.readline())

        for _ in range(n):
            string = list(f.readline().strip('\n').split())
            try:
                command, x, y = string
            except ValueError:
                command, x = string
            match command:
                case 'get':
                    output.append(arr.get(x))
                case 'prev':
                    output.append(arr.prev(x))
                case 'next':
                    output.append(arr.next(x))
                case 'put':
                    arr.put(x, y)
                case 'delete':
                    arr.delete(x)

    file_output(output)
    print('Time:', str(process_time()), 'sec')
    print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')
