from time import process_time
from tracemalloc import start, get_traced_memory


def min_price(n: int, prices: list[int]) -> int:
    min_cost = 10 ** 10
    result = 0
    for i in range(6, -1, -1):
        n_new = n
        if n != 0:
            k = int(n / 10 ** i)
            if k > 0:
                result += k * prices[i]
                n -= k * 10 ** i
            if k == 0:
                n_new -= 10**i
                if n_new <= 0:
                    min_cost = min(min_cost, prices[i])
        else:
            break
    return min(result, min_cost)
    
    
if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        N = int(f.readline())
        prices = [int(f.readline()) for _ in range(7)]
        res = min_price(N, prices)
        with open('output.txt', 'w') as g:
            g.write(str(res))

        print('Time:', str(process_time()), 'sec')
        print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')
        
