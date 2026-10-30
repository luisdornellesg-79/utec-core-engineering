#!/usr/bin/env python3
"""Module that defines the class Rectangle."""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that represents a rectangle with a private width and height."""

    def __init__(self, width, height):
        """Initialize the rectangle.

        Args:
            width: width of the rectangle (positive integer).
            height: height of the rectangle (positive integer).
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
