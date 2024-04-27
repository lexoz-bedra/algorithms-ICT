from time import process_time
from tracemalloc import start, get_traced_memory


class HashSet:
    def __init__(self):
        self.set = {}
        self.length = len(self.set)

    def add(self, element):
        self.set[element] = self.length

    def delete(self, element):
        try:
            self.set.pop(element)
        except KeyError:
            pass

    def check(self, element):
        if self.set.get(element) is None:
            return 'N'
        return 'Y'

    def __repr__(self):
        return repr(self.set)


def file_output(array):
    with open('output.txt', 'w+') as f:
        f.write('\n'.join([str(i) for i in array]))


if __name__ == '__main__':
    start()
    hashset = HashSet()
    stack = []

    with open('input.txt') as f:
        n = int(f.readline())
        for _ in range(n):
            command, number = f.readline().split()
            match command:
                case 'A':
                    hashset.add(number)
                case 'D':
                    hashset.delete(number)
                case '?':
                    stack.append(hashset.check(number))
                    print(hashset.check(number))

    file_output(stack)
    print('Time:', str(process_time()), 'sec')
    print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')

