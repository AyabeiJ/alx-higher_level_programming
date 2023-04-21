#!/usr/bin/python3
<<<<<<< HEAD
"""Defines an inherite list class Mylist."""

class MyList(list):
    """A subclass of list that provides a print_sorted method."""

    def print_sorted(self):
        """Print the list, but sorted in ascending order."""
=======
"""MyList module"""


class MyList(list):
    """MyList class - Inherits from list"""
    def print_sorted(self):
        """Prints a sorted list"""
>>>>>>> 217dfab9b336e76edc5a44b26d4f70f47dc0590f
        print(sorted(self))
