#!/usr/bin/python3
"""Module documentation"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """Method to calculate the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method to validate value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """Initialization method"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """String representation method"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Method to calculate the area"""
        return self.__width * self.__height


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Initialization method"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """String representation method"""
        return "[Square] {}/{}".format(self.__size, self.__size)
