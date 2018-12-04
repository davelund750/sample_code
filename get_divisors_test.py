"""Test divisors function."""
import unittest
from get_divisors import divisors


class TestDivisors(unittest.TestCase):
    """Create basic test class."""

    def setUp(self):
        """Initialize variables."""
        self.result_sixty = [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60]
        self.result_adams = [1, 2, 3, 6, 7, 14, 21, 42]

    def test_divisors(self):
        """Test function results against known outcomes."""
        self.assertEqual(divisors(60), self.result_sixty)
        self.assertEqual(divisors(42), self.result_adams)

    def test_error(self):
        """Test that function throw AttributeError when string provided."""
        self.assertRaises(AttributeError, divisors, 'shenanigans')


if __name__ == '__main__':
    unittest.main()
