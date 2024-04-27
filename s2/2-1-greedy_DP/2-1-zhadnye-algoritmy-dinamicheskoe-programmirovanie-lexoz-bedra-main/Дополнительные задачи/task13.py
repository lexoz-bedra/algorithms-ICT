from time import process_time
from tracemalloc import start, get_traced_memory


def can_divide(nums: list[int], i: int, subset_sum: int, subset_count: int, taken: list[bool]) -> bool:
    if subset_count == 0:
        return True
    if subset_sum == 0:
        return can_divide(nums, 0, sum(nums) // 3, subset_count - 1, taken)
    for j in range(i, len(nums)):
        if not taken[j] and subset_sum - nums[j] >= 0:
            taken[j] = True
            if can_divide(nums, j + 1, subset_sum - nums[j], subset_count, taken):
                return True
            taken[j] = False
    return False


def can_divide_equally(nums: list[int]) -> bool:
    if len(nums) < 3:
        return False
    total_sum = sum(nums)
    if total_sum % 3 != 0:
        return False
    subset_sum = total_sum // 3
    subset_count = 3
    taken = [False for _ in range(len(nums))]
    return can_divide(nums, 0, subset_sum, subset_count, taken)


if __name__ == '__main__':
    start()
    with open('input.txt', 'r') as f:
        n = int(f.readline())
        nums = list(map(int, f.readline().split()))

    with open('output.txt', 'w') as f:
        f.write(str(int(can_divide_equally(nums))))

    print('Time:', str(process_time()), 'sec')
    print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')
