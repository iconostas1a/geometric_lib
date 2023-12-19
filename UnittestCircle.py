from circle import *
import unittest


class CircleTestCase(unittest.TestCase):
    def test_zero_mul_area(self):
        self.assertEqual(area(0), 0)

    def test_negative_number(self):
        self.assertEqual(area(-1), "Incorrect input")
        self.assertEqual(area(4), 50.26548245743669)
        self.assertEqual(perimeter(-1), "Incorrect input")

    def test_zero_sum(self):
        self.assertEqual(perimeter(0), 0)
