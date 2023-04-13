#!/usr/bin/python3
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
    return type(obj) == a_class
