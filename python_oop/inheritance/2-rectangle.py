#!/usr/bin/env python3
"""Módulo que define la clase Rectangle."""


class Rectangle:
    """Representa un rectángulo."""

    def __init__(self, width, height):
        """Inicializa un rectángulo con ancho y alto validados.
        
        Args:
            width (int): El ancho del rectángulo.
            height (int): El alto del rectángulo.
        """
        if not isinstance(width, int) or isinstance(width, bool):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be greater than 0")

        if not isinstance(height, int) or isinstance(height, bool):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be greater than 0")

        self.__width = width
        self.__height = height

    def area(self):
        """Calcula y devuelve el área del rectángulo."""
        return self.__width * self.__height

    def __str__(self):
        """Devuelve la representación informal del rectángulo."""
        return f"[Rectangle] {self.__width}/{self.__height}"
