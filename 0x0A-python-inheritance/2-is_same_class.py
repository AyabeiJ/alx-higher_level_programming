#!/usr/bin/python3
<<<<<<< HEAD
"""Defines a class-checking function."""

def is_same_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class; otherwise False.

    Args:
        obj (object): The object to check.
        a_class (class): The class to compare to.

    Returns:
        bool: True if obj is an instance of a_class; otherwise False.
    """
=======
"""Module containing is_same_class method"""


def is_same_class(obj, a_class):
    """Returns:
    True: if the object is exactly an instance of the specified class
    False: otherwise"""
>>>>>>> 217dfab9b336e76edc5a44b26d4f70f47dc0590f
    return type(obj) == a_class
