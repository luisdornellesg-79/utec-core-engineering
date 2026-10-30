#!/usr/bin/env python3
"""Módulo BaseGeometry."""


class BaseGeometry:
    """Clase base para geometría."""

    def area(self):
        """Lanza una excepción de que no está implementado."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Valida que un valor sea un entero positivo."""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
