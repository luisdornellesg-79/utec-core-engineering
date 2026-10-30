#!/usr/bin/env python3
"""Module that defines the class BaseGeometry."""


class BaseGeometry:
    """Class that defines shared behavior for geometric shapes."""

    def area(self):
        """Raise an exception because area is not implemented here.

        Raises:
            Exception: always, with the message area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is an integer greater than 0.

        Args:
            name: name of the value, used in the error messages.
            value: value to validate.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than or equal to 0.
        """
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
