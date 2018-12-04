"""Test url parser."""
import unittest

from unittest.mock import patch

from link_scraper import get_html_from_file
from link_scraper import parse_html

GOOD_LINKS_RESULT = [
    'http://www.google.com',
    'http://www.python.org',
    'https://indypopcon.com/',
    'http://www.facebook.com']
BAD_LINKS_RESULT = [
    'http://www.thereisnothingtoseeheremovealong.edu/',
    'https://www.linkedin.com/in/david-lund-mba-9b640419/']


def mocked_requests(*args):
    """Mock requests library for dependable results."""
    class MockResponse(object):
        """Mock class."""
        def __init__(self):
            if args[0] in GOOD_LINKS_RESULT:
                self.status_code = 200
            else:
                self.status_code = 403


class TestParser(unittest.TestCase):
    """Create basic test class."""

    def setUp(self):
        """Initialize variables."""
        self.html_text = open('HTMLFiles/base.html')

    def test_get_html_from_file(self):
        """Test HTML reader."""
        read_html_text = get_html_from_file('HTMLFiles/base.html')
        self.assertEqual(
            read_html_text.readlines(),
            self.html_text.readlines())

    @patch('requests.get', side_effect="mocked_requests")
    def test_parser(self, mock):
        """Test parser against the stored HTML text."""
        good_links, bad_links = parse_html(self.html_text)
        self.assertEqual(good_links, GOOD_LINKS_RESULT)
        self.assertEqual(bad_links, BAD_LINKS_RESULT)


if __name__ == '__main__':
    unittest.main()
