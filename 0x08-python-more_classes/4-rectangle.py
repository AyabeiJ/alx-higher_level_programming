#!/usr/bin/python3

"""Defines a class Rectangle."""


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
        width (int): The with of the new rectangle.
        height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height
        
    @property
    def width(self):
        """Get/set the with of the Recttangle."""
        return self.__width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        
    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self.__height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
        
    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height
    
    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
    
    def __str__(self):
        """Return the printable representation of the Rectangle.
        Represents the rectangle with # character.
        """
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width] * self.height)
    
    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"
