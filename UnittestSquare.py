from square import *
import unittest


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul_area(self):
        self.assertEqual(area(10, 0), 0)

    def test_negative_number(self):
        self.assertEqual(area(-1, 0), "Incorrect input")

        self.assertEqual(perimeter(-5, -5), "Incorrect input")

    def test_zero_sum(self):
        self.assertEqual(perimeter(12, 0), 24)
