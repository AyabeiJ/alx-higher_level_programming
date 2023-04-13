#!/usr/bin/python3
"""Documentation for Rectangle class"""


class BaseGeometry:
    """A class representing a base geometry"""

    def area(self):
        """Calculate the area of the geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate an integer value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A class representing a rectangle"""

    def __init__(self, width, height):
        """Initialize a new rectangle instance"""
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)
