#!/usr/bin/env python3
"""Module that defines a class Square with position and string form."""


class Square:
    """Class that represents a square with a size and a position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square.

        Args:
            size: size of the square (integer greater than or equal to 0).
            position: tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value: tuple of 2 positive integers.

        Raises:
            TypeError: if value is not a tuple of 2 positive integers.
        """
        message = "position must be a tuple of 2 positive integers"
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError(message)
        if not all(isinstance(n, int) and n >= 0 for n in value):
            raise TypeError(message)
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character #.

        If size is 0, print an empty line.
        """
        print(self)

    def __str__(self):
        """Return the square as a string made of # characters.

        The position moves the square down (lines) and right (spaces).
        If size is 0, return an empty string.
        """
        if self.__size == 0:
            return ""
        row = " " * self.__position[0] + "#" * self.__size
        return "\n" * self.__position[1] + "\n".join([row] * self.__size)
