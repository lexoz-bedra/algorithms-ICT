from time import process_time
from tracemalloc import start, get_traced_memory


def read_inf_from_file(filename):
    input_file = open(filename, "r")
    data = []

    for line in input_file.readlines():
        line = line.strip()
        line_data = line.split()
        line_data[0] = int(line_data[0])

        data.append(line_data)

    return data


def find_mistakes(data):
    results = []

    for query in data:
        mistake_range = query[0]
        string = query[1]
        substring = query[2]

        result = []

        for i in range(len(string) - len(substring) + 1):
            mistakes = 0

            for j in range(len(substring)):
                part_of_string = string[i + j]
                part_of_substring = substring[j]

                if part_of_string != part_of_substring:
                    mistakes += 1

                if mistakes > mistake_range:
                    break

            if mistakes == mistake_range:
                result.append(i)

        if len(result) == 0:
            results.append([0])
        else:
            results.append([len(result)] + result)

    return results


if __name__ == '__main__':
    start()
    data = read_inf_from_file("../input.txt")
    with open('../output.txt', 'w+') as g:
        st = ''
        for string in find_mistakes(data):
            st += (' '.join([str(i) for i in string]) + '\n')
        g.write(st)

    print('Time:', str(process_time()), 'sec')
    print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')