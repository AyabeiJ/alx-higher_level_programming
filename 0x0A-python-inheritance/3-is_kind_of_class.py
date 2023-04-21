#!/usr/bin/python3
<<<<<<< HEAD
"""Defines a class and inherited class-checking function."""

def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class or a subclass of a_class; otherwise False.

    Args:
        obj (object): The object to check.
        a_class (class): The class to compare to.

    Returns:
        bool: True if obj is an instance of a_class or a subclass of a_class; otherwise False.
    """
=======
"""Module containing is_kind_of_class method"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of, or if the
    object is an instance of a class that inherited from
    the specified class ; otherwise False """
>>>>>>> 217dfab9b336e76edc5a44b26d4f70f47dc0590f
    return isinstance(obj, a_class)
