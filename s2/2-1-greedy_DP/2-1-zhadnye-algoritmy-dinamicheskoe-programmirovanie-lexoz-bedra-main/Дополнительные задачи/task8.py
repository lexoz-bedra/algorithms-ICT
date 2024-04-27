from time import process_time
from tracemalloc import start, get_traced_memory


# берём лекцию, у которой конец ближе всего к концу прошлой (или к началу суток)
# а также проверяем на непересекаемость с другими (т. е. начало не раньше конца прошлой)
def max_lecs(lectures: list[tuple[int, int]], last: int, lecs_used: list[int]) -> int:
    # возвращаем значение, если список лекций пуст
    if len(lectures) == 0:
        used = len(lecs_used)
        return used
    # считаем, насколько конец каждой лекции позже предыдущей
    lecs_diff = [lec[1] - last for lec in lectures]
    # если начало какой-то лекции раньше прошлой, она не проведётся
    for i, lec in enumerate(lectures):
        if lec[0] < last:
            lecs_diff[i] = 1441
    # если ни одну лекцию нельзя провести, возвращаем значение
    if lecs_diff.count(1441) == len(lecs_diff):
        return len(lecs_used)
    # берём лекцию с концом, максимально близким к предыдущей
    lecs_used.append(min(lecs_diff) + last)
    # обновляем время последней лекции
    last += min(lecs_diff)
    # удаляем использованную лекцию
    lectures.pop(lecs_diff.index(min(lecs_diff)))
    return max_lecs(lectures, last, lecs_used)


if __name__ == '__main__':
    start()
    with open('input.txt', 'r') as f:
        n = int(f.readline())
        lectures = []
        for i in range(n):
            t1, t2 = map(int, f.readline().split())
            lectures.append((t1, t2))
    res = max_lecs(lectures, 0, [])
    with open('output.txt', 'w+') as g:
        g.write(str(res))

    print('Time:', str(process_time()), 'sec')
    print('Memory usage:', str(get_traced_memory()[1] / 1024), 'KB')
