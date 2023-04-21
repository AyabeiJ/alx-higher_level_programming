#!/usr/bin/python3
<<<<<<< HEAD
"""Documentation for BaseGeometry class"""


class BaseGeometry:
    """A class representing a base geometry"""

    def area(self):
        """Calculate the area of the geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate an integer value"""
        if type(value) is not int:
=======
"""
This module contains the BaseGeometry class
"""


class BaseGeometry:
    """
    A class named BaseGeometry
    """
    def area(self):
        """
        Raises an Exception with the message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value

        Args:
            name (str): The name of the value
            value (int): The value to validate

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less or equal to 0
        """
        if not isinstance(value, int):
>>>>>>> 217dfab9b336e76edc5a44b26d4f70f47dc0590f
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
