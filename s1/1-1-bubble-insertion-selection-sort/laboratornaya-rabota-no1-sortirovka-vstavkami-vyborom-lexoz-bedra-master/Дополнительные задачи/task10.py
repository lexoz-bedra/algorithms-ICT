from time import process_time
from tracemalloc import *
start()
with open('../input.txt') as f:
    n = int(f.readline())
    s = [i for i in f.readline()]
def palindrome(s1):
    s2 = ''
    s3 = ''
    minn = 'a'
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[j] < minn:
                minn = s[j]
                s[j], s[i] = s[i], s[j]
        minn = 'a'
        for i in range(len(s1)):
            if s1.count(s1[i]) % 2 != 0 and s2.count(s1[i]) < 1:
                s2 += s1[i]
    if s2 != '':
        for i in s1[::-1]:
            if s1.count(i) % 2 != 0 and s2[0] != i:
                s1.remove(i)
        s1.remove(s2[0])
    for i in range(len(s1)):
        if s3.count(s1[i]) < s1.count(s1[i]) // 2:
            s3 += s1[i]
    s4 = s3[::-1]
    if s2 != '':
        s3 += s2[0]
    s3 += s4
    return s3
print(process_time())
snapshot = take_snapshot()
for stat in snapshot.statistics('lineno'):
    print(stat)
with open('../output.txt', 'w+') as g:
    g.write(palindrome(s))
