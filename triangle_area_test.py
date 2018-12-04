"""Test triangle area function."""
import unittest
from triangle_area import compute_area
from triangle_area import InvalidTriangleException


class TestArea(unittest.TestCase):
    """Create basic test class."""

    def setUp(self):
        """Initialize variables."""
        self.valid_triangle_1 = [3, 4, 5]
        self.valid_triangle_1_result = 6
        self.valid_triangle_2 = [5, 5, 6]
        self.valid_triangle_2_result = 12
        self.invalid_triangle_1 = [1, 2, 3]
        self.invalid_triangle_2 = [4, 'five', 6]
        self.invalid_triangle_3 = [4, 4, 4, 4]

    def test_divisors(self):
        """Test function results against known outcomes."""
        self.assertEqual(compute_area(
            self.valid_triangle_1), self.valid_triangle_1_result)
        self.assertEqual(compute_area(
            self.valid_triangle_2), self.valid_triangle_2_result)

    def test_error(self):
        """Test that function throw AttributeError when string provided."""
        self.assertRaises(
            InvalidTriangleException, compute_area, self.invalid_triangle_1)
        self.assertRaises(
            InvalidTriangleException, compute_area, self.invalid_triangle_2)
        self.assertRaises(
            InvalidTriangleException, compute_area, self.invalid_triangle_3)


if __name__ == '__main__':
    unittest.main()
