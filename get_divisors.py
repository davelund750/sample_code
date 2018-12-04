"""
Accept a positive integer input and output divisors.

Usage:
    Command line:
        python question_two.py #int#
    Importing to other modules:
        from question_two import divisors
        divisors(#int#)

Prompt:
Write a function that takes a single positive integer, and returns a
collection / sequence (e.g. array) of integers.  The return value should
contain those integers that are positive divisors of the input integer.

Sample inputs       Sample Outputs
=============       ===============================================
60                  {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}
42                  {1, 2, 3, 6, 7, 14, 21, 42}
"""
import sys


def divisors(multiple):
    """Accept positive integer and return all positive divisors."""
    multiple = eval_input(multiple)
    divisors_list = list()
    for divisor in range(1, multiple+1):
        if not multiple % divisor:
            divisors_list.append(divisor)
    return divisors_list


def eval_input(multiple):
    """Evaluate the variable supplied."""
    try:
        multiple = int(multiple)
    except ValueError:
        multiple = 0
    if multiple < 1:
        raise AttributeError(
            'Suppplied value is not an integer or is less than 1')
    return multiple


def main(multiple):
    """Call divisors function."""
    divisors_list = divisors(multiple)
    print(divisors_list)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
