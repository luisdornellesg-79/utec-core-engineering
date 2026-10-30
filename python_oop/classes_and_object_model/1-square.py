#!/usr/bin/env python3
"""Module that defines a class Square with a private size."""


class Square:
    """Class that represents a square with a private size."""

    def __init__(self, size):
        """Initialize the square.

        Args:
            size: size of the square.
        """
        self.__size = size
