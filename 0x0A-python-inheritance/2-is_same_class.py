#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.

    Args:
        obj (any): The object to run checks on.
        a_class (type): The class to check obj type to.
    Returns:
        If obj is exactly  an instance of a_class - True.
        Otherwise - False.
    """
    return (type(obj) == a_class)
