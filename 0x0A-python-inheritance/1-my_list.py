#!/usr/bin/python3
"""Defines an inherite list class Mylist."""

class MyList(list):
    """A subclass of list that provides a print_sorted method."""

    def print_sorted(self):
        """Print the list, but sorted in ascending order."""
        print(sorted(self))
