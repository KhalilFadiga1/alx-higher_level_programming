#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """Executes sorted printing for the built-in list class."""

    def print_sorted(self):
        """Print a list in sorted order."""
        print(sorted(self))
