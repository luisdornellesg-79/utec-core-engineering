#!/usr/bin/env python3
"""Módulo Square."""


Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Representa un cuadrado que hereda de Rectangle."""

    def __init__(self, size):
        """Inicializa un cuadrado con un tamaño validado.

        Args:
            size (int): El tamaño de los lados del cuadrado.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Devuelve la representación informal del cuadrado."""
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
