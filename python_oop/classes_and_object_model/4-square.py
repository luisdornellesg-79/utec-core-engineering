#!/usr/bin/env python3
"""Module that defines a class Square with a getter and a setter for size."""


class Square:
    """Class that represents a square with a private, validated size."""

    def __init__(self, size=0):
        """Initialize the square.

        Args:
            size: size of the square (integer greater than or equal to 0).
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value: new size (integer greater than or equal to 0).

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
