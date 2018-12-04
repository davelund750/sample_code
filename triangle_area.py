"""
Compute the area of a triangle.

Usage:
    Command line:
        python question_three.py #int# #int# #int#
    Importing to other modules:
        from question_three import compute_area
        compute_area([#int#, #int#, #int#])

Prompt:
Write a function that takes three integer inputs and returns a single output.
The inputs are the lengths of the sides of a triangle.  The output is the
area of the triangle.

Sample inputs                               Sample Outputs
==================                          ==================================
3, 4, 5                                     6
Any inputs that are negative.               (throw) InvalidTriangleException
Inputs that cannot form a valid triangle.   (throw) InvalidTriangleException
"""
import sys
import math
from functools import reduce


class InvalidTriangleException(Exception):
    """Raise when inputs are invalid."""

    pass


def compute_area(side_len_list):
    """Evaluate the variables supplied."""
    side_len_list = evaluate_inputs(side_len_list)
    # Area computed using Heron's Formula
    # https://en.wikipedia.org/wiki/Heron%27s_formula
    semi_perimeter = sum(side_len_list)/2
    factor_list = [semi_perimeter - len_item for len_item in side_len_list]
    area = math.sqrt(reduce(lambda x, y: x*y, factor_list) * semi_perimeter)
    if area <= 0:
        raise InvalidTriangleException(
            "Supplied lengths will not make a valid triangle")
    return area


def evaluate_inputs(side_len_list):
    """Evaluate lengths provided as input."""
    if len(side_len_list) != 3:
        raise InvalidTriangleException("Number of sides does not equal 3.")
    try:
        side_len_list = list(map(int, side_len_list))
    except ValueError:
        raise InvalidTriangleException(
            'A suppplied value is not an integer')
    if not all(side_val > 0 for side_val in side_len_list):
        raise InvalidTriangleException(
            'A supplied value is not a positive number')
    return side_len_list


def main(inputs):
    """Call triangle area function."""
    triangle_area = compute_area(inputs)
    print(triangle_area)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        sys.argv.pop(0)
        main(sys.argv)
