from time import process_time
from tracemalloc import start, get_traced_memory


def play(own, opposite, trump):
    opposite_num = len(opposite)
    deck = ['6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A', trump]
    cnt, i, j = 0, 0, 0
    own.sort(key=lambda x: (x[1] == trump, deck.index(x[0])))
    while i < len(own):
        while j < len(opposite):
            if len(opposite) == 0:
                break
            elif own[i][1] == opposite[j][1]:
                if deck.index(own[i][0]) > deck.index(opposite[j][0]):
                    cnt += 1
                    own.pop(i)
                    i = max(i - 1, 0)
                    opposite.pop(j)
                    j -= 1
            else:
                if own[i][1] == trump:
                    if opposite[j][1] != trump:
                        cnt += 1
                        own.pop(i)
                        i = max(i - 1, 0)
                        opposite.pop(j)
                        j -= 1
                    else:
                        if deck.index(own[i][0]) > deck.index(opposite[j][0]):
                            cnt += 1
                            own.pop(i)
                            i = max(i - 1, 0)
                            opposite.pop(j)
                            j -= 1
            j += 1
        i = max(i + 1, 0)
        j = 0
    return cnt, own, opposite_num


if __name__ == '__main__':
    start()
    with open('input.txt', 'r') as f:
        n1, n2, trump = tuple(f.readline().split())
        own = f.readline().split()
        opposite = f.readline().split()

    res = play(own, opposite, trump)

    with open('output.txt', 'w+') as g:
        if res[0] == res[-1]:
            g.write('YES')
        else:
            g.write('NO')

    print('Time:', str(process_time()), 'sec')
    print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')

