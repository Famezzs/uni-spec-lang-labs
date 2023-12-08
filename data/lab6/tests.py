import unittest
from module.Calculator import Calculator

class CalculatorTests(unittest.TestCase):
    calculator = Calculator()

    def test_positive_addition_result(self):
        augend = 5
        addend = 10.5

        expected = augend + addend
        actual = self.calculator.add(augend, addend)

        self.assertEqual(expected, actual)
        self.assertGreaterEqual(actual, 0)

    def test_negative_addition_result(self):
        augend = 5
        addend = -10.5

        expected = augend + addend
        actual = self.calculator.add(augend, addend)

        self.assertEqual(expected, actual)
        self.assertLess(actual, 0)

    def test_positive_subtraction_result(self):
        minuend = 5
        subtrahend = -10.5

        expected = minuend - subtrahend
        actual = self.calculator.subtract(minuend, subtrahend)

        self.assertEqual(expected, actual)
        self.assertGreaterEqual(actual, 0)

    def test_negative_subtraction_result(self):
        minuend = -5
        subtrahend = 10.5

        expected = minuend - subtrahend
        actual = self.calculator.subtract(minuend, subtrahend)

        self.assertEqual(expected, actual)
        self.assertLess(actual, 0)

    def test_both_negative_values_subtraction_result(self):
        minuend = -5
        subtrahend = -10.5

        expected = minuend - subtrahend
        actual = self.calculator.subtract(minuend, subtrahend)

        self.assertEqual(expected, actual)

    def test_positive_multiplication_result(self):
        multiplier = 5
        multiplicand = 10.5

        expected = multiplier * multiplicand
        actual = self.calculator.multiply(multiplier, multiplicand)

        self.assertEqual(expected, actual)
        self.assertGreaterEqual(actual, 0)

    def test_negative_multiplication_result(self):
        multiplier = 5
        multiplicand = -10.5

        expected = multiplier * multiplicand
        actual = self.calculator.multiply(multiplier, multiplicand)

        self.assertEqual(expected, actual)
        self.assertLess(actual, 0)

    def test_zero_multiplication_result(self):
        multiplier = 0
        multiplicand = 10.5

        expected = 0
        actual = self.calculator.multiply(multiplier, multiplicand)

        self.assertEqual(expected, actual)
    
    def test_positive_division_result(self):
        numerator = 5
        denominator = 10.5

        expected = numerator / denominator
        actual = self.calculator.divide(numerator, denominator)

        self.assertEqual(expected, actual)
        self.assertGreaterEqual(actual, 0)

    def test_negative_division_result(self):
        numerator = 5
        denominator = -10.5

        expected = numerator / denominator
        actual = self.calculator.divide(numerator, denominator)

        self.assertEqual(expected, actual)
        self.assertLess(actual, 0)

    def test_numerator_is_zero_division_result(self):
        numerator = 0
        denominator = 10.5

        expected = 0
        actual = self.calculator.divide(numerator, denominator)

        self.assertEqual(expected, actual)

    def test_denominator_is_zero_division_result(self):
        numerator = 5
        denominator = 0

        with self.assertRaises(Exception):
            self.calculator.divide(numerator, denominator)

if __name__ == '__main__':
    unittest.main()