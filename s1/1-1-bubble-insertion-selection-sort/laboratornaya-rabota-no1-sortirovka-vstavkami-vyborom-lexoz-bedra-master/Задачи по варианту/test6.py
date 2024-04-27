import unittest
from task6 import bubble_sort
class MyTestCase(unittest.TestCase):
    def test_min(self):
        a1 = [i for i in range(11)]
        a1[-1], a1[-2] = a1[-2], a1[-1]
        a2 = [i for i in range(101)]
        a2[-1], a2[-2] = a2[-2], a2[-1]
        a3 = [i for i in range(1001)]
        a3[-1], a3[-2] = a3[-2], a3[-1]
        self.assertEqual(bubble_sort(a1), sorted(a1))
        self.assertEqual(bubble_sort(a2), sorted(a2))
        self.assertEqual(bubble_sort(a3), sorted(a3))
    def test_average(self):
        a1 = [i for i in range(6)]
        a1.extend([i for i in range(10, 5, -1)])
        a2 = [i for i in range(6)]
        a2.extend([i for i in range(10, 5, -1)])
        a3 = [i for i in range(6)]
        a3.extend([i for i in range(10, 5, -1)])
        self.assertEqual(bubble_sort(a1), sorted(a1))
        self.assertEqual(bubble_sort(a2), sorted(a2))
        self.assertEqual(bubble_sort(a3), sorted(a3))
    def test_max(self):
        a1 = [i for i in range(10, 0, -1)]
        a2 = [i for i in range(100, 0, -1)]
        a3 = [i for i in range(1000, 0, -1)]
        self.assertEqual(bubble_sort(a1), sorted(a1))
        self.assertEqual(bubble_sort(a2), sorted(a2))
        self.assertEqual(bubble_sort(a3), sorted(a3))
if __name__ == '__main__':
    unittest.main()
