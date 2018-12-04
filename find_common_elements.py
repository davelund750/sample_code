"""
Find the most common elements in a list of integers.

Usage:
    Command line:
        python question_four.py #int# #int# #int# ...
    Importing to other modules:
        from question_four import find_frequency
        divisors([#int#, #int#, #int#, ...])

Prompt:
Write a function that takes an array of integers, and returns an array of
integers. The return value should contain those integers which are most common
in the input array.

Sample inputs                               Sample Outputs
======================================      ============================
{5, 4, 3, 2, 4, 5, 1, 6, 1, 2, 5, 4}        {5, 4} *Order does not matter
{1, 2, 3, 4, 5, 1, 6, 7}                    {1}
{1, 2, 3, 4, 5, 6, 7}                       {1, 2, 3, 4, 5, 6, 7}
"""
import sys
from collections import Counter


def find_frequency(integer_list):
    """Evaluate the variables supplied."""
    integer_list = evaluate_inputs(integer_list)
    freq_dict = dict(Counter(integer_list).most_common())
    max_count = max(freq_dict.values())
    high_freq_list = [
        key for key, value in freq_dict.items() if value == max_count]
    return high_freq_list


def evaluate_inputs(integer_list):
    """Evaluate integers provided as input."""
    if isinstance(integer_list, str):
        integer_list = integer_list.split()
    try:
        integer_list = list(map(int, integer_list))
    except ValueError:
        raise
    return integer_list


def main(inputs):
    """Call triangle area function."""
    common_list = find_frequency(inputs)
    print(common_list)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        sys.argv.pop(0)
        main(sys.argv)
