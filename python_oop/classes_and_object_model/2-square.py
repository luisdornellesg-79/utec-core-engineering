#!/usr/bin/env python3
"""Module that defines a class Square with a validated size."""


class Square:
    """Class that represents a square with a private, validated size."""

    def __init__(self, size=0):
        """Initialize the square.

        Args:
            size: size of the square (integer greater than or equal to 0).

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
