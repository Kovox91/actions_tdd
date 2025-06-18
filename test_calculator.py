# test_calculator.py

import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    """Test cases for the Calculator class."""

    def setUp(self):
        """Set up a new Calculator instance before each test."""
        self.calc = Calculator()

    def test_add(self):
        """Test the add method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -5), -10)

    def test_subtract(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(5, 10), -5)

    def test_multiply(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(3, 7), 21)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(5, 0), 0)

    def test_divide(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertAlmostEqual(self.calc.divide(5, 2), 2.5)

    def test_divide_by_zero(self):
        """Test that dividing by zero raises a ValueError."""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    def test_square_root(self):
        """Test the square root method."""
        self.assertEqual(self.calc.square_root(4), 2)
        self.assertEqual(self.calc.square_root(0), 0)
        self.assertAlmostEqual(self.calc.square_root(2), 1.4142135623730951)
        with self.assertRaises(ValueError):
            self.calc.square_root(-1)

    def test_power(self):
        """Test the power method."""
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 0), 1)
        self.assertEqual(self.calc.power(3, -2), 1/9)
        self.assertEqual(self.calc.power(4, 0.5), 2)
    def test_power_negative_base(self):
        """Test the power method with a negative base."""
        self.assertEqual(self.calc.power(-2, 3), -8)
        self.assertEqual(self.calc.power(-2, 2), 4)
        self.assertEqual(self.calc.power(-3, 3), -27)
        self.assertEqual(self.calc.power(-3, 2), 9)
        self.assertEqual(self.calc.power(-2, -2), 0.25)
        self.assertEqual(self.calc.power(-2, 0), 1)

if __name__ == '__main__':
    unittest.main()