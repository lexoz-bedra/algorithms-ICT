from time import process_time
from tracemalloc import start, get_traced_memory


class PhoneBook:
    def __init__(self):
        self.arr = [[] for _ in range(0, 101)]
        self.output_file = open('output.txt', 'w')

    def add(self, number, name):
        idx = self.hash(number)
        if type(self.arr[idx]) != int:
            for element in self.arr[idx]:
                if element[0] == number:
                    element[1] = name
                    return
            self.arr[idx].append([number, name])
        else:
            self.arr[idx] = [number, name]

    def remove(self, number):
        idx = self.hash(int(number))
        self.arr[idx] = []

    def find(self, number):
        idx = self.hash(int(number))
        for i in self.arr[idx]:
            if i[0] == number:
                self.output_file.write(i[1] + '\n')
                return
        self.output_file.write('not found\n')

    @staticmethod
    def hash(value):
        return value % 101

    def __repr__(self):
        return repr(self.arr)


if __name__ == '__main__':
    start()
    p = PhoneBook()

    with open('input.txt', 'r') as f:
        lines = f.readlines()
    for i in range(1, len(lines)):
        temp = lines[i].split()
        command = temp[0]
        number = int(temp[1])
        match command:
            case 'add':
                p.add(number, temp[2])
            case 'del':
                p.remove(number)
            case 'find':
                p.find(number)
        print(p.arr)

    print('Time:', str(process_time()), 'sec')
    print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')


