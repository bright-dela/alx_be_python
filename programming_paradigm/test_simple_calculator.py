import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(8, 5), 13)
        self.assertEqual(self.calc.add(-8, 5), -3)
        self.assertEqual(self.calc.add(8, -5), 3)
        self.assertEqual(self.calc.add(-8, -5), -13)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(8, 5), 3)
        self.assertEqual(self.calc.subtract(-5, 8), -13)
        self.assertEqual(self.calc.subtract(8, -5), 13)
        self.assertEqual(self.calc.subtract(0, -5), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-8, -5), -3)
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(8, 5), 40)
        self.assertEqual(self.calc.multiply(-5, 8), -40)
        self.assertEqual(self.calc.multiply(8, -5), -40)
        self.assertEqual(self.calc.multiply(0, -5), 0)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(-8, -5), 40)
        self.assertEqual(self.calc.multiply(0, 0), 0)

    def test_division(self):
        self.assertEqual(self.calc.divide(8, 5), 1.6)
        self.assertEqual(self.calc.divide(-5, 8), -0.625)
        self.assertEqual(self.calc.divide(8, -5), -1.6)
        self.assertEqual(self.calc.divide(0, -5), 0)
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertEqual(self.calc.divide(-8, -5), 1.6)
        self.assertEqual(self.calc.divide(0, 0), None)
        self.assertEqual(self.calc.divide(5, 0), None)
        self.assertEqual(self.calc.divide(-5, 0), None)

    