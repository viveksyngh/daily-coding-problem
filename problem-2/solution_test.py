import unittest
from solution import product_array


class TestSolution(unittest.TestCase):
    def test_positive_case(self):
        self.assertEqual(product_array([1, 2, 3, 4, 5]), [120, 60, 40, 30, 24])
        self.assertEqual(product_array([3, 2, 1]), [2, 3, 6])

    def test_negative_case(self):
        self.assertNotEqual(product_array([1, 2, 3, 4, 5]), [120, 60, 40, 30, 34])
        self.assertNotEqual(product_array([3, 2, 1]), [6, 3, 2])

if __name__ == '__main__':
    unittest.main()