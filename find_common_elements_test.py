"""Test integer frequency function."""
import unittest
from find_common_elements import find_frequency



class TestFrequency(unittest.TestCase):
    """Create basic test class."""

    def setUp(self):
        """Initialize variables."""
        self.freq_test_1 = [5, 4, 3, 2, 4, 5, 1, 6, 1, 2, 5, 4]
        self.freq_test_1_results = [4, 5]
        self.freq_test_2 = [1, 2, 3, 4, 5, 1, 6, 7]
        self.freq_test_2_results = [1]
        self.freq_test_3 = [1, 2, 3, 4, 5, 6, 7]
        self.freq_test_3_results = [1, 2, 3, 4, 5, 6, 7]
        self.invalid_freq_test = [1, 'two', 3, 'two', 4]

    def test_frequency(self):
        """Test function results against known outcomes."""
        self.assertEqual(find_frequency(
            self.freq_test_1), self.freq_test_1_results)
        self.assertEqual(find_frequency(
            self.freq_test_2), self.freq_test_2_results)
        self.assertEqual(find_frequency(
            self.freq_test_3), self.freq_test_3_results)

    def test_error(self):
        """Test that function throw AttributeError when string provided."""
        self.assertRaises(
            ValueError, find_frequency, self.invalid_freq_test)


if __name__ == '__main__':
    unittest.main()
