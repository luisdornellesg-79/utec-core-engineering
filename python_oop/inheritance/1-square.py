#!/usr/bin/env python3
"""Módulo que define la clase Square basada en Rectangle."""


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
