# Test class
import unittest
from app import add, sub, mul


class TestMathFunction(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(4, 3), 7)
        self.assertEqual(add(-4, -3), -7)

    def test_sub(self):
        self.assertEqual(sub(4, 3), 1)
        self.assertEqual(sub(-4, -3), -1)

    def test_mul(self):
        self.assertEqual(mul(4, 3), 12)
        self.assertEqual(mul(-4, -3), -12)
