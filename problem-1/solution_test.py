import unittest
from solution import find_pair


class TestFinaPair(unittest.TestCase):
    def test_positive_case(self):
        self.assertEqual(find_pair([10, 15, 3, 7], 17), True)
        self.assertEqual(find_pair([10, 7, 6, 8, 2, 5, 9], 10), True)

    def test_negative_case(self):
        self.assertEqual(find_pair([10, 15, 3, 7], 20), False)
        self.assertEqual(find_pair([10, 7, 6, 8, 2, 5, 9], 21), False)

if __name__ == '__main__':
    unittest.main()