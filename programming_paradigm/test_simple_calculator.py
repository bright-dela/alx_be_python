import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    def test_add_two_numbers(self):
        add_numbers = SimpleCalculator()
        result = add_numbers.add(10, 5)
        self.assertEqual(result, 15)

    def test_subtract_two_numbers(self):
        subtract_numbers = SimpleCalculator()
        result = subtract_numbers.subtract(10, 5)
        self.assertEqual(result, 5)

    def test_multiply_two_numbers(self):
        multiply_numbers = SimpleCalculator()
        result = multiply_numbers.multiply(10, 5)
        self.assertEqual(result, 50)

    def test_divide_two_numbers_with_non_zero_denominator(self):
        multiply_numbers = SimpleCalculator()
        result = multiply_numbers.divide(10, 5)
        self.assertEqual(result, 2)

    def test_divide_two_numbers_with_zero_as_denominator(self):
        multiply_numbers = SimpleCalculator()
        result = multiply_numbers.divide(10, 0)
        self.assertEqual(result, None)
