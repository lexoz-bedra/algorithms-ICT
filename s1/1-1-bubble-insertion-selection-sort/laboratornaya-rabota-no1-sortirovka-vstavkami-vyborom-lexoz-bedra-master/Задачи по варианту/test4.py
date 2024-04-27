import unittest
from task4 import linear_search
def search(l, v):
    idxs = []
    while v in l:
        idxs.append(l.index(v))
        l[l.index(v)] = v + 1
    return idxs
class MyTestCase(unittest.TestCase):
    def test(self):
        a1 = [i for i in range(11)]
        v1 = 1000
        a2 = [i for i in range(101)]
        v2 = 13
        a3 = [i for i in range(901)]
        a3.extend([100] * 100)
        v3 = 100
        self.assertEqual(linear_search(a1, v1), search(a1, v1))
        self.assertEqual(linear_search(a2, v2), search(a2, v2))
        self.assertEqual(linear_search(a3, v3), search(a3, v3))
if __name__ == '__main__':
    unittest.main()
