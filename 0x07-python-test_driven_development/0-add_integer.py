#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b = 98):
    """Return the summation of a and b.

    Float args are typecasted to ints before arithmetic is perform

    Raises:
        TypeError: IF  either of a or b is  anon-integer and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
