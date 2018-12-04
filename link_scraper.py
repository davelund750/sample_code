"""
Scrape links from HTML.

Usage:
    Command line:
        python question_seven.py
    Optional Arguments:
        -h, --help              Show optional arguments.
        -f FILE, --file FILE    File with HTML to be processed. File takes
                                precedence over URL
        -u URL, --url URL       URL to parse.
        -s, --output_screen     Output results to screen.
        -c, --output_csv        Output results to CSV file.

    Importing to other modules:
        from question_seven import parse_html
        good_links, bad_links = parse_html(#varaible_containing_html#)

    Other helper functions in this file can be imported and used as well.

Prompt:
You have a large bunch of HTML.  Inside that HTML par p tags, li tags, table
tags, really any and all kinds of HTML tags.  Most importantly there are
anchor/link tags.

Write a program to find all of the URLs to which those link tags link and
verify that the URLs return a 200 response.  In a given chunk of this HTML, we
could have anywhere from 0 to 100+ links, so your solution should handle the
case where there are pleny of links.

Requirements:
->  First, youll want to figure out a way to extract all of the URLs.
->  Second, you'll want to test the URLs and report back to the user which are
    valid and which are not.
->  Third, youll want to make it really fast by checking the URLs concurrently
    or by parallelizing the checks.  You might want to think about caching as
    well.
"""

import csv
import re
import argparse

from concurrent import futures
from time import strftime
from urllib import request
from urllib.error import HTTPError
from urllib.error import URLError

from bs4 import BeautifulSoup


def parse_html(html_text):
    """Parse html text and extract links."""
    soup = BeautifulSoup(html_text, 'html.parser')
    links_list = list()
    for link in soup.findAll('a', attrs={'href': re.compile("^https*://")}):
        links_list.append(link.get('href'))
    good_links, bad_links = thread_tests(links_list)
    return good_links, bad_links


def test_url(url):
    """Check URL for response code."""
    try:
        resp_code = request.urlopen(url).getcode()
    except (HTTPError, URLError):
        return False
    if resp_code != 200:
        return False
    return True


def thread_tests(links_list):
    """Run URL tests via thread pool."""
    good_links = list()
    bad_links = list()
    with futures.ThreadPoolExecutor(max_workers=10) as executor:
        # Start the load operations and mark each future with its URL
        future_to_link = {
            executor.submit(test_url, link): link for link in links_list}
        for future in futures.as_completed(future_to_link):
            link = future_to_link[future]
            if future.result():
                good_links.append(link)
            else:
                bad_links.append(link)
    return good_links, bad_links


def get_html_from_file(file_location):
    """Read HTML from a local file."""
    html_text = open(file_location, 'r')
    return html_text


def get_html_from_url(url):
    """Read HTML from a remote URL."""
    with request.urlopen(url) as response:
        html_page = response.read()

    return html_page


def output_to_screen(good_links, bad_links):
    """Print results to the screen."""
    print("Good Links ==========")
    for url in good_links:
        print("     %s" % url)
    print("Bad Links ===========")
    for url in bad_links:
        print("     %s" % url)


def output_to_csv(good_links, bad_links):
    """Save results to a CSV file."""
    filename = "LinkFiles/"+strftime("%Y%m%d-%H%M%S")+"-links.csv"
    with open(filename, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Status', 'URL'])
        for url in good_links:
            writer.writerow(['Good', url])
        for url in bad_links:
            writer.writerow(['Bad', url])


def main(**kwargs):
    """Process command line requests."""
    if kwargs['file']:
        html_text = get_html_from_file(kwargs['file'])
    elif kwargs['url']:
        html_text = get_html_from_url(kwargs['url'])
    else:
        raise AttributeError('A file or url to parse must be provided.')

    if html_text:
        good_links, bad_links = parse_html(html_text)
    else:
        raise AttributeError('No valid HTML text supplied.')
    if kwargs['output_screen']:
        output_to_screen(good_links, bad_links)

    if kwargs['output_csv']:
        output_to_csv(good_links, bad_links)


if __name__ == '__main__':
    PARSER = argparse.ArgumentParser(description="Process HTML for links.")

    PARSER.add_argument(
        '-f',
        '--file',
        help='File with HTML to be processed.  File takes precedence over URL')

    PARSER.add_argument(
        '-u',
        '--url',
        help='URL to parse.')

    PARSER.add_argument(
        '-s',
        '--output_screen',
        help='Output results to screen.',
        action='store_true',
        default=False)

    PARSER.add_argument(
        '-c',
        '--output_csv',
        help='Output results to CSV file.',
        action='store_true',
        default=False)

    COMMAND_ARGS = vars(PARSER.parse_args())

    main(**COMMAND_ARGS)
